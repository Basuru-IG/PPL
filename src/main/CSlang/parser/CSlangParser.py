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
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7u\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\b\u0085\n\b\3\t\3\t\3\t\7\t\u008a")
        buf.write("\n\t\f\t\16\t\u008d\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\5\13\u0098\n\13\3\13\3\13\3\f\3\f\3\f\7\f\u009f")
        buf.write("\n\f\f\f\16\f\u00a2\13\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00af\n\16\3\17\3\17\3\17\7")
        buf.write("\17\u00b4\n\17\f\17\16\17\u00b7\13\17\3\20\5\20\u00ba")
        buf.write("\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u00c3\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\5\22\u00ca\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\7\23\u00d2\n\23\f\23\16\23\u00d5")
        buf.write("\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u00dd\n\24\f")
        buf.write("\24\16\24\u00e0\13\24\3\25\3\25\3\25\3\25\3\25\3\25\7")
        buf.write("\25\u00e8\n\25\f\25\16\25\u00eb\13\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\7\26\u00f3\n\26\f\26\16\26\u00f6\13\26\3")
        buf.write("\27\3\27\3\27\5\27\u00fb\n\27\3\30\3\30\3\30\5\30\u0100")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0108\n\31\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u010e\n\32\3\32\3\32\3\32\5\32")
        buf.write("\u0113\n\32\3\32\5\32\u0116\n\32\3\32\5\32\u0119\n\32")
        buf.write("\3\32\5\32\u011c\n\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\5\32\u0126\n\32\3\32\5\32\u0129\n\32\7\32\u012b")
        buf.write("\n\32\f\32\16\32\u012e\13\32\3\33\3\33\3\33\3\33\5\33")
        buf.write("\u0134\n\33\3\33\3\33\5\33\u0138\n\33\3\33\5\33\u013b")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\5\34\u0147\n\34\3\35\3\35\3\35\7\35\u014c\n\35\f\35\16")
        buf.write("\35\u014f\13\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\5\37\u015e\n\37\3 \3 \3 \3 ")
        buf.write("\3!\3!\3!\3!\7!\u0168\n!\f!\16!\u016b\13!\3\"\3\"\5\"")
        buf.write("\u016f\n\"\3\"\3\"\3\"\3#\3#\5#\u0176\n#\3#\3#\3#\3#\5")
        buf.write("#\u017c\n#\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\5\'\u018e\n\'\3\'\3\'\3(\3(\5(\u0194\n(\3(\3(\3")
        buf.write("(\3(\5(\u019a\n(\3(\3(\3(\3(\5(\u01a0\n(\3(\2\7$&(*\62")
        buf.write(")\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLN\2\t\3\2\b\t\3\2.\61\3\2,-\3\2*+\3\2")
        buf.write("$%\4\2&(\64\64\4\2\67\679<\2\u01b6\2Q\3\2\2\2\4W\3\2\2")
        buf.write("\2\6e\3\2\2\2\bh\3\2\2\2\nj\3\2\2\2\ft\3\2\2\2\16\u0084")
        buf.write("\3\2\2\2\20\u0086\3\2\2\2\22\u008e\3\2\2\2\24\u0095\3")
        buf.write("\2\2\2\26\u009b\3\2\2\2\30\u00a3\3\2\2\2\32\u00ae\3\2")
        buf.write("\2\2\34\u00b0\3\2\2\2\36\u00b9\3\2\2\2 \u00c2\3\2\2\2")
        buf.write("\"\u00c9\3\2\2\2$\u00cb\3\2\2\2&\u00d6\3\2\2\2(\u00e1")
        buf.write("\3\2\2\2*\u00ec\3\2\2\2,\u00fa\3\2\2\2.\u00ff\3\2\2\2")
        buf.write("\60\u0107\3\2\2\2\62\u011b\3\2\2\2\64\u013a\3\2\2\2\66")
        buf.write("\u0146\3\2\2\28\u0148\3\2\2\2:\u0150\3\2\2\2<\u015d\3")
        buf.write("\2\2\2>\u015f\3\2\2\2@\u0169\3\2\2\2B\u016e\3\2\2\2D\u0173")
        buf.write("\3\2\2\2F\u017d\3\2\2\2H\u0185\3\2\2\2J\u0188\3\2\2\2")
        buf.write("L\u018b\3\2\2\2N\u019f\3\2\2\2PR\5\4\3\2QP\3\2\2\2RS\3")
        buf.write("\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\7\2\2\3V\3\3\2")
        buf.write("\2\2WX\7\4\2\2XZ\5\b\5\2Y[\5\6\4\2ZY\3\2\2\2Z[\3\2\2\2")
        buf.write("[\\\3\2\2\2\\`\7\35\2\2]_\5\f\7\2^]\3\2\2\2_b\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2ac\3\2\2\2b`\3\2\2\2cd\7\36\2\2d\5")
        buf.write("\3\2\2\2ef\7\66\2\2fg\5\b\5\2g\7\3\2\2\2hi\7?\2\2i\t\3")
        buf.write("\2\2\2jk\7\n\2\2kl\7\f\2\2lm\5\24\13\2mn\5> \2n\13\3\2")
        buf.write("\2\2op\5\16\b\2pq\7!\2\2qu\3\2\2\2ru\5\22\n\2su\5\n\6")
        buf.write("\2to\3\2\2\2tr\3\2\2\2ts\3\2\2\2u\r\3\2\2\2vw\t\2\2\2")
        buf.write("wx\5\34\17\2xy\7\65\2\2yz\5\32\16\2z{\7\34\2\2{|\5\20")
        buf.write("\t\2|}\3\2\2\2}~\6\b\2\3~\u0085\3\2\2\2\177\u0080\t\2")
        buf.write("\2\2\u0080\u0081\5\34\17\2\u0081\u0082\7\65\2\2\u0082")
        buf.write("\u0083\5\32\16\2\u0083\u0085\3\2\2\2\u0084v\3\2\2\2\u0084")
        buf.write("\177\3\2\2\2\u0085\17\3\2\2\2\u0086\u008b\5 \21\2\u0087")
        buf.write("\u0088\7\"\2\2\u0088\u008a\5 \21\2\u0089\u0087\3\2\2\2")
        buf.write("\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3")
        buf.write("\2\2\2\u008c\21\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u008f")
        buf.write("\7\n\2\2\u008f\u0090\5\36\20\2\u0090\u0091\5\24\13\2\u0091")
        buf.write("\u0092\7\65\2\2\u0092\u0093\5\32\16\2\u0093\u0094\5> ")
        buf.write("\2\u0094\23\3\2\2\2\u0095\u0097\7\37\2\2\u0096\u0098\5")
        buf.write("\26\f\2\u0097\u0096\3\2\2\2\u0097\u0098\3\2\2\2\u0098")
        buf.write("\u0099\3\2\2\2\u0099\u009a\7 \2\2\u009a\25\3\2\2\2\u009b")
        buf.write("\u00a0\5\30\r\2\u009c\u009d\7\"\2\2\u009d\u009f\5\30\r")
        buf.write("\2\u009e\u009c\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e")
        buf.write("\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\27\3\2\2\2\u00a2\u00a0")
        buf.write("\3\2\2\2\u00a3\u00a4\5\34\17\2\u00a4\u00a5\7\65\2\2\u00a5")
        buf.write("\u00a6\5\32\16\2\u00a6\31\3\2\2\2\u00a7\u00af\7\6\2\2")
        buf.write("\u00a8\u00af\7\7\2\2\u00a9\u00af\7\24\2\2\u00aa\u00af")
        buf.write("\7\25\2\2\u00ab\u00af\7\13\2\2\u00ac\u00af\5\b\5\2\u00ad")
        buf.write("\u00af\7\3\2\2\u00ae\u00a7\3\2\2\2\u00ae\u00a8\3\2\2\2")
        buf.write("\u00ae\u00a9\3\2\2\2\u00ae\u00aa\3\2\2\2\u00ae\u00ab\3")
        buf.write("\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\33")
        buf.write("\3\2\2\2\u00b0\u00b5\5\36\20\2\u00b1\u00b2\7\"\2\2\u00b2")
        buf.write("\u00b4\5\36\20\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\3\2\2")
        buf.write("\2\u00b5\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\35\3")
        buf.write("\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00ba\7\31\2\2\u00b9")
        buf.write("\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2")
        buf.write("\u00bb\u00bc\7?\2\2\u00bc\37\3\2\2\2\u00bd\u00be\5\"\22")
        buf.write("\2\u00be\u00bf\t\3\2\2\u00bf\u00c0\5\"\22\2\u00c0\u00c3")
        buf.write("\3\2\2\2\u00c1\u00c3\5\"\22\2\u00c2\u00bd\3\2\2\2\u00c2")
        buf.write("\u00c1\3\2\2\2\u00c3!\3\2\2\2\u00c4\u00c5\5$\23\2\u00c5")
        buf.write("\u00c6\t\4\2\2\u00c6\u00c7\5$\23\2\u00c7\u00ca\3\2\2\2")
        buf.write("\u00c8\u00ca\5$\23\2\u00c9\u00c4\3\2\2\2\u00c9\u00c8\3")
        buf.write("\2\2\2\u00ca#\3\2\2\2\u00cb\u00cc\b\23\1\2\u00cc\u00cd")
        buf.write("\5&\24\2\u00cd\u00d3\3\2\2\2\u00ce\u00cf\f\4\2\2\u00cf")
        buf.write("\u00d0\t\5\2\2\u00d0\u00d2\5&\24\2\u00d1\u00ce\3\2\2\2")
        buf.write("\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3")
        buf.write("\2\2\2\u00d4%\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7")
        buf.write("\b\24\1\2\u00d7\u00d8\5(\25\2\u00d8\u00de\3\2\2\2\u00d9")
        buf.write("\u00da\f\4\2\2\u00da\u00db\t\6\2\2\u00db\u00dd\5(\25\2")
        buf.write("\u00dc\u00d9\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3")
        buf.write("\2\2\2\u00de\u00df\3\2\2\2\u00df\'\3\2\2\2\u00e0\u00de")
        buf.write("\3\2\2\2\u00e1\u00e2\b\25\1\2\u00e2\u00e3\5*\26\2\u00e3")
        buf.write("\u00e9\3\2\2\2\u00e4\u00e5\f\4\2\2\u00e5\u00e6\t\7\2\2")
        buf.write("\u00e6\u00e8\5*\26\2\u00e7\u00e4\3\2\2\2\u00e8\u00eb\3")
        buf.write("\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea)")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec\u00ed\b\26\1\2\u00ed")
        buf.write("\u00ee\5,\27\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0\f\4\2\2")
        buf.write("\u00f0\u00f1\7\63\2\2\u00f1\u00f3\5,\27\2\u00f2\u00ef")
        buf.write("\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5+\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7")
        buf.write("\u00f8\7)\2\2\u00f8\u00fb\5,\27\2\u00f9\u00fb\5.\30\2")
        buf.write("\u00fa\u00f7\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb-\3\2\2")
        buf.write("\2\u00fc\u00fd\t\6\2\2\u00fd\u0100\5.\30\2\u00fe\u0100")
        buf.write("\5\60\31\2\u00ff\u00fc\3\2\2\2\u00ff\u00fe\3\2\2\2\u0100")
        buf.write("/\3\2\2\2\u0101\u0102\5\62\32\2\u0102\u0103\7\32\2\2\u0103")
        buf.write("\u0104\5 \21\2\u0104\u0105\7\33\2\2\u0105\u0108\3\2\2")
        buf.write("\2\u0106\u0108\5\62\32\2\u0107\u0101\3\2\2\2\u0107\u0106")
        buf.write("\3\2\2\2\u0108\61\3\2\2\2\u0109\u010d\b\32\1\2\u010a\u010b")
        buf.write("\5\36\20\2\u010b\u010c\7#\2\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u010a\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\3\2\2\2")
        buf.write("\u010f\u0115\5\36\20\2\u0110\u0112\7\37\2\2\u0111\u0113")
        buf.write("\58\35\2\u0112\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114\u0116\7 \2\2\u0115\u0110\3\2\2\2")
        buf.write("\u0115\u0116\3\2\2\2\u0116\u0118\3\2\2\2\u0117\u0119\7")
        buf.write("!\2\2\u0118\u0117\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011c")
        buf.write("\3\2\2\2\u011a\u011c\5\64\33\2\u011b\u0109\3\2\2\2\u011b")
        buf.write("\u011a\3\2\2\2\u011c\u012c\3\2\2\2\u011d\u011e\f\6\2\2")
        buf.write("\u011e\u011f\7#\2\2\u011f\u012b\7?\2\2\u0120\u0121\f\5")
        buf.write("\2\2\u0121\u0122\7#\2\2\u0122\u0128\5\36\20\2\u0123\u0125")
        buf.write("\7\37\2\2\u0124\u0126\58\35\2\u0125\u0124\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0129\7 \2\2")
        buf.write("\u0128\u0123\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012b\3")
        buf.write("\2\2\2\u012a\u011d\3\2\2\2\u012a\u0120\3\2\2\2\u012b\u012e")
        buf.write("\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("\63\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130\7\30\2\2\u0130")
        buf.write("\u0131\7?\2\2\u0131\u0133\7\37\2\2\u0132\u0134\58\35\2")
        buf.write("\u0133\u0132\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0137\7 \2\2\u0136\u0138\5\64\33\2\u0137")
        buf.write("\u0136\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013b\3\2\2\2")
        buf.write("\u0139\u013b\5\66\34\2\u013a\u012f\3\2\2\2\u013a\u0139")
        buf.write("\3\2\2\2\u013b\65\3\2\2\2\u013c\u013d\7\37\2\2\u013d\u013e")
        buf.write("\5 \21\2\u013e\u013f\7 \2\2\u013f\u0147\3\2\2\2\u0140")
        buf.write("\u0147\7?\2\2\u0141\u0147\5:\36\2\u0142\u0143\7\27\2\2")
        buf.write("\u0143\u0144\7#\2\2\u0144\u0147\7?\2\2\u0145\u0147\7\26")
        buf.write("\2\2\u0146\u013c\3\2\2\2\u0146\u0140\3\2\2\2\u0146\u0141")
        buf.write("\3\2\2\2\u0146\u0142\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("\67\3\2\2\2\u0148\u014d\5 \21\2\u0149\u014a\7\"\2\2\u014a")
        buf.write("\u014c\5 \21\2\u014b\u0149\3\2\2\2\u014c\u014f\3\2\2\2")
        buf.write("\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e9\3\2\2")
        buf.write("\2\u014f\u014d\3\2\2\2\u0150\u0151\t\b\2\2\u0151;\3\2")
        buf.write("\2\2\u0152\u015e\5\16\b\2\u0153\u0154\5B\"\2\u0154\u0155")
        buf.write("\7!\2\2\u0155\u015e\3\2\2\2\u0156\u015e\5D#\2\u0157\u015e")
        buf.write("\5F$\2\u0158\u015e\5H%\2\u0159\u015e\5J&\2\u015a\u015e")
        buf.write("\5L\'\2\u015b\u015e\5N(\2\u015c\u015e\5> \2\u015d\u0152")
        buf.write("\3\2\2\2\u015d\u0153\3\2\2\2\u015d\u0156\3\2\2\2\u015d")
        buf.write("\u0157\3\2\2\2\u015d\u0158\3\2\2\2\u015d\u0159\3\2\2\2")
        buf.write("\u015d\u015a\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015c\3")
        buf.write("\2\2\2\u015e=\3\2\2\2\u015f\u0160\7\35\2\2\u0160\u0161")
        buf.write("\5@!\2\u0161\u0162\7\36\2\2\u0162?\3\2\2\2\u0163\u0164")
        buf.write("\5\16\b\2\u0164\u0165\7!\2\2\u0165\u0168\3\2\2\2\u0166")
        buf.write("\u0168\5<\37\2\u0167\u0163\3\2\2\2\u0167\u0166\3\2\2\2")
        buf.write("\u0168\u016b\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3")
        buf.write("\2\2\2\u016aA\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016f")
        buf.write("\7?\2\2\u016d\u016f\5\60\31\2\u016e\u016c\3\2\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171\7\62\2")
        buf.write("\2\u0171\u0172\5 \21\2\u0172C\3\2\2\2\u0173\u0175\7\17")
        buf.write("\2\2\u0174\u0176\5> \2\u0175\u0174\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\5 \21\2\u0178")
        buf.write("\u017b\5> \2\u0179\u017a\7\20\2\2\u017a\u017c\5> \2\u017b")
        buf.write("\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017cE\3\2\2\2\u017d")
        buf.write("\u017e\7\21\2\2\u017e\u017f\5B\"\2\u017f\u0180\7!\2\2")
        buf.write("\u0180\u0181\5 \21\2\u0181\u0182\7!\2\2\u0182\u0183\5")
        buf.write("B\"\2\u0183\u0184\5> \2\u0184G\3\2\2\2\u0185\u0186\7\r")
        buf.write("\2\2\u0186\u0187\7!\2\2\u0187I\3\2\2\2\u0188\u0189\7\16")
        buf.write("\2\2\u0189\u018a\7!\2\2\u018aK\3\2\2\2\u018b\u018d\7\5")
        buf.write("\2\2\u018c\u018e\5 \21\2\u018d\u018c\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0190\7!\2\2\u0190")
        buf.write("M\3\2\2\2\u0191\u0194\7?\2\2\u0192\u0194\5 \21\2\u0193")
        buf.write("\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194\u0195\3\2\2\2")
        buf.write("\u0195\u0196\7#\2\2\u0196\u0197\5\36\20\2\u0197\u0199")
        buf.write("\7\37\2\2\u0198\u019a\58\35\2\u0199\u0198\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019c\7 \2\2")
        buf.write("\u019c\u019d\7!\2\2\u019d\u01a0\3\2\2\2\u019e\u01a0\5")
        buf.write("\62\32\2\u019f\u0193\3\2\2\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("O\3\2\2\2.SZ`t\u0084\u008b\u0097\u00a0\u00ae\u00b5\u00b9")
        buf.write("\u00c2\u00c9\u00d3\u00de\u00e9\u00f4\u00fa\u00ff\u0107")
        buf.write("\u010d\u0112\u0115\u0118\u011b\u0125\u0128\u012a\u012c")
        buf.write("\u0133\u0137\u013a\u0146\u014d\u015d\u0167\u0169\u016e")
        buf.write("\u0175\u017b\u018d\u0193\u0199\u019f")
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
                     "<INVALID>", "<INVALID>", "<INVALID>", "'@'", "'['", 
                     "']'", "'='", "'{'", "'}'", "'('", "')'", "';'", "','", 
                     "'.'", "'+'", "'-'", "'/'", "'\\'", "'%'", "'!'", "'||'", 
                     "'&&'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "':='", "'^'", "'*'", "':'", "'<-'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "ARRAY", "CLASS", "RETURN", "INT", "FLOAT", 
                      "CONST", "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", 
                      "BOOL", "STRING", "NULL", "SELF", "NEW", "AC", "OB", 
                      "CB", "EQ", "LB", "RB", "LP", "RP", "SM", "CM", "DOT", 
                      "ADD", "SUB", "DIV", "BS", "MOD", "NOT", "OR", "AND", 
                      "EQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", 
                      "GREATEREQUAL", "ASSIGN", "CONCATENATION", "MUL", 
                      "COLON", "EXTENDS", "ARRAYLIT", "ARRAY_ELEMENT", "FLOATLIT", 
                      "INTLIT", "BOOLLIT", "STRING_LITERAL", "LineComment", 
                      "BlockComment", "ID", "WS", "NEWLINE", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_supperclass = 2
    RULE_classname = 3
    RULE_construcdecl = 4
    RULE_classmember = 5
    RULE_attributedecl = 6
    RULE_initlist = 7
    RULE_methoddecl = 8
    RULE_paramdecl = 9
    RULE_paramlist = 10
    RULE_param = 11
    RULE_mctype = 12
    RULE_attributelist = 13
    RULE_membername = 14
    RULE_expr = 15
    RULE_expr1 = 16
    RULE_expr2 = 17
    RULE_expr3 = 18
    RULE_expr4 = 19
    RULE_expr5 = 20
    RULE_expr6 = 21
    RULE_expr7 = 22
    RULE_expr8 = 23
    RULE_expr9 = 24
    RULE_expr10 = 25
    RULE_expr11 = 26
    RULE_list_of_expr = 27
    RULE_literal = 28
    RULE_statement = 29
    RULE_block_stmt = 30
    RULE_member_block = 31
    RULE_assign_stmt = 32
    RULE_if_stmt = 33
    RULE_for_stmt = 34
    RULE_break_stmt = 35
    RULE_continue_stmt = 36
    RULE_return_stmt = 37
    RULE_method_stm = 38

    ruleNames =  [ "program", "classdecl", "supperclass", "classname", "construcdecl", 
                   "classmember", "attributedecl", "initlist", "methoddecl", 
                   "paramdecl", "paramlist", "param", "mctype", "attributelist", 
                   "membername", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "list_of_expr", "literal", "statement", "block_stmt", 
                   "member_block", "assign_stmt", "if_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_stm" ]

    EOF = Token.EOF
    ARRAY=1
    CLASS=2
    RETURN=3
    INT=4
    FLOAT=5
    CONST=6
    VAR=7
    FUNC=8
    VOID=9
    CONSTRUCTOR=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELSE=14
    FOR=15
    TRUE=16
    FALSE=17
    BOOL=18
    STRING=19
    NULL=20
    SELF=21
    NEW=22
    AC=23
    OB=24
    CB=25
    EQ=26
    LB=27
    RB=28
    LP=29
    RP=30
    SM=31
    CM=32
    DOT=33
    ADD=34
    SUB=35
    DIV=36
    BS=37
    MOD=38
    NOT=39
    OR=40
    AND=41
    EQUAL=42
    NOTEQUAL=43
    LESS=44
    GREATER=45
    LESSEQUAL=46
    GREATEREQUAL=47
    ASSIGN=48
    CONCATENATION=49
    MUL=50
    COLON=51
    EXTENDS=52
    ARRAYLIT=53
    ARRAY_ELEMENT=54
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
            self.state = 102
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
        self.enterRule(localctx, 8, self.RULE_construcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(CSlangParser.FUNC)
            self.state = 105
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 106
            self.paramdecl()
            self.state = 107
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
        self.enterRule(localctx, 10, self.RULE_classmember)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.attributedecl()
                self.state = 110
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
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
        self.enterRule(localctx, 12, self.RULE_attributedecl)
        self._la = 0 # Token type
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                localctx._attributelist = self.attributelist()
                self.state = 118
                self.match(CSlangParser.COLON)
                self.state = 119
                self.mctype()

                self.state = 120
                self.match(CSlangParser.EQ)
                self.state = 121
                localctx._initlist = self.initlist()
                self.state = 123
                if not len((None if localctx._attributelist is None else self._input.getText(localctx._attributelist.start,localctx._attributelist.stop)).split(',')) == len((None if localctx._initlist is None else self._input.getText(localctx._initlist.start,localctx._initlist.stop)).split(',')):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "len($attributelist.text.split(',')) == len($initlist.text.split(','))")
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 126
                self.attributelist()
                self.state = 127
                self.match(CSlangParser.COLON)
                self.state = 128
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
        self.enterRule(localctx, 14, self.RULE_initlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.expr()
            self.state = 137
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 133
                    self.match(CSlangParser.CM)
                    self.state = 134
                    self.expr() 
                self.state = 139
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
        self.enterRule(localctx, 16, self.RULE_methoddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CSlangParser.FUNC)
            self.state = 141
            self.membername()
            self.state = 142
            self.paramdecl()
            self.state = 143
            self.match(CSlangParser.COLON)
            self.state = 144
            self.mctype()
            self.state = 145
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
        self.enterRule(localctx, 18, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(CSlangParser.LP)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.AC or _la==CSlangParser.ID:
                self.state = 148
                self.paramlist()


            self.state = 151
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
        self.enterRule(localctx, 20, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.param()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 154
                self.match(CSlangParser.CM)
                self.state = 155
                self.param()
                self.state = 160
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
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.attributelist()
            self.state = 162
            self.match(CSlangParser.COLON)
            self.state = 163
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
        self.enterRule(localctx, 24, self.RULE_mctype)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 167
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 170
                self.classname()
                pass
            elif token in [CSlangParser.ARRAY]:
                self.enterOuterAlt(localctx, 7)
                self.state = 171
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


    class MembernameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def AC(self):
            return self.getToken(CSlangParser.AC, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_membername

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMembername" ):
                return visitor.visitMembername(self)
            else:
                return visitor.visitChildren(self)




    def membername(self):

        localctx = CSlangParser.MembernameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_membername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.AC:
                self.state = 182
                self.match(CSlangParser.AC)


            self.state = 185
            self.match(CSlangParser.ID)
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

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr1Context,i)


        def LESS(self):
            return self.getToken(CSlangParser.LESS, 0)

        def GREATER(self):
            return self.getToken(CSlangParser.GREATER, 0)

        def LESSEQUAL(self):
            return self.getToken(CSlangParser.LESSEQUAL, 0)

        def GREATEREQUAL(self):
            return self.getToken(CSlangParser.GREATEREQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = CSlangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.expr1()
                self.state = 188
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.LESS) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.LESSEQUAL) | (1 << CSlangParser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CSlangParser.Expr2Context,i)


        def EQUAL(self):
            return self.getToken(CSlangParser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(CSlangParser.NOTEQUAL, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = CSlangParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.expr2(0)
                self.state = 195
                _la = self._input.LA(1)
                if not(_la==CSlangParser.EQUAL or _la==CSlangParser.NOTEQUAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(CSlangParser.Expr2Context,0)


        def AND(self):
            return self.getToken(CSlangParser.AND, 0)

        def OR(self):
            return self.getToken(CSlangParser.OR, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 209
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 204
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 205
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.OR or _la==CSlangParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 206
                    self.expr3(0) 
                self.state = 211
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(CSlangParser.Expr3Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 36
        self.enterRecursionRule(localctx, 36, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 215
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 216
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 217
                    self.expr4(0) 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(CSlangParser.Expr4Context,0)


        def MUL(self):
            return self.getToken(CSlangParser.MUL, 0)

        def DIV(self):
            return self.getToken(CSlangParser.DIV, 0)

        def MOD(self):
            return self.getToken(CSlangParser.MOD, 0)

        def BS(self):
            return self.getToken(CSlangParser.BS, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 226
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 227
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.DIV) | (1 << CSlangParser.BS) | (1 << CSlangParser.MOD) | (1 << CSlangParser.MUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 228
                    self.expr5(0) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(CSlangParser.Expr5Context,0)


        def CONCATENATION(self):
            return self.getToken(CSlangParser.CONCATENATION, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_expr5, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.expr6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                    self.state = 238
                    self.match(CSlangParser.CONCATENATION)
                    self.state = 239
                    self.expr6() 
                self.state = 244
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(CSlangParser.NOT, 0)

        def expr6(self):
            return self.getTypedRuleContext(CSlangParser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = CSlangParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr6)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(CSlangParser.NOT)
                self.state = 246
                self.expr6()
                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.AC, CSlangParser.LP, CSlangParser.ADD, CSlangParser.SUB, CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.expr7()
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(CSlangParser.Expr7Context,0)


        def ADD(self):
            return self.getToken(CSlangParser.ADD, 0)

        def SUB(self):
            return self.getToken(CSlangParser.SUB, 0)

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = CSlangParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.ADD, CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                _la = self._input.LA(1)
                if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 251
                self.expr7()
                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.AC, CSlangParser.LP, CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.expr8()
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


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def OB(self):
            return self.getToken(CSlangParser.OB, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def CB(self):
            return self.getToken(CSlangParser.CB, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)




    def expr8(self):

        localctx = CSlangParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr8)
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.expr9(0)
                self.state = 256
                self.match(CSlangParser.OB)
                self.state = 257
                self.expr()
                self.state = 258
                self.match(CSlangParser.CB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.expr9(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
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

        def list_of_expr(self):
            return self.getTypedRuleContext(CSlangParser.List_of_exprContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)



    def expr9(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSlangParser.Expr9Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr9, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 267
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 264
                    self.membername()
                    self.state = 265
                    self.match(CSlangParser.DOT)


                self.state = 269
                self.membername()
                self.state = 275
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 270
                    self.match(CSlangParser.LP)
                    self.state = 272
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.AC) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                        self.state = 271
                        self.list_of_expr()


                    self.state = 274
                    self.match(CSlangParser.RP)


                self.state = 278
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 277
                    self.match(CSlangParser.SM)


                pass

            elif la_ == 2:
                self.state = 280
                self.expr10()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 298
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 296
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 283
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 284
                        self.match(CSlangParser.DOT)
                        self.state = 285
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expr9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr9)
                        self.state = 286
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 287
                        self.match(CSlangParser.DOT)
                        self.state = 288
                        self.membername()
                        self.state = 294
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                        if la_ == 1:
                            self.state = 289
                            self.match(CSlangParser.LP)
                            self.state = 291
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.AC) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                                self.state = 290
                                self.list_of_expr()


                            self.state = 293
                            self.match(CSlangParser.RP)


                        pass

             
                self.state = 300
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr10Context(ParserRuleContext):
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

        def list_of_expr(self):
            return self.getTypedRuleContext(CSlangParser.List_of_exprContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CSlangParser.Expr10Context,0)


        def expr11(self):
            return self.getTypedRuleContext(CSlangParser.Expr11Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = CSlangParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(CSlangParser.NEW)
                self.state = 302
                self.match(CSlangParser.ID)
                self.state = 303
                self.match(CSlangParser.LP)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.AC) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 304
                    self.list_of_expr()


                self.state = 307
                self.match(CSlangParser.RP)
                self.state = 309
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 308
                    self.expr10()


                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.LP, CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.expr11()
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


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


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
            return CSlangParser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = CSlangParser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr11)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(CSlangParser.LP)
                self.state = 315
                self.expr()
                self.state = 316
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.ARRAYLIT, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 319
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 320
                self.match(CSlangParser.SELF)
                self.state = 321
                self.match(CSlangParser.DOT)
                self.state = 322
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 323
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


    class List_of_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return CSlangParser.RULE_list_of_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_expr" ):
                return visitor.visitList_of_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_of_expr(self):

        localctx = CSlangParser.List_of_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_list_of_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.expr()
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 327
                self.match(CSlangParser.CM)
                self.state = 328
                self.expr()
                self.state = 333
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

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(CSlangParser.FLOATLIT, 0)

        def STRING_LITERAL(self):
            return self.getToken(CSlangParser.STRING_LITERAL, 0)

        def BOOLLIT(self):
            return self.getToken(CSlangParser.BOOLLIT, 0)

        def ARRAYLIT(self):
            return self.getToken(CSlangParser.ARRAYLIT, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSlangParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
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
        self.enterRule(localctx, 58, self.RULE_statement)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 337
                self.assign_stmt()
                self.state = 338
                self.match(CSlangParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 340
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 341
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 342
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 343
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 344
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 345
                self.method_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 346
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
        self.enterRule(localctx, 60, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(CSlangParser.LB)
            self.state = 350
            self.member_block()
            self.state = 351
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
        self.enterRule(localctx, 62, self.RULE_member_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.RETURN) | (1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.AC) | (1 << CSlangParser.LB) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 357
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                if la_ == 1:
                    self.state = 353
                    self.attributedecl()
                    self.state = 354
                    self.match(CSlangParser.SM)
                    pass

                elif la_ == 2:
                    self.state = 356
                    self.statement()
                    pass


                self.state = 361
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def expr8(self):
            return self.getTypedRuleContext(CSlangParser.Expr8Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = CSlangParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 362
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.state = 363
                self.expr8()
                pass


            self.state = 366
            self.match(CSlangParser.ASSIGN)
            self.state = 367
            self.expr()
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


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
        self.enterRule(localctx, 66, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(CSlangParser.IF)
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LB:
                self.state = 370
                self.block_stmt()


            self.state = 373
            self.expr()
            self.state = 374
            self.block_stmt()
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 375
                self.match(CSlangParser.ELSE)
                self.state = 376
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


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
        self.enterRule(localctx, 68, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(CSlangParser.FOR)
            self.state = 380
            self.assign_stmt()
            self.state = 381
            self.match(CSlangParser.SM)
            self.state = 382
            self.expr()
            self.state = 383
            self.match(CSlangParser.SM)
            self.state = 384
            self.assign_stmt()
            self.state = 385
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
        self.enterRule(localctx, 70, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(CSlangParser.BREAK)
            self.state = 388
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
        self.enterRule(localctx, 72, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(CSlangParser.CONTINUE)
            self.state = 391
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = CSlangParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(CSlangParser.RETURN)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.AC) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 394
                self.expr()


            self.state = 397
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

        def expr(self):
            return self.getTypedRuleContext(CSlangParser.ExprContext,0)


        def list_of_expr(self):
            return self.getTypedRuleContext(CSlangParser.List_of_exprContext,0)


        def expr9(self):
            return self.getTypedRuleContext(CSlangParser.Expr9Context,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_method_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_stm" ):
                return visitor.visitMethod_stm(self)
            else:
                return visitor.visitChildren(self)




    def method_stm(self):

        localctx = CSlangParser.Method_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_method_stm)
        self._la = 0 # Token type
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 399
                    self.match(CSlangParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 400
                    self.expr()
                    pass


                self.state = 403
                self.match(CSlangParser.DOT)
                self.state = 404
                self.membername()
                self.state = 405
                self.match(CSlangParser.LP)
                self.state = 407
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.AC) | (1 << CSlangParser.LP) | (1 << CSlangParser.ADD) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.ARRAYLIT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 406
                    self.list_of_expr()


                self.state = 409
                self.match(CSlangParser.RP)
                self.state = 410
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.expr9(0)
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
        self._predicates[6] = self.attributedecl_sempred
        self._predicates[17] = self.expr2_sempred
        self._predicates[18] = self.expr3_sempred
        self._predicates[19] = self.expr4_sempred
        self._predicates[20] = self.expr5_sempred
        self._predicates[24] = self.expr9_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def attributedecl_sempred(self, localctx:AttributedeclContext, predIndex:int):
            if predIndex == 0:
                return len((None if localctx._attributelist is None else self._input.getText(localctx._attributelist.start,localctx._attributelist.stop)).split(',')) == len((None if localctx._initlist is None else self._input.getText(localctx._initlist.start,localctx._initlist.stop)).split(','))
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr9_sempred(self, localctx:Expr9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         




