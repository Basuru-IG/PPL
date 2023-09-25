# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u00d5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\6\2\66\n\2\r\2\16\2\67\3\2\3\2\3\3")
        buf.write("\3\3\3\3\5\3?\n\3\3\3\3\3\3\3\7\3D\n\3\f\3\16\3G\13\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\5\7W\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b`\n\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\7\tg\n\t\f\t\16\tj\13\t\3\n\3\n\3\n\3\n")
        buf.write("\7\np\n\n\f\n\16\ns\13\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\5\f~\n\f\3\f\3\f\3\r\3\r\3\r\7\r\u0085\n")
        buf.write("\r\f\r\16\r\u0088\13\r\3\16\3\16\3\16\3\16\3\17\3\17\7")
        buf.write("\17\u0090\n\17\f\17\16\17\u0093\13\17\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\5\22\u009c\n\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\5\24\u00a7\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u00ae\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\5\26\u00b5\n\26\3\27\3\27\3\27\3\27\3\27\5\27\u00bc\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00c4\n\30\f\30")
        buf.write("\16\30\u00c7\13\30\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u00d3\n\32\3\32\2\3.\33\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\5\3\2\t")
        buf.write("\n\3\2\7\b\4\2$$\61\61\2\u00d0\2\65\3\2\2\2\4;\3\2\2\2")
        buf.write("\6J\3\2\2\2\bM\3\2\2\2\nO\3\2\2\2\fV\3\2\2\2\16Z\3\2\2")
        buf.write("\2\20c\3\2\2\2\22k\3\2\2\2\24t\3\2\2\2\26{\3\2\2\2\30")
        buf.write("\u0081\3\2\2\2\32\u0089\3\2\2\2\34\u008d\3\2\2\2\36\u0096")
        buf.write("\3\2\2\2 \u0098\3\2\2\2\"\u009b\3\2\2\2$\u009f\3\2\2\2")
        buf.write("&\u00a6\3\2\2\2(\u00ad\3\2\2\2*\u00b4\3\2\2\2,\u00bb\3")
        buf.write("\2\2\2.\u00bd\3\2\2\2\60\u00c8\3\2\2\2\62\u00d2\3\2\2")
        buf.write("\2\64\66\5\4\3\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2")
        buf.write("\2\2\678\3\2\2\289\3\2\2\29:\7\2\2\3:\3\3\2\2\2;<\7\5")
        buf.write("\2\2<>\5\b\5\2=?\5\6\4\2>=\3\2\2\2>?\3\2\2\2?@\3\2\2\2")
        buf.write("@E\7\33\2\2AD\5\f\7\2BD\5\n\6\2CA\3\2\2\2CB\3\2\2\2DG")
        buf.write("\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\7\34")
        buf.write("\2\2I\5\3\2\2\2JK\7\63\2\2KL\5\b\5\2L\7\3\2\2\2MN\7\66")
        buf.write("\2\2N\t\3\2\2\2OP\7\13\2\2PQ\7\r\2\2QR\5\26\f\2RS\5\34")
        buf.write("\17\2S\13\3\2\2\2TW\5\16\b\2UW\5\24\13\2VT\3\2\2\2VU\3")
        buf.write("\2\2\2WX\3\2\2\2XY\7\37\2\2Y\r\3\2\2\2Z[\t\2\2\2[\\\5")
        buf.write("\20\t\2\\]\7\62\2\2]_\5 \21\2^`\5\22\n\2_^\3\2\2\2_`\3")
        buf.write("\2\2\2`a\3\2\2\2ab\b\b\1\2b\17\3\2\2\2ch\5\"\22\2de\7")
        buf.write(" \2\2eg\5\"\22\2fd\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2")
        buf.write("\2i\21\3\2\2\2jh\3\2\2\2kl\7\32\2\2lq\5*\26\2mn\7 \2\2")
        buf.write("np\5*\26\2om\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2\2r\23")
        buf.write("\3\2\2\2sq\3\2\2\2tu\7\13\2\2uv\5\"\22\2vw\5\26\f\2wx")
        buf.write("\7\62\2\2xy\5 \21\2yz\5\34\17\2z\25\3\2\2\2{}\7\35\2\2")
        buf.write("|~\5\30\r\2}|\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\7\36\2\2\u0080\27\3\2\2\2\u0081\u0086\5\32\16\2\u0082")
        buf.write("\u0083\7 \2\2\u0083\u0085\5\32\16\2\u0084\u0082\3\2\2")
        buf.write("\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\31\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a")
        buf.write("\5\"\22\2\u008a\u008b\7\62\2\2\u008b\u008c\5 \21\2\u008c")
        buf.write("\33\3\2\2\2\u008d\u0091\7\33\2\2\u008e\u0090\5\36\20\2")
        buf.write("\u008f\u008e\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3")
        buf.write("\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\3\2\2\2\u0093\u0091")
        buf.write("\3\2\2\2\u0094\u0095\7\34\2\2\u0095\35\3\2\2\2\u0096\u0097")
        buf.write("\7\3\2\2\u0097\37\3\2\2\2\u0098\u0099\t\3\2\2\u0099!\3")
        buf.write("\2\2\2\u009a\u009c\7\4\2\2\u009b\u009a\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\7\66\2\2\u009e")
        buf.write("#\3\2\2\2\u009f\u00a0\7\66\2\2\u00a0\u00a1\7\35\2\2\u00a1")
        buf.write("\u00a2\5&\24\2\u00a2\u00a3\7\36\2\2\u00a3%\3\2\2\2\u00a4")
        buf.write("\u00a7\5(\25\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\'\3\2\2\2\u00a8\u00a9\5*\26")
        buf.write("\2\u00a9\u00aa\7 \2\2\u00aa\u00ab\5(\25\2\u00ab\u00ae")
        buf.write("\3\2\2\2\u00ac\u00ae\5*\26\2\u00ad\u00a8\3\2\2\2\u00ad")
        buf.write("\u00ac\3\2\2\2\u00ae)\3\2\2\2\u00af\u00b0\5,\27\2\u00b0")
        buf.write("\u00b1\7\"\2\2\u00b1\u00b2\5*\26\2\u00b2\u00b5\3\2\2\2")
        buf.write("\u00b3\u00b5\5,\27\2\u00b4\u00af\3\2\2\2\u00b4\u00b3\3")
        buf.write("\2\2\2\u00b5+\3\2\2\2\u00b6\u00b7\5.\30\2\u00b7\u00b8")
        buf.write("\7#\2\2\u00b8\u00b9\5.\30\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00bc\5.\30\2\u00bb\u00b6\3\2\2\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bc-\3\2\2\2\u00bd\u00be\b\30\1\2\u00be\u00bf\5\60")
        buf.write("\31\2\u00bf\u00c5\3\2\2\2\u00c0\u00c1\f\4\2\2\u00c1\u00c2")
        buf.write("\t\4\2\2\u00c2\u00c4\5\60\31\2\u00c3\u00c0\3\2\2\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6/\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\5\62\32")
        buf.write("\2\u00c9\61\3\2\2\2\u00ca\u00d3\7\65\2\2\u00cb\u00d3\7")
        buf.write("\64\2\2\u00cc\u00d3\7\66\2\2\u00cd\u00d3\5$\23\2\u00ce")
        buf.write("\u00cf\7\35\2\2\u00cf\u00d0\5*\26\2\u00d0\u00d1\7\36\2")
        buf.write("\2\u00d1\u00d3\3\2\2\2\u00d2\u00ca\3\2\2\2\u00d2\u00cb")
        buf.write("\3\2\2\2\u00d2\u00cc\3\2\2\2\u00d2\u00cd\3\2\2\2\u00d2")
        buf.write("\u00ce\3\2\2\2\u00d3\63\3\2\2\2\24\67>CEV_hq}\u0086\u0091")
        buf.write("\u009b\u00a6\u00ad\u00b4\u00bb\u00c5\u00d2")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'body'", "'@'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='", "'{'", 
                     "'}'", "'('", "')'", "';'", "','", "'.'", "'+'", "'-'", 
                     "'/'", "'%'", "'!'", "'||'", "'&&'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "':='", "'^'", "'*'", 
                     "':'", "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "CLASS", "RETURN", 
                      "INT", "FLOAT", "CONST", "VAR", "FUNC", "VOID", "CONSTRUCTOR", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                      "FALSE", "BOOL", "STRING", "NULL", "SELF", "NEW", 
                      "EQ", "LB", "RB", "LP", "RP", "SM", "CM", "DOT", "ADD", 
                      "SUB", "DIV", "MOD", "NOT", "OR", "AND", "EQUAL", 
                      "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", 
                      "ASSIGN", "EXP", "MUL", "COLON", "EXTENDS", "FLOATLIT", 
                      "INTLIT", "ID", "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_supperclass = 2
    RULE_classname = 3
    RULE_construcdecl = 4
    RULE_classmember = 5
    RULE_attributedecl = 6
    RULE_attributelist = 7
    RULE_initlist = 8
    RULE_methoddecl = 9
    RULE_paramdecl = 10
    RULE_paramlist = 11
    RULE_param = 12
    RULE_body = 13
    RULE_bodydecl = 14
    RULE_mctype = 15
    RULE_membername = 16
    RULE_call_stmt = 17
    RULE_exprlist = 18
    RULE_nonNULL_exprlist = 19
    RULE_expr = 20
    RULE_exp1 = 21
    RULE_exp2 = 22
    RULE_exp3 = 23
    RULE_operands = 24

    ruleNames =  [ "program", "classdecl", "supperclass", "classname", "construcdecl", 
                   "classmember", "attributedecl", "attributelist", "initlist", 
                   "methoddecl", "paramdecl", "paramlist", "param", "body", 
                   "bodydecl", "mctype", "membername", "call_stmt", "exprlist", 
                   "nonNULL_exprlist", "expr", "exp1", "exp2", "exp3", "operands" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    CLASS=3
    RETURN=4
    INT=5
    FLOAT=6
    CONST=7
    VAR=8
    FUNC=9
    VOID=10
    CONSTRUCTOR=11
    BREAK=12
    CONTINUE=13
    IF=14
    ELSE=15
    FOR=16
    TRUE=17
    FALSE=18
    BOOL=19
    STRING=20
    NULL=21
    SELF=22
    NEW=23
    EQ=24
    LB=25
    RB=26
    LP=27
    RP=28
    SM=29
    CM=30
    DOT=31
    ADD=32
    SUB=33
    DIV=34
    MOD=35
    NOT=36
    OR=37
    AND=38
    EQUAL=39
    NOTEQUAL=40
    LESS=41
    GREATER=42
    LESSEQUAL=43
    GREATEREQUAL=44
    ASSIGN=45
    EXP=46
    MUL=47
    COLON=48
    EXTENDS=49
    FLOATLIT=50
    INTLIT=51
    ID=52
    WS=53
    NEWLINE=54
    LINE_COMMENT=55
    BLOCK_COMMENT=56
    ERROR_CHAR=57
    UNCLOSE_STRING=58
    ILLEGAL_ESCAPE=59

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSlangParser.EOF, 0)

        def classdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassdeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSlangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.classdecl()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 55
            self.match(CSlangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(CSlangParser.CLASS, 0)

        def classname(self):
            return self.getTypedRuleContext(CSlangParser.ClassnameContext,0)


        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def supperclass(self):
            return self.getTypedRuleContext(CSlangParser.SupperclassContext,0)


        def classmember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ClassmemberContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ClassmemberContext,i)


        def construcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ConstrucdeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ConstrucdeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = CSlangParser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(CSlangParser.CLASS)
            self.state = 58
            self.classname()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EXTENDS:
                self.state = 59
                self.supperclass()


            self.state = 62
            self.match(CSlangParser.LB)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 65
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 63
                    self.classmember()
                    pass

                elif la_ == 2:
                    self.state = 64
                    self.construcdecl()
                    pass


                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SupperclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTENDS(self):
            return self.getToken(CSlangParser.EXTENDS, 0)

        def classname(self):
            return self.getTypedRuleContext(CSlangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_supperclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSupperclass" ):
                return visitor.visitSupperclass(self)
            else:
                return visitor.visitChildren(self)




    def supperclass(self):

        localctx = CSlangParser.SupperclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_supperclass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(CSlangParser.EXTENDS)
            self.state = 73
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassname" ):
                return visitor.visitClassname(self)
            else:
                return visitor.visitChildren(self)




    def classname(self):

        localctx = CSlangParser.ClassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_classname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstrucdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def CONSTRUCTOR(self):
            return self.getToken(CSlangParser.CONSTRUCTOR, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(CSlangParser.ParamdeclContext,0)


        def body(self):
            return self.getTypedRuleContext(CSlangParser.BodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_construcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstrucdecl" ):
                return visitor.visitConstrucdecl(self)
            else:
                return visitor.visitChildren(self)




    def construcdecl(self):

        localctx = CSlangParser.ConstrucdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_construcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(CSlangParser.FUNC)
            self.state = 78
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 79
            self.paramdecl()
            self.state = 80
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassmemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(CSlangParser.MethoddeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classmember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassmember" ):
                return visitor.visitClassmember(self)
            else:
                return visitor.visitChildren(self)




    def classmember(self):

        localctx = CSlangParser.ClassmemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_classmember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.CONST, CSlangParser.VAR]:
                self.state = 82
                self.attributedecl()
                pass
            elif token in [CSlangParser.FUNC]:
                self.state = 83
                self.methoddecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 86
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributelist(self):
            return self.getTypedRuleContext(CSlangParser.AttributelistContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def mctype(self):
            return self.getTypedRuleContext(CSlangParser.MctypeContext,0)


        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def initlist(self):
            return self.getTypedRuleContext(CSlangParser.InitlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = CSlangParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 89
            self.attributelist()
            self.state = 90
            self.match(CSlangParser.COLON)
            self.state = 91
            self.mctype()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EQ:
                self.state = 92
                self.initlist()



                (3 == len(initlist))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def membername(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.MembernameContext)
            else:
                return self.getTypedRuleContext(CSlangParser.MembernameContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_attributelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributelist" ):
                return visitor.visitAttributelist(self)
            else:
                return visitor.visitChildren(self)




    def attributelist(self):

        localctx = CSlangParser.AttributelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attributelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.membername()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 98
                self.match(CSlangParser.CM)
                self.state = 99
                self.membername()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExprContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_initlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitlist" ):
                return visitor.visitInitlist(self)
            else:
                return visitor.visitChildren(self)




    def initlist(self):

        localctx = CSlangParser.InitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_initlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(CSlangParser.EQ)
            self.state = 106
            self.expr()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 107
                self.match(CSlangParser.CM)
                self.state = 108
                self.expr()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(CSlangParser.FUNC, 0)

        def membername(self):
            return self.getTypedRuleContext(CSlangParser.MembernameContext,0)


        def paramdecl(self):
            return self.getTypedRuleContext(CSlangParser.ParamdeclContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def mctype(self):
            return self.getTypedRuleContext(CSlangParser.MctypeContext,0)


        def body(self):
            return self.getTypedRuleContext(CSlangParser.BodyContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = CSlangParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methoddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(CSlangParser.FUNC)
            self.state = 115
            self.membername()
            self.state = 116
            self.paramdecl()
            self.state = 117
            self.match(CSlangParser.COLON)
            self.state = 118
            self.mctype()
            self.state = 119
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdecl" ):
                return visitor.visitParamdecl(self)
            else:
                return visitor.visitChildren(self)




    def paramdecl(self):

        localctx = CSlangParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(CSlangParser.LP)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.T__1 or _la==CSlangParser.ID:
                self.state = 122
                self.paramlist()


            self.state = 125
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ParamContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ParamContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.param()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 128
                self.match(CSlangParser.CM)
                self.state = 129
                self.param()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def membername(self):
            return self.getTypedRuleContext(CSlangParser.MembernameContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def mctype(self):
            return self.getTypedRuleContext(CSlangParser.MctypeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = CSlangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.membername()
            self.state = 136
            self.match(CSlangParser.COLON)
            self.state = 137
            self.mctype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def bodydecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.BodydeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.BodydeclContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = CSlangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(CSlangParser.LB)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.T__0:
                self.state = 140
                self.bodydecl()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CSlangParser.RULE_bodydecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBodydecl" ):
                return visitor.visitBodydecl(self)
            else:
                return visitor.visitChildren(self)




    def bodydecl(self):

        localctx = CSlangParser.BodydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_bodydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CSlangParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MctypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = CSlangParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_mctype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==CSlangParser.INT or _la==CSlangParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MembernameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_membername

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembername" ):
                return visitor.visitMembername(self)
            else:
                return visitor.visitChildren(self)




    def membername(self):

        localctx = CSlangParser.MembernameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_membername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.T__1:
                self.state = 152
                self.match(CSlangParser.T__1)


            self.state = 155
            self.match(CSlangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(CSlangParser.ExprlistContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = CSlangParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(CSlangParser.ID)
            self.state = 158
            self.match(CSlangParser.LP)
            self.state = 159
            self.exprlist()
            self.state = 160
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonNULL_exprlist(self):
            return self.getTypedRuleContext(CSlangParser.NonNULL_exprlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = CSlangParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprlist)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.nonNULL_exprlist()
                pass
            elif token in [CSlangParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonNULL_exprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def nonNULL_exprlist(self):
            return self.getTypedRuleContext(CSlangParser.NonNULL_exprlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_nonNULL_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonNULL_exprlist" ):
                return visitor.visitNonNULL_exprlist(self)
            else:
                return visitor.visitChildren(self)




    def nonNULL_exprlist(self):

        localctx = CSlangParser.NonNULL_exprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_nonNULL_exprlist)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.expr()
                self.state = 167
                self.match(CSlangParser.CM)
                self.state = 168
                self.nonNULL_exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(CSlangParser.Exp1Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.exp1()
                self.state = 174
                self.match(CSlangParser.ADD)
                self.state = 175
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Exp2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Exp2Context,i)


        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = CSlangParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp1)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.exp2(0)
                self.state = 181
                self.match(CSlangParser.SUB)
                self.state = 182
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(CSlangParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(CSlangParser.Exp2Context,0)


        def DIV(self):
            return self.getToken(CSlangParser.DIV, 0)

        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.exp3()
            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 190
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 191
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.DIV or _la==CSlangParser.MUL):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 192
                    self.exp3() 
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(CSlangParser.OperandsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)




    def exp3(self):

        localctx = CSlangParser.Exp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.operands()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def call_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Call_stmtContext,0)


        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = CSlangParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operands)
        try:
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(CSlangParser.INTLIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(CSlangParser.FLOATLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.match(CSlangParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.call_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.match(CSlangParser.LP)
                self.state = 205
                self.expr()
                self.state = 206
                self.match(CSlangParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.exp2_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




