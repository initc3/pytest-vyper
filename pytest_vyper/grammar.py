import pathlib

from lark import Lark
from lark.indenter import Indenter

PARENT_DIR = pathlib.Path(__file__).resolve().parent


class PythonIndenter(Indenter):
    NL_type = "_NEWLINE"
    OPEN_PAREN_types = ["LPAR", "LSQB", "LBRACE"]
    CLOSE_PAREN_types = ["RPAR", "RSQB", "RBRACE"]
    INDENT_type = "_INDENT"
    DEDENT_type = "_DEDENT"
    tab_len = 4


def get_lark_grammar():
    return Lark.open(
        PARENT_DIR.joinpath("vyper.lark"),
        parser="lalr",
        start="module",
        postlex=PythonIndenter(),
    )


LARK_GRAMMAR = get_lark_grammar()
