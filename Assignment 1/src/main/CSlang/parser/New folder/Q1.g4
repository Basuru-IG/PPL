grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: Q3 EOF;


// Q2: LwrLetter (LwrLetter | Digit)*;
// fragment LwrLetter: [a-z]; 

fragment Digit: [0-9];

// Q5:
// 	'0'
// 	| [1-9] '_'? [0-9_]* {self.text = "".join(self.text.split("_"))};

Q3: INTPART DECPART | INTPART DECPART? EXPPART;
fragment INTPART: Digit+;
fragment DECPART: '.' [0-9]+;
fragment EXPPART: ('e'|'E') '-'? [0-9]+;

// Q4: Quote (NonQuote | ConsecQuote)* Quote; fragment Quote: '\''; fragment NonQuote:
// [a-zA-Z0-9\-.? ]; fragment ConsecQuote: '\'\'';

// Q1: ValidSegment '.' ValidSegment '.' ValidSegment '.' ValidSegment; 
// fragment DigitExclude0: [1-9]; 
// fragment ValidSegment: Digit | DigitExclude0 Digit | '1' Digit Digit | '2' [0-4] [0-9]|'2' '5' [0-5];

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;