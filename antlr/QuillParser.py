# Generated from Quill.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 43, 257, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 2, 20,
        7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2, 26, 7, 26,
        2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 5, 1, 66, 8, 1, 10,
        1, 12, 1, 69, 9, 1, 1, 2, 1, 2, 3, 2, 73, 8, 2, 1, 2, 1, 2, 3, 2, 77, 8, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 1, 2, 3, 2, 85, 8, 2, 1, 2, 3, 2, 88, 8, 2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1,
        3, 5, 3, 97, 8, 3, 10, 3, 12, 3, 100, 9, 3, 1, 4, 1, 4, 5, 4, 104, 8, 4, 10, 4, 12, 4, 107,
        9, 4, 1, 5, 1, 5, 3, 5, 111, 8, 5, 1, 5, 1, 5, 1, 5, 3, 5, 116, 8, 5, 1, 5, 1, 5, 3, 5, 120,
        8, 5, 1, 6, 1, 6, 1, 6, 1, 6, 3, 6, 126, 8, 6, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 3, 7, 134,
        8, 7, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 3, 8, 142, 8, 8, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9,
        1, 9, 1, 9, 1, 10, 1, 10, 1, 10, 1, 10, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 11, 1, 12, 1,
        12, 1, 13, 1, 13, 1, 13, 1, 13, 1, 13, 5, 13, 169, 8, 13, 10, 13, 12, 13, 172, 9, 13, 1,
        13, 1, 13, 1, 14, 1, 14, 1, 14, 1, 14, 5, 14, 180, 8, 14, 10, 14, 12, 14, 183, 9, 14, 1,
        15, 1, 15, 1, 16, 3, 16, 188, 8, 16, 1, 16, 1, 16, 1, 16, 5, 16, 193, 8, 16, 10, 16, 12,
        16, 196, 9, 16, 1, 17, 1, 17, 1, 17, 5, 17, 201, 8, 17, 10, 17, 12, 17, 204, 9, 17, 1,
        18, 1, 18, 1, 18, 5, 18, 209, 8, 18, 10, 18, 12, 18, 212, 9, 18, 1, 19, 1, 19, 1, 19, 1,
        19, 1, 19, 1, 19, 3, 19, 220, 8, 19, 1, 20, 1, 20, 1, 20, 3, 20, 225, 8, 20, 1, 21, 1, 21,
        1, 22, 1, 22, 1, 23, 1, 23, 1, 24, 1, 24, 1, 25, 3, 25, 236, 8, 25, 1, 25, 1, 25, 1, 26,
        1, 26, 1, 26, 1, 26, 1, 27, 1, 27, 5, 27, 246, 8, 27, 10, 27, 12, 27, 249, 9, 27, 1, 28,
        1, 28, 1, 28, 1, 28, 1, 29, 1, 29, 1, 29, 0, 0, 30, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
        22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 0, 9, 2, 0,
        3, 3, 39, 40, 2, 0, 3, 3, 39, 41, 1, 0, 17, 22, 1, 0, 23, 24, 1, 0, 25, 26, 1, 0, 28, 29,
        1, 0, 30, 32, 1, 0, 33, 34, 1, 0, 36, 37, 258, 0, 60, 1, 0, 0, 0, 2, 67, 1, 0, 0, 0, 4, 87,
        1, 0, 0, 0, 6, 89, 1, 0, 0, 0, 8, 101, 1, 0, 0, 0, 10, 119, 1, 0, 0, 0, 12, 121, 1, 0, 0, 0,
        14, 127, 1, 0, 0, 0, 16, 135, 1, 0, 0, 0, 18, 143, 1, 0, 0, 0, 20, 151, 1, 0, 0, 0, 22, 155,
        1, 0, 0, 0, 24, 161, 1, 0, 0, 0, 26, 163, 1, 0, 0, 0, 28, 175, 1, 0, 0, 0, 30, 184, 1, 0,
        0, 0, 32, 187, 1, 0, 0, 0, 34, 197, 1, 0, 0, 0, 36, 205, 1, 0, 0, 0, 38, 219, 1, 0, 0, 0,
        40, 224, 1, 0, 0, 0, 42, 226, 1, 0, 0, 0, 44, 228, 1, 0, 0, 0, 46, 230, 1, 0, 0, 0, 48, 232,
        1, 0, 0, 0, 50, 235, 1, 0, 0, 0, 52, 239, 1, 0, 0, 0, 54, 243, 1, 0, 0, 0, 56, 250, 1, 0,
        0, 0, 58, 254, 1, 0, 0, 0, 60, 61, 3, 2, 1, 0, 61, 62, 5, 0, 0, 1, 62, 1, 1, 0, 0, 0, 63, 66,
        3, 4, 2, 0, 64, 66, 5, 38, 0, 0, 65, 63, 1, 0, 0, 0, 65, 64, 1, 0, 0, 0, 66, 69, 1, 0, 0, 0,
        67, 65, 1, 0, 0, 0, 67, 68, 1, 0, 0, 0, 68, 3, 1, 0, 0, 0, 69, 67, 1, 0, 0, 0, 70, 72, 3, 6,
        3, 0, 71, 73, 5, 1, 0, 0, 72, 71, 1, 0, 0, 0, 72, 73, 1, 0, 0, 0, 73, 88, 1, 0, 0, 0, 74, 76,
        3, 12, 6, 0, 75, 77, 5, 1, 0, 0, 76, 75, 1, 0, 0, 0, 76, 77, 1, 0, 0, 0, 77, 88, 1, 0, 0, 0,
        78, 88, 3, 14, 7, 0, 79, 88, 3, 18, 9, 0, 80, 88, 3, 22, 11, 0, 81, 88, 5, 38, 0, 0, 82,
        84, 3, 26, 13, 0, 83, 85, 5, 1, 0, 0, 84, 83, 1, 0, 0, 0, 84, 85, 1, 0, 0, 0, 85, 88, 1, 0,
        0, 0, 86, 88, 5, 42, 0, 0, 87, 70, 1, 0, 0, 0, 87, 74, 1, 0, 0, 0, 87, 78, 1, 0, 0, 0, 87,
        79, 1, 0, 0, 0, 87, 80, 1, 0, 0, 0, 87, 81, 1, 0, 0, 0, 87, 82, 1, 0, 0, 0, 87, 86, 1, 0, 0,
        0, 88, 5, 1, 0, 0, 0, 89, 90, 3, 42, 21, 0, 90, 91, 3, 8, 4, 0, 91, 98, 3, 10, 5, 0, 92, 93,
        5, 2, 0, 0, 93, 94, 3, 8, 4, 0, 94, 95, 3, 10, 5, 0, 95, 97, 1, 0, 0, 0, 96, 92, 1, 0, 0, 0,
        97, 100, 1, 0, 0, 0, 98, 96, 1, 0, 0, 0, 98, 99, 1, 0, 0, 0, 99, 7, 1, 0, 0, 0, 100, 98, 1,
        0, 0, 0, 101, 105, 7, 0, 0, 0, 102, 104, 7, 1, 0, 0, 103, 102, 1, 0, 0, 0, 104, 107, 1,
        0, 0, 0, 105, 103, 1, 0, 0, 0, 105, 106, 1, 0, 0, 0, 106, 9, 1, 0, 0, 0, 107, 105, 1, 0,
        0, 0, 108, 109, 5, 4, 0, 0, 109, 111, 3, 46, 23, 0, 110, 108, 1, 0, 0, 0, 110, 111, 1,
        0, 0, 0, 111, 112, 1, 0, 0, 0, 112, 115, 5, 5, 0, 0, 113, 116, 3, 28, 14, 0, 114, 116,
        3, 24, 12, 0, 115, 113, 1, 0, 0, 0, 115, 114, 1, 0, 0, 0, 116, 120, 1, 0, 0, 0, 117, 118,
        5, 4, 0, 0, 118, 120, 3, 46, 23, 0, 119, 110, 1, 0, 0, 0, 119, 117, 1, 0, 0, 0, 120, 11,
        1, 0, 0, 0, 121, 122, 3, 8, 4, 0, 122, 125, 5, 5, 0, 0, 123, 126, 3, 28, 14, 0, 124, 126,
        3, 24, 12, 0, 125, 123, 1, 0, 0, 0, 125, 124, 1, 0, 0, 0, 126, 13, 1, 0, 0, 0, 127, 128,
        5, 6, 0, 0, 128, 129, 3, 28, 14, 0, 129, 130, 5, 7, 0, 0, 130, 131, 3, 2, 1, 0, 131, 133,
        5, 8, 0, 0, 132, 134, 3, 16, 8, 0, 133, 132, 1, 0, 0, 0, 133, 134, 1, 0, 0, 0, 134, 15,
        1, 0, 0, 0, 135, 141, 5, 9, 0, 0, 136, 137, 5, 7, 0, 0, 137, 138, 3, 2, 1, 0, 138, 139,
        5, 8, 0, 0, 139, 142, 1, 0, 0, 0, 140, 142, 3, 14, 7, 0, 141, 136, 1, 0, 0, 0, 141, 140,
        1, 0, 0, 0, 142, 17, 1, 0, 0, 0, 143, 144, 5, 10, 0, 0, 144, 145, 3, 8, 4, 0, 145, 146,
        5, 11, 0, 0, 146, 147, 3, 20, 10, 0, 147, 148, 5, 7, 0, 0, 148, 149, 3, 2, 1, 0, 149, 150,
        5, 8, 0, 0, 150, 19, 1, 0, 0, 0, 151, 152, 3, 28, 14, 0, 152, 153, 3, 48, 24, 0, 153, 154,
        3, 28, 14, 0, 154, 21, 1, 0, 0, 0, 155, 156, 5, 12, 0, 0, 156, 157, 3, 28, 14, 0, 157,
        158, 5, 7, 0, 0, 158, 159, 3, 2, 1, 0, 159, 160, 5, 8, 0, 0, 160, 23, 1, 0, 0, 0, 161, 162,
        5, 13, 0, 0, 162, 25, 1, 0, 0, 0, 163, 164, 5, 14, 0, 0, 164, 165, 5, 15, 0, 0, 165, 170,
        3, 28, 14, 0, 166, 167, 5, 2, 0, 0, 167, 169, 3, 28, 14, 0, 168, 166, 1, 0, 0, 0, 169,
        172, 1, 0, 0, 0, 170, 168, 1, 0, 0, 0, 170, 171, 1, 0, 0, 0, 171, 173, 1, 0, 0, 0, 172,
        170, 1, 0, 0, 0, 173, 174, 5, 16, 0, 0, 174, 27, 1, 0, 0, 0, 175, 181, 3, 32, 16, 0, 176,
        177, 3, 30, 15, 0, 177, 178, 3, 32, 16, 0, 178, 180, 1, 0, 0, 0, 179, 176, 1, 0, 0, 0,
        180, 183, 1, 0, 0, 0, 181, 179, 1, 0, 0, 0, 181, 182, 1, 0, 0, 0, 182, 29, 1, 0, 0, 0, 183,
        181, 1, 0, 0, 0, 184, 185, 7, 2, 0, 0, 185, 31, 1, 0, 0, 0, 186, 188, 3, 44, 22, 0, 187,
        186, 1, 0, 0, 0, 187, 188, 1, 0, 0, 0, 188, 189, 1, 0, 0, 0, 189, 194, 3, 34, 17, 0, 190,
        191, 7, 3, 0, 0, 191, 193, 3, 34, 17, 0, 192, 190, 1, 0, 0, 0, 193, 196, 1, 0, 0, 0, 194,
        192, 1, 0, 0, 0, 194, 195, 1, 0, 0, 0, 195, 33, 1, 0, 0, 0, 196, 194, 1, 0, 0, 0, 197, 202,
        3, 36, 18, 0, 198, 199, 7, 4, 0, 0, 199, 201, 3, 36, 18, 0, 200, 198, 1, 0, 0, 0, 201,
        204, 1, 0, 0, 0, 202, 200, 1, 0, 0, 0, 202, 203, 1, 0, 0, 0, 203, 35, 1, 0, 0, 0, 204, 202,
        1, 0, 0, 0, 205, 210, 3, 38, 19, 0, 206, 207, 5, 27, 0, 0, 207, 209, 3, 38, 19, 0, 208,
        206, 1, 0, 0, 0, 209, 212, 1, 0, 0, 0, 210, 208, 1, 0, 0, 0, 210, 211, 1, 0, 0, 0, 211,
        37, 1, 0, 0, 0, 212, 210, 1, 0, 0, 0, 213, 220, 3, 8, 4, 0, 214, 220, 3, 40, 20, 0, 215,
        216, 5, 15, 0, 0, 216, 217, 3, 28, 14, 0, 217, 218, 5, 16, 0, 0, 218, 220, 1, 0, 0, 0,
        219, 213, 1, 0, 0, 0, 219, 214, 1, 0, 0, 0, 219, 215, 1, 0, 0, 0, 220, 39, 1, 0, 0, 0, 221,
        225, 3, 50, 25, 0, 222, 225, 3, 52, 26, 0, 223, 225, 3, 58, 29, 0, 224, 221, 1, 0, 0,
        0, 224, 222, 1, 0, 0, 0, 224, 223, 1, 0, 0, 0, 225, 41, 1, 0, 0, 0, 226, 227, 7, 5, 0, 0,
        227, 43, 1, 0, 0, 0, 228, 229, 7, 3, 0, 0, 229, 45, 1, 0, 0, 0, 230, 231, 7, 6, 0, 0, 231,
        47, 1, 0, 0, 0, 232, 233, 7, 7, 0, 0, 233, 49, 1, 0, 0, 0, 234, 236, 3, 44, 22, 0, 235,
        234, 1, 0, 0, 0, 235, 236, 1, 0, 0, 0, 236, 237, 1, 0, 0, 0, 237, 238, 3, 54, 27, 0, 238,
        51, 1, 0, 0, 0, 239, 240, 3, 56, 28, 0, 240, 241, 5, 35, 0, 0, 241, 242, 3, 56, 28, 0,
        242, 53, 1, 0, 0, 0, 243, 247, 5, 41, 0, 0, 244, 246, 5, 41, 0, 0, 245, 244, 1, 0, 0, 0,
        246, 249, 1, 0, 0, 0, 247, 245, 1, 0, 0, 0, 247, 248, 1, 0, 0, 0, 248, 55, 1, 0, 0, 0, 249,
        247, 1, 0, 0, 0, 250, 251, 3, 54, 27, 0, 251, 252, 5, 35, 0, 0, 252, 253, 3, 54, 27, 0,
        253, 57, 1, 0, 0, 0, 254, 255, 7, 8, 0, 0, 255, 59, 1, 0, 0, 0, 24, 65, 67, 72, 76, 84,
        87, 98, 105, 110, 115, 119, 125, 133, 141, 170, 181, 187, 194, 202, 210, 219, 224,
        235, 247
    ]


class QuillParser(Parser):
    grammarFileName = "Quill.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "';'", "','", "'_'", "':'", "'='", "'if'",
                    "'{'", "'}'", "'else'", "'for'", "'in'", "'while'",
                    "'readLine()'", "'print'", "'('", "')'", "'=='", "'<='",
                    "'<'", "'>'", "'>='", "'!='", "'+'", "'-'", "'*'",
                    "'/'", "'^'", "'var'", "'let'", "'Int'", "'Float'",
                    "'Bool'", "'...'", "'..<'", "'.'", "'true'", "'false'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "COMMENT", "LETTER", "UNICODE_SYMBOL",
                     "DIGIT", "NEWLINE", "WS"]

    RULE_program = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_declaration = 3
    RULE_ident = 4
    RULE_declarationExpression = 5
    RULE_assign = 6
    RULE_ifStatement = 7
    RULE_ifTail = 8
    RULE_forStatement = 9
    RULE_rangeExpr = 10
    RULE_whileStatement = 11
    RULE_inp = 12
    RULE_out = 13
    RULE_expression = 14
    RULE_relOp = 15
    RULE_arithmExpression = 16
    RULE_term = 17
    RULE_exponent = 18
    RULE_factor = 19
    RULE_constant = 20
    RULE_declarationKeyword = 21
    RULE_sign = 22
    RULE_type = 23
    RULE_rangeOp = 24
    RULE_intNumb = 25
    RULE_floatNumb = 26
    RULE_unsignedInt = 27
    RULE_unsignedFloat = 28
    RULE_boolConst = 29

    ruleNames = ["program", "statementList", "statement", "declaration",
                 "ident", "declarationExpression", "assign", "ifStatement",
                 "ifTail", "forStatement", "rangeExpr", "whileStatement",
                 "inp", "out", "expression", "relOp", "arithmExpression",
                 "term", "exponent", "factor", "constant", "declarationKeyword",
                 "sign", "type", "rangeOp", "intNumb", "floatNumb", "unsignedInt",
                 "unsignedFloat", "boolConst"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    COMMENT = 38
    LETTER = 39
    UNICODE_SYMBOL = 40
    DIGIT = 41
    NEWLINE = 42
    WS = 43

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(QuillParser.StatementListContext, 0)

        def EOF(self):
            return self.getToken(QuillParser.EOF, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_program

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

    def program(self):

        localctx = QuillParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.statementList()
            self.state = 61
            self.match(QuillParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.StatementContext)
            else:
                return self.getTypedRuleContext(QuillParser.StatementContext, i)

        def COMMENT(self, i: int = None):
            if i is None:
                return self.getTokens(QuillParser.COMMENT)
            else:
                return self.getToken(QuillParser.COMMENT, i)

        def getRuleIndex(self):
            return QuillParser.RULE_statementList

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatementList"):
                listener.enterStatementList(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatementList"):
                listener.exitStatementList(self)

    def statementList(self):

        localctx = QuillParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6322997187656) != 0):
                self.state = 65
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 0, self._ctx)
                if la_ == 1:
                    self.state = 63
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 64
                    self.match(QuillParser.COMMENT)
                    pass

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(QuillParser.DeclarationContext, 0)

        def assign(self):
            return self.getTypedRuleContext(QuillParser.AssignContext, 0)

        def ifStatement(self):
            return self.getTypedRuleContext(QuillParser.IfStatementContext, 0)

        def forStatement(self):
            return self.getTypedRuleContext(QuillParser.ForStatementContext, 0)

        def whileStatement(self):
            return self.getTypedRuleContext(QuillParser.WhileStatementContext, 0)

        def COMMENT(self):
            return self.getToken(QuillParser.COMMENT, 0)

        def out(self):
            return self.getTypedRuleContext(QuillParser.OutContext, 0)

        def NEWLINE(self):
            return self.getToken(QuillParser.NEWLINE, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_statement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStatement"):
                listener.enterStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStatement"):
                listener.exitStatement(self)

    def statement(self):

        localctx = QuillParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0  # Token type
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.declaration()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 1:
                    self.state = 71
                    self.match(QuillParser.T__0)

                pass
            elif token in [3, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.assign()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 1:
                    self.state = 75
                    self.match(QuillParser.T__0)

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.ifStatement()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.forStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.whileStatement()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 6)
                self.state = 81
                self.match(QuillParser.COMMENT)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 7)
                self.state = 82
                self.out()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 1:
                    self.state = 83
                    self.match(QuillParser.T__0)

                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.match(QuillParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationKeyword(self):
            return self.getTypedRuleContext(QuillParser.DeclarationKeywordContext, 0)

        def ident(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.IdentContext)
            else:
                return self.getTypedRuleContext(QuillParser.IdentContext, i)

        def declarationExpression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.DeclarationExpressionContext)
            else:
                return self.getTypedRuleContext(QuillParser.DeclarationExpressionContext, i)

        def getRuleIndex(self):
            return QuillParser.RULE_declaration

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)

    def declaration(self):

        localctx = QuillParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.declarationKeyword()
            self.state = 90
            self.ident()
            self.state = 91
            self.declarationExpression()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 2:
                self.state = 92
                self.match(QuillParser.T__1)
                self.state = 93
                self.ident()
                self.state = 94
                self.declarationExpression()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i: int = None):
            if i is None:
                return self.getTokens(QuillParser.LETTER)
            else:
                return self.getToken(QuillParser.LETTER, i)

        def UNICODE_SYMBOL(self, i: int = None):
            if i is None:
                return self.getTokens(QuillParser.UNICODE_SYMBOL)
            else:
                return self.getToken(QuillParser.UNICODE_SYMBOL, i)

        def DIGIT(self, i: int = None):
            if i is None:
                return self.getTokens(QuillParser.DIGIT)
            else:
                return self.getToken(QuillParser.DIGIT, i)

        def getRuleIndex(self):
            return QuillParser.RULE_ident

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdent"):
                listener.enterIdent(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdent"):
                listener.exitIdent(self)

    def ident(self):

        localctx = QuillParser.IdentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ident)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 1649267441672) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 102
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697224) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(QuillParser.ExpressionContext, 0)

        def inp(self):
            return self.getTypedRuleContext(QuillParser.InpContext, 0)

        def type_(self):
            return self.getTypedRuleContext(QuillParser.TypeContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_declarationExpression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDeclarationExpression"):
                listener.enterDeclarationExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDeclarationExpression"):
                listener.exitDeclarationExpression(self)

    def declarationExpression(self):

        localctx = QuillParser.DeclarationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declarationExpression)
        self._la = 0  # Token type
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 10, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 4:
                    self.state = 108
                    self.match(QuillParser.T__3)
                    self.state = 109
                    self.type_()

                self.state = 112
                self.match(QuillParser.T__4)
                self.state = 115
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 15, 23, 24, 36, 37, 39, 40, 41]:
                    self.state = 113
                    self.expression()
                    pass
                elif token in [13]:
                    self.state = 114
                    self.inp()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(QuillParser.T__3)
                self.state = 118
                self.type_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(QuillParser.IdentContext, 0)

        def expression(self):
            return self.getTypedRuleContext(QuillParser.ExpressionContext, 0)

        def inp(self):
            return self.getTypedRuleContext(QuillParser.InpContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_assign

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAssign"):
                listener.enterAssign(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAssign"):
                listener.exitAssign(self)

    def assign(self):

        localctx = QuillParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.ident()
            self.state = 122
            self.match(QuillParser.T__4)
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 15, 23, 24, 36, 37, 39, 40, 41]:
                self.state = 123
                self.expression()
                pass
            elif token in [13]:
                self.state = 124
                self.inp()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(QuillParser.ExpressionContext, 0)

        def statementList(self):
            return self.getTypedRuleContext(QuillParser.StatementListContext, 0)

        def ifTail(self):
            return self.getTypedRuleContext(QuillParser.IfTailContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_ifStatement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIfStatement"):
                listener.enterIfStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIfStatement"):
                listener.exitIfStatement(self)

    def ifStatement(self):

        localctx = QuillParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifStatement)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(QuillParser.T__5)
            self.state = 128
            self.expression()
            self.state = 129
            self.match(QuillParser.T__6)
            self.state = 130
            self.statementList()
            self.state = 131
            self.match(QuillParser.T__7)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 9:
                self.state = 132
                self.ifTail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfTailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(QuillParser.IfStatementContext, 0)

        def statementList(self):
            return self.getTypedRuleContext(QuillParser.StatementListContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_ifTail

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIfTail"):
                listener.enterIfTail(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIfTail"):
                listener.exitIfTail(self)

    def ifTail(self):

        localctx = QuillParser.IfTailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifTail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(QuillParser.T__8)
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 136
                self.match(QuillParser.T__6)
                self.state = 137
                self.statementList()
                self.state = 138
                self.match(QuillParser.T__7)
                pass
            elif token in [6]:
                self.state = 140
                self.ifStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(QuillParser.IdentContext, 0)

        def rangeExpr(self):
            return self.getTypedRuleContext(QuillParser.RangeExprContext, 0)

        def statementList(self):
            return self.getTypedRuleContext(QuillParser.StatementListContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_forStatement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterForStatement"):
                listener.enterForStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitForStatement"):
                listener.exitForStatement(self)

    def forStatement(self):

        localctx = QuillParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(QuillParser.T__9)
            self.state = 144
            self.ident()
            self.state = 145
            self.match(QuillParser.T__10)
            self.state = 146
            self.rangeExpr()
            self.state = 147
            self.match(QuillParser.T__6)
            self.state = 148
            self.statementList()
            self.state = 149
            self.match(QuillParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuillParser.ExpressionContext, i)

        def rangeOp(self):
            return self.getTypedRuleContext(QuillParser.RangeOpContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_rangeExpr

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRangeExpr"):
                listener.enterRangeExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRangeExpr"):
                listener.exitRangeExpr(self)

    def rangeExpr(self):

        localctx = QuillParser.RangeExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_rangeExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.expression()
            self.state = 152
            self.rangeOp()
            self.state = 153
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(QuillParser.ExpressionContext, 0)

        def statementList(self):
            return self.getTypedRuleContext(QuillParser.StatementListContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_whileStatement

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterWhileStatement"):
                listener.enterWhileStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitWhileStatement"):
                listener.exitWhileStatement(self)

    def whileStatement(self):

        localctx = QuillParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(QuillParser.T__11)
            self.state = 156
            self.expression()
            self.state = 157
            self.match(QuillParser.T__6)
            self.state = 158
            self.statementList()
            self.state = 159
            self.match(QuillParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return QuillParser.RULE_inp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInp"):
                listener.enterInp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInp"):
                listener.exitInp(self)

    def inp(self):

        localctx = QuillParser.InpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(QuillParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OutContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(QuillParser.ExpressionContext, i)

        def getRuleIndex(self):
            return QuillParser.RULE_out

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOut"):
                listener.enterOut(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOut"):
                listener.exitOut(self)

    def out(self):

        localctx = QuillParser.OutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_out)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(QuillParser.T__13)
            self.state = 164
            self.match(QuillParser.T__14)
            self.state = 165
            self.expression()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 2:
                self.state = 166
                self.match(QuillParser.T__1)
                self.state = 167
                self.expression()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(QuillParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmExpression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.ArithmExpressionContext)
            else:
                return self.getTypedRuleContext(QuillParser.ArithmExpressionContext, i)

        def relOp(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.RelOpContext)
            else:
                return self.getTypedRuleContext(QuillParser.RelOpContext, i)

        def getRuleIndex(self):
            return QuillParser.RULE_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)

    def expression(self):

        localctx = QuillParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.arithmExpression()
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0):
                self.state = 176
                self.relOp()
                self.state = 177
                self.arithmExpression()
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return QuillParser.RULE_relOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRelOp"):
                listener.enterRelOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRelOp"):
                listener.exitRelOp(self)

    def relOp(self):

        localctx = QuillParser.RelOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_relOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8257536) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArithmExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.TermContext)
            else:
                return self.getTypedRuleContext(QuillParser.TermContext, i)

        def sign(self):
            return self.getTypedRuleContext(QuillParser.SignContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_arithmExpression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArithmExpression"):
                listener.enterArithmExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArithmExpression"):
                listener.exitArithmExpression(self)

    def arithmExpression(self):

        localctx = QuillParser.ArithmExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arithmExpression)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 16, self._ctx)
            if la_ == 1:
                self.state = 186
                self.sign()

            self.state = 189
            self.term()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 23 or _la == 24:
                self.state = 190
                _la = self._input.LA(1)
                if not (_la == 23 or _la == 24):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.term()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponent(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.ExponentContext)
            else:
                return self.getTypedRuleContext(QuillParser.ExponentContext, i)

        def getRuleIndex(self):
            return QuillParser.RULE_term

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterTerm"):
                listener.enterTerm(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitTerm"):
                listener.exitTerm(self)

    def term(self):

        localctx = QuillParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.exponent()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 25 or _la == 26:
                self.state = 198
                _la = self._input.LA(1)
                if not (_la == 25 or _la == 26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.exponent()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.FactorContext)
            else:
                return self.getTypedRuleContext(QuillParser.FactorContext, i)

        def getRuleIndex(self):
            return QuillParser.RULE_exponent

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExponent"):
                listener.enterExponent(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExponent"):
                listener.exitExponent(self)

    def exponent(self):

        localctx = QuillParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exponent)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.factor()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 27:
                self.state = 206
                self.match(QuillParser.T__26)
                self.state = 207
                self.factor()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ident(self):
            return self.getTypedRuleContext(QuillParser.IdentContext, 0)

        def constant(self):
            return self.getTypedRuleContext(QuillParser.ConstantContext, 0)

        def expression(self):
            return self.getTypedRuleContext(QuillParser.ExpressionContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_factor

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFactor"):
                listener.enterFactor(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFactor"):
                listener.exitFactor(self)

    def factor(self):

        localctx = QuillParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        try:
            self.state = 219
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.ident()
                pass
            elif token in [23, 24, 36, 37, 41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.constant()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.match(QuillParser.T__14)
                self.state = 216
                self.expression()
                self.state = 217
                self.match(QuillParser.T__15)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def intNumb(self):
            return self.getTypedRuleContext(QuillParser.IntNumbContext, 0)

        def floatNumb(self):
            return self.getTypedRuleContext(QuillParser.FloatNumbContext, 0)

        def boolConst(self):
            return self.getTypedRuleContext(QuillParser.BoolConstContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_constant

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConstant"):
                listener.enterConstant(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConstant"):
                listener.exitConstant(self)

    def constant(self):

        localctx = QuillParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_constant)
        try:
            self.state = 224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 21, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.intNumb()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self.floatNumb()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 223
                self.boolConst()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationKeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return QuillParser.RULE_declarationKeyword

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterDeclarationKeyword"):
                listener.enterDeclarationKeyword(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitDeclarationKeyword"):
                listener.exitDeclarationKeyword(self)

    def declarationKeyword(self):

        localctx = QuillParser.DeclarationKeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_declarationKeyword)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            _la = self._input.LA(1)
            if not (_la == 28 or _la == 29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return QuillParser.RULE_sign

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSign"):
                listener.enterSign(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSign"):
                listener.exitSign(self)

    def sign(self):

        localctx = QuillParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sign)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            _la = self._input.LA(1)
            if not (_la == 23 or _la == 24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return QuillParser.RULE_type

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterType"):
                listener.enterType(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitType"):
                listener.exitType(self)

    def type_(self):

        localctx = QuillParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_type)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RangeOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return QuillParser.RULE_rangeOp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRangeOp"):
                listener.enterRangeOp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRangeOp"):
                listener.exitRangeOp(self)

    def rangeOp(self):

        localctx = QuillParser.RangeOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_rangeOp)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            _la = self._input.LA(1)
            if not (_la == 33 or _la == 34):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IntNumbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unsignedInt(self):
            return self.getTypedRuleContext(QuillParser.UnsignedIntContext, 0)

        def sign(self):
            return self.getTypedRuleContext(QuillParser.SignContext, 0)

        def getRuleIndex(self):
            return QuillParser.RULE_intNumb

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIntNumb"):
                listener.enterIntNumb(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIntNumb"):
                listener.exitIntNumb(self)

    def intNumb(self):

        localctx = QuillParser.IntNumbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_intNumb)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == 23 or _la == 24:
                self.state = 234
                self.sign()

            self.state = 237
            self.unsignedInt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FloatNumbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unsignedFloat(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.UnsignedFloatContext)
            else:
                return self.getTypedRuleContext(QuillParser.UnsignedFloatContext, i)

        def getRuleIndex(self):
            return QuillParser.RULE_floatNumb

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFloatNumb"):
                listener.enterFloatNumb(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFloatNumb"):
                listener.exitFloatNumb(self)

    def floatNumb(self):

        localctx = QuillParser.FloatNumbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_floatNumb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.unsignedFloat()
            self.state = 240
            self.match(QuillParser.T__34)
            self.state = 241
            self.unsignedFloat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnsignedIntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self, i: int = None):
            if i is None:
                return self.getTokens(QuillParser.DIGIT)
            else:
                return self.getToken(QuillParser.DIGIT, i)

        def getRuleIndex(self):
            return QuillParser.RULE_unsignedInt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUnsignedInt"):
                listener.enterUnsignedInt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUnsignedInt"):
                listener.exitUnsignedInt(self)

    def unsignedInt(self):

        localctx = QuillParser.UnsignedIntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unsignedInt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(QuillParser.DIGIT)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 41:
                self.state = 244
                self.match(QuillParser.DIGIT)
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnsignedFloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unsignedInt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(QuillParser.UnsignedIntContext)
            else:
                return self.getTypedRuleContext(QuillParser.UnsignedIntContext, i)

        def getRuleIndex(self):
            return QuillParser.RULE_unsignedFloat

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUnsignedFloat"):
                listener.enterUnsignedFloat(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUnsignedFloat"):
                listener.exitUnsignedFloat(self)

    def unsignedFloat(self):

        localctx = QuillParser.UnsignedFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unsignedFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.unsignedInt()
            self.state = 251
            self.match(QuillParser.T__34)
            self.state = 252
            self.unsignedInt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BoolConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return QuillParser.RULE_boolConst

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBoolConst"):
                listener.enterBoolConst(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBoolConst"):
                listener.exitBoolConst(self)

    def boolConst(self):

        localctx = QuillParser.BoolConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_boolConst)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            _la = self._input.LA(1)
            if not (_la == 36 or _la == 37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
