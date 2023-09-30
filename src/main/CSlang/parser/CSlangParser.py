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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u01ce\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\6\2d\n\2\r\2\16\2e\3\2\3")
        buf.write("\2\3\3\3\3\3\3\5\3m\n\3\3\3\3\3\7\3q\n\3\f\3\16\3t\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\5\6\u0083\n\6\3\7\3\7\5\7\u0087\n\7\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\5\n\u0091\n\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00a5\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\5\16")
        buf.write("\u00b0\n\16\3\16\3\16\3\17\3\17\3\17\7\17\u00b7\n\17\f")
        buf.write("\17\16\17\u00ba\13\17\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\5\21\u00c7\n\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\24\3\24\3\24\7\24\u00d3\n\24\f")
        buf.write("\24\16\24\u00d6\13\24\3\25\3\25\3\25\3\25\3\25\5\25\u00dd")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u00e4\n\26\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\7\27\u00ec\n\27\f\27\16\27\u00ef")
        buf.write("\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00f7\n\30\f")
        buf.write("\30\16\30\u00fa\13\30\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u0102\n\31\f\31\16\31\u0105\13\31\3\32\3\32\3\32\5")
        buf.write("\32\u010a\n\32\3\33\3\33\3\33\5\33\u010f\n\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0119\n\34\f\34\16")
        buf.write("\34\u011c\13\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0126\n\35\3\35\5\35\u0129\n\35\7\35\u012b\n\35")
        buf.write("\f\35\16\35\u012e\13\35\3\36\3\36\5\36\u0132\n\36\3\36")
        buf.write("\3\36\3\36\5\36\u0137\n\36\3\36\5\36\u013a\n\36\3\36\5")
        buf.write("\36\u013d\n\36\3\37\3\37\3\37\3\37\5\37\u0143\n\37\3\37")
        buf.write("\3\37\5\37\u0147\n\37\3\37\5\37\u014a\n\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \5 \u0156\n \3!\3!\3!\7!\u015b\n!\f")
        buf.write("!\16!\u015e\13!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u016b\n\"\3#\3#\3#\3#\3$\7$\u0172\n$\f$\16")
        buf.write("$\u0175\13$\3%\3%\5%\u0179\n%\3%\3%\3%\3&\3&\5&\u0180")
        buf.write("\n&\3&\3&\3&\3&\5&\u0186\n&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\5*\u0198\n*\3*\3*\3+\3")
        buf.write("+\5+\u019e\n+\3+\3+\3,\3,\3,\3,\3,\5,\u01a7\n,\3,\3,\3")
        buf.write("-\3-\5-\u01ad\n-\3-\3-\3-\5-\u01b2\n-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\5.\u01bb\n.\3/\3/\3\60\3\60\3\60\3\60\7\60\u01c3")
        buf.write("\n\60\f\60\16\60\u01c6\13\60\5\60\u01c8\n\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\2\7,.\60\668\62\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`\2\b\3\2*/\3\2()\3\2\"#\4\2$&\62\62\4\2\4\499\3\2")
        buf.write("\658\2\u01dc\2c\3\2\2\2\4i\3\2\2\2\6w\3\2\2\2\bz\3\2\2")
        buf.write("\2\n\u0082\3\2\2\2\f\u0086\3\2\2\2\16\u0088\3\2\2\2\20")
        buf.write("\u008b\3\2\2\2\22\u0090\3\2\2\2\24\u0094\3\2\2\2\26\u00a4")
        buf.write("\3\2\2\2\30\u00a6\3\2\2\2\32\u00ad\3\2\2\2\34\u00b3\3")
        buf.write("\2\2\2\36\u00bb\3\2\2\2 \u00c6\3\2\2\2\"\u00c8\3\2\2\2")
        buf.write("$\u00cd\3\2\2\2&\u00cf\3\2\2\2(\u00dc\3\2\2\2*\u00e3\3")
        buf.write("\2\2\2,\u00e5\3\2\2\2.\u00f0\3\2\2\2\60\u00fb\3\2\2\2")
        buf.write("\62\u0109\3\2\2\2\64\u010e\3\2\2\2\66\u0110\3\2\2\28\u011d")
        buf.write("\3\2\2\2:\u013c\3\2\2\2<\u0149\3\2\2\2>\u0155\3\2\2\2")
        buf.write("@\u0157\3\2\2\2B\u016a\3\2\2\2D\u016c\3\2\2\2F\u0173\3")
        buf.write("\2\2\2H\u0178\3\2\2\2J\u017d\3\2\2\2L\u0187\3\2\2\2N\u018f")
        buf.write("\3\2\2\2P\u0192\3\2\2\2R\u0195\3\2\2\2T\u019d\3\2\2\2")
        buf.write("V\u01a1\3\2\2\2X\u01ac\3\2\2\2Z\u01ba\3\2\2\2\\\u01bc")
        buf.write("\3\2\2\2^\u01be\3\2\2\2`\u01cb\3\2\2\2bd\5\4\3\2cb\3\2")
        buf.write("\2\2de\3\2\2\2ec\3\2\2\2ef\3\2\2\2fg\3\2\2\2gh\7\2\2\3")
        buf.write("h\3\3\2\2\2ij\7\5\2\2jl\5$\23\2km\5\6\4\2lk\3\2\2\2lm")
        buf.write("\3\2\2\2mn\3\2\2\2nr\7\33\2\2oq\5\n\6\2po\3\2\2\2qt\3")
        buf.write("\2\2\2rp\3\2\2\2rs\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7\34")
        buf.write("\2\2v\5\3\2\2\2wx\7\64\2\2xy\5$\23\2y\7\3\2\2\2z{\7\13")
        buf.write("\2\2{|\7\r\2\2|}\5\32\16\2}~\5D#\2~\t\3\2\2\2\177\u0083")
        buf.write("\5\f\7\2\u0080\u0083\5\30\r\2\u0081\u0083\5\b\5\2\u0082")
        buf.write("\177\3\2\2\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083")
        buf.write("\13\3\2\2\2\u0084\u0087\5\16\b\2\u0085\u0087\5\20\t\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0085\3\2\2\2\u0087\r\3\2\2")
        buf.write("\2\u0088\u0089\7\n\2\2\u0089\u008a\5\22\n\2\u008a\17\3")
        buf.write("\2\2\2\u008b\u008c\7\t\2\2\u008c\u008d\5\22\n\2\u008d")
        buf.write("\21\3\2\2\2\u008e\u0091\5\24\13\2\u008f\u0091\5\26\f\2")
        buf.write("\u0090\u008e\3\2\2\2\u0090\u008f\3\2\2\2\u0091\u0092\3")
        buf.write("\2\2\2\u0092\u0093\7\37\2\2\u0093\23\3\2\2\2\u0094\u0095")
        buf.write("\5&\24\2\u0095\u0096\7\63\2\2\u0096\u0097\5 \21\2\u0097")
        buf.write("\25\3\2\2\2\u0098\u0099\5\\/\2\u0099\u009a\7 \2\2\u009a")
        buf.write("\u009b\5\26\f\2\u009b\u009c\7 \2\2\u009c\u009d\5(\25\2")
        buf.write("\u009d\u00a5\3\2\2\2\u009e\u009f\5\\/\2\u009f\u00a0\7")
        buf.write("\63\2\2\u00a0\u00a1\5 \21\2\u00a1\u00a2\7\32\2\2\u00a2")
        buf.write("\u00a3\5(\25\2\u00a3\u00a5\3\2\2\2\u00a4\u0098\3\2\2\2")
        buf.write("\u00a4\u009e\3\2\2\2\u00a5\27\3\2\2\2\u00a6\u00a7\7\13")
        buf.write("\2\2\u00a7\u00a8\5\\/\2\u00a8\u00a9\5\32\16\2\u00a9\u00aa")
        buf.write("\7\63\2\2\u00aa\u00ab\5 \21\2\u00ab\u00ac\5D#\2\u00ac")
        buf.write("\31\3\2\2\2\u00ad\u00af\7\35\2\2\u00ae\u00b0\5\34\17\2")
        buf.write("\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\u00b2\7\36\2\2\u00b2\33\3\2\2\2\u00b3\u00b8")
        buf.write("\5\36\20\2\u00b4\u00b5\7 \2\2\u00b5\u00b7\5\36\20\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00b6\3\2\2\2")
        buf.write("\u00b8\u00b9\3\2\2\2\u00b9\35\3\2\2\2\u00ba\u00b8\3\2")
        buf.write("\2\2\u00bb\u00bc\5&\24\2\u00bc\u00bd\7\63\2\2\u00bd\u00be")
        buf.write("\5 \21\2\u00be\37\3\2\2\2\u00bf\u00c7\7\7\2\2\u00c0\u00c7")
        buf.write("\7\b\2\2\u00c1\u00c7\7\23\2\2\u00c2\u00c7\7\24\2\2\u00c3")
        buf.write("\u00c7\7\f\2\2\u00c4\u00c7\5\"\22\2\u00c5\u00c7\7\3\2")
        buf.write("\2\u00c6\u00bf\3\2\2\2\u00c6\u00c0\3\2\2\2\u00c6\u00c1")
        buf.write("\3\2\2\2\u00c6\u00c2\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c5\3\2\2\2\u00c7!\3\2\2\2\u00c8")
        buf.write("\u00c9\7\27\2\2\u00c9\u00ca\5$\23\2\u00ca\u00cb\7\35\2")
        buf.write("\2\u00cb\u00cc\7\36\2\2\u00cc#\3\2\2\2\u00cd\u00ce\79")
        buf.write("\2\2\u00ce%\3\2\2\2\u00cf\u00d4\5\\/\2\u00d0\u00d1\7 ")
        buf.write("\2\2\u00d1\u00d3\5\\/\2\u00d2\u00d0\3\2\2\2\u00d3\u00d6")
        buf.write("\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\'\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\5*\26\2\u00d8")
        buf.write("\u00d9\7\61\2\2\u00d9\u00da\5*\26\2\u00da\u00dd\3\2\2")
        buf.write("\2\u00db\u00dd\5*\26\2\u00dc\u00d7\3\2\2\2\u00dc\u00db")
        buf.write("\3\2\2\2\u00dd)\3\2\2\2\u00de\u00df\5,\27\2\u00df\u00e0")
        buf.write("\t\2\2\2\u00e0\u00e1\5,\27\2\u00e1\u00e4\3\2\2\2\u00e2")
        buf.write("\u00e4\5,\27\2\u00e3\u00de\3\2\2\2\u00e3\u00e2\3\2\2\2")
        buf.write("\u00e4+\3\2\2\2\u00e5\u00e6\b\27\1\2\u00e6\u00e7\5.\30")
        buf.write("\2\u00e7\u00ed\3\2\2\2\u00e8\u00e9\f\4\2\2\u00e9\u00ea")
        buf.write("\t\3\2\2\u00ea\u00ec\5.\30\2\u00eb\u00e8\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee-\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\b\30\1")
        buf.write("\2\u00f1\u00f2\5\60\31\2\u00f2\u00f8\3\2\2\2\u00f3\u00f4")
        buf.write("\f\4\2\2\u00f4\u00f5\t\4\2\2\u00f5\u00f7\5\60\31\2\u00f6")
        buf.write("\u00f3\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9/\3\2\2\2\u00fa\u00f8\3\2\2")
        buf.write("\2\u00fb\u00fc\b\31\1\2\u00fc\u00fd\5\62\32\2\u00fd\u0103")
        buf.write("\3\2\2\2\u00fe\u00ff\f\4\2\2\u00ff\u0100\t\5\2\2\u0100")
        buf.write("\u0102\5\62\32\2\u0101\u00fe\3\2\2\2\u0102\u0105\3\2\2")
        buf.write("\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2\u0104\61\3")
        buf.write("\2\2\2\u0105\u0103\3\2\2\2\u0106\u0107\7\'\2\2\u0107\u010a")
        buf.write("\5\62\32\2\u0108\u010a\5\64\33\2\u0109\u0106\3\2\2\2\u0109")
        buf.write("\u0108\3\2\2\2\u010a\63\3\2\2\2\u010b\u010c\7#\2\2\u010c")
        buf.write("\u010f\5\64\33\2\u010d\u010f\5\66\34\2\u010e\u010b\3\2")
        buf.write("\2\2\u010e\u010d\3\2\2\2\u010f\65\3\2\2\2\u0110\u0111")
        buf.write("\b\34\1\2\u0111\u0112\58\35\2\u0112\u011a\3\2\2\2\u0113")
        buf.write("\u0114\f\4\2\2\u0114\u0115\7\30\2\2\u0115\u0116\5(\25")
        buf.write("\2\u0116\u0117\7\31\2\2\u0117\u0119\3\2\2\2\u0118\u0113")
        buf.write("\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\67\3\2\2\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u011e\b\35\1\2\u011e\u011f\5:\36\2\u011f\u012c\3\2\2")
        buf.write("\2\u0120\u0121\f\4\2\2\u0121\u0122\7!\2\2\u0122\u0128")
        buf.write("\79\2\2\u0123\u0125\7\35\2\2\u0124\u0126\5@!\2\u0125\u0124")
        buf.write("\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0129\7\36\2\2\u0128\u0123\3\2\2\2\u0128\u0129\3\2\2")
        buf.write("\2\u0129\u012b\3\2\2\2\u012a\u0120\3\2\2\2\u012b\u012e")
        buf.write("\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("9\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130\79\2\2\u0130")
        buf.write("\u0132\7!\2\2\u0131\u012f\3\2\2\2\u0131\u0132\3\2\2\2")
        buf.write("\u0132\u0133\3\2\2\2\u0133\u0139\7\4\2\2\u0134\u0136\7")
        buf.write("\35\2\2\u0135\u0137\5@!\2\u0136\u0135\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a\7\36\2\2\u0139")
        buf.write("\u0134\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013d\3\2\2\2")
        buf.write("\u013b\u013d\5<\37\2\u013c\u0131\3\2\2\2\u013c\u013b\3")
        buf.write("\2\2\2\u013d;\3\2\2\2\u013e\u013f\7\27\2\2\u013f\u0140")
        buf.write("\79\2\2\u0140\u0142\7\35\2\2\u0141\u0143\5@!\2\u0142\u0141")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144")
        buf.write("\u0146\7\36\2\2\u0145\u0147\5<\37\2\u0146\u0145\3\2\2")
        buf.write("\2\u0146\u0147\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u014a")
        buf.write("\5> \2\u0149\u013e\3\2\2\2\u0149\u0148\3\2\2\2\u014a=")
        buf.write("\3\2\2\2\u014b\u014c\7\35\2\2\u014c\u014d\5(\25\2\u014d")
        buf.write("\u014e\7\36\2\2\u014e\u0156\3\2\2\2\u014f\u0156\79\2\2")
        buf.write("\u0150\u0156\5Z.\2\u0151\u0152\7\26\2\2\u0152\u0153\7")
        buf.write("!\2\2\u0153\u0156\79\2\2\u0154\u0156\7\25\2\2\u0155\u014b")
        buf.write("\3\2\2\2\u0155\u014f\3\2\2\2\u0155\u0150\3\2\2\2\u0155")
        buf.write("\u0151\3\2\2\2\u0155\u0154\3\2\2\2\u0156?\3\2\2\2\u0157")
        buf.write("\u015c\5(\25\2\u0158\u0159\7 \2\2\u0159\u015b\5(\25\2")
        buf.write("\u015a\u0158\3\2\2\2\u015b\u015e\3\2\2\2\u015c\u015a\3")
        buf.write("\2\2\2\u015c\u015d\3\2\2\2\u015dA\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015f\u016b\5\f\7\2\u0160\u0161\5H%\2\u0161\u0162")
        buf.write("\7\37\2\2\u0162\u016b\3\2\2\2\u0163\u016b\5J&\2\u0164")
        buf.write("\u016b\5L\'\2\u0165\u016b\5N(\2\u0166\u016b\5P)\2\u0167")
        buf.write("\u016b\5R*\2\u0168\u016b\5T+\2\u0169\u016b\5D#\2\u016a")
        buf.write("\u015f\3\2\2\2\u016a\u0160\3\2\2\2\u016a\u0163\3\2\2\2")
        buf.write("\u016a\u0164\3\2\2\2\u016a\u0165\3\2\2\2\u016a\u0166\3")
        buf.write("\2\2\2\u016a\u0167\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016bC\3\2\2\2\u016c\u016d\7\33\2\2\u016d\u016e")
        buf.write("\5F$\2\u016e\u016f\7\34\2\2\u016fE\3\2\2\2\u0170\u0172")
        buf.write("\5B\"\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2\u0173")
        buf.write("\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174G\3\2\2\2\u0175")
        buf.write("\u0173\3\2\2\2\u0176\u0179\79\2\2\u0177\u0179\5\66\34")
        buf.write("\2\u0178\u0176\3\2\2\2\u0178\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017b\7\60\2\2\u017b\u017c\5(\25\2\u017c")
        buf.write("I\3\2\2\2\u017d\u017f\7\20\2\2\u017e\u0180\5D#\2\u017f")
        buf.write("\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181\3\2\2\2")
        buf.write("\u0181\u0182\5(\25\2\u0182\u0185\5D#\2\u0183\u0184\7\21")
        buf.write("\2\2\u0184\u0186\5D#\2\u0185\u0183\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186K\3\2\2\2\u0187\u0188\7\22\2\2\u0188\u0189")
        buf.write("\5H%\2\u0189\u018a\7\37\2\2\u018a\u018b\5(\25\2\u018b")
        buf.write("\u018c\7\37\2\2\u018c\u018d\5H%\2\u018d\u018e\5D#\2\u018e")
        buf.write("M\3\2\2\2\u018f\u0190\7\16\2\2\u0190\u0191\7\37\2\2\u0191")
        buf.write("O\3\2\2\2\u0192\u0193\7\17\2\2\u0193\u0194\7\37\2\2\u0194")
        buf.write("Q\3\2\2\2\u0195\u0197\7\6\2\2\u0196\u0198\5(\25\2\u0197")
        buf.write("\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019a\7\37\2\2\u019aS\3\2\2\2\u019b\u019e\5V,\2")
        buf.write("\u019c\u019e\5X-\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2")
        buf.write("\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\7\37\2\2\u01a0U\3")
        buf.write("\2\2\2\u01a1\u01a2\5(\25\2\u01a2\u01a3\7!\2\2\u01a3\u01a4")
        buf.write("\79\2\2\u01a4\u01a6\7\35\2\2\u01a5\u01a7\5@!\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u01a9\7\36\2\2\u01a9W\3\2\2\2\u01aa\u01ab\79\2\2\u01ab")
        buf.write("\u01ad\7!\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01af\7\4\2\2\u01af\u01b1\7")
        buf.write("\35\2\2\u01b0\u01b2\5@!\2\u01b1\u01b0\3\2\2\2\u01b1\u01b2")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4\7\36\2\2\u01b4")
        buf.write("Y\3\2\2\2\u01b5\u01bb\7\66\2\2\u01b6\u01bb\7\65\2\2\u01b7")
        buf.write("\u01bb\78\2\2\u01b8\u01bb\7\67\2\2\u01b9\u01bb\5^\60\2")
        buf.write("\u01ba\u01b5\3\2\2\2\u01ba\u01b6\3\2\2\2\u01ba\u01b7\3")
        buf.write("\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb[")
        buf.write("\3\2\2\2\u01bc\u01bd\t\6\2\2\u01bd]\3\2\2\2\u01be\u01c7")
        buf.write("\7\30\2\2\u01bf\u01c4\5`\61\2\u01c0\u01c1\7 \2\2\u01c1")
        buf.write("\u01c3\5`\61\2\u01c2\u01c0\3\2\2\2\u01c3\u01c6\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c8\3")
        buf.write("\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01bf\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\7\31\2\2\u01ca")
        buf.write("_\3\2\2\2\u01cb\u01cc\t\7\2\2\u01cca\3\2\2\2.elr\u0082")
        buf.write("\u0086\u0090\u00a4\u00af\u00b8\u00c6\u00d4\u00dc\u00e3")
        buf.write("\u00ed\u00f8\u0103\u0109\u010e\u011a\u0125\u0128\u012c")
        buf.write("\u0131\u0136\u0139\u013c\u0142\u0146\u0149\u0155\u015c")
        buf.write("\u016a\u0173\u0178\u017f\u0185\u0197\u019d\u01a6\u01ac")
        buf.write("\u01b1\u01ba\u01c4\u01c7")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'class'", "'return'", 
                     "'int'", "'float'", "'const'", "'var'", "'func'", "'void'", 
                     "'constructor'", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'bool'", "'string'", "'null'", "'self'", 
                     "'new'", "'['", "']'", "'='", "'{'", "'}'", "'('", 
                     "')'", "';'", "','", "'.'", "'+'", "'-'", "'/'", "'\\'", 
                     "'%'", "'!'", "'||'", "'&&'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "':='", "'^'", "'*'", "':'", 
                     "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "ARRAY", "STATIC", "CLASS", "RETURN", 
                      "INT", "FLOAT", "CONST", "VAR", "FUNC", "VOID", "CONSTRUCTOR", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "BOOL", 
                      "STRING", "NULL", "SELF", "NEW", "OB", "CB", "EQ", 
                      "LB", "RB", "LP", "RP", "SM", "CM", "DOT", "ADD", 
                      "SUB", "DIV", "BS", "MOD", "NOT", "OR", "AND", "EQUAL", 
                      "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", 
                      "ASSIGN", "CONCATENATION", "MUL", "COLON", "EXTENDS", 
                      "FLOATLIT", "INTLIT", "BOOLLIT", "STRING_LITERAL", 
                      "ID", "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_supperclass = 2
    RULE_construcdecl = 3
    RULE_classmember = 4
    RULE_attributedecl = 5
    RULE_var_attr = 6
    RULE_const_attr = 7
    RULE_attr_frag = 8
    RULE_no_initlist = 9
    RULE_initlist = 10
    RULE_methoddecl = 11
    RULE_paramdecl = 12
    RULE_paramlist = 13
    RULE_param = 14
    RULE_mctype = 15
    RULE_classtype = 16
    RULE_classname = 17
    RULE_attributelist = 18
    RULE_expression = 19
    RULE_expression1 = 20
    RULE_expression2 = 21
    RULE_expression3 = 22
    RULE_expression4 = 23
    RULE_expression5 = 24
    RULE_expression6 = 25
    RULE_expression7 = 26
    RULE_expression8 = 27
    RULE_expression9 = 28
    RULE_expression10 = 29
    RULE_operands = 30
    RULE_list_of_expression = 31
    RULE_statement = 32
    RULE_block_stmt = 33
    RULE_member_block = 34
    RULE_assign_stmt = 35
    RULE_if_stmt = 36
    RULE_for_stmt = 37
    RULE_break_stmt = 38
    RULE_continue_stmt = 39
    RULE_return_stmt = 40
    RULE_method_stm = 41
    RULE_instance_method = 42
    RULE_static_method = 43
    RULE_literal = 44
    RULE_membername = 45
    RULE_array_literal = 46
    RULE_elem = 47

    ruleNames =  [ "program", "classdecl", "supperclass", "construcdecl", 
                   "classmember", "attributedecl", "var_attr", "const_attr", 
                   "attr_frag", "no_initlist", "initlist", "methoddecl", 
                   "paramdecl", "paramlist", "param", "mctype", "classtype", 
                   "classname", "attributelist", "expression", "expression1", 
                   "expression2", "expression3", "expression4", "expression5", 
                   "expression6", "expression7", "expression8", "expression9", 
                   "expression10", "operands", "list_of_expression", "statement", 
                   "block_stmt", "member_block", "assign_stmt", "if_stmt", 
                   "for_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "method_stm", "instance_method", "static_method", "literal", 
                   "membername", "array_literal", "elem" ]

    EOF = Token.EOF
    ARRAY=1
    STATIC=2
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
    BOOL=17
    STRING=18
    NULL=19
    SELF=20
    NEW=21
    OB=22
    CB=23
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
    BS=35
    MOD=36
    NOT=37
    OR=38
    AND=39
    EQUAL=40
    NOTEQUAL=41
    LESS=42
    GREATER=43
    LESSEQUAL=44
    GREATEREQUAL=45
    ASSIGN=46
    CONCATENATION=47
    MUL=48
    COLON=49
    EXTENDS=50
    FLOATLIT=51
    INTLIT=52
    BOOLLIT=53
    STRING_LITERAL=54
    ID=55
    WS=56
    NEWLINE=57
    LINE_COMMENT=58
    BLOCK_COMMENT=59
    ERROR_CHAR=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62

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
            self.state = 97 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                self.classdecl()
                self.state = 99 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 101
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
            self.state = 103
            self.match(CSlangParser.CLASS)
            self.state = 104
            self.classname()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EXTENDS:
                self.state = 105
                self.supperclass()


            self.state = 108
            self.match(CSlangParser.LB)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 109
                self.classmember()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 115
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
            self.state = 117
            self.match(CSlangParser.EXTENDS)
            self.state = 118
            self.classname()
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


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_construcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstrucdecl" ):
                return visitor.visitConstrucdecl(self)
            else:
                return visitor.visitChildren(self)




    def construcdecl(self):

        localctx = CSlangParser.ConstrucdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_construcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(CSlangParser.FUNC)
            self.state = 121
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 122
            self.paramdecl()
            self.state = 123
            self.block_stmt()
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

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(CSlangParser.MethoddeclContext,0)


        def construcdecl(self):
            return self.getTypedRuleContext(CSlangParser.ConstrucdeclContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classmember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassmember" ):
                return visitor.visitClassmember(self)
            else:
                return visitor.visitChildren(self)




    def classmember(self):

        localctx = CSlangParser.ClassmemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_classmember)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.construcdecl()
                pass


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

        def var_attr(self):
            return self.getTypedRuleContext(CSlangParser.Var_attrContext,0)


        def const_attr(self):
            return self.getTypedRuleContext(CSlangParser.Const_attrContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = CSlangParser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attributedecl)
        try:
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 130
                self.var_attr()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.const_attr()
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


    class Var_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def attr_frag(self):
            return self.getTypedRuleContext(CSlangParser.Attr_fragContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_var_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_attr" ):
                return visitor.visitVar_attr(self)
            else:
                return visitor.visitChildren(self)




    def var_attr(self):

        localctx = CSlangParser.Var_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(CSlangParser.VAR)
            self.state = 135
            self.attr_frag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def attr_frag(self):
            return self.getTypedRuleContext(CSlangParser.Attr_fragContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_const_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_attr" ):
                return visitor.visitConst_attr(self)
            else:
                return visitor.visitChildren(self)




    def const_attr(self):

        localctx = CSlangParser.Const_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_const_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(CSlangParser.CONST)
            self.state = 138
            self.attr_frag()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_fragContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def no_initlist(self):
            return self.getTypedRuleContext(CSlangParser.No_initlistContext,0)


        def initlist(self):
            return self.getTypedRuleContext(CSlangParser.InitlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_attr_frag

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr_frag" ):
                return visitor.visitAttr_frag(self)
            else:
                return visitor.visitChildren(self)




    def attr_frag(self):

        localctx = CSlangParser.Attr_fragContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr_frag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 140
                self.no_initlist()
                pass

            elif la_ == 2:
                self.state = 141
                self.initlist()
                pass


            self.state = 144
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class No_initlistContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return CSlangParser.RULE_no_initlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNo_initlist" ):
                return visitor.visitNo_initlist(self)
            else:
                return visitor.visitChildren(self)




    def no_initlist(self):

        localctx = CSlangParser.No_initlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_no_initlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.attributelist()
            self.state = 147
            self.match(CSlangParser.COLON)
            self.state = 148
            self.mctype()
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

        def membername(self):
            return self.getTypedRuleContext(CSlangParser.MembernameContext,0)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def initlist(self):
            return self.getTypedRuleContext(CSlangParser.InitlistContext,0)


        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(CSlangParser.COLON, 0)

        def mctype(self):
            return self.getTypedRuleContext(CSlangParser.MctypeContext,0)


        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_initlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitlist" ):
                return visitor.visitInitlist(self)
            else:
                return visitor.visitChildren(self)




    def initlist(self):

        localctx = CSlangParser.InitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_initlist)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.membername()
                self.state = 151
                self.match(CSlangParser.CM)
                self.state = 152
                self.initlist()
                self.state = 153
                self.match(CSlangParser.CM)
                self.state = 154
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.membername()
                self.state = 157
                self.match(CSlangParser.COLON)
                self.state = 158
                self.mctype()
                self.state = 159
                self.match(CSlangParser.EQ)
                self.state = 160
                self.expression()
                pass


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


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = CSlangParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_methoddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(CSlangParser.FUNC)
            self.state = 165
            self.membername()
            self.state = 166
            self.paramdecl()
            self.state = 167
            self.match(CSlangParser.COLON)
            self.state = 168
            self.mctype()
            self.state = 169
            self.block_stmt()
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
        self.enterRule(localctx, 24, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(CSlangParser.LP)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.STATIC or _la==CSlangParser.ID:
                self.state = 172
                self.paramlist()


            self.state = 175
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
        self.enterRule(localctx, 26, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.param()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 178
                self.match(CSlangParser.CM)
                self.state = 179
                self.param()
                self.state = 184
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

        def attributelist(self):
            return self.getTypedRuleContext(CSlangParser.AttributelistContext,0)


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
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.attributelist()
            self.state = 186
            self.match(CSlangParser.COLON)
            self.state = 187
            self.mctype()
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

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def VOID(self):
            return self.getToken(CSlangParser.VOID, 0)

        def classtype(self):
            return self.getTypedRuleContext(CSlangParser.ClasstypeContext,0)


        def ARRAY(self):
            return self.getToken(CSlangParser.ARRAY, 0)

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
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 193
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 6)
                self.state = 194
                self.classtype()
                pass
            elif token in [CSlangParser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 195
                self.match(CSlangParser.ARRAY)
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


    class ClasstypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def classname(self):
            return self.getTypedRuleContext(CSlangParser.ClassnameContext,0)


        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_classtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasstype" ):
                return visitor.visitClasstype(self)
            else:
                return visitor.visitChildren(self)




    def classtype(self):

        localctx = CSlangParser.ClasstypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(CSlangParser.NEW)
            self.state = 199
            self.classname()
            self.state = 200
            self.match(CSlangParser.LP)
            self.state = 201
            self.match(CSlangParser.RP)
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
        self.enterRule(localctx, 34, self.RULE_classname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(CSlangParser.ID)
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
        self.enterRule(localctx, 36, self.RULE_attributelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.membername()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 206
                self.match(CSlangParser.CM)
                self.state = 207
                self.membername()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expression1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expression1Context,i)


        def CONCATENATION(self):
            return self.getToken(CSlangParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CSlangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.expression1()
                self.state = 214
                self.match(CSlangParser.CONCATENATION)
                self.state = 215
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expression2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(CSlangParser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def GREATER(self):
            return self.getToken(CSlangParser.GREATER, 0)

        def LESSEQUAL(self):
            return self.getToken(CSlangParser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(CSlangParser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = CSlangParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.expression2(0)
                self.state = 221
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.NOTEQUAL) | (1 << CSlangParser.LESS) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.LESSEQUAL) | (1 << CSlangParser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(CSlangParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(CSlangParser.Expression2Context,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 230
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 231
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.OR or _la==CSlangParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 232
                    self.expression3(0) 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(CSlangParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(CSlangParser.Expression3Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 246
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 241
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 242
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 243
                    self.expression4(0) 
                self.state = 248
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(CSlangParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(CSlangParser.Expression4Context,0)


        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def DIV(self):
            return self.getToken(CSlangParser.DIV, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def BS(self):
            return self.getToken(CSlangParser.BS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 257
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 252
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 253
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.DIV) | (1 << CSlangParser.BS) | (1 << CSlangParser.MOD) | (1 << CSlangParser.MUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 254
                    self.expression5() 
                self.state = 259
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(CSlangParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(CSlangParser.Expression6Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = CSlangParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression5)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(CSlangParser.NOT)
                self.state = 261
                self.expression5()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.SUB, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.expression6()
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


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(CSlangParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(CSlangParser.Expression7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = CSlangParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression6)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(CSlangParser.SUB)
                self.state = 266
                self.expression6()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.expression7(0)
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression8(self):
            return self.getTypedRuleContext(CSlangParser.Expression8Context,0)


        def expression7(self):
            return self.getTypedRuleContext(CSlangParser.Expression7Context,0)


        def OB(self):
            return self.getToken(CSlangParser.OB, 0)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def CB(self):
            return self.getToken(CSlangParser.CB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)



    def expression7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expression7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.expression8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                    self.state = 273
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 274
                    self.match(CSlangParser.OB)
                    self.state = 275
                    self.expression()
                    self.state = 276
                    self.match(CSlangParser.CB) 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(CSlangParser.Expression9Context,0)


        def expression8(self):
            return self.getTypedRuleContext(CSlangParser.Expression8Context,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)



    def expression8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expression8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expression8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expression9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    self.match(CSlangParser.DOT)
                    self.state = 288
                    self.match(CSlangParser.ID)
                    self.state = 294
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        self.state = 289
                        self.match(CSlangParser.LP)
                        self.state = 291
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                            self.state = 290
                            self.list_of_expression()


                        self.state = 293
                        self.match(CSlangParser.RP)

             
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(CSlangParser.STATIC, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def expression10(self):
            return self.getTypedRuleContext(CSlangParser.Expression10Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)




    def expression9(self):

        localctx = CSlangParser.Expression9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression9)
        self._la = 0 # Token type
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 301
                    self.match(CSlangParser.ID)
                    self.state = 302
                    self.match(CSlangParser.DOT)


                self.state = 305
                self.match(CSlangParser.STATIC)
                self.state = 311
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 306
                    self.match(CSlangParser.LP)
                    self.state = 308
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                        self.state = 307
                        self.list_of_expression()


                    self.state = 310
                    self.match(CSlangParser.RP)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.expression10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def expression10(self):
            return self.getTypedRuleContext(CSlangParser.Expression10Context,0)


        def operands(self):
            return self.getTypedRuleContext(CSlangParser.OperandsContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)




    def expression10(self):

        localctx = CSlangParser.Expression10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expression10)
        self._la = 0 # Token type
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.match(CSlangParser.NEW)
                self.state = 317
                self.match(CSlangParser.ID)
                self.state = 318
                self.match(CSlangParser.LP)
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 319
                    self.list_of_expression()


                self.state = 322
                self.match(CSlangParser.RP)
                self.state = 324
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 323
                    self.expression10()


                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.operands()
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


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(CSlangParser.LiteralContext,0)


        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def NULL(self):
            return self.getToken(CSlangParser.NULL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = CSlangParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_operands)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.match(CSlangParser.LP)
                self.state = 330
                self.expression()
                self.state = 331
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.OB, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 335
                self.match(CSlangParser.SELF)
                self.state = 336
                self.match(CSlangParser.DOT)
                self.state = 337
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.match(CSlangParser.NULL)
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


    class List_of_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ExpressionContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_list_of_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expression" ):
                return visitor.visitList_of_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expression(self):

        localctx = CSlangParser.List_of_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_list_of_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.expression()
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 342
                self.match(CSlangParser.CM)
                self.state = 343
                self.expression()
                self.state = 348
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(CSlangParser.AttributedeclContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,0)


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(CSlangParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(CSlangParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Return_stmtContext,0)


        def method_stm(self):
            return self.getTypedRuleContext(CSlangParser.Method_stmContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CSlangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.assign_stmt()
                self.state = 351
                self.match(CSlangParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 354
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 355
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 356
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 357
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 358
                self.method_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 359
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def member_block(self):
            return self.getTypedRuleContext(CSlangParser.Member_blockContext,0)


        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = CSlangParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(CSlangParser.LB)
            self.state = 363
            self.member_block()
            self.state = 364
            self.match(CSlangParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSlangParser.StatementContext,i)


        def getRuleIndex(self):
            return CSlangParser.RULE_member_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_block" ):
                return visitor.visitMember_block(self)
            else:
                return visitor.visitChildren(self)




    def member_block(self):

        localctx = CSlangParser.Member_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_member_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 366
                self.statement()
                self.state = 371
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(CSlangParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expression7(self):
            return self.getTypedRuleContext(CSlangParser.Expression7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 372
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.state = 373
                self.expression7(0)
                pass


            self.state = 376
            self.match(CSlangParser.ASSIGN)
            self.state = 377
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSlangParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_stmtContext,i)


        def ELSE(self):
            return self.getToken(CSlangParser.ELSE, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = CSlangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(CSlangParser.IF)
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LB:
                self.state = 380
                self.block_stmt()


            self.state = 383
            self.expression()
            self.state = 384
            self.block_stmt()
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 385
                self.match(CSlangParser.ELSE)
                self.state = 386
                self.block_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSlangParser.FOR, 0)

        def assign_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Assign_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Assign_stmtContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SM)
            else:
                return self.getToken(CSlangParser.SM, i)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(CSlangParser.Block_stmtContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = CSlangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(CSlangParser.FOR)
            self.state = 390
            self.assign_stmt()
            self.state = 391
            self.match(CSlangParser.SM)
            self.state = 392
            self.expression()
            self.state = 393
            self.match(CSlangParser.SM)
            self.state = 394
            self.assign_stmt()
            self.state = 395
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSlangParser.BREAK, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = CSlangParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(CSlangParser.BREAK)
            self.state = 398
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSlangParser.CONTINUE, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = CSlangParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(CSlangParser.CONTINUE)
            self.state = 401
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSlangParser.RETURN, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(CSlangParser.RETURN)
            self.state = 405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 404
                self.expression()


            self.state = 407
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_stmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def instance_method(self):
            return self.getTypedRuleContext(CSlangParser.Instance_methodContext,0)


        def static_method(self):
            return self.getTypedRuleContext(CSlangParser.Static_methodContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_stm" ):
                return visitor.visitMethod_stm(self)
            else:
                return visitor.visitChildren(self)




    def method_stm(self):

        localctx = CSlangParser.Method_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_method_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 409
                self.instance_method()
                pass

            elif la_ == 2:
                self.state = 410
                self.static_method()
                pass


            self.state = 413
            self.match(CSlangParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_instance_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method" ):
                return visitor.visitInstance_method(self)
            else:
                return visitor.visitChildren(self)




    def instance_method(self):

        localctx = CSlangParser.Instance_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.expression()
            self.state = 416
            self.match(CSlangParser.DOT)
            self.state = 417
            self.match(CSlangParser.ID)
            self.state = 418
            self.match(CSlangParser.LP)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 419
                self.list_of_expression()


            self.state = 422
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(CSlangParser.STATIC, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_static_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method" ):
                return visitor.visitStatic_method(self)
            else:
                return visitor.visitChildren(self)




    def static_method(self):

        localctx = CSlangParser.Static_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 424
                self.match(CSlangParser.ID)
                self.state = 425
                self.match(CSlangParser.DOT)


            self.state = 428
            self.match(CSlangParser.STATIC)
            self.state = 429
            self.match(CSlangParser.LP)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 430
                self.list_of_expression()


            self.state = 433
            self.match(CSlangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def STRING_LITERAL(self):
            return self.getToken(CSlangParser.STRING_LITERAL, 0)

        def BOOLLIT(self):
            return self.getToken(CSlangParser.BOOLLIT, 0)

        def array_literal(self):
            return self.getTypedRuleContext(CSlangParser.Array_literalContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literal)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 438
                self.match(CSlangParser.BOOLLIT)
                pass
            elif token in [CSlangParser.OB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 439
                self.array_literal()
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


    class MembernameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC(self):
            return self.getToken(CSlangParser.STATIC, 0)

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
        self.enterRule(localctx, 90, self.RULE_membername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            _la = self._input.LA(1)
            if not(_la==CSlangParser.STATIC or _la==CSlangParser.ID):
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(CSlangParser.OB, 0)

        def CB(self):
            return self.getToken(CSlangParser.CB, 0)

        def elem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.ElemContext)
            else:
                return self.getTypedRuleContext(CSlangParser.ElemContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.CM)
            else:
                return self.getToken(CSlangParser.CM, i)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = CSlangParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(CSlangParser.OB)
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL))) != 0):
                self.state = 445
                self.elem()
                self.state = 450
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 446
                    self.match(CSlangParser.CM)
                    self.state = 447
                    self.elem()
                    self.state = 452
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 455
            self.match(CSlangParser.CB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def STRING_LITERAL(self):
            return self.getToken(CSlangParser.STRING_LITERAL, 0)

        def BOOLLIT(self):
            return self.getToken(CSlangParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem" ):
                return visitor.visitElem(self)
            else:
                return visitor.visitChildren(self)




    def elem(self):

        localctx = CSlangParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[21] = self.expression2_sempred
        self._predicates[22] = self.expression3_sempred
        self._predicates[23] = self.expression4_sempred
        self._predicates[26] = self.expression7_sempred
        self._predicates[27] = self.expression8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression7_sempred(self, localctx:Expression7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression8_sempred(self, localctx:Expression8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




