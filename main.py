from lexer import Lexer
from my_parser import Parser
from lexer.config import lexer_config

lexer: Lexer = Lexer(**lexer_config)
parser: Parser = Parser()

with open("test.ql", "r", encoding="utf8") as source_code:
    table_of_symbols, _, table_of_constants = lexer.analyze(source_code.read())
    parser.analyze(table_of_symbols, table_of_constants)
