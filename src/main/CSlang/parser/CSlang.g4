grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}


program: (classdecl)+ EOF;

classdecl: CLASS classname (supperclass)? LB (classmember)* RB;

supperclass: EXTENDS classname;

classname: ID;

construcdecl: FUNC CONSTRUCTOR paramdecl block_stmt;

classmember: attributedecl SM | methoddecl | construcdecl;

// attributedecl: (CONST | VAR) attribute=attributelist COLON mctype (init=initlist)?
// {
//     print(type($attributelist.text))  # Assuming $attributelist.text contains "a,b,c,d"
    
// };

attributedecl: (CONST | VAR) attributelist COLON mctype (EQ initlist){len($attributelist.text.split(',')) == len($initlist.text.split(','))}?
	| (CONST | VAR) attributelist COLON mctype;

// attributedecl: (CONST | VAR) attributelist COLON mctype (initlist)?
//     { (attributelist is None and initlist is None) or (attributelist.size() == len(initlist))};

initlist: expr (CM expr)*;

methoddecl: FUNC membername paramdecl COLON mctype block_stmt;

paramdecl: LP paramlist? RP;

paramlist: param (CM param)*;

param: attributelist COLON mctype; // When two or more consecutive named function parameters share a common type

// body: LB bodydecl* RB;

// bodydecl: 'body';

mctype: INT | FLOAT | BOOL | STRING | VOID  | classname | ARRAY;

ARRAY: OB INTLIT CB (INT | FLOAT | BOOL | STRING | ID);

attributelist: membername (CM membername)*;

membername: AC? ID;



expr: expr1 (LESS | GREATER | LESSEQUAL | GREATEREQUAL) expr1 | expr1;
expr1: expr2 (EQUAL | NOTEQUAL) expr2 | expr2;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 ( ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD | BS) expr5 | expr5;
expr5: expr5 (CONCATENATION) expr6 | expr6;
expr6: NOT expr6 | expr7;
expr7: ( ADD | SUB) expr7 | expr8;
expr8: expr9 OB expr CB | expr9;
// member_access: expr DOT ID | ID DOT ID | expr DOT ID LB (list_of_expr)? RB | ID DOT ID LB
// (list_of_expr)? RB;
expr9:
	expr9 DOT ID 
	| expr9 DOT membername (LP list_of_expr? RP)?
	| (membername DOT)? membername (LP list_of_expr? RP)? SM?
	| expr10;
expr10: NEW ID LP (list_of_expr)? RP expr10? | expr11;
expr11: LP expr RP | ID | literal | SELF DOT ID | NULL;

list_of_expr: expr (CM expr)*;

literal: INTLIT | FLOATLIT | STRING_LITERAL | BOOLLIT | ARRAYLIT;


statement: 
	attributedecl
	| assign_stmt SM
	| if_stmt
	| for_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| method_stm
	| block_stmt;

block_stmt: LB member_block RB;
member_block: (attributedecl SM | statement)*;
assign_stmt: (ID | expr8) ASSIGN expr;
if_stmt: IF block_stmt? expr block_stmt (ELSE block_stmt)?;
for_stmt: FOR assign_stmt SM expr SM assign_stmt block_stmt;
break_stmt: BREAK SM;
continue_stmt: CONTINUE SM;
return_stmt: RETURN expr? SM;
method_stm: (ID | expr ) DOT membername LP list_of_expr? RP SM | expr9;
// io: 'io' DOT (WRITE | WRITELN) LP expr RP SM;
// WRITE: '@write';
// WRITELN: '@writeInt';


CLASS: 'c' L A S S;
RETURN: 'r' E T U R N;
INT: 'i' N T;
FLOAT: 'f' L O A T;
CONST: 'c' O N S T;
VAR: 'v' A R;
FUNC: 'f' U N C;
VOID: 'v' O I D;
CONSTRUCTOR: 'c' O N S T R U C T O R;
BREAK: 'b' R E A K;
CONTINUE: 'c' O N T I N U E;
IF: 'i' F;
ELSE: 'e' L S E;
FOR: 'f' O R;
TRUE: 't' R U E;
FALSE: 'f' A L S E;
BOOL: 'b' O O L;
STRING: 's' T R I N G;
NULL: 'n' U L L;
SELF: 's' E L F;
NEW: 'n' E W;



AC: '@';
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


ARRAYLIT: OB (ARRAY_ELEMENT (CM ARRAY_ELEMENT)*)? CB;
ARRAY_ELEMENT: INTLIT | FLOATLIT | STRING_LITERAL | BOOLLIT;

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


// Define a token for line comments
LineComment: '//' ~[\r\n]* -> skip;

// Define a token for block comments
BlockComment: '/*' ( ~[*/] | '*/' ~'/' | BlockComment )* '*/' -> skip;

ID: [_a-zA-Z][_a-zA-Z0-9]*;

// WS: [ \t\r\n] -> skip;

// Define lexer rules for characters and whitespace
WS: [ \t\r\b\f]+ -> skip;
NEWLINE: '\n' -> skip;

// Define lexer rules for comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;


ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"\\] | EOF ) 
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', '\\']
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

fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];