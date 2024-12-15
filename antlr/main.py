import sys
from antlr4 import *
from QuillLexer import QuillLexer
from QuillParser import QuillParser


def pretty_print_tree(tree, parser, prefix="", is_last=True):
    rule_names = parser.ruleNames
    rule_index = tree.getRuleIndex()
    rule_name = rule_names[rule_index]

    connector = "└── " if is_last else "├── "
    print(prefix + connector + rule_name)

    if is_last:
        new_prefix = prefix + "    "
    else:
        new_prefix = prefix + "│   "

    child_count = tree.getChildCount()
    for i in range(child_count):
        child = tree.getChild(i)
        is_last_child = (i == child_count - 1)
        if isinstance(child, TerminalNode):
            print(new_prefix + ("└── " if is_last_child else "├── ") + f"TOKEN: {child.getText()}")
        else:
            pretty_print_tree(child, parser, new_prefix, is_last_child)


def main(argv):
    input_stream = FileStream(argv[1], encoding="utf-8")

    lexer = QuillLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print("Tokens:")
    for token in token_stream.tokens:
        print(token)

    parser = QuillParser(token_stream)
    tree = parser.program()

    print("Parse Tree:")
    pretty_print_tree(tree, parser)


if __name__ == "__main__":
    main(sys.argv)
