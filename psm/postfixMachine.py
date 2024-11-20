# завантаження ПОЛІЗ-програми у форматі .postfix
import re
import time

from .stack import Stack
from .forParsePostfixProgram import getValue, f2i, i2f

toView = False


class PSM():  # Postfix Stack Macine
    def __init__(self):
        self.tableOfId = {}
        self.tableOfLabel = {}
        self.tableOfConst = {}
        self.postfixCode = []
        self.mapDebug = {}
        self.numLine = 0
        self.fileName = ""
        self.file = ""
        self.slt = ""
        self.headSection = {"VarDecl": ".vars(", "LblDecl": ".labels(", "ConstDecl": ".constants(", "Code": ".code("}
        self.errMsg = {1: "неочікуваний заголовок", 2: "тут очікувався хоч один порожній рядок",
                       3: "тут очікувався заголовок секції", 4: "очікувалось два елемента в рядку"}
        self.stack = Stack()
        self.numInstr = 0
        self.maxNumbInstr = 0

    def printOp(self, lex, tok):
        if toView:
            print(f'-=-=-=========({lex},{tok})  numInstr={self.numInstr}')
        return True

    # завантаження ПОЛІЗ-програми у форматі .postfix
    def loadPostfixFile(self, fileName):
        try:
            self.fileName = fileName + ".postfix"
            self.file = open(self.fileName, 'r', encoding="utf8")
            self.parsePostfixProgram()
            self.file.close()
        except PSMExcept as e:
            print(
                f"PSM.loadPostfixFile ERROR: у рядку {self.numLine}, код винятку - {e.msg}, msg = {self.errMsg[e.msg]}")
            raise

    def parsePostfixProgram(self):
        # print("--------- header ")
        self.parseHeader(".target: Postfix Machine")
        # print(f"have header1 {self.numLine}")
        self.parseHeader(".version: 0.2")
        # print(f"have header2 {self.numLine}")

        self.parseSection("VarDecl")
        # print(f"have var {self.numLine}")

        self.parseSection("LblDecl")
        # print("have lbl ")

        self.parseSection("ConstDecl")
        # print("have const ")

        self.parseSection("Code")  # mapDebug:: numInstr -> numLine
        # print("have code ")

    def parseHeader(self, header):
        if self.file.readline().rstrip() != header:
            raise PSMExcept(1)
        self.numLine += 1

    def parseSection(self, section):
        # print("============Section: "+section)
        headerSect = self.headSection[section]
        s = self.file.readline().partition("#")[0].strip()
        self.numLine += 1
        # один порожній рядок обов'язковий
        if s != "":
            raise PSMExcept(2)
        # інші (можливі) порожні рядки та заголовок секції
        F = True
        while F:
            s = self.file.readline().partition("#")[0].strip()
            # print("s=",s)
            self.numLine += 1
            if s == "":
                pass  # self.numLine += 1
            elif s == headerSect:
                # self.numLine += 1
                F = False
            else:
                raise PSMExcept(3)
        # формування відповідної таблиці (можливі і порожні рядки)
        F = True
        while F:
            s = self.file.readline().partition("#")[0].strip()
            self.numLine += 1
            if s == "":
                pass
            elif s == ")":  # кінець секції
                F = False
            else:
                self.slt = s
                self.procSection(section)

    def procSection(self, section):
        list = self.slt.split()
        if len(list) != 2:
            raise PSMExcept(4)
        else:
            item1 = list[0]
            item2 = list[1]
            if section == "VarDecl":
                table = self.tableOfId
                indx = len(table) + 1
                table[item1] = (indx, item2, 'val_undef')

            if section == "LblDecl":
                table = self.tableOfLabel
                indx = len(table) + 1
                table[item1] = item2

            if section == "ConstDecl":
                table = self.tableOfConst
                indx = len(table) + 1
                if item2 == "intnum":
                    val = int(item1)
                elif item2 == "floatnum":
                    val = float(item1)
                elif item2 == "boolval":
                    val = item1
                table[item1] = (indx, item2, val)

            if section == "Code":
                indx = len(self.postfixCode)
                self.postfixCode.append((item1, item2))
                instrNum = len(self.postfixCode) - 1
                self.mapDebug[instrNum] = self.numLine

    def postfixExec(self):
        "Виконує postfixCode"
        self.maxNumbInstr = len(self.postfixCode)
        try:
            while self.numInstr < self.maxNumbInstr:
                if toView: self.stack.print()
                lex, tok = self.postfixCode[self.numInstr]
                if tok in ('intnum', 'floatnum', 'l-val', 'r-val', 'label', 'boolval'):
                    self.stack.push((lex, tok))
                    self.numInstr = self.numInstr + 1
                elif tok in ('jump', 'jf', 'colon'):
                    self.printOp(lex, tok)
                    self.doJumps(tok)
                elif tok == 'print':
                    self.printOp(lex, tok)
                    lexx, tokk = self.stack.pop()
                    if tokk == 'r-val':
                        print(f'\n{lexx}={self.tableOfId[lexx][2]}\n')
                    else:
                        print(f'\nлітерал: {lexx}\n')
                    self.numInstr = self.numInstr + 1
                elif tok == 'readline':
                    self.printOp(lex, tok)
                    # введення з клавіатури
                    # зняти зі стека (id,'l-val')
                    id, _ = self.stack.pop()  #
                    typeVar = self.tableOfId[id][1]
                    if typeVar == 'intnum':
                        tmpVal = int(input(f'\nВведіть значення типу {typeVar}: {id}='))
                    elif typeVar == 'floatnum':
                        tmpVal = float(input(f'\nВведіть значення типу {typeVar}: {id}='))
                    print()
                    self.numInstr = self.numInstr + 1
                    self.tableOfId[id] = (self.tableOfId[id][0], typeVar, tmpVal)
                elif tok == 'print':
                    self.printOp(lex, tok)
                    self.numInstr = self.numInstr + 1
                elif lex == 'NEG':
                    self.printOp(lex, tok)
                    lexx, tokk = self.stack.pop()  #
                    typeVar, valVar = self.getValTypeOperand(lexx, tokk)
                    if typeVar == 'intnum':
                        tmpVal = -int(valVar)
                    elif typeVar == 'floatnum':
                        tmpVal = -float(valVar)
                    self.stack.push((str(tmpVal), typeVar))
                    self.numInstr = self.numInstr + 1
                elif tok == 'conv_op':
                    self.printOp(lex, tok)
                    lexx, tokk = self.stack.pop()  #
                    typeVar, valVar = self.getValTypeOperand(lexx, tokk)
                    if lex == 'i2f':
                        tmpVal = i2f(valVar)
                        toType = 'float'
                    elif lex == 'f2i':
                        tmpVal = f2i(valVar)
                        toType = 'int'
                    self.stack.push((str(tmpVal), toType))
                    self.numInstr = self.numInstr + 1
                else:
                    self.printOp(lex, tok)
                    # if toView: print(f'-=-=-=========({lex},{tok})  numInstr={self.numInstr}')
                    self.doIt(lex, tok)
                    self.numInstr = self.numInstr + 1
        except PSMExcept as e:
            # Повідомити про факт виявлення помилки
            print('RunTime: Аварійне завершення програми з кодом {0}'.format(e))
            raise

    def doJumps(self, tok):
        # time.sleep(1)
        if tok == 'jump':
            lexLbl, _ = self.stack.pop()  # зняти з вершини стека мітку
            self.numInstr = int(self.tableOfLabel[lexLbl])  # номер наступної інструкції = значення мітки
        elif tok == 'colon':
            _ = self.stack.pop()  # зняти з вершини стека
            self.numInstr = self.numInstr + 1  # непотрібну нам мітку
        elif tok == 'jf':
            lexLbl, _ = self.stack.pop()  # зняти з вершини стека мітку
            valBoolExpr, _ = self.stack.pop()  # зняти з вершини стека значення BoolExpr
            if valBoolExpr == 'false':
                self.numInstr = int(self.tableOfLabel[lexLbl])
            else:
                self.numInstr = self.numInstr + 1

    def doIt(self, lex, tok):
        # зняти з вершини стека ідентифікатор (правий операнд)
        (lexR, tokR) = self.stack.pop()
        # зняти з вершини стека запис (лівий операнд)
        (lexL, tokL) = self.stack.pop()

        if (lex, tok) == ('=', 'assign_op'):
            tokL = self.tableOfId[lexL][1]
            if tokL != tokR:
                print(f'(lexR,tokR)={(lexR, tokR)}\n(lexL,tokL)={(lexL, tokL)}')
                raise PSMExcept(7)  # типи змінної відрізняється від типу значення
            else:
                # виконати операцію:
                # оновлюємо запис у таблиці ідентифікаторів
                # ідентифікатор/змінна  =
                #              (index - не змінився,
                #               тип - як у правого операнда (вони однакові),
                #               значення - як у правого операнда)
                # print((self.tableOfId[lexL][0], tokR, getValue(lexR, tokR)))
                self.tableOfId[lexL] = (self.tableOfId[lexL][0], tokR, getValue(lexR, tokR))
        else:
            self.processingArthBoolOp((lexL, tokL), lex, (lexR, tokR))

    def processingArthBoolOp(self, lexTokL, arthBoolOp, lexTokR):
        (lexL, tokL) = lexTokL
        (lexR, tokR) = lexTokR
        typeL, valL = self.getValTypeOperand(lexL, tokL)
        typeR, valR = self.getValTypeOperand(lexR, tokR)
        self.applyOperator((lexL, typeL, valL), arthBoolOp, (lexR, typeR, valR))

    def getValTypeOperand(self, lex, tok):
        if tok == "r-val":
            if self.tableOfId[lex][2] == 'val_undef':
                raise PSMExcept(8)  # 'неініційована змінна', (lexL,tableOfId[lexL], (lexL,tokL
            else:
                type, val = (self.tableOfId[lex][1], self.tableOfId[lex][2])
        elif tok == 'intnum':
            val = int(lex)
            type = tok
        elif tok == 'floatnum':
            val = float(lex)
            type = tok
        elif tok == 'boolval':
            val = lex
            type = tok
        return (type, val)

    def applyOperator(self, lexTypeValL, arthBoolOp, lexTypeValR):
        (lexL, typeL, valL) = lexTypeValL
        (lexR, typeR, valR) = lexTypeValR
        if typeL != typeR:
            if {typeL, typeR} == {'intnum', 'floatnum'}:
                # Якщо типи intnum і floatnum, обидва значення переводяться у floatnum
                typeL = typeR = 'floatnum'
                valL = float(valL)
                valR = float(valR)
            else:
                raise PSMExcept(9)
        if arthBoolOp == '+':
            value = valL + valR
        elif arthBoolOp == '-':
            value = valL - valR
        elif arthBoolOp == '*':
            value = valL * valR
        elif arthBoolOp == '/' and valR == 0:
            raise PSMExcept(10)  # ділення на нуль
        elif arthBoolOp == '/':
            value = valL / valR
            typeL = typeR = 'floatnum'
        elif arthBoolOp == '^':
            val = pow(valL, valR)
            if isinstance(val, complex):
                exit(f'Значенням {valL}^{valR} є комплексне число {val}')
            elif isinstance(val, int):
                value = float(val)
            else:
                value = val
            # результат має бути типу float
            typeL = 'floatnum'
        elif arthBoolOp == '<':
            value = str(valL < valR).lower()
        elif arthBoolOp == '<=':
            value = str(valL <= valR).lower()
        elif arthBoolOp == '>':
            value = str(valL > valR).lower()
        elif arthBoolOp == '>=':
            value = str(valL >= valR).lower()
        elif arthBoolOp == '==':
            value = str(valL == valR).lower()
        elif arthBoolOp == '!=':
            value = str(valL != valR).lower()
        else:
            pass
        # покласти результат на стек
        if arthBoolOp in ('<', '<=', '>', '>=', '==', '!='):
            self.stack.push((str(value), 'boolval'))
        else:
            self.stack.push((str(value), typeL))


class PSMExcept(Exception):
    def __init__(self, msg):
        self.msg = msg


if __name__ == '__main__':
    pm1 = PSM()
    pm1.loadPostfixFile("test1")  # завантаження .postfix - файла

    print('postfixExec:')
    pm1.postfixExec()

    print('\n' * 5)
    # Вивести таблиці
    print(f"pm1.tableOfId:\n  {pm1.tableOfId}\n")
    print(f"pm1.tableOfLabel:\n  {pm1.tableOfLabel}\n")
    print(f"pm1.tableOfConst:\n  {pm1.tableOfConst}\n")
    print(f"pm1.postfixCode:\n  {pm1.postfixCode}\n")

    # Вивести в консоль
    # i - номер postfix-інструкції
    # pm1.mapDebug[i] - номер рядка у postfix-файлі
    # pm1.postfixCode[i]) - інструкція
    for i in range(0, len(pm1.postfixCode)):
        print(i, pm1.mapDebug[i], pm1.postfixCode[i])

    # mapDebug:: numInstr -> numLine
    print(f"pm1.mapDebug:\n  {pm1.mapDebug}\n")
