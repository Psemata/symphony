
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftADD_OPleftMUL_OPrightUMINUSADD_OP COMMA C_BRACKET_IN C_BRACKET_OUT EQUALS IDENTIFIER MEL MUL_OP NUMBER PARENTH_IN PARENTH_OUT RANGE SEMI_COLON STRINGprogramme : statementprogramme : statement programmeassignation : MEL IDENTIFIER EQUALS expressionassignation : IDENTIFIER EQUALS expressionstatement : assignation SEMI_COLON\n    | function SEMI_COLONstatement : structurestructure : RANGE PARENTH_IN expression COMMA expression COMMA expression PARENTH_OUT C_BRACKET_IN programme C_BRACKET_OUTexpression : NUMBER\n    | STRINGexpression : IDENTIFIERfunction : IDENTIFIER PARENTH_IN PARENTH_OUTfunction : IDENTIFIER PARENTH_IN expression PARENTH_OUTfunction : IDENTIFIER PARENTH_IN expression COMMA expression COMMA expression PARENTH_OUTfunction : IDENTIFIER PARENTH_IN expression COMMA expression COMMA expression COMMA expression PARENTH_OUTexpression : ADD_OP expression %prec UMINUSexpression : expression ADD_OP expression\n    | expression MUL_OP expression'
    
_lr_action_items = {'MEL':([0,2,5,10,11,44,47,],[6,6,-7,-5,-6,6,-8,]),'IDENTIFIER':([0,2,5,6,10,11,13,14,15,16,21,26,27,30,31,36,37,40,44,47,],[7,7,-7,12,-5,-6,17,17,17,17,17,17,17,17,17,17,17,17,7,-8,]),'RANGE':([0,2,5,10,11,44,47,],[8,8,-7,-5,-6,8,-8,]),'$end':([1,2,5,9,10,11,47,],[0,-1,-7,-2,-5,-6,-8,]),'C_BRACKET_OUT':([2,5,9,10,11,46,47,],[-1,-7,-2,-5,-6,47,-8,]),'SEMI_COLON':([3,4,17,18,19,20,22,25,28,29,32,33,41,45,],[10,11,-11,-4,-9,-10,-12,-3,-16,-13,-17,-18,-14,-15,]),'EQUALS':([7,12,],[13,16,]),'PARENTH_IN':([7,8,],[14,15,]),'NUMBER':([13,14,15,16,21,26,27,30,31,36,37,40,],[19,19,19,19,19,19,19,19,19,19,19,19,]),'STRING':([13,14,15,16,21,26,27,30,31,36,37,40,],[20,20,20,20,20,20,20,20,20,20,20,20,]),'ADD_OP':([13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,43,],[21,21,21,21,-11,26,-9,-10,21,26,26,26,21,21,-16,21,21,-17,-18,26,26,21,21,26,26,21,26,]),'PARENTH_OUT':([14,17,19,20,23,28,32,33,38,39,43,],[22,-11,-9,-10,29,-16,-17,-18,41,42,45,]),'MUL_OP':([17,18,19,20,23,24,25,28,32,33,34,35,38,39,43,],[-11,27,-9,-10,27,27,27,-16,27,-18,27,27,27,27,27,]),'COMMA':([17,19,20,23,24,28,32,33,34,35,38,],[-11,-9,-10,30,31,-16,-17,-18,36,37,40,]),'C_BRACKET_IN':([42,],[44,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programme':([0,2,44,],[1,9,46,]),'statement':([0,2,44,],[2,2,2,]),'assignation':([0,2,44,],[3,3,3,]),'function':([0,2,44,],[4,4,4,]),'structure':([0,2,44,],[5,5,5,]),'expression':([13,14,15,16,21,26,27,30,31,36,37,40,],[18,23,24,25,28,32,33,34,35,38,39,43,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programme","S'",1,None,None,None),
  ('programme -> statement','programme',1,'p_expression_statement','symphony_parser.py',15),
  ('programme -> statement programme','programme',2,'p_expression_recursive','symphony_parser.py',20),
  ('assignation -> MEL IDENTIFIER EQUALS expression','assignation',4,'p_assignation_mel','symphony_parser.py',25),
  ('assignation -> IDENTIFIER EQUALS expression','assignation',3,'p_assignation','symphony_parser.py',30),
  ('statement -> assignation SEMI_COLON','statement',2,'p_statement','symphony_parser.py',35),
  ('statement -> function SEMI_COLON','statement',2,'p_statement','symphony_parser.py',36),
  ('statement -> structure','statement',1,'p_statement_struct','symphony_parser.py',41),
  ('structure -> RANGE PARENTH_IN expression COMMA expression COMMA expression PARENTH_OUT C_BRACKET_IN programme C_BRACKET_OUT','structure',11,'p_structure','symphony_parser.py',46),
  ('expression -> NUMBER','expression',1,'p_expression_num','symphony_parser.py',51),
  ('expression -> STRING','expression',1,'p_expression_num','symphony_parser.py',52),
  ('expression -> IDENTIFIER','expression',1,'p_expression_var','symphony_parser.py',57),
  ('function -> IDENTIFIER PARENTH_IN PARENTH_OUT','function',3,'p_function','symphony_parser.py',62),
  ('function -> IDENTIFIER PARENTH_IN expression PARENTH_OUT','function',4,'p_function_one_param','symphony_parser.py',67),
  ('function -> IDENTIFIER PARENTH_IN expression COMMA expression COMMA expression PARENTH_OUT','function',8,'p_function_three_param','symphony_parser.py',72),
  ('function -> IDENTIFIER PARENTH_IN expression COMMA expression COMMA expression COMMA expression PARENTH_OUT','function',10,'p_function_four_param','symphony_parser.py',77),
  ('expression -> ADD_OP expression','expression',2,'p_minus','symphony_parser.py',82),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','symphony_parser.py',87),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','symphony_parser.py',88),
]
