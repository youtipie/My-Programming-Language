letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
    "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z"
]

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

signs = [
    ".", ",", ":", ";", "=", "*", "+", "-", "/", "^", "(", ")", "<", ">", "!", "{", "}", "_"
]

type_to_token = {
    "Int": "intnum",
    "Float": "floatnum",
    "Bool": "boolval"
}

lexer_config = {
    "token_table": {
        "true": "boolval", "false": "boolval",
        "var": "keyword", "let": "keyword",
        "for": "keyword",
        "while": "keyword", "in": "keyword", "if": "keyword", "else": "keyword", "readLine": "keyword",
        "print": "keyword", "Int": "keyword", "Float": "keyword", "Bool": "keyword",
        "=": "assign_op",
        "+": "add_op", "-": "add_op",
        "*": "mult_op", "/": "mult_op",
        "^": "power_op",
        "...": "range_op", "..<": "range_op",
        "==": "rel_op", "<=": "rel_op", "<": "rel_op", ">=": "rel_op", ">": "rel_op", "!=": "rel_op",
        "(": "brackets_op", ")": "brackets_op", "{": "brackets_op", "}": "brackets_op",
        ".": "punct", ",": "punct", ":": "punct", ";": "punct",
        " ": "ws", "\t": "ws",
        "\n": "eol"
    },
    "tok_state_table": {4: "id", 10: "intnum", 13: "floatnum"},
    "stf": {
        (0, "ws"): 0,
        (0, "other"): 101,
        (0, "eol"): 1,
        (0, "{"): 2, (0, "}"): 2, (0, "^"): 2, (0, ":"): 2, (0, ";"): 2, (0, "*"): 2, (0, "+"): 2, (0, "("): 2,
        (0, ")"): 2,
        (0, ","): 2, (0, "-"): 2,
        (0, "Letter"): 3, (0, "UnicodeSymbol"): 3, (0, "_"): 3, (3, "Letter"): 3, (3, "UnicodeSymbol"): 3,
        (3, "Digit"): 3,
        (3, "_"): 3, (3, "other"): 4,
        (0, "/"): 5, (5, "other"): 8, (5, "/"): 6, (6, "other"): 6, (6, "eol"): 7,
        (0, "Digit"): 9, (9, "Digit"): 9, (9, "other"): 10, (9, "dot"): 11, (11, "Digit"): 12, (11, "other"): 104,
        (11, "dot"): 10,
        (12, "Digit"): 12, (12, "other"): 13,
        (0, ">"): 14, (0, "<"): 14, (0, "="): 14, (14, "="): 16, (14, "other"): 15,
        (0, "!"): 17, (17, "="): 18, (17, "other"): 102,
        (0, "dot"): 19, (19, "dot"): 20, (20, "dot"): 21, (20, "<"): 21, (19, "other"): 103, (20, "other"): 103
    },
    "initial_state": 0,
    "F": [1, 2, 4, 7, 8, 10, 13, 15, 16, 18, 21, 101, 102, 103, 104],
    "F_star": [4, 8, 10, 13, 15],
    "F_error": [101, 102, 103, 104]
}
