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


class IllegalIfStatement(Exception):
    def __init__(self, current_line, current_lexeme, current_token):
        self.message = (
            f"Encountered illegal if statement on line {current_line} with token {(current_lexeme, current_token)}. "
            f"Expected to get '{{' or 'else' "
        )
        super().__init__(self.message)
