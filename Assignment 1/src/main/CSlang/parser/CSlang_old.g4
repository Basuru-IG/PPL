grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: (vardecl|funcdecl)+ EOF;

vardecl: mctype idlist SM;
idlist: ID CM idlist | ID;
mctype: INT | FLOAT;
funcdecl: mctype ID paramdecl body;
paramdecl: LP paramlist* RP;
paramlist: param SM paramlist| param;
param: mctype idlist;

body: LB bodydecl* RB;
bodydecls: bodydecl bodydecls | ;
bodydecl: vardecl | statement;

statement: (assign_stmt|call_stmt|return_stmt) SM;
assign_stmt: ID EQ expr;
call_stmt: ID LP exprlist RP;
exprlist: nonNULL_exprlist| ;
nonNULL_exprlist: expr CM nonNULL_exprlist | expr;
return_stmt: RETURN expr;

expr: exp1 ADD expr | exp1;
exp1: exp2 SUB exp2 | exp2;
exp2: exp2 (DIV | MUL ) exp3 | exp3;
exp3: operands;
operands: INTLIT | FLOATLIT | ID | call_stmt | LP expr RP;


RETURN: R E T U R N;
INT: I N T;
FLOAT: F L O A T;

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
MUL: '*';

FLOATLIT
	: DIGIT+ DOT (DIGIT | EXPONENT)* // 1 | 1.5 | 1.e-4
	| DIGIT* DOT DIGIT+ EXPONENT? // (1).5(e-4)
	| DIGIT+ EXPONENT // 12e-5
	;
INTLIT : DIGIT+ ;

fragment EXPONENT: [eE] [-]? DIGIT+ ;
fragment DIGIT: [0-9] ;

ID: [_a-zA-Z][_a-zA-Z0-9]*;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};

UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;


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