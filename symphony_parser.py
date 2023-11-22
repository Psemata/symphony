'''
Le parser va réduire une longue séquence de "mots" pour les transformer en un seul arbre, "programme".
Si on ne réussit pas à réduire en un seul programme alors le parse n'est pas bon.
Le but est de voir que ce qu'on a validé dans l'analyseur lexicale ait du sens.
AST est utilisé pour la création de nodes.
'''

from symphony_lex import tokens
import os
import ply.yacc as yacc
import AST


def p_expression_statement(p):
    """programme : statement"""
    p[0] = AST.ProgramNode(p[1])


def p_expression_recursive(p):
    """programme : statement programme"""
    p[0] = AST.ProgramNode([p[1]] + p[2].children)


def p_assignation_mel(p):
    """assignation : MEL IDENTIFIER EQUALS expression"""
    p[0] = AST.AssignNode(True, [AST.TokenNode(p[2]), p[4]])


def p_assignation(p):
    """assignation : IDENTIFIER EQUALS expression"""
    p[0] = AST.AssignNode(False, [AST.TokenNode(p[1]), p[3]])


def p_statement(p):
    """statement : assignation SEMI_COLON
    | function SEMI_COLON"""
    p[0] = p[1]


def p_statement_struct(p):
    """statement : structure"""
    p[0] = p[1]


def p_structure(p):
    """structure : RANGE PARENTH_IN expression COMMA expression COMMA expression PARENTH_OUT C_BRACKET_IN programme C_BRACKET_OUT"""
    p[0] = AST.RangeNode([p[3], p[5], p[7], p[10]])


def p_expression_num(p):
    """expression : NUMBER
    | STRING"""
    p[0] = AST.TokenNode(p[1])


def p_expression_var(p):
    """expression : IDENTIFIER"""
    p[0] = AST.TokenNode(p[1])


def p_function(p):
    """function : IDENTIFIER PARENTH_IN PARENTH_OUT"""
    p[0] = AST.FuncNode(p[1])


def p_function_one_param(p):
    """function : IDENTIFIER PARENTH_IN expression PARENTH_OUT"""
    p[0] = AST.FuncNode(p[1], [p[3]])


def p_function_three_param(p):
    """function : IDENTIFIER PARENTH_IN expression COMMA expression COMMA expression PARENTH_OUT"""
    p[0] = AST.FuncNode(p[1], [p[3], p[5], p[7]])


def p_function_four_param(p):
    """function : IDENTIFIER PARENTH_IN expression COMMA expression COMMA expression COMMA expression PARENTH_OUT"""
    p[0] = AST.FuncNode(p[1], [p[3], p[5], p[7], p[9]])


def p_minus(p):
    """expression : ADD_OP expression %prec UMINUS"""
    p[0] = AST.OpNode(p[1], [p[2]])


def p_expression_op(p):
    """expression : expression ADD_OP expression
    | expression MUL_OP expression"""
    p[0] = AST.OpNode(p[2], [p[1], p[3]])


def p_error(p):
    print("Syntax error in line %d" % p.lineno)
    yacc.errok()


precedence = (
    ("left", "ADD_OP"),
    ("left", "MUL_OP"),
    ("right", "UMINUS"),
)


def parse(program):
    return yacc.parse(program)


yacc.yacc(outputdir="generated")

if __name__ == "__main__":
    prog = open("Test Files/input6.txt").read()
    result = yacc.parse(prog)

    graph = result.makegraphicaltree()
    name = os.path.splitext("input6.txt")[0] + "-ast.pdf"
    graph.write_pdf(name)

    print(result)
