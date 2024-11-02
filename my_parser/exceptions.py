class ParserError(Exception):
    def __init__(self):
        self.message = f"Unexpected end of program."
        super().__init__(self.message)


class UnexpectedToken(Exception):
    def __init__(self, current_line, current_lexeme, current_token, expected_lexeme, expected_token):
        self.message = f"Unexpected token encountered on line {current_line}: {(current_lexeme, current_token)}."
        if expected_lexeme and expected_token:
            self.message += f" Expected {(expected_lexeme, expected_token)}"
        super().__init__(self.message)


class UnexpectedStatement(UnexpectedToken):
    def __init__(self, current_line, current_lexeme, current_token):
        super().__init__(current_line, current_lexeme, current_token, None, None)
        self.message += ("Available statements: Declaration | Assign | IfStatement | ForStatement | WhileStatement | "
                         "Comment | Out")


class IllegalExpression(Exception):
    def __init__(self, current_line, current_lexeme, current_token):
        self.message = f"Encountered illegal expression on line {current_line}: {(current_lexeme, current_token)}"
        super().__init__(self.message)


class IllegalDeclaration(Exception):
    def __init__(self, current_line):
        self.message = (f"Encountered illegal declaration on line {current_line}: declared variables neither "
                        f"initialized and have no type.")
        super().__init__(self.message)


class IllegalReadLine(Exception):
    def __init__(self, current_line):
        self.message = (f"Encountered illegal readLine use on line {current_line}: "
                        f"declared variable must have explicit type!")
        super().__init__(self.message)


class RedeclarationError(Exception):
    def __init__(self, current_line, ident):
        self.message = f"Encountered redeclaration on line {current_line}: {ident}"
        super().__init__(self.message)


class IllegalIfStatement(Exception):
    def __init__(self, current_line, current_lexeme, current_token):
        self.message = (
            f"Encountered illegal if statement on line {current_line} with token {(current_lexeme, current_token)}. "
            f"Expected to get '{{' or 'else' "
        )
        super().__init__(self.message)


class UnknownType(Exception):
    def __init__(self, l_type, op, r_type):
        self.message = (
            f"Cannot get type of expression {(l_type, op, r_type)}"
        )
        super().__init__(self.message)


class IllegalType(Exception):
    def __init__(self, current_line, expected_type, actual_type):
        self.message = (
            f"Encountered illegal type on line {current_line}. Expected {expected_type}, got {actual_type}"
        )
        super().__init__(self.message)


class IllegalBoolExpression(Exception):
    def __init__(self, l_type, op, r_type):
        self.message = (
            f"Encountered illegal bool expression: cannot use operator '{op}' between '{l_type}' and '{r_type}'"
        )
        super().__init__(self.message)
