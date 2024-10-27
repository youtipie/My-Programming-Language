from my_parser.exceptions import ParserError, UnexpectedToken, UnexpectedStatement, IllegalExpression, \
    IllegalDeclaration, IllegalIfStatement

from my_parser.utils import with_indent


class Parser:
    def __init__(self):
        self._current_row = 0
        self._current_indent = 1
        self._table_of_symbols = None

    def analyze(self, table_of_symbols):
        self._current_row = 0
        self._current_indent = 1
        self._table_of_symbols = table_of_symbols
        self._parse_statement_list()

    @with_indent
    def _parse_token(self, lexeme, token):
        if self._current_row == len(self._table_of_symbols):
            raise ParserError()

        current_line, current_lexeme, current_token, _ = self._next_symbol()

        if (current_lexeme, current_token) == (lexeme, token):
            self._log(f"parse_token: line {current_line} token: {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, lexeme, token)
        return True

    def _next_symbol(self, should_increment_row=True):
        try:
            line, lexeme, token, table_index = self._table_of_symbols[self._current_row].values()
            if should_increment_row:
                self._current_row += 1
            return line, lexeme, token, table_index
        except IndexError:
            if should_increment_row:
                raise ParserError
            else:
                return None, None, None, None

    def _parse_eos(self):
        # If this is last line in the file, we accept it
        if self._current_row == len(self._table_of_symbols):
            return True

        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_token != "eol" and (current_lexeme, current_token) != (";", "punct"):
            raise UnexpectedToken(current_line, current_lexeme, current_token, ";", "punct")
        return True

    # StatementList = Statement { (((';' | '\n') Statement) | Comment}.
    @with_indent
    def _parse_statement_list(self):
        self._log("parse_statement_list:")
        while self._parse_statement():
            pass
        return True

    # Statement = Declaration
    # 		| Assign
    # 		| IfStatement
    # 		| ForStatement
    # 		| WhileStatement
    # 		| Comment
    # 		| Out.
    @with_indent
    def _parse_statement(self):
        if self._current_row >= len(self._table_of_symbols):
            return False

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)

        if (current_lexeme, current_token) == ("}", "brackets_op"):
            return False

        if current_token == "eol":
            # Just skip the \n
            self._next_symbol()
            return True

        self._log("parse_statement:")

        if current_lexeme in ("var", "let") and current_token == "keyword":
            self._parse_declaration()
            self._parse_eos()
        elif current_token == "id":
            self._parse_assign()
            self._parse_eos()
        elif (current_lexeme, current_token) == ("if", "keyword"):
            self._parse_if()
        elif (current_lexeme, current_token) == ("for", "keyword"):
            self._parse_for()
        elif (current_lexeme, current_token) == ("while", "keyword"):
            self._parse_while()
        elif (current_lexeme, current_token) == ("print", "keyword"):
            self._parse_out()
            self._parse_eos()
        else:
            raise UnexpectedStatement(current_line, current_lexeme, current_token)
        return True

    # Declaration = DeclarationKeyword Ident DeclarationExpression {',' Ident DeclarationExpression}.
    @with_indent
    def _parse_declaration(self):
        self._log("parse_declaration:")
        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_lexeme in ("var", "let") and current_token == "keyword":
            self._log(f"Declaration keyword: {current_lexeme}")

        self._parse_token_type("id")
        self._parse_declaration_expression()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)

            if (current_lexeme, current_token) == (",", "punct"):
                self._parse_token(",", "punct")
                self._parse_token_type("id")
                self._parse_declaration_expression()
            else:
                break
        return True

    # DeclarationExpression = [':' Type] '=' (Expression | Inp)
    #        				| ':' Type.
    @with_indent
    def _parse_declaration_expression(self):
        is_valid = False
        current_line, current_lexeme, current_token, _ = self._next_symbol(False)

        if (current_lexeme, current_token) == (":", "punct"):
            is_valid = True
            self._parse_token(":", "punct")
            self._parse_type()

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)
        if (current_lexeme, current_token) == ("=", "assign_op"):
            is_valid = True
            self._parse_token("=", "assign_op")

            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if (current_lexeme, current_token) == ("readLine", "keyword"):
                self._parse_token("readLine", "keyword")
                self._parse_token("(", "brackets_op")
                self._parse_token(")", "brackets_op")
            else:
                self._parse_expression()

        if not is_valid:
            raise IllegalDeclaration(current_line)
        return True

    @with_indent
    def _parse_type(self):
        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_token == "keyword" and current_lexeme in ["Int", "Float", "Bool"]:
            self._log(f"parse_type: line {current_line} {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, "Int | Float | Bool", "keyword")
        return True

    @with_indent
    def _parse_token_type(self, expected_token):
        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_token == expected_token:
            self._log(f"parse_{expected_token}: line {current_line} {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, expected_token, expected_token)
        return True

    # Assign = Ident '=' Expression.
    @with_indent
    def _parse_assign(self):
        self._log("parse_assign:")
        self._parse_token_type("id")
        self._parse_token("=", "assign_op")
        self._parse_expression()

    # IfStatement = 'if' Expression '{' StatementList '}' [IfTail].
    @with_indent
    def _parse_if(self):
        self._log("parse_if:")
        self._parse_token("if", "keyword")
        self._parse_expression()
        self._parse_token("{", "brackets_op")
        self._parse_statement_list()
        self._parse_token("}", "brackets_op")
        if self._current_row < len(self._table_of_symbols):
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if (current_lexeme, current_token) == ("else", "keyword"):
                self._parse_token("else", "keyword")
                self._parse_if_tail()
        return True

    # IfTail = 'else' ('{' StatementList '}' | IfStatement).
    @with_indent
    def _parse_if_tail(self):
        self._log("parse_if_tail:")

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)
        if (current_lexeme, current_token) == ("{", "brackets_op"):
            self._parse_token("{", "brackets_op")
            self._parse_statement_list()
            self._parse_token("}", "brackets_op")
        elif (current_lexeme, current_token) == ("if", "keyword"):
            self._parse_if()
        else:
            raise IllegalIfStatement(current_line, current_lexeme, current_token)

        return True

    # ForStatement = 'for' Ident 'in' RangeExpr '{' StatementList '}'.
    @with_indent
    def _parse_for(self):
        self._log("parse_for:")

        self._parse_token("for", "keyword")
        self._parse_token_type("id")
        self._parse_token("in", "keyword")
        self._parse_range_expression()
        self._parse_token("{", "brackets_op")
        self._parse_statement_list()
        self._parse_token("}", "brackets_op")

        return True

    # RangeExpr = Expression RangeOp Expression.
    @with_indent
    def _parse_range_expression(self):
        self._log("parse_range_expression:")
        self._parse_expression()

        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_lexeme in ["...", "..<"] and current_token == "range_op":
            self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, "... | ..<", "range_op")

        self._parse_expression()
        return True

    # WhileStatement = 'while' Expression '{' StatementList '}'.
    @with_indent
    def _parse_while(self):
        self._log("parse_while:")

        self._parse_token("while", "keyword")
        self._parse_expression()
        self._parse_token("{", "brackets_op")
        self._parse_statement_list()
        self._parse_token("}", "brackets_op")

        return True

    # Out = 'print' '(' Expression {',' Expression} ')'.
    @with_indent
    def _parse_out(self):
        self._log("parse_out:")

        self._parse_token("print", "keyword")
        self._parse_token("(", "brackets_op")
        self._parse_expression()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if (current_lexeme, current_token) == (",", "punct"):
                self._parse_token(",", "punct")
                self._parse_expression()
            else:
                break

        self._parse_token(")", "brackets_op")
        return True

    # Expression = ArithmExpression
    # 		| BoolExpr.
    @with_indent
    def _parse_expression(self):
        self._log("parse_expression:")

        self._parse_arithm_expression()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)

            if current_token == "rel_op":
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                self._next_symbol()
                self._parse_arithm_expression()
            else:
                break

        return True

    # ArithmExpression = [Sign] Term { '+' | '-' Term }.
    @with_indent
    def _parse_arithm_expression(self):
        self._log("parse_arithm_expression:")

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)

        if current_lexeme in ('+', '-'):
            self._next_symbol()
            self._log(f"line {current_line} unary operator: {(current_lexeme, current_token)}")

        self._parse_term()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if current_token == "add_op":
                self._next_symbol()
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                self._parse_term()
            else:
                break

        return True

    # Term = Exponent { '*' | '/' Exponent }.
    @with_indent
    def _parse_term(self):
        self._log("parse_term:")

        self._parse_exponent()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if current_token == "mult_op":
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                self._next_symbol()
                self._parse_exponent()
            else:
                break

        return True

    # Exponent = Factor { '^' Factor }.
    @with_indent
    def _parse_exponent(self):
        self._log("parse_exponent:")

        self._parse_factor()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if current_token == "power_op":
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                self._next_symbol()
                self._parse_factor()
            else:
                break
        return True

    # Factor = Ident
    # 	| Const
    # 	| '(' ArithmExpression ')'.
    @with_indent
    def _parse_factor(self):
        self._log("parse_factor:")

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)

        if current_token in ('intnum', "floatnum", "boolval", "id"):
            self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
            self._next_symbol()
        elif current_lexeme == '(':
            self._parse_token("(", "brackets_op")
            self._parse_expression()
            self._parse_token(")", "brackets_op")
        else:
            raise IllegalExpression(current_line, current_lexeme, current_token)
        return True

    def _log(self, *args):
        print(self._current_indent * "│  ", end="")
        print("└──", *args)

    def _next_indent(self):
        self._current_indent += 1

    def _prev_indent(self):
        self._current_indent -= 1
