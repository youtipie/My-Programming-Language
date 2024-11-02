import unicodedata

from lexer.config import letters, digits, signs
from lexer.utils import print_table
from lexer.exceptions import IllegalSymbolError, LexerError


class Lexer:
    _current_position: int = 0
    _current_line: int = 1
    _current_state: int = 0
    _current_lexeme: str = 0
    _source_code: str = None

    _table_of_symbols: list = []
    _table_of_identifiers: list = []
    _table_of_constants: dict = {}

    def __init__(self, token_table: dict, tok_state_table: dict, stf: dict, F: list, F_star: list, F_error: list,
                 initial_state: int = 0):
        self._token_table: dict = token_table
        self._tok_state_table: dict = tok_state_table
        self._stf: dict = stf
        self._F: list = F
        self._F_star: list = F_star
        self._F_error: list = F_error
        self._initial_state: int = initial_state
        self._current_state = initial_state

    def analyze(self, source_code: str, verbose=True):
        self._source_code = source_code
        self._current_position = -1
        self._current_line = 1
        self._current_lexeme = ""
        self._table_of_symbols = []
        self._table_of_identifiers = []
        self._table_of_constants = {}

        while self._current_position < len(self._source_code) - 1:
            next_char = self._get_next_char()
            char_class = self._get_char_class(next_char)
            # print(char_class)
            self._current_state = self._get_next_state(self._current_state, char_class)

            if self._is_final_state(self._current_state):
                self._process_lexeme(next_char)
            elif self._current_state == self._initial_state:
                self._current_lexeme = ""
            else:
                self._current_lexeme += next_char

        # If source code doesn't end with ws or eol then lexeme will be incomplete, so we have to check this manually
        if self._current_lexeme:
            self._current_state = self._get_next_state(self._current_state, "other")
            if self._is_final_state(self._current_state):
                self._process_lexeme("")

        if verbose:
            print("Lexer finished successfully with following results:")
            print(f"Table of symbols:")
            print_table(self._table_of_symbols)
            print(f"Table of identifiers: {self._table_of_identifiers}")
            print(f"Table of constants:")
            print(self._table_of_constants)

        return self._table_of_symbols, self._table_of_identifiers, self._table_of_constants

    def _process_lexeme(self, next_char: str):
        if self._current_state == 1:
            self._current_lexeme += next_char
            token = self._get_token(self._current_state, self._current_lexeme)
            self._add_to_table_of_symbols(token, None)
            self._current_lexeme = ""
            self._current_state = self._initial_state
            self._current_line += 1
            return
        if self._current_state == 7:
            self._current_lexeme = "\n"
            self._add_to_table_of_symbols("eol", None)
            self._current_lexeme = ""
            self._current_state = self._initial_state
            self._current_line += 1
        elif self._current_state in self._F_star:
            token = self._get_token(self._current_state, self._current_lexeme)
            index = None
            if token == "id":
                if self._current_lexeme not in self._table_of_identifiers:
                    self._table_of_identifiers.append(self._current_lexeme)
                index = self._table_of_identifiers.index(self._current_lexeme)
            elif token in ["intnum", "floatnum", "boolval"]:
                if self._current_lexeme[-1] == ".":
                    self._current_lexeme = self._current_lexeme[:-1]
                    self._put_char_back()
                if self._current_lexeme not in self._table_of_constants:
                    self._table_of_constants[self._current_lexeme] = token
                index = list(self._table_of_constants.keys()).index(self._current_lexeme)

            self._add_to_table_of_symbols(token, index)
            self._put_char_back()
            self._current_lexeme = ""
            self._current_state = self._initial_state
        elif self._current_state in self._F_error:
            raise LexerError(self._current_line, self._current_state, self._current_lexeme)
        elif self._current_state in self._F:
            self._current_lexeme += next_char
            token = self._get_token(self._current_state, self._current_lexeme)
            self._add_to_table_of_symbols(token, None)
            self._current_lexeme = ""
            self._current_state = self._initial_state

    def _is_final_state(self, state: int) -> bool:
        return state in self._F

    def _get_next_state(self, state: int, char_class: str) -> int:
        if (state, char_class) in self._stf.keys():
            return self._stf[(state, char_class)]
        else:
            return self._stf[(state, "other")]

    def _get_next_char(self) -> str:
        self._current_position += 1
        return self._source_code[self._current_position]

    def _put_char_back(self) -> None:
        self._current_position -= 1

    def _get_char_class(self, char: str) -> str:
        if char == ".":
            return "dot"
        elif char in letters:
            return "Letter"
        elif char in digits:
            return "Digit"
        elif char in [" ", "\t"]:
            return "ws"
        elif char in "\n":
            return "eol"
        elif char in signs:
            return char
        elif unicodedata.category(char) in [
            'Ll', 'Lu', 'Lt', 'Lo', 'Lm', 'Nl', 'Ps', 'Pe', 'Pc', 'Pd', 'Ps', 'So'
        ]:
            return "UnicodeSymbol"
        raise IllegalSymbolError(char, self._current_line, self._current_lexeme)

    def _get_token(self, state: int, lexeme: str) -> str:
        if lexeme in self._token_table:
            return self._token_table[lexeme]
        return self._tok_state_table[state]

    def _add_to_table_of_symbols(self, token, index):
        self._table_of_symbols.append({
            "line": self._current_line,
            "lexeme": self._current_lexeme,
            "token": token,
            "table_index": index
        })
