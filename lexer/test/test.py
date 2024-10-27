from lexer import Lexer
from config import lexer_config

lexer: Lexer = Lexer(**lexer_config)

# with open("test_1.ql", "r", encoding="utf8") as source_code:
#     lexer.analyze(source_code.read())
#
# with open("test_2.ql", "r", encoding="utf8") as source_code:
#     lexer.analyze(source_code.read())

with open("test_3.ql", "r", encoding="utf8") as source_code:
    lexer.analyze(source_code.read())

# with open("test_4.ql", "r", encoding="utf8") as source_code:
#     lexer.analyze(source_code.read())
