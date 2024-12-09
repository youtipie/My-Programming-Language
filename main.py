from lexer import Lexer
from my_parser import Parser
from lexer.config import lexer_config
from my_parser.saveCIL import saveCIL
from psm.postfixMachine import PSM

lexer: Lexer = Lexer(**lexer_config)
parser: Parser = Parser()

with open("example.ql", "r", encoding="utf8") as source_code:
    table_of_symbols, _, table_of_constants = lexer.analyze(source_code.read())
    table_of_vars, postfix_code, = parser.analyze(table_of_symbols, table_of_constants, "example")
    saveCIL("example", table_of_vars, postfix_code)
    print(postfix_code)
    # psm = PSM()
    # psm.loadPostfixFile("example")
    # psm.postfixExec()
