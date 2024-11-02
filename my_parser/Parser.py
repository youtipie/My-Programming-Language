from lexer.config import type_to_token
from my_parser.exceptions import ParserError, UnexpectedToken, UnexpectedStatement, IllegalExpression, \
    IllegalDeclaration, IllegalIfStatement, RedeclarationError, IllegalType, UnknownType, IllegalBoolExpression, \
    IllegalReadLine

from my_parser.utils import with_indent


class Parser:
    def __init__(self):
        self._current_row = 0
        self._current_indent = 1
        self._table_of_symbols = None
        self._table_of_constants = None
        self._scope_stack = []

    def analyze(self, table_of_symbols, table_of_constants):
        self._current_row = 0
        self._current_indent = 1
        self._table_of_symbols = table_of_symbols
        self._table_of_constants = table_of_constants
        self._scope_stack = [{}]
        self._parse_statement_list()

    def _enter_scope(self):
        self._scope_stack.append({})
        self._log("Entering new scope")

    def _exit_scope(self):
        exited_scope = self._scope_stack.pop()
        self._log("Exiting scope, removed variables:", exited_scope)

    def _add_variable(self, ident, var_type, is_initialized, line):
        current_scope = self._scope_stack[-1]
        if ident in current_scope:
            raise RedeclarationError(line, ident)
        current_scope[ident] = {"var_type": var_type, "is_initialized": is_initialized}
        self._log(f"Added variable '{ident}' to current scope:", current_scope)

    def _find_variable(self, ident):
        for scope in reversed(self._scope_stack):
            if ident in scope:
                return scope[ident]
        raise NameError(f"Variable '{ident}' not declared")

    def _initialize_variable(self, ident):
        variable = self._find_variable(ident)
        variable["is_initialized"] = True

    def _check_is_initialized(self, ident):
        if not self._find_variable(ident)["is_initialized"]:
            raise ValueError(f"Cannot use not initialized variable '{ident}'!")

    def _get_ident_type(self, ident):
        return self._find_variable(ident)["var_type"]

    def _get_const_type(self, literal):
        return self._table_of_constants[literal]

    def _get_op_type(self, l_type, op, r_type):
        is_num = l_type in ("intnum", "floatnum") and r_type in ("intnum", "floatnum")
        is_bool = l_type == "boolval" and r_type == "boolval"

        if is_num and op in "/":
            return "floatnum"
        elif "floatnum" in (l_type, r_type) and op in "+-*^":
            return "floatnum"
        elif is_num and op in "+-*^":
            return l_type
        if is_bool and op in ("==", "!="):
            return "boolval"
        elif is_num and op in ("<", "<=", ">", ">=", "==", "!="):
            return "boolval"
        elif op in ("<", "<=", ">", ">=", "==", "!="):
            if ((l_type == "boolval" and r_type in ("intnum", "floatnum")) or
                    (r_type == "boolval" and l_type in ("intnum", "floatnum"))):
                raise IllegalBoolExpression(l_type, op, r_type)
            else:
                raise UnknownType(l_type, op, r_type)
        else:
            raise UnknownType(l_type, op, r_type)

    @with_indent
    def _parse_token(self, lexeme, token):
        if self._current_row == len(self._table_of_symbols):
            raise ParserError()

        current_line, current_lexeme, current_token, _ = self._next_symbol()

        if (current_lexeme, current_token) == (lexeme, token):
            self._log(f"parse_token: line {current_line} token: {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, lexeme, token)
        return current_line, current_lexeme, current_token

    @with_indent
    def _parse_token_type(self, expected_token):
        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_token == expected_token:
            self._log(f"parse_{expected_token}: line {current_line} {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, expected_token, expected_token)
        return current_lexeme

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

        ident = self._parse_token_type("id")
        self._parse_declaration_expression(ident)

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)

            if (current_lexeme, current_token) == (",", "punct"):
                self._parse_token(",", "punct")
                ident = self._parse_token_type("id")
                self._parse_declaration_expression(ident)
            else:
                break
        return True

    # DeclarationExpression = [':' Type] '=' (Expression | Inp)
    #        				| ':' Type.
    @with_indent
    def _parse_declaration_expression(self, ident):
        is_valid = False
        is_initialized = False
        has_type = False

        expected_type = None
        expression_type = None

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)

        if (current_lexeme, current_token) == (":", "punct"):
            is_valid = True
            has_type = True
            self._parse_token(":", "punct")
            expected_type = self._parse_type()

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)
        if (current_lexeme, current_token) == ("=", "assign_op"):
            is_valid = True
            is_initialized = True
            self._parse_token("=", "assign_op")

            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if (current_lexeme, current_token) == ("readLine", "keyword"):
                if not has_type:
                    raise IllegalReadLine(current_line)
                self._parse_inp()
            else:
                expression_type = self._parse_expression()

        if not is_valid:
            raise IllegalDeclaration(current_line)

        var_type = expected_type if has_type else expression_type
        if expression_type and expected_type and expected_type != expression_type:
            raise IllegalType(current_line, expected_type, expression_type)
        self._add_variable(ident, var_type, is_initialized, current_line)
        return True

    @with_indent
    def _parse_type(self):
        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_token == "keyword" and current_lexeme in ["Int", "Float", "Bool"]:
            self._log(f"parse_type: line {current_line} {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, "Int | Float | Bool", "keyword")
        return type_to_token[current_lexeme]

    # Assign = Ident '=' (Expression | Inp).
    @with_indent
    def _parse_assign(self):
        self._log("parse_assign:")
        ident = self._parse_token_type("id")
        current_line, _, _ = self._parse_token("=", "assign_op")

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)
        if (current_lexeme, current_token) == ("readLine", "keyword"):
            self._parse_inp()
        else:
            var_type = self._parse_expression()
            expected_type = self._get_ident_type(ident)
            if expected_type != var_type:
                raise IllegalType(current_line, expected_type, var_type)
        self._initialize_variable(ident)

    # Inp = 'readLine()'.
    @with_indent
    def _parse_inp(self):
        self._parse_token("readLine", "keyword")
        self._parse_token("(", "brackets_op")
        self._parse_token(")", "brackets_op")
        return True

    # IfStatement = 'if' Expression '{' StatementList '}' [IfTail].
    @with_indent
    def _parse_if(self):
        self._log("parse_if:")
        current_line, _, _ = self._parse_token("if", "keyword")
        actual_type = self._parse_expression()
        if actual_type != "boolval":
            raise IllegalType(current_line, "boolval", actual_type)
        self._parse_token("{", "brackets_op")
        self._enter_scope()
        self._parse_statement_list()
        self._parse_token("}", "brackets_op")
        self._exit_scope()
        if self._current_row < len(self._table_of_symbols):
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if (current_lexeme, current_token) == ("else", "keyword"):
                self._parse_token("else", "keyword")
                self._enter_scope()
                self._parse_if_tail()
                self._exit_scope()
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

        current_line, _, _ = self._parse_token("for", "keyword")
        self._enter_scope()
        ident = self._parse_token_type("id")
        self._add_variable(ident, "intnum", True, current_line)
        self._parse_token("in", "keyword")
        self._parse_range_expression()
        self._parse_token("{", "brackets_op")
        self._parse_statement_list()
        self._parse_token("}", "brackets_op")
        self._exit_scope()

        return True

    # RangeExpr = Expression RangeOp Expression.
    @with_indent
    def _parse_range_expression(self):
        self._log("parse_range_expression:")
        l_type = self._parse_expression()

        current_line, current_lexeme, current_token, _ = self._next_symbol()
        if current_lexeme in ["...", "..<"] and current_token == "range_op":
            self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
        else:
            raise UnexpectedToken(current_line, current_lexeme, current_token, "... | ..<", "range_op")

        r_type = self._parse_expression()
        if l_type != "intnum" or r_type != "intnum":
            actual_type = l_type if l_type != "intnum" else r_type
            raise IllegalType(current_line, "intnum", actual_type)
        return True

    # WhileStatement = 'while' Expression '{' StatementList '}'.
    @with_indent
    def _parse_while(self):
        self._log("parse_while:")

        current_line, _, _ = self._parse_token("while", "keyword")
        actual_type = self._parse_expression()
        if actual_type != "boolval":
            raise IllegalType(current_line, "boolval", actual_type)
        self._parse_token("{", "brackets_op")
        self._enter_scope()
        self._parse_statement_list()
        self._parse_token("}", "brackets_op")
        self._exit_scope()

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

    # Expression = ArithmExpression { RelOp ArithmExpression }.
    @with_indent
    def _parse_expression(self):
        self._log("parse_expression:")

        result_type = self._parse_arithm_expression()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)

            if current_token == "rel_op":
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                self._next_symbol()
                arithm_type = self._parse_arithm_expression()
                result_type = self._get_op_type(result_type, current_lexeme, arithm_type)
            else:
                break

        return result_type

    # ArithmExpression = [Sign] Term { '+' | '-' Term }.
    @with_indent
    def _parse_arithm_expression(self):
        self._log("parse_arithm_expression:")

        current_line, current_lexeme, current_token, _ = self._next_symbol(False)

        unary_applied = False
        if current_lexeme in ('+', '-'):
            unary_applied = True
            self._next_symbol()
            self._log(f"line {current_line} unary operator: {(current_lexeme, current_token)}")

        result_type = self._parse_term()
        if unary_applied and result_type == "boolval":
            raise IllegalType(current_line, ("intnum", "float"), type_to_token["Bool"])

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if current_token == "add_op":
                self._next_symbol()
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                term_type = self._parse_term()
                result_type = self._get_op_type(result_type, current_lexeme, term_type)
            else:
                break

        return result_type

    # Term = Exponent { '*' | '/' Exponent }.
    @with_indent
    def _parse_term(self):
        self._log("parse_term:")

        result_type = self._parse_exponent()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if current_token == "mult_op":
                if current_lexeme == "/":
                    self._current_row += 1
                    current_line, current_lexeme, current_token, _ = self._next_symbol(False)
                    if current_lexeme == "0":
                        raise ZeroDivisionError(f"Encountered zero division on line {current_line}")
                    self._current_row -= 1
                current_line, current_lexeme, current_token, _ = self._next_symbol()
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                exponent_type = self._parse_exponent()
                result_type = self._get_op_type(result_type, current_lexeme, exponent_type)
            else:
                break
        return result_type

    # Exponent = Factor { '^' Factor }.
    @with_indent
    def _parse_exponent(self):
        self._log("parse_exponent:")

        result_type = self._parse_factor()

        while True:
            current_line, current_lexeme, current_token, _ = self._next_symbol(False)
            if current_token == "power_op":
                self._log(f"line {current_line} token: {(current_lexeme, current_token)}")
                self._next_symbol()
                factor_type = self._parse_factor()
                result_type = self._get_op_type(result_type, current_lexeme, factor_type)
            else:
                break
        return result_type

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

            if current_token == "id":
                self._check_is_initialized(current_lexeme)
                return self._get_ident_type(current_lexeme)
            else:
                return self._get_const_type(current_lexeme)

        elif current_lexeme == '(':
            self._parse_token("(", "brackets_op")
            exp_type = self._parse_expression()
            self._parse_token(")", "brackets_op")
            return exp_type
        else:
            raise IllegalExpression(current_line, current_lexeme, current_token)

    def _log(self, *args):
        print(self._current_indent * "│  ", end="")
        print("└──", *args)

    def _next_indent(self):
        self._current_indent += 1

    def _prev_indent(self):
        self._current_indent -= 1
