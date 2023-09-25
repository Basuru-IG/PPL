grammar CSlang;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

program: (classdecl)+ EOF;

classdecl: CLASS classname (supperclass)? LB (classmember|construcdecl)* RB;

supperclass: EXTENDS classname;

classname: ID;

construcdecl: FUNC CONSTRUCTOR paramdecl body;

classmember: (attributedecl | methoddecl) SM;

attributedecl: (CONST | VAR) attributelist COLON mctype (initlist)?
{
    (3 == len(initlist))
};

// attributedecl: (CONST | VAR) attributelist COLON mctype (initlist)?;

// attributedecl: (CONST | VAR) attributelist COLON mctype (initlist)?
//     { (attributelist is None and initlist is None) or (attributelist.size() == len(initlist))};

attributelist: membername (CM membername)*;

initlist: EQ expr (CM expr)*;

methoddecl: FUNC membername paramdecl COLON mctype body;

paramdecl: LP paramlist? RP;

paramlist: param (CM param)*;

param: membername COLON mctype;

body: LB bodydecl* RB;

bodydecl: 'body';

mctype: (INT | FLOAT);

membername: ('@')? ID;




// attributedecl: mctype idlist SM;
// idlist: ID CM idlist | ID;
// mctype: INT | FLOAT;
// methoddecl: mctype ID paramdecl body;
// paramdecl: LP paramlist* RP;
// paramlist: param SM paramlist| param;
// param: mctype idlist;

// body: LB bodydecl* RB;
// bodydecls: bodydecl bodydecls | ;
// bodydecl: attributedecl | statement;

// statement: (assign_stmt|call_stmt|return_stmt) SM;
// assign_stmt: ID EQ expr;
call_stmt: ID LP exprlist RP;
exprlist: nonNULL_exprlist| ;
nonNULL_exprlist: expr CM nonNULL_exprlist | expr;
// return_stmt: RETURN expr;

expr: exp1 ADD expr | exp1;
exp1: exp2 SUB exp2 | exp2;
exp2: exp2 (DIV | MUL ) exp3 | exp3;
exp3: operands;
operands: INTLIT | FLOATLIT | ID | call_stmt | LP expr RP;

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
EXP: '^';
MUL: '*';
COLON: ':';
EXTENDS: '<-';

FLOATLIT
    : DIGIT+ DOT (DIGIT | EXPONENT)* // 1 | 1.5 | 1.e-4
    | DIGIT* DOT DIGIT+ EXPONENT? // (1).5(e-4)
    | DIGIT+ EXPONENT // 12e-5
    ;
INTLIT : DIGIT+ ;

fragment EXPONENT: [eE] [-]? DIGIT+ ;
fragment DIGIT: [0-9] ;

ID: [_a-zA-Z][_a-zA-Z0-9]*;

// WS: [ \t\r\n] -> skip;

// Define lexer rules for characters and whitespace
WS: [ \t\r\b\f]+ -> skip;
NEWLINE: '\n' -> skip;

// Define lexer rules for comments
LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;


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