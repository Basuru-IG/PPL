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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u01a2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\6\2R\n\2\r\2\16\2S\3\2\3\2\3\3\3\3")
        buf.write("\3\3\5\3[\n\3\3\3\3\3\7\3_\n\3\f\3\16\3b\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6s\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u0083\n\7\3\b\3\b\3\b\7\b\u0088\n\b\f\b")
        buf.write("\16\b\u008b\13\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\5")
        buf.write("\n\u0096\n\n\3\n\3\n\3\13\3\13\3\13\7\13\u009d\n\13\f")
        buf.write("\13\16\13\u00a0\13\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\r\u00ad\n\r\3\16\3\16\3\17\3\17\3\17\7")
        buf.write("\17\u00b4\n\17\f\17\16\17\u00b7\13\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\5\20\u00be\n\20\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00c5\n\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00cd\n")
        buf.write("\22\f\22\16\22\u00d0\13\22\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\7\23\u00d8\n\23\f\23\16\23\u00db\13\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\7\24\u00e3\n\24\f\24\16\24\u00e6\13")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\7\25\u00ee\n\25\f\25")
        buf.write("\16\25\u00f1\13\25\3\26\3\26\3\26\5\26\u00f6\n\26\3\27")
        buf.write("\3\27\3\27\5\27\u00fb\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u0106\n\30\3\31\3\31\3\31\3\31")
        buf.write("\5\31\u010c\n\31\3\31\3\31\3\31\5\31\u0111\n\31\3\31\5")
        buf.write("\31\u0114\n\31\3\31\5\31\u0117\n\31\3\31\5\31\u011a\n")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0124")
        buf.write("\n\31\3\31\5\31\u0127\n\31\7\31\u0129\n\31\f\31\16\31")
        buf.write("\u012c\13\31\3\32\3\32\3\32\3\32\5\32\u0132\n\32\3\32")
        buf.write("\3\32\5\32\u0136\n\32\3\32\5\32\u0139\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0145\n\33")
        buf.write("\3\34\3\34\3\34\7\34\u014a\n\34\f\34\16\34\u014d\13\34")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\5\36\u015c\n\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \7 \u0166\n \f \16 \u0169\13 \3!\3!\5!\u016d\n!\3")
        buf.write("!\3!\3!\3\"\3\"\5\"\u0174\n\"\3\"\3\"\3\"\3\"\5\"\u017a")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\5")
        buf.write("&\u018c\n&\3&\3&\3\'\3\'\5\'\u0192\n\'\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u0198\n\'\3\'\3\'\3\'\3\'\5\'\u019e\n\'\3(\3(\3(")
        buf.write("\2\7\"$&(\60)\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$&(*,.\60\62\64\668:<>@BDFHJLN\2\n\3\2\t\n\3\2/\62\3")
        buf.write("\2-.\3\2+,\3\2%&\4\2\')\65\65\3\28<\4\2\4\4??\2\u01b6")
        buf.write("\2Q\3\2\2\2\4W\3\2\2\2\6e\3\2\2\2\bh\3\2\2\2\nr\3\2\2")
        buf.write("\2\f\u0082\3\2\2\2\16\u0084\3\2\2\2\20\u008c\3\2\2\2\22")
        buf.write("\u0093\3\2\2\2\24\u0099\3\2\2\2\26\u00a1\3\2\2\2\30\u00ac")
        buf.write("\3\2\2\2\32\u00ae\3\2\2\2\34\u00b0\3\2\2\2\36\u00bd\3")
        buf.write("\2\2\2 \u00c4\3\2\2\2\"\u00c6\3\2\2\2$\u00d1\3\2\2\2&")
        buf.write("\u00dc\3\2\2\2(\u00e7\3\2\2\2*\u00f5\3\2\2\2,\u00fa\3")
        buf.write("\2\2\2.\u0105\3\2\2\2\60\u0119\3\2\2\2\62\u0138\3\2\2")
        buf.write("\2\64\u0144\3\2\2\2\66\u0146\3\2\2\28\u014e\3\2\2\2:\u015b")
        buf.write("\3\2\2\2<\u015d\3\2\2\2>\u0167\3\2\2\2@\u016c\3\2\2\2")
        buf.write("B\u0171\3\2\2\2D\u017b\3\2\2\2F\u0183\3\2\2\2H\u0186\3")
        buf.write("\2\2\2J\u0189\3\2\2\2L\u019d\3\2\2\2N\u019f\3\2\2\2PR")
        buf.write("\5\4\3\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2")
        buf.write("\2\2UV\7\2\2\3V\3\3\2\2\2WX\7\5\2\2XZ\5\32\16\2Y[\5\6")
        buf.write("\4\2ZY\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\`\7\36\2\2]_\5\n")
        buf.write("\6\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2")
        buf.write("b`\3\2\2\2cd\7\37\2\2d\5\3\2\2\2ef\7\67\2\2fg\5\32\16")
        buf.write("\2g\7\3\2\2\2hi\7\13\2\2ij\7\r\2\2jk\5\22\n\2kl\5<\37")
        buf.write("\2l\t\3\2\2\2mn\5\f\7\2no\7\"\2\2os\3\2\2\2ps\5\20\t\2")
        buf.write("qs\5\b\5\2rm\3\2\2\2rp\3\2\2\2rq\3\2\2\2s\13\3\2\2\2t")
        buf.write("u\t\2\2\2uv\5\34\17\2vw\7\66\2\2wx\5\30\r\2xy\7\35\2\2")
        buf.write("yz\5\16\b\2z{\3\2\2\2{|\6\7\2\3|\u0083\3\2\2\2}~\t\2\2")
        buf.write("\2~\177\5\34\17\2\177\u0080\7\66\2\2\u0080\u0081\5\30")
        buf.write("\r\2\u0081\u0083\3\2\2\2\u0082t\3\2\2\2\u0082}\3\2\2\2")
        buf.write("\u0083\r\3\2\2\2\u0084\u0089\5\36\20\2\u0085\u0086\7#")
        buf.write("\2\2\u0086\u0088\5\36\20\2\u0087\u0085\3\2\2\2\u0088\u008b")
        buf.write("\3\2\2\2\u0089\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a")
        buf.write("\17\3\2\2\2\u008b\u0089\3\2\2\2\u008c\u008d\7\13\2\2\u008d")
        buf.write("\u008e\5N(\2\u008e\u008f\5\22\n\2\u008f\u0090\7\66\2\2")
        buf.write("\u0090\u0091\5\30\r\2\u0091\u0092\5<\37\2\u0092\21\3\2")
        buf.write("\2\2\u0093\u0095\7 \2\2\u0094\u0096\5\24\13\2\u0095\u0094")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\3\2\2\2\u0097")
        buf.write("\u0098\7!\2\2\u0098\23\3\2\2\2\u0099\u009e\5\26\f\2\u009a")
        buf.write("\u009b\7#\2\2\u009b\u009d\5\26\f\2\u009c\u009a\3\2\2\2")
        buf.write("\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009f\3")
        buf.write("\2\2\2\u009f\25\3\2\2\2\u00a0\u009e\3\2\2\2\u00a1\u00a2")
        buf.write("\5\34\17\2\u00a2\u00a3\7\66\2\2\u00a3\u00a4\5\30\r\2\u00a4")
        buf.write("\27\3\2\2\2\u00a5\u00ad\7\7\2\2\u00a6\u00ad\7\b\2\2\u00a7")
        buf.write("\u00ad\7\25\2\2\u00a8\u00ad\7\26\2\2\u00a9\u00ad\7\f\2")
        buf.write("\2\u00aa\u00ad\5\32\16\2\u00ab\u00ad\7\3\2\2\u00ac\u00a5")
        buf.write("\3\2\2\2\u00ac\u00a6\3\2\2\2\u00ac\u00a7\3\2\2\2\u00ac")
        buf.write("\u00a8\3\2\2\2\u00ac\u00a9\3\2\2\2\u00ac\u00aa\3\2\2\2")
        buf.write("\u00ac\u00ab\3\2\2\2\u00ad\31\3\2\2\2\u00ae\u00af\7?\2")
        buf.write("\2\u00af\33\3\2\2\2\u00b0\u00b5\5N(\2\u00b1\u00b2\7#\2")
        buf.write("\2\u00b2\u00b4\5N(\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\3")
        buf.write("\2\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\35")
        buf.write("\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\5 \21\2\u00b9")
        buf.write("\u00ba\t\3\2\2\u00ba\u00bb\5 \21\2\u00bb\u00be\3\2\2\2")
        buf.write("\u00bc\u00be\5 \21\2\u00bd\u00b8\3\2\2\2\u00bd\u00bc\3")
        buf.write("\2\2\2\u00be\37\3\2\2\2\u00bf\u00c0\5\"\22\2\u00c0\u00c1")
        buf.write("\t\4\2\2\u00c1\u00c2\5\"\22\2\u00c2\u00c5\3\2\2\2\u00c3")
        buf.write("\u00c5\5\"\22\2\u00c4\u00bf\3\2\2\2\u00c4\u00c3\3\2\2")
        buf.write("\2\u00c5!\3\2\2\2\u00c6\u00c7\b\22\1\2\u00c7\u00c8\5$")
        buf.write("\23\2\u00c8\u00ce\3\2\2\2\u00c9\u00ca\f\4\2\2\u00ca\u00cb")
        buf.write("\t\5\2\2\u00cb\u00cd\5$\23\2\u00cc\u00c9\3\2\2\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf#\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\b\23\1")
        buf.write("\2\u00d2\u00d3\5&\24\2\u00d3\u00d9\3\2\2\2\u00d4\u00d5")
        buf.write("\f\4\2\2\u00d5\u00d6\t\6\2\2\u00d6\u00d8\5&\24\2\u00d7")
        buf.write("\u00d4\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da%\3\2\2\2\u00db\u00d9\3\2\2")
        buf.write("\2\u00dc\u00dd\b\24\1\2\u00dd\u00de\5(\25\2\u00de\u00e4")
        buf.write("\3\2\2\2\u00df\u00e0\f\4\2\2\u00e0\u00e1\t\7\2\2\u00e1")
        buf.write("\u00e3\5(\25\2\u00e2\u00df\3\2\2\2\u00e3\u00e6\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\'\3\2\2")
        buf.write("\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\b\25\1\2\u00e8\u00e9")
        buf.write("\5*\26\2\u00e9\u00ef\3\2\2\2\u00ea\u00eb\f\4\2\2\u00eb")
        buf.write("\u00ec\7\64\2\2\u00ec\u00ee\5*\26\2\u00ed\u00ea\3\2\2")
        buf.write("\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0")
        buf.write("\3\2\2\2\u00f0)\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3")
        buf.write("\7*\2\2\u00f3\u00f6\5*\26\2\u00f4\u00f6\5,\27\2\u00f5")
        buf.write("\u00f2\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6+\3\2\2\2\u00f7")
        buf.write("\u00f8\t\6\2\2\u00f8\u00fb\5,\27\2\u00f9\u00fb\5.\30\2")
        buf.write("\u00fa\u00f7\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb-\3\2\2")
        buf.write("\2\u00fc\u00fd\5\60\31\2\u00fd\u00fe\7\33\2\2\u00fe\u00ff")
        buf.write("\5\36\20\2\u00ff\u0100\7\34\2\2\u0100\u0106\3\2\2\2\u0101")
        buf.write("\u0102\5\60\31\2\u0102\u0103\78\2\2\u0103\u0106\3\2\2")
        buf.write("\2\u0104\u0106\5\60\31\2\u0105\u00fc\3\2\2\2\u0105\u0101")
        buf.write("\3\2\2\2\u0105\u0104\3\2\2\2\u0106/\3\2\2\2\u0107\u010b")
        buf.write("\b\31\1\2\u0108\u0109\5N(\2\u0109\u010a\7$\2\2\u010a\u010c")
        buf.write("\3\2\2\2\u010b\u0108\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d\u0113\5N(\2\u010e\u0110\7 \2\2\u010f")
        buf.write("\u0111\5\66\34\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2")
        buf.write("\2\u0111\u0112\3\2\2\2\u0112\u0114\7!\2\2\u0113\u010e")
        buf.write("\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2\u0115")
        buf.write("\u0117\7\"\2\2\u0116\u0115\3\2\2\2\u0116\u0117\3\2\2\2")
        buf.write("\u0117\u011a\3\2\2\2\u0118\u011a\5\62\32\2\u0119\u0107")
        buf.write("\3\2\2\2\u0119\u0118\3\2\2\2\u011a\u012a\3\2\2\2\u011b")
        buf.write("\u011c\f\6\2\2\u011c\u011d\7$\2\2\u011d\u0129\7?\2\2\u011e")
        buf.write("\u011f\f\5\2\2\u011f\u0120\7$\2\2\u0120\u0126\5N(\2\u0121")
        buf.write("\u0123\7 \2\2\u0122\u0124\5\66\34\2\u0123\u0122\3\2\2")
        buf.write("\2\u0123\u0124\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u0127")
        buf.write("\7!\2\2\u0126\u0121\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u011b\3\2\2\2\u0128\u011e\3\2\2\2")
        buf.write("\u0129\u012c\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3")
        buf.write("\2\2\2\u012b\61\3\2\2\2\u012c\u012a\3\2\2\2\u012d\u012e")
        buf.write("\7\31\2\2\u012e\u012f\7?\2\2\u012f\u0131\7 \2\2\u0130")
        buf.write("\u0132\5\66\34\2\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2")
        buf.write("\2\u0132\u0133\3\2\2\2\u0133\u0135\7!\2\2\u0134\u0136")
        buf.write("\5\62\32\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0139\3\2\2\2\u0137\u0139\5\64\33\2\u0138\u012d\3\2\2")
        buf.write("\2\u0138\u0137\3\2\2\2\u0139\63\3\2\2\2\u013a\u013b\7")
        buf.write(" \2\2\u013b\u013c\5\36\20\2\u013c\u013d\7!\2\2\u013d\u0145")
        buf.write("\3\2\2\2\u013e\u0145\7?\2\2\u013f\u0145\58\35\2\u0140")
        buf.write("\u0141\7\30\2\2\u0141\u0142\7$\2\2\u0142\u0145\7?\2\2")
        buf.write("\u0143\u0145\7\27\2\2\u0144\u013a\3\2\2\2\u0144\u013e")
        buf.write("\3\2\2\2\u0144\u013f\3\2\2\2\u0144\u0140\3\2\2\2\u0144")
        buf.write("\u0143\3\2\2\2\u0145\65\3\2\2\2\u0146\u014b\5\36\20\2")
        buf.write("\u0147\u0148\7#\2\2\u0148\u014a\5\36\20\2\u0149\u0147")
        buf.write("\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\67\3\2\2\2\u014d\u014b\3\2\2\2\u014e")
        buf.write("\u014f\t\b\2\2\u014f9\3\2\2\2\u0150\u015c\5\f\7\2\u0151")
        buf.write("\u0152\5@!\2\u0152\u0153\7\"\2\2\u0153\u015c\3\2\2\2\u0154")
        buf.write("\u015c\5B\"\2\u0155\u015c\5D#\2\u0156\u015c\5F$\2\u0157")
        buf.write("\u015c\5H%\2\u0158\u015c\5J&\2\u0159\u015c\5L\'\2\u015a")
        buf.write("\u015c\5<\37\2\u015b\u0150\3\2\2\2\u015b\u0151\3\2\2\2")
        buf.write("\u015b\u0154\3\2\2\2\u015b\u0155\3\2\2\2\u015b\u0156\3")
        buf.write("\2\2\2\u015b\u0157\3\2\2\2\u015b\u0158\3\2\2\2\u015b\u0159")
        buf.write("\3\2\2\2\u015b\u015a\3\2\2\2\u015c;\3\2\2\2\u015d\u015e")
        buf.write("\7\36\2\2\u015e\u015f\5> \2\u015f\u0160\7\37\2\2\u0160")
        buf.write("=\3\2\2\2\u0161\u0162\5\f\7\2\u0162\u0163\7\"\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0166\5:\36\2\u0165\u0161\3\2\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0166\u0169\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0167\u0168\3\2\2\2\u0168?\3\2\2\2\u0169\u0167")
        buf.write("\3\2\2\2\u016a\u016d\7?\2\2\u016b\u016d\5.\30\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016f\7\63\2\2\u016f\u0170\5\36\20\2\u0170A\3\2")
        buf.write("\2\2\u0171\u0173\7\20\2\2\u0172\u0174\5<\37\2\u0173\u0172")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0176\5\36\20\2\u0176\u0179\5<\37\2\u0177\u0178\7\21")
        buf.write("\2\2\u0178\u017a\5<\37\2\u0179\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017aC\3\2\2\2\u017b\u017c\7\22\2\2\u017c\u017d")
        buf.write("\5@!\2\u017d\u017e\7\"\2\2\u017e\u017f\5\36\20\2\u017f")
        buf.write("\u0180\7\"\2\2\u0180\u0181\5@!\2\u0181\u0182\5<\37\2\u0182")
        buf.write("E\3\2\2\2\u0183\u0184\7\16\2\2\u0184\u0185\7\"\2\2\u0185")
        buf.write("G\3\2\2\2\u0186\u0187\7\17\2\2\u0187\u0188\7\"\2\2\u0188")
        buf.write("I\3\2\2\2\u0189\u018b\7\6\2\2\u018a\u018c\5\36\20\2\u018b")
        buf.write("\u018a\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\3\2\2\2")
        buf.write("\u018d\u018e\7\"\2\2\u018eK\3\2\2\2\u018f\u0192\7?\2\2")
        buf.write("\u0190\u0192\5\36\20\2\u0191\u018f\3\2\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\7$\2\2\u0194")
        buf.write("\u0195\5N(\2\u0195\u0197\7 \2\2\u0196\u0198\5\66\34\2")
        buf.write("\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3")
        buf.write("\2\2\2\u0199\u019a\7!\2\2\u019a\u019b\7\"\2\2\u019b\u019e")
        buf.write("\3\2\2\2\u019c\u019e\5\60\31\2\u019d\u0191\3\2\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019eM\3\2\2\2\u019f\u01a0\t\t\2\2\u01a0")
        buf.write("O\3\2\2\2-SZ`r\u0082\u0089\u0095\u009e\u00ac\u00b5\u00bd")
        buf.write("\u00c4\u00ce\u00d9\u00e4\u00ef\u00f5\u00fa\u0105\u010b")
        buf.write("\u0110\u0113\u0116\u0119\u0123\u0126\u0128\u012a\u0131")
        buf.write("\u0135\u0138\u0144\u014b\u015b\u0165\u0167\u016c\u0173")
        buf.write("\u0179\u018b\u0191\u0197\u019d")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@'", "'['", "']'", "'='", "'{'", "'}'", "'('", "')'", 
                     "';'", "','", "'.'", "'+'", "'-'", "'/'", "'\\'", "'%'", 
                     "'!'", "'||'", "'&&'", "'=='", "'!='", "'<'", "'>'", 
                     "'<='", "'>='", "':='", "'^'", "'*'", "':'", "'<-'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "ARRAY", "MEMBERl", "CLASS", "RETURN", 
                      "INT", "FLOAT", "CONST", "VAR", "FUNC", "VOID", "CONSTRUCTOR", 
                      "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
                      "FALSE", "BOOL", "STRING", "NULL", "SELF", "NEW", 
                      "AC", "OB", "CB", "EQ", "LB", "RB", "LP", "RP", "SM", 
                      "CM", "DOT", "ADD", "SUB", "DIV", "BS", "MOD", "NOT", 
                      "OR", "AND", "EQUAL", "NOTEQUAL", "LESS", "GREATER", 
                      "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "CONCATENATION", 
                      "MUL", "COLON", "EXTENDS", "ARRAYLIT", "FLOATLIT", 
                      "INTLIT", "BOOLLIT", "STRING_LITERAL", "LineComment", 
                      "BlockComment", "ID", "WS", "NEWLINE", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_supperclass = 2
    RULE_construcdecl = 3
    RULE_classmember = 4
    RULE_attributedecl = 5
    RULE_initlist = 6
    RULE_methoddecl = 7
    RULE_paramdecl = 8
    RULE_paramlist = 9
    RULE_param = 10
    RULE_mctype = 11
    RULE_classname = 12
    RULE_attributelist = 13
    RULE_expression = 14
    RULE_expression1 = 15
    RULE_expression2 = 16
    RULE_expression3 = 17
    RULE_expression4 = 18
    RULE_expression5 = 19
    RULE_expression6 = 20
    RULE_expression7 = 21
    RULE_expression8 = 22
    RULE_expression9 = 23
    RULE_expression10 = 24
    RULE_expression11 = 25
    RULE_list_of_expression = 26
    RULE_literal = 27
    RULE_statement = 28
    RULE_block_stmt = 29
    RULE_member_block = 30
    RULE_assign_stmt = 31
    RULE_if_stmt = 32
    RULE_for_stmt = 33
    RULE_break_stmt = 34
    RULE_continue_stmt = 35
    RULE_return_stmt = 36
    RULE_method_stm = 37
    RULE_membername = 38

    ruleNames =  [ "program", "classdecl", "supperclass", "construcdecl", 
                   "classmember", "attributedecl", "initlist", "methoddecl", 
                   "paramdecl", "paramlist", "param", "mctype", "classname", 
                   "attributelist", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "expression8", "expression9", "expression10", 
                   "expression11", "list_of_expression", "literal", "statement", 
                   "block_stmt", "member_block", "assign_stmt", "if_stmt", 
                   "for_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "method_stm", "membername" ]

    EOF = Token.EOF
    ARRAY=1
    MEMBERl=2
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
    AC=24
    OB=25
    CB=26
    EQ=27
    LB=28
    RB=29
    LP=30
    RP=31
    SM=32
    CM=33
    DOT=34
    ADD=35
    SUB=36
    DIV=37
    BS=38
    MOD=39
    NOT=40
    OR=41
    AND=42
    EQUAL=43
    NOTEQUAL=44
    LESS=45
    GREATER=46
    LESSEQUAL=47
    GREATEREQUAL=48
    ASSIGN=49
    CONCATENATION=50
    MUL=51
    COLON=52
    EXTENDS=53
    ARRAYLIT=54
    FLOATLIT=55
    INTLIT=56
    BOOLLIT=57
    STRING_LITERAL=58
    LineComment=59
    BlockComment=60
    ID=61
    WS=62
    NEWLINE=63
    LINE_COMMENT=64
    BLOCK_COMMENT=65
    ERROR_CHAR=66
    UNCLOSE_STRING=67
    ILLEGAL_ESCAPE=68

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
            self.state = 79 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 78
                self.classdecl()
                self.state = 81 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 83
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
            self.state = 85
            self.match(CSlangParser.CLASS)
            self.state = 86
            self.classname()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EXTENDS:
                self.state = 87
                self.supperclass()


            self.state = 90
            self.match(CSlangParser.LB)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 91
                self.classmember()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
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
            self.state = 99
            self.match(CSlangParser.EXTENDS)
            self.state = 100
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
            self.state = 102
            self.match(CSlangParser.FUNC)
            self.state = 103
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 104
            self.paramdecl()
            self.state = 105
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


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

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
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.attributedecl()
                self.state = 108
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111
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
            self._attributelist = None # AttributelistContext
            self._initlist = None # InitlistContext

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

        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

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
        self.enterRule(localctx, 10, self.RULE_attributedecl)
        self._la = 0 # Token type
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 115
                localctx._attributelist = self.attributelist()
                self.state = 116
                self.match(CSlangParser.COLON)
                self.state = 117
                self.mctype()

                self.state = 118
                self.match(CSlangParser.EQ)
                self.state = 119
                localctx._initlist = self.initlist()
                self.state = 121
                if not len((None if localctx._attributelist is None else self._input.getText(localctx._attributelist.start,localctx._attributelist.stop)).split(',')) == len((None if localctx._initlist is None else self._input.getText(localctx._initlist.start,localctx._initlist.stop)).split(',')):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "len($attributelist.text.split(',')) == len($initlist.text.split(','))")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 124
                self.attributelist()
                self.state = 125
                self.match(CSlangParser.COLON)
                self.state = 126
                self.mctype()
                pass


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
            return CSlangParser.RULE_initlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitlist" ):
                return visitor.visitInitlist(self)
            else:
                return visitor.visitChildren(self)




    def initlist(self):

        localctx = CSlangParser.InitlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_initlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.expression()
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 131
                    self.match(CSlangParser.CM)
                    self.state = 132
                    self.expression() 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_methoddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(CSlangParser.FUNC)
            self.state = 139
            self.membername()
            self.state = 140
            self.paramdecl()
            self.state = 141
            self.match(CSlangParser.COLON)
            self.state = 142
            self.mctype()
            self.state = 143
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
        self.enterRule(localctx, 16, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(CSlangParser.LP)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.MEMBERl or _la==CSlangParser.ID:
                self.state = 146
                self.paramlist()


            self.state = 149
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
        self.enterRule(localctx, 18, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.param()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 152
                self.match(CSlangParser.CM)
                self.state = 153
                self.param()
                self.state = 158
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
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.attributelist()
            self.state = 160
            self.match(CSlangParser.COLON)
            self.state = 161
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

        def classname(self):
            return self.getTypedRuleContext(CSlangParser.ClassnameContext,0)


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
        self.enterRule(localctx, 22, self.RULE_mctype)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 167
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 168
                self.classname()
                pass
            elif token in [CSlangParser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 169
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
        self.enterRule(localctx, 24, self.RULE_classname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
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
        self.enterRule(localctx, 26, self.RULE_attributelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.membername()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 175
                self.match(CSlangParser.CM)
                self.state = 176
                self.membername()
                self.state = 181
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


        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def GREATER(self):
            return self.getToken(CSlangParser.GREATER, 0)

        def LESSEQUAL(self):
            return self.getToken(CSlangParser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(CSlangParser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CSlangParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.expression1()
                self.state = 183
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.LESS) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.LESSEQUAL) | (1 << CSlangParser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 184
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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

        def getRuleIndex(self):
            return CSlangParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = CSlangParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.expression2(0)
                self.state = 190
                _la = self._input.LA(1)
                if not(_la==CSlangParser.EQUAL or _la==CSlangParser.NOTEQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 204
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 199
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 200
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.OR or _la==CSlangParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 201
                    self.expression3(0) 
                self.state = 206
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 215
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 210
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 211
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 212
                    self.expression4(0) 
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 221
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 222
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.DIV) | (1 << CSlangParser.BS) | (1 << CSlangParser.MOD) | (1 << CSlangParser.MUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 223
                    self.expression5(0) 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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

        def expression6(self):
            return self.getTypedRuleContext(CSlangParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(CSlangParser.Expression5Context,0)


        def CONCATENATION(self):
            return self.getToken(CSlangParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expression5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 232
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 233
                    self.match(CSlangParser.CONCATENATION)
                    self.state = 234
                    self.expression6() 
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

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
        self.enterRule(localctx, 40, self.RULE_expression6)
        try:
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(CSlangParser.NOT)
                self.state = 241
                self.expression6()
                pass
            elif token in [CSlangParser.MEMBERl, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.ADD, CSlangParser.SUB, CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.expression7()
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

        def expression7(self):
            return self.getTypedRuleContext(CSlangParser.Expression7Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def expression8(self):
            return self.getTypedRuleContext(CSlangParser.Expression8Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = CSlangParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ADD, CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 246
                self.expression7()
                pass
            elif token in [CSlangParser.MEMBERl, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.LP, CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.expression8()
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


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(CSlangParser.Expression9Context,0)


        def OB(self):
            return self.getToken(CSlangParser.OB, 0)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def CB(self):
            return self.getToken(CSlangParser.CB, 0)

        def ARRAYLIT(self):
            return self.getToken(CSlangParser.ARRAYLIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = CSlangParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expression8)
        try:
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.expression9(0)
                self.state = 251
                self.match(CSlangParser.OB)
                self.state = 252
                self.expression()
                self.state = 253
                self.match(CSlangParser.CB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.expression9(0)
                self.state = 256
                self.match(CSlangParser.ARRAYLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.expression9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def membername(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.MembernameContext)
            else:
                return self.getTypedRuleContext(CSlangParser.MembernameContext,i)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def expression10(self):
            return self.getTypedRuleContext(CSlangParser.Expression10Context,0)


        def expression9(self):
            return self.getTypedRuleContext(CSlangParser.Expression9Context,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)



    def expression9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expression9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 265
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 262
                    self.membername()
                    self.state = 263
                    self.match(CSlangParser.DOT)


                self.state = 267
                self.membername()
                self.state = 273
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 268
                    self.match(CSlangParser.LP)
                    self.state = 270
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MEMBERl) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                        self.state = 269
                        self.list_of_expression()


                    self.state = 272
                    self.match(CSlangParser.RP)


                self.state = 276
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 275
                    self.match(CSlangParser.SM)


                pass

            elif la_ == 2:
                self.state = 278
                self.expression10()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 294
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 281
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 282
                        self.match(CSlangParser.DOT)
                        self.state = 283
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 284
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 285
                        self.match(CSlangParser.DOT)
                        self.state = 286
                        self.membername()
                        self.state = 292
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                        if la_ == 1:
                            self.state = 287
                            self.match(CSlangParser.LP)
                            self.state = 289
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MEMBERl) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                                self.state = 288
                                self.list_of_expression()


                            self.state = 291
                            self.match(CSlangParser.RP)


                        pass

             
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def expression11(self):
            return self.getTypedRuleContext(CSlangParser.Expression11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expression10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)




    def expression10(self):

        localctx = CSlangParser.Expression10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expression10)
        self._la = 0 # Token type
        try:
            self.state = 310
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(CSlangParser.NEW)
                self.state = 300
                self.match(CSlangParser.ID)
                self.state = 301
                self.match(CSlangParser.LP)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MEMBERl) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 302
                    self.list_of_expression()


                self.state = 305
                self.match(CSlangParser.RP)
                self.state = 307
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                if la_ == 1:
                    self.state = 306
                    self.expression10()


                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LP, CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.expression11()
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


    class Expression11Context(ParserRuleContext):
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
            return CSlangParser.RULE_expression11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression11" ):
                return visitor.visitExpression11(self)
            else:
                return visitor.visitChildren(self)




    def expression11(self):

        localctx = CSlangParser.Expression11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expression11)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(CSlangParser.LP)
                self.state = 313
                self.expression()
                self.state = 314
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 316
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 317
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 318
                self.match(CSlangParser.SELF)
                self.state = 319
                self.match(CSlangParser.DOT)
                self.state = 320
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 321
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
        self.enterRule(localctx, 52, self.RULE_list_of_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.expression()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 325
                self.match(CSlangParser.CM)
                self.state = 326
                self.expression()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ARRAYLIT(self):
            return self.getToken(CSlangParser.ARRAYLIT, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def STRING_LITERAL(self):
            return self.getToken(CSlangParser.STRING_LITERAL, 0)

        def BOOLLIT(self):
            return self.getToken(CSlangParser.BOOLLIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL))) != 0)):
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
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.assign_stmt()
                self.state = 336
                self.match(CSlangParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 338
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 339
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 340
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 341
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 342
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 343
                self.method_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 344
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
        self.enterRule(localctx, 58, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(CSlangParser.LB)
            self.state = 348
            self.member_block()
            self.state = 349
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

        def attributedecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.AttributedeclContext)
            else:
                return self.getTypedRuleContext(CSlangParser.AttributedeclContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.SM)
            else:
                return self.getToken(CSlangParser.SM, i)

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
        self.enterRule(localctx, 60, self.RULE_member_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MEMBERl) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LB) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 355
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 351
                    self.attributedecl()
                    self.state = 352
                    self.match(CSlangParser.SM)
                    pass

                elif la_ == 2:
                    self.state = 354
                    self.statement()
                    pass


                self.state = 359
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

        def expression8(self):
            return self.getTypedRuleContext(CSlangParser.Expression8Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 360
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.state = 361
                self.expression8()
                pass


            self.state = 364
            self.match(CSlangParser.ASSIGN)
            self.state = 365
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
        self.enterRule(localctx, 64, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(CSlangParser.IF)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LB:
                self.state = 368
                self.block_stmt()


            self.state = 371
            self.expression()
            self.state = 372
            self.block_stmt()
            self.state = 375
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 373
                self.match(CSlangParser.ELSE)
                self.state = 374
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
        self.enterRule(localctx, 66, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(CSlangParser.FOR)
            self.state = 378
            self.assign_stmt()
            self.state = 379
            self.match(CSlangParser.SM)
            self.state = 380
            self.expression()
            self.state = 381
            self.match(CSlangParser.SM)
            self.state = 382
            self.assign_stmt()
            self.state = 383
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
        self.enterRule(localctx, 68, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(CSlangParser.BREAK)
            self.state = 386
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
        self.enterRule(localctx, 70, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(CSlangParser.CONTINUE)
            self.state = 389
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
        self.enterRule(localctx, 72, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(CSlangParser.RETURN)
            self.state = 393
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MEMBERl) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 392
                self.expression()


            self.state = 395
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

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def membername(self):
            return self.getTypedRuleContext(CSlangParser.MembernameContext,0)


        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def expression9(self):
            return self.getTypedRuleContext(CSlangParser.Expression9Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_stm" ):
                return visitor.visitMethod_stm(self)
            else:
                return visitor.visitChildren(self)




    def method_stm(self):

        localctx = CSlangParser.Method_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_method_stm)
        self._la = 0 # Token type
        try:
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 397
                    self.match(CSlangParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 398
                    self.expression()
                    pass


                self.state = 401
                self.match(CSlangParser.DOT)
                self.state = 402
                self.membername()
                self.state = 403
                self.match(CSlangParser.LP)
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.MEMBERl) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 404
                    self.list_of_expression()


                self.state = 407
                self.match(CSlangParser.RP)
                self.state = 408
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.expression9(0)
                pass


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

        def MEMBERl(self):
            return self.getToken(CSlangParser.MEMBERl, 0)

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
        self.enterRule(localctx, 76, self.RULE_membername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            _la = self._input.LA(1)
            if not(_la==CSlangParser.MEMBERl or _la==CSlangParser.ID):
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
        self._predicates[5] = self.attributedecl_sempred
        self._predicates[16] = self.expression2_sempred
        self._predicates[17] = self.expression3_sempred
        self._predicates[18] = self.expression4_sempred
        self._predicates[19] = self.expression5_sempred
        self._predicates[23] = self.expression9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attributedecl_sempred(self, localctx:AttributedeclContext, predIndex:int):
            if predIndex == 0:
                return len((None if localctx._attributelist is None else self._input.getText(localctx._attributelist.start,localctx._attributelist.stop)).split(',')) == len((None if localctx._initlist is None else self._input.getText(localctx._initlist.start,localctx._initlist.stop)).split(','))
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression9_sempred(self, localctx:Expression9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




