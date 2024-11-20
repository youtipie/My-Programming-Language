from lexer import Lexer
from my_parser import Parser
from lexer.config import lexer_config
from psm.postfixMachine import PSM

lexer: Lexer = Lexer(**lexer_config)
parser: Parser = Parser()

with open("test.ql", "r", encoding="utf8") as source_code:
    table_of_symbols, _, table_of_constants = lexer.analyze(source_code.read())
    parser.analyze(table_of_symbols, table_of_constants, "example")
    psm = PSM()
    psm.loadPostfixFile("example")
    psm.postfixExec()

    print('\n' * 5)
    print(f"pm1.tableOfId:\n  {psm.tableOfId}\n")
    print(f"pm1.tableOfLabel:\n  {psm.tableOfLabel}\n")
    print(f"pm1.tableOfConst:\n  {psm.tableOfConst}\n")
    print(f"pm1.postfixCode:\n  {psm.postfixCode}\n")

    for i in range(0, len(psm.postfixCode)):
        print(i, psm.mapDebug[i], psm.postfixCode[i])

    print(f"pm1.mapDebug:\n  {psm.mapDebug}\n")
