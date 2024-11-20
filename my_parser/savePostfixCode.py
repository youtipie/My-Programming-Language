# Функція для збереження у файлі postfix-програми
# це інформація з таблиць:
# tableOfVar
# tableOfLabel
# tableOfConst
# postfixCodeTSM
def savePostfixCode(filename, tableOfVar, tableOfLabel, tableOfConst, postfixCodeTSM):
    fname = filename + ".postfix"
    f = open(fname, 'w', encoding="utf8")
    header = ".target: Postfix Machine\n.version: 0.2\n"
    f.write(header)

    f.write("\n" + ".vars" + "(\n")
    for ident, ident_type in tableOfVar.items():
        f.write("   {} {} \n".format(ident, ident_type))
    f.write(")\n")

    f.write("\n" + ".labels" + "(\n")
    for lbl in tableOfLabel:
        f.write("   {} {} \n".format(lbl, tableOfLabel[lbl]))
    f.write(")\n")

    f.write("\n" + ".constants" + "(\n")
    for literal, c_type in tableOfConst.items():
        f.write("   {} {} \n".format(literal, c_type))
    f.write(")\n")

    f.write("\n" + ".code" + "(\n")
    for instr in postfixCodeTSM:
        f.write("   {} {} \n".format(instr[0], instr[1]))
        # f.write("   " + str(instr[0]).ljust(6) + str(instr[1]).ljust(6) + "\n")
    f.write(")\n")

    f.close()
    print(f"postfix-код збережено у файлі {fname}")
