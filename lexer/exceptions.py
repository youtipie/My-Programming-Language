class IllegalSymbolError(Exception):
    def __init__(self, symbol, line, lexeme, message="Illegal symbol encountered"):
        self.message = f"{lexeme} <--\n{message}: '{symbol}' at line {line}"
        super().__init__(self.message)


class LexerError(Exception):
    def __init__(self, line, status_code, lexeme, message="Encountered error during lexical analyze"):
        self.message = f"{lexeme} <--\n{message} with code {status_code}: Encountered illegal symbol at line {line}."

        if status_code == 101:
            pass
        elif status_code == 102:
            self.message += f" Expected symbol is '='"
        elif status_code == 103:
            self.message += f" Expected symbol is '.'"
        elif status_code == 104:
            self.message += f" Expected symbol has to be digit"
        else:
            self.message += "Unknown error"
        super().__init__(self.message)
