'''
Analyseur lexicale qui va reconnaitres les différentes séquences valides.
Un certains nombre de tokens sont déclarés.
Si une simple expression régulière suffit alors on déclare une variable.
Si en plus de l'expression régulière, du traitement est requis, alors on fait une fonction.
Les noms des variables/foncions doivent être préfixé d'un 't_'.
'''

import ply.lex as lex

reserved_words = ("range", "mel")

tokens = (
    "NUMBER",
    "STRING",
    "ADD_OP",
    "MUL_OP",
    "PARENTH_IN",
    "PARENTH_OUT",
    "SEMI_COLON",
    "COMMA",
    "C_BRACKET_IN",
    "C_BRACKET_OUT",
    "EQUALS",
    "IDENTIFIER",
) + tuple(map(lambda s: s.upper(), reserved_words))

t_ADD_OP = r"(\+|-)"
t_MUL_OP = r"(\\|\*)"
t_PARENTH_IN = r"\("
t_PARENTH_OUT = r"\)"
t_SEMI_COLON = r"\;"
t_COMMA = r","
t_C_BRACKET_IN = r"\{"
t_C_BRACKET_OUT = r"\}"
t_EQUALS = r"="


def t_IDENTIFIER(t):
    r"[A-Za-z_]\w*"
    if t.value in reserved_words:
        t.type = t.value.upper()
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r"\"\w*\" "
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()

if __name__ == "__main__":
    prog = open("Test Files/input6.txt").read()
    lex.input(prog)

    while 1:
        tok = lex.token()
        if not tok:
            break
        print("line %d : %s(%s)" % (tok.lineno, tok.type, tok.value))
