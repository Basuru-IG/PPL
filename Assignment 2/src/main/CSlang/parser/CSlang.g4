grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}


program: classdecl+ EOF;

classdecl: CLASS ID (EXTENDS ID)? LB classmember? RB; //  bỏ CLASS, LB và RB

// supperclass: EXTENDS classname;



classmember: attributedecl 
	| methoddecl 
	| construcdecl
	| attributedecl classmember
	| methoddecl classmember
	| construcdecl classmember;

construcdecl: FUNC CONSTRUCTOR paramdecl block_stmt;
attributedecl: (CONST | VAR) attributelist COLON mctype (EQ initlist) SM 
	| (CONST | VAR) attributelist COLON mctype SM;

// attributedecl: var_attr | const_attr;

// var_attr: VAR attr_frag;
// const_attr: CONST attr_frag;

// attr_frag: (no_initlist | initlist) SM;
// no_initlist: attributelist COLON mctype;
// initlist: membername CM initlist CM expression 
// 	| membername COLON mctype EQ expression;

initlist: expression (CM expression)*;



methoddecl: FUNC membername paramdecl COLON mctype block_stmt;

paramdecl: LP paramlist? RP;

paramlist: param CM paramlist | param;

param: attributelist COLON mctype; // When two or more consecutive named function parameters share a common type


mctype: INT | FLOAT | BOOL | STRING | VOID  | classtype | array_type;

classtype: membername;
// classname: ID;

array_type: OB INTLIT CB (INT | FLOAT | BOOL | STRING | ID);


attributelist: membername (CM membername)*;


expression: expression1 CONCATENATION expression1 | expression1;
expression1: expression2 (EQUAL | NOTEQUAL | LESS | GREATER | LESSEQUAL | GREATEREQUAL) expression2 | expression2;
expression2: expression2 (AND | OR) expression3 | expression3;
expression3: expression3 ( ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD | BS) expression5 | expression5;
expression5: NOT expression5 | expression6;
expression6: SUB expression6 | expression7;
expression7: expression7 OB expression CB | expression8;
expression8: expression8 DOT ID (LP list_of_expression? RP)?| expression9;
// expression9: (expression9 DOT)? STATIC (LP list_of_expression? RP)? 
// 			| (expression9 DOT)? STATIC (LP list_of_expression? RP)? 
// 			| expression9 DOT STATIC LP RP
// 			| expression9 DOT STATIC LP list_of_expression RP
// 			| expression10;
expression9: expression9 DOT ID  	
			| ID DOT STATIC
			| STATIC
			| expression9 DOT ID LP list_of_expression RP
			| ID DOT STATIC LP list_of_expression RP
			| STATIC LP list_of_expression RP
			| expression9 DOT ID LP RP
			| ID DOT STATIC LP RP
			| STATIC LP RP
			| expression10;

expression10: NEW ID LP (list_of_expression)? RP expression10? | operands;

operands: LP expression RP | ID | literal | SELF DOT ID | SELF DOT ID LP list_of_expression RP |SELF DOT ID LP RP| NULL ;

list_of_expression: expression (CM expression)*;


statement: 
	block_vardecl
	| assign_stmt SM
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_stm SM
	| block_stmt;

block_stmt: LB member_block RB;
member_block: statement*;
block_vardecl: (VAR | CONST) attributelist COLON mctype (EQ initlist) SM 
	| (VAR | CONST) attributelist COLON mctype SM;
assign_stmt: (ID | expression7) ASSIGN expression;
// if_stmt: IF block_stmt? expression block_stmt (ELSE block_stmt)?; 
if_stmt: IF block_stmt expression block_stmt ELSE block_stmt
	| IF block_stmt expression block_stmt
	| IF expression block_stmt ELSE block_stmt
	| IF expression block_stmt
	;


for_stmt: FOR assign_stmt SM expression SM assign_stmt block_stmt;
break_stmt: BREAK SM;
continue_stmt: CONTINUE SM;
return_stmt: RETURN expression? SM;
// method_stm: (instance_method | static_method) SM;
method_stm: | expression DOT ID LP list_of_expression RP
			| ID DOT STATIC LP list_of_expression RP
			| STATIC LP list_of_expression RP
			| expression DOT ID LP RP
			| ID DOT STATIC LP RP
			| STATIC LP RP
			| SELF DOT ID LP list_of_expression RP
			| SELF DOT ID LP RP;
// instance_method: expression DOT ID LP list_of_expression? RP;
// static_method: (ID DOT)? STATIC LP list_of_expression? RP;



literal:  INTLIT | FLOATLIT | STRING_LITERAL | BOOLLIT | array_literal;


membername: STATIC | ID;
STATIC: '@' [_a-zA-Z0-9]+;

CLASS: 'class';
RETURN: 'return';
INT: 'int';
FLOAT: 'float';
CONST: 'const';
VAR: 'var';
FUNC: 'func';
VOID: 'void';
CONSTRUCTOR: 'constructor';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
FOR: 'for';
fragment TRUE: 'true';
fragment FALSE: 'false';
BOOL: 'bool';
STRING: 'string';
NULL: 'null';
SELF: 'self';
NEW: 'new';


OB : '[';
CB: ']';
EQ: '=';
LB: '{';
RB: '}';
LP: '(';
RP: ')';
SM: ';';
CM: ',';
DOT: '.';
ADD: '+';
SUB: '-';
DIV: '/';
BS: '\\';
MOD: '%';
NOT: '!';
OR: '||';
AND: '&&';
EQUAL: '==';
NOTEQUAL: '!=';
LESS: '<';
GREATER: '>';
LESSEQUAL: '<=';
GREATEREQUAL: '>=';
ASSIGN: ':=';
CONCATENATION: '^';
MUL: '*';
COLON: ':';
EXTENDS: '<-';

array_literal: OB (elem (CM elem)*)? CB;
elem: INTLIT | FLOATLIT | STRING_LITERAL | BOOLLIT | NEW ID LP (list_of_expression)? RP;




FLOATLIT
    : '-'? DIGIT+ DOT (DIGIT | EXPONENT)* // 1 | 1.5 | 1.e-4
    | '-'? DIGIT+ DOT DIGIT+ EXPONENT? // (1).5(e-4)
    | '-'? DIGIT+ EXPONENT // 12e-5
    ;
INTLIT : DIGIT+ ;
BOOLLIT: TRUE | FALSE;

STRING_LITERAL: '"' STR_CHAR* '"'
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;



fragment EXPONENT: [eE] [-+]? DIGIT+ ;
fragment DIGIT: [0-9] ;


ID: [_a-zA-Z][_a-zA-Z0-9]*;



// Define lexer rules for characters and whitespace

WS: [ \t\r\f]+ -> skip;
NEWLINE: '\n' -> skip;

// Define lexer rules for comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"\\] | EOF ) 
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '\"', '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;


ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;


fragment STR_CHAR: ~[\b\t\n\f\r"\\] | ESC_SEQ ;

fragment ESC_SEQ: '\\' [btnfr"\\] ;

fragment ESC_ILLEGAL: '\\' ~[btnfr"\\] | ~'\\' ;



