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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3?")
        buf.write("\u022b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\3\2\6\2X\n\2\r\2\16")
        buf.write("\2Y\3\2\3\2\3\3\3\3\3\3\3\3\5\3b\n\3\3\3\3\3\5\3f\n\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\5\4v\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008c\n\6\3")
        buf.write("\7\3\7\3\7\7\7\u0091\n\7\f\7\16\7\u0094\13\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\t\3\t\5\t\u009f\n\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\5\n\u00a8\n\n\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b5\n\f\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u00c1\n\17\f\17\16")
        buf.write("\17\u00c4\13\17\3\20\3\20\3\20\3\20\3\20\5\20\u00cb\n")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\5\21\u00d2\n\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\7\22\u00da\n\22\f\22\16\22\u00dd")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00e5\n\23\f")
        buf.write("\23\16\23\u00e8\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u00f0\n\24\f\24\16\24\u00f3\13\24\3\25\3\25\3\25\5")
        buf.write("\25\u00f8\n\25\3\26\3\26\3\26\5\26\u00fd\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0107\n\27\f\27\16")
        buf.write("\27\u010a\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0114\n\30\3\30\5\30\u0117\n\30\7\30\u0119\n\30")
        buf.write("\f\30\16\30\u011c\13\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0138")
        buf.write("\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\7\31\u0149\n\31\f\31\16\31\u014c")
        buf.write("\13\31\3\32\3\32\3\32\3\32\5\32\u0152\n\32\3\32\3\32\5")
        buf.write("\32\u0156\n\32\3\32\5\32\u0159\n\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0171\n\33\3")
        buf.write("\34\3\34\3\34\7\34\u0176\n\34\f\34\16\34\u0179\13\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u0188\n\35\3\36\3\36\3\36\3\36\3\37\7")
        buf.write("\37\u018f\n\37\f\37\16\37\u0192\13\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u01a3\n \3!\3!\5!\u01a7")
        buf.write("\n!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u01c2")
        buf.write("\n\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\5")
        buf.write("&\u01d4\n&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0206\n\'\3")
        buf.write("(\3(\3(\3(\3(\5(\u020d\n(\3)\3)\3*\3*\3*\3*\7*\u0215\n")
        buf.write("*\f*\16*\u0218\13*\5*\u021a\n*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\5+\u0226\n+\3+\5+\u0229\n+\3+\2\b\"$&,.\60,\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRT\2\t\3\2\b\t\5\2\6\7\22\2388\3\2).\3")
        buf.write("\2\'(\3\2!\"\4\2#%\61\61\4\2\3\388\2\u0253\2W\3\2\2\2")
        buf.write("\4]\3\2\2\2\6u\3\2\2\2\bw\3\2\2\2\n\u008b\3\2\2\2\f\u008d")
        buf.write("\3\2\2\2\16\u0095\3\2\2\2\20\u009c\3\2\2\2\22\u00a7\3")
        buf.write("\2\2\2\24\u00a9\3\2\2\2\26\u00b4\3\2\2\2\30\u00b6\3\2")
        buf.write("\2\2\32\u00b8\3\2\2\2\34\u00bd\3\2\2\2\36\u00ca\3\2\2")
        buf.write("\2 \u00d1\3\2\2\2\"\u00d3\3\2\2\2$\u00de\3\2\2\2&\u00e9")
        buf.write("\3\2\2\2(\u00f7\3\2\2\2*\u00fc\3\2\2\2,\u00fe\3\2\2\2")
        buf.write(".\u010b\3\2\2\2\60\u0137\3\2\2\2\62\u0158\3\2\2\2\64\u0170")
        buf.write("\3\2\2\2\66\u0172\3\2\2\28\u0187\3\2\2\2:\u0189\3\2\2")
        buf.write("\2<\u0190\3\2\2\2>\u01a2\3\2\2\2@\u01a6\3\2\2\2B\u01c1")
        buf.write("\3\2\2\2D\u01c3\3\2\2\2F\u01cb\3\2\2\2H\u01ce\3\2\2\2")
        buf.write("J\u01d1\3\2\2\2L\u0205\3\2\2\2N\u020c\3\2\2\2P\u020e\3")
        buf.write("\2\2\2R\u0210\3\2\2\2T\u0228\3\2\2\2VX\5\4\3\2WV\3\2\2")
        buf.write("\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\7\2\2\3")
        buf.write("\\\3\3\2\2\2]^\7\4\2\2^a\78\2\2_`\7\63\2\2`b\78\2\2a_")
        buf.write("\3\2\2\2ab\3\2\2\2bc\3\2\2\2ce\7\32\2\2df\5\6\4\2ed\3")
        buf.write("\2\2\2ef\3\2\2\2fg\3\2\2\2gh\7\33\2\2h\5\3\2\2\2iv\5\n")
        buf.write("\6\2jv\5\16\b\2kv\5\b\5\2lm\5\n\6\2mn\5\6\4\2nv\3\2\2")
        buf.write("\2op\5\16\b\2pq\5\6\4\2qv\3\2\2\2rs\5\b\5\2st\5\6\4\2")
        buf.write("tv\3\2\2\2ui\3\2\2\2uj\3\2\2\2uk\3\2\2\2ul\3\2\2\2uo\3")
        buf.write("\2\2\2ur\3\2\2\2v\7\3\2\2\2wx\7\n\2\2xy\7\f\2\2yz\5\20")
        buf.write("\t\2z{\5:\36\2{\t\3\2\2\2|}\t\2\2\2}~\5\34\17\2~\177\7")
        buf.write("\62\2\2\177\u0080\5\26\f\2\u0080\u0081\7\31\2\2\u0081")
        buf.write("\u0082\5\f\7\2\u0082\u0083\3\2\2\2\u0083\u0084\7\36\2")
        buf.write("\2\u0084\u008c\3\2\2\2\u0085\u0086\t\2\2\2\u0086\u0087")
        buf.write("\5\34\17\2\u0087\u0088\7\62\2\2\u0088\u0089\5\26\f\2\u0089")
        buf.write("\u008a\7\36\2\2\u008a\u008c\3\2\2\2\u008b|\3\2\2\2\u008b")
        buf.write("\u0085\3\2\2\2\u008c\13\3\2\2\2\u008d\u0092\5\36\20\2")
        buf.write("\u008e\u008f\7\37\2\2\u008f\u0091\5\36\20\2\u0090\u008e")
        buf.write("\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\r\3\2\2\2\u0094\u0092\3\2\2\2\u0095")
        buf.write("\u0096\7\n\2\2\u0096\u0097\5P)\2\u0097\u0098\5\20\t\2")
        buf.write("\u0098\u0099\7\62\2\2\u0099\u009a\5\26\f\2\u009a\u009b")
        buf.write("\5:\36\2\u009b\17\3\2\2\2\u009c\u009e\7\34\2\2\u009d\u009f")
        buf.write("\5\22\n\2\u009e\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f")
        buf.write("\u00a0\3\2\2\2\u00a0\u00a1\7\35\2\2\u00a1\21\3\2\2\2\u00a2")
        buf.write("\u00a3\5\24\13\2\u00a3\u00a4\7\37\2\2\u00a4\u00a5\5\22")
        buf.write("\n\2\u00a5\u00a8\3\2\2\2\u00a6\u00a8\5\24\13\2\u00a7\u00a2")
        buf.write("\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\23\3\2\2\2\u00a9\u00aa")
        buf.write("\5\34\17\2\u00aa\u00ab\7\62\2\2\u00ab\u00ac\5\26\f\2\u00ac")
        buf.write("\25\3\2\2\2\u00ad\u00b5\7\6\2\2\u00ae\u00b5\7\7\2\2\u00af")
        buf.write("\u00b5\7\22\2\2\u00b0\u00b5\7\23\2\2\u00b1\u00b5\7\13")
        buf.write("\2\2\u00b2\u00b5\5\30\r\2\u00b3\u00b5\5\32\16\2\u00b4")
        buf.write("\u00ad\3\2\2\2\u00b4\u00ae\3\2\2\2\u00b4\u00af\3\2\2\2")
        buf.write("\u00b4\u00b0\3\2\2\2\u00b4\u00b1\3\2\2\2\u00b4\u00b2\3")
        buf.write("\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\27\3\2\2\2\u00b6\u00b7")
        buf.write("\5P)\2\u00b7\31\3\2\2\2\u00b8\u00b9\7\27\2\2\u00b9\u00ba")
        buf.write("\7\65\2\2\u00ba\u00bb\7\30\2\2\u00bb\u00bc\t\3\2\2\u00bc")
        buf.write("\33\3\2\2\2\u00bd\u00c2\5P)\2\u00be\u00bf\7\37\2\2\u00bf")
        buf.write("\u00c1\5P)\2\u00c0\u00be\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\35\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c5\u00c6\5 \21\2\u00c6\u00c7\7\60\2")
        buf.write("\2\u00c7\u00c8\5 \21\2\u00c8\u00cb\3\2\2\2\u00c9\u00cb")
        buf.write("\5 \21\2\u00ca\u00c5\3\2\2\2\u00ca\u00c9\3\2\2\2\u00cb")
        buf.write("\37\3\2\2\2\u00cc\u00cd\5\"\22\2\u00cd\u00ce\t\4\2\2\u00ce")
        buf.write("\u00cf\5\"\22\2\u00cf\u00d2\3\2\2\2\u00d0\u00d2\5\"\22")
        buf.write("\2\u00d1\u00cc\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2!\3\2")
        buf.write("\2\2\u00d3\u00d4\b\22\1\2\u00d4\u00d5\5$\23\2\u00d5\u00db")
        buf.write("\3\2\2\2\u00d6\u00d7\f\4\2\2\u00d7\u00d8\t\5\2\2\u00d8")
        buf.write("\u00da\5$\23\2\u00d9\u00d6\3\2\2\2\u00da\u00dd\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc#\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00de\u00df\b\23\1\2\u00df\u00e0")
        buf.write("\5&\24\2\u00e0\u00e6\3\2\2\2\u00e1\u00e2\f\4\2\2\u00e2")
        buf.write("\u00e3\t\6\2\2\u00e3\u00e5\5&\24\2\u00e4\u00e1\3\2\2\2")
        buf.write("\u00e5\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7%\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea")
        buf.write("\b\24\1\2\u00ea\u00eb\5(\25\2\u00eb\u00f1\3\2\2\2\u00ec")
        buf.write("\u00ed\f\4\2\2\u00ed\u00ee\t\7\2\2\u00ee\u00f0\5(\25\2")
        buf.write("\u00ef\u00ec\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3")
        buf.write("\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\'\3\2\2\2\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f4\u00f5\7&\2\2\u00f5\u00f8\5(\25\2\u00f6")
        buf.write("\u00f8\5*\26\2\u00f7\u00f4\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8)\3\2\2\2\u00f9\u00fa\7\"\2\2\u00fa\u00fd\5*\26")
        buf.write("\2\u00fb\u00fd\5,\27\2\u00fc\u00f9\3\2\2\2\u00fc\u00fb")
        buf.write("\3\2\2\2\u00fd+\3\2\2\2\u00fe\u00ff\b\27\1\2\u00ff\u0100")
        buf.write("\5.\30\2\u0100\u0108\3\2\2\2\u0101\u0102\f\4\2\2\u0102")
        buf.write("\u0103\7\27\2\2\u0103\u0104\5\36\20\2\u0104\u0105\7\30")
        buf.write("\2\2\u0105\u0107\3\2\2\2\u0106\u0101\3\2\2\2\u0107\u010a")
        buf.write("\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("-\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\b\30\1\2\u010c")
        buf.write("\u010d\5\60\31\2\u010d\u011a\3\2\2\2\u010e\u010f\f\4\2")
        buf.write("\2\u010f\u0110\7 \2\2\u0110\u0116\78\2\2\u0111\u0113\7")
        buf.write("\34\2\2\u0112\u0114\5\66\34\2\u0113\u0112\3\2\2\2\u0113")
        buf.write("\u0114\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\7\35\2")
        buf.write("\2\u0116\u0111\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u0119")
        buf.write("\3\2\2\2\u0118\u010e\3\2\2\2\u0119\u011c\3\2\2\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b/\3\2\2\2\u011c")
        buf.write("\u011a\3\2\2\2\u011d\u011e\b\31\1\2\u011e\u011f\78\2\2")
        buf.write("\u011f\u0120\7 \2\2\u0120\u0138\7\3\2\2\u0121\u0138\7")
        buf.write("\3\2\2\u0122\u0123\78\2\2\u0123\u0124\7 \2\2\u0124\u0125")
        buf.write("\7\3\2\2\u0125\u0126\7\34\2\2\u0126\u0127\5\66\34\2\u0127")
        buf.write("\u0128\7\35\2\2\u0128\u0138\3\2\2\2\u0129\u012a\7\3\2")
        buf.write("\2\u012a\u012b\7\34\2\2\u012b\u012c\5\66\34\2\u012c\u012d")
        buf.write("\7\35\2\2\u012d\u0138\3\2\2\2\u012e\u012f\78\2\2\u012f")
        buf.write("\u0130\7 \2\2\u0130\u0131\7\3\2\2\u0131\u0132\7\34\2\2")
        buf.write("\u0132\u0138\7\35\2\2\u0133\u0134\7\3\2\2\u0134\u0135")
        buf.write("\7\34\2\2\u0135\u0138\7\35\2\2\u0136\u0138\5\62\32\2\u0137")
        buf.write("\u011d\3\2\2\2\u0137\u0121\3\2\2\2\u0137\u0122\3\2\2\2")
        buf.write("\u0137\u0129\3\2\2\2\u0137\u012e\3\2\2\2\u0137\u0133\3")
        buf.write("\2\2\2\u0137\u0136\3\2\2\2\u0138\u014a\3\2\2\2\u0139\u013a")
        buf.write("\f\f\2\2\u013a\u013b\7 \2\2\u013b\u0149\78\2\2\u013c\u013d")
        buf.write("\f\t\2\2\u013d\u013e\7 \2\2\u013e\u013f\78\2\2\u013f\u0140")
        buf.write("\7\34\2\2\u0140\u0141\5\66\34\2\u0141\u0142\7\35\2\2\u0142")
        buf.write("\u0149\3\2\2\2\u0143\u0144\f\6\2\2\u0144\u0145\7 \2\2")
        buf.write("\u0145\u0146\78\2\2\u0146\u0147\7\34\2\2\u0147\u0149\7")
        buf.write("\35\2\2\u0148\u0139\3\2\2\2\u0148\u013c\3\2\2\2\u0148")
        buf.write("\u0143\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\61\3\2\2\2\u014c\u014a\3\2")
        buf.write("\2\2\u014d\u014e\7\26\2\2\u014e\u014f\78\2\2\u014f\u0151")
        buf.write("\7\34\2\2\u0150\u0152\5\66\34\2\u0151\u0150\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0155\7\35\2")
        buf.write("\2\u0154\u0156\5\62\32\2\u0155\u0154\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0159\5\64\33\2\u0158")
        buf.write("\u014d\3\2\2\2\u0158\u0157\3\2\2\2\u0159\63\3\2\2\2\u015a")
        buf.write("\u015b\7\34\2\2\u015b\u015c\5\36\20\2\u015c\u015d\7\35")
        buf.write("\2\2\u015d\u0171\3\2\2\2\u015e\u0171\78\2\2\u015f\u0171")
        buf.write("\5N(\2\u0160\u0161\7\25\2\2\u0161\u0162\7 \2\2\u0162\u0171")
        buf.write("\78\2\2\u0163\u0164\7\25\2\2\u0164\u0165\7 \2\2\u0165")
        buf.write("\u0166\78\2\2\u0166\u0167\7\34\2\2\u0167\u0168\5\66\34")
        buf.write("\2\u0168\u0169\7\35\2\2\u0169\u0171\3\2\2\2\u016a\u016b")
        buf.write("\7\25\2\2\u016b\u016c\7 \2\2\u016c\u016d\78\2\2\u016d")
        buf.write("\u016e\7\34\2\2\u016e\u0171\7\35\2\2\u016f\u0171\7\24")
        buf.write("\2\2\u0170\u015a\3\2\2\2\u0170\u015e\3\2\2\2\u0170\u015f")
        buf.write("\3\2\2\2\u0170\u0160\3\2\2\2\u0170\u0163\3\2\2\2\u0170")
        buf.write("\u016a\3\2\2\2\u0170\u016f\3\2\2\2\u0171\65\3\2\2\2\u0172")
        buf.write("\u0177\5\36\20\2\u0173\u0174\7\37\2\2\u0174\u0176\5\36")
        buf.write("\20\2\u0175\u0173\3\2\2\2\u0176\u0179\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0178\3\2\2\2\u0178\67\3\2\2\2\u0179\u0177")
        buf.write("\3\2\2\2\u017a\u0188\5> \2\u017b\u017c\5@!\2\u017c\u017d")
        buf.write("\7\36\2\2\u017d\u0188\3\2\2\2\u017e\u0188\5B\"\2\u017f")
        buf.write("\u0188\5D#\2\u0180\u0188\5F$\2\u0181\u0188\5H%\2\u0182")
        buf.write("\u0188\5J&\2\u0183\u0184\5L\'\2\u0184\u0185\7\36\2\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0188\5:\36\2\u0187\u017a\3\2\2\2")
        buf.write("\u0187\u017b\3\2\2\2\u0187\u017e\3\2\2\2\u0187\u017f\3")
        buf.write("\2\2\2\u0187\u0180\3\2\2\2\u0187\u0181\3\2\2\2\u0187\u0182")
        buf.write("\3\2\2\2\u0187\u0183\3\2\2\2\u0187\u0186\3\2\2\2\u0188")
        buf.write("9\3\2\2\2\u0189\u018a\7\32\2\2\u018a\u018b\5<\37\2\u018b")
        buf.write("\u018c\7\33\2\2\u018c;\3\2\2\2\u018d\u018f\58\35\2\u018e")
        buf.write("\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191=\3\2\2\2\u0192\u0190\3\2\2")
        buf.write("\2\u0193\u0194\t\2\2\2\u0194\u0195\5\34\17\2\u0195\u0196")
        buf.write("\7\62\2\2\u0196\u0197\5\26\f\2\u0197\u0198\7\31\2\2\u0198")
        buf.write("\u0199\5\f\7\2\u0199\u019a\3\2\2\2\u019a\u019b\7\36\2")
        buf.write("\2\u019b\u01a3\3\2\2\2\u019c\u019d\t\2\2\2\u019d\u019e")
        buf.write("\5\34\17\2\u019e\u019f\7\62\2\2\u019f\u01a0\5\26\f\2\u01a0")
        buf.write("\u01a1\7\36\2\2\u01a1\u01a3\3\2\2\2\u01a2\u0193\3\2\2")
        buf.write("\2\u01a2\u019c\3\2\2\2\u01a3?\3\2\2\2\u01a4\u01a7\78\2")
        buf.write("\2\u01a5\u01a7\5,\27\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\7/\2\2\u01a9")
        buf.write("\u01aa\5\36\20\2\u01aaA\3\2\2\2\u01ab\u01ac\7\17\2\2\u01ac")
        buf.write("\u01ad\5:\36\2\u01ad\u01ae\5\36\20\2\u01ae\u01af\5:\36")
        buf.write("\2\u01af\u01b0\7\20\2\2\u01b0\u01b1\5:\36\2\u01b1\u01c2")
        buf.write("\3\2\2\2\u01b2\u01b3\7\17\2\2\u01b3\u01b4\5:\36\2\u01b4")
        buf.write("\u01b5\5\36\20\2\u01b5\u01b6\5:\36\2\u01b6\u01c2\3\2\2")
        buf.write("\2\u01b7\u01b8\7\17\2\2\u01b8\u01b9\5\36\20\2\u01b9\u01ba")
        buf.write("\5:\36\2\u01ba\u01bb\7\20\2\2\u01bb\u01bc\5:\36\2\u01bc")
        buf.write("\u01c2\3\2\2\2\u01bd\u01be\7\17\2\2\u01be\u01bf\5\36\20")
        buf.write("\2\u01bf\u01c0\5:\36\2\u01c0\u01c2\3\2\2\2\u01c1\u01ab")
        buf.write("\3\2\2\2\u01c1\u01b2\3\2\2\2\u01c1\u01b7\3\2\2\2\u01c1")
        buf.write("\u01bd\3\2\2\2\u01c2C\3\2\2\2\u01c3\u01c4\7\21\2\2\u01c4")
        buf.write("\u01c5\5@!\2\u01c5\u01c6\7\36\2\2\u01c6\u01c7\5\36\20")
        buf.write("\2\u01c7\u01c8\7\36\2\2\u01c8\u01c9\5@!\2\u01c9\u01ca")
        buf.write("\5:\36\2\u01caE\3\2\2\2\u01cb\u01cc\7\r\2\2\u01cc\u01cd")
        buf.write("\7\36\2\2\u01cdG\3\2\2\2\u01ce\u01cf\7\16\2\2\u01cf\u01d0")
        buf.write("\7\36\2\2\u01d0I\3\2\2\2\u01d1\u01d3\7\5\2\2\u01d2\u01d4")
        buf.write("\5\36\20\2\u01d3\u01d2\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("\u01d5\3\2\2\2\u01d5\u01d6\7\36\2\2\u01d6K\3\2\2\2\u01d7")
        buf.write("\u0206\3\2\2\2\u01d8\u01d9\5\36\20\2\u01d9\u01da\7 \2")
        buf.write("\2\u01da\u01db\78\2\2\u01db\u01dc\7\34\2\2\u01dc\u01dd")
        buf.write("\5\66\34\2\u01dd\u01de\7\35\2\2\u01de\u0206\3\2\2\2\u01df")
        buf.write("\u01e0\78\2\2\u01e0\u01e1\7 \2\2\u01e1\u01e2\7\3\2\2\u01e2")
        buf.write("\u01e3\7\34\2\2\u01e3\u01e4\5\66\34\2\u01e4\u01e5\7\35")
        buf.write("\2\2\u01e5\u0206\3\2\2\2\u01e6\u01e7\7\3\2\2\u01e7\u01e8")
        buf.write("\7\34\2\2\u01e8\u01e9\5\66\34\2\u01e9\u01ea\7\35\2\2\u01ea")
        buf.write("\u0206\3\2\2\2\u01eb\u01ec\5\36\20\2\u01ec\u01ed\7 \2")
        buf.write("\2\u01ed\u01ee\78\2\2\u01ee\u01ef\7\34\2\2\u01ef\u01f0")
        buf.write("\7\35\2\2\u01f0\u0206\3\2\2\2\u01f1\u01f2\78\2\2\u01f2")
        buf.write("\u01f3\7 \2\2\u01f3\u01f4\7\3\2\2\u01f4\u01f5\7\34\2\2")
        buf.write("\u01f5\u0206\7\35\2\2\u01f6\u01f7\7\3\2\2\u01f7\u01f8")
        buf.write("\7\34\2\2\u01f8\u0206\7\35\2\2\u01f9\u01fa\7\25\2\2\u01fa")
        buf.write("\u01fb\7 \2\2\u01fb\u01fc\78\2\2\u01fc\u01fd\7\34\2\2")
        buf.write("\u01fd\u01fe\5\66\34\2\u01fe\u01ff\7\35\2\2\u01ff\u0206")
        buf.write("\3\2\2\2\u0200\u0201\7\25\2\2\u0201\u0202\7 \2\2\u0202")
        buf.write("\u0203\78\2\2\u0203\u0204\7\34\2\2\u0204\u0206\7\35\2")
        buf.write("\2\u0205\u01d7\3\2\2\2\u0205\u01d8\3\2\2\2\u0205\u01df")
        buf.write("\3\2\2\2\u0205\u01e6\3\2\2\2\u0205\u01eb\3\2\2\2\u0205")
        buf.write("\u01f1\3\2\2\2\u0205\u01f6\3\2\2\2\u0205\u01f9\3\2\2\2")
        buf.write("\u0205\u0200\3\2\2\2\u0206M\3\2\2\2\u0207\u020d\7\65\2")
        buf.write("\2\u0208\u020d\7\64\2\2\u0209\u020d\7\67\2\2\u020a\u020d")
        buf.write("\7\66\2\2\u020b\u020d\5R*\2\u020c\u0207\3\2\2\2\u020c")
        buf.write("\u0208\3\2\2\2\u020c\u0209\3\2\2\2\u020c\u020a\3\2\2\2")
        buf.write("\u020c\u020b\3\2\2\2\u020dO\3\2\2\2\u020e\u020f\t\b\2")
        buf.write("\2\u020fQ\3\2\2\2\u0210\u0219\7\27\2\2\u0211\u0216\5T")
        buf.write("+\2\u0212\u0213\7\37\2\2\u0213\u0215\5T+\2\u0214\u0212")
        buf.write("\3\2\2\2\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216")
        buf.write("\u0217\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2")
        buf.write("\u0219\u0211\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021b\3")
        buf.write("\2\2\2\u021b\u021c\7\30\2\2\u021cS\3\2\2\2\u021d\u0229")
        buf.write("\7\65\2\2\u021e\u0229\7\64\2\2\u021f\u0229\7\67\2\2\u0220")
        buf.write("\u0229\7\66\2\2\u0221\u0222\7\26\2\2\u0222\u0223\78\2")
        buf.write("\2\u0223\u0225\7\34\2\2\u0224\u0226\5\66\34\2\u0225\u0224")
        buf.write("\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0229\7\35\2\2\u0228\u021d\3\2\2\2\u0228\u021e\3\2\2")
        buf.write("\2\u0228\u021f\3\2\2\2\u0228\u0220\3\2\2\2\u0228\u0221")
        buf.write("\3\2\2\2\u0229U\3\2\2\2+Yaeu\u008b\u0092\u009e\u00a7\u00b4")
        buf.write("\u00c2\u00ca\u00d1\u00db\u00e6\u00f1\u00f7\u00fc\u0108")
        buf.write("\u0113\u0116\u011a\u0137\u0148\u014a\u0151\u0155\u0158")
        buf.write("\u0170\u0177\u0187\u0190\u01a2\u01a6\u01c1\u01d3\u0205")
        buf.write("\u020c\u0216\u0219\u0225\u0228")
        return buf.getvalue()


class CSlangParser ( Parser ):

    grammarFileName = "CSlang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'class'", "'return'", "'int'", 
                     "'float'", "'const'", "'var'", "'func'", "'void'", 
                     "'constructor'", "'break'", "'continue'", "'if'", "'else'", 
                     "'for'", "'bool'", "'string'", "'null'", "'self'", 
                     "'new'", "'['", "']'", "'='", "'{'", "'}'", "'('", 
                     "')'", "';'", "','", "'.'", "'+'", "'-'", "'/'", "'\\'", 
                     "'%'", "'!'", "'||'", "'&&'", "'=='", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "':='", "'^'", "'*'", "':'", 
                     "'<-'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "STATIC", "CLASS", "RETURN", "INT", "FLOAT", 
                      "CONST", "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "FOR", "BOOL", "STRING", 
                      "NULL", "SELF", "NEW", "OB", "CB", "EQ", "LB", "RB", 
                      "LP", "RP", "SM", "CM", "DOT", "ADD", "SUB", "DIV", 
                      "BS", "MOD", "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", 
                      "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", 
                      "CONCATENATION", "MUL", "COLON", "EXTENDS", "FLOATLIT", 
                      "INTLIT", "BOOLLIT", "STRING_LITERAL", "ID", "WS", 
                      "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_classdecl = 1
    RULE_classmember = 2
    RULE_construcdecl = 3
    RULE_attributedecl = 4
    RULE_initlist = 5
    RULE_methoddecl = 6
    RULE_paramdecl = 7
    RULE_paramlist = 8
    RULE_param = 9
    RULE_mctype = 10
    RULE_classtype = 11
    RULE_array_type = 12
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
    RULE_operands = 25
    RULE_list_of_expression = 26
    RULE_statement = 27
    RULE_block_stmt = 28
    RULE_member_block = 29
    RULE_block_vardecl = 30
    RULE_assign_stmt = 31
    RULE_if_stmt = 32
    RULE_for_stmt = 33
    RULE_break_stmt = 34
    RULE_continue_stmt = 35
    RULE_return_stmt = 36
    RULE_method_stm = 37
    RULE_literal = 38
    RULE_membername = 39
    RULE_array_literal = 40
    RULE_elem = 41

    ruleNames =  [ "program", "classdecl", "classmember", "construcdecl", 
                   "attributedecl", "initlist", "methoddecl", "paramdecl", 
                   "paramlist", "param", "mctype", "classtype", "array_type", 
                   "attributelist", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "expression8", "expression9", "expression10", 
                   "operands", "list_of_expression", "statement", "block_stmt", 
                   "member_block", "block_vardecl", "assign_stmt", "if_stmt", 
                   "for_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "method_stm", "literal", "membername", "array_literal", 
                   "elem" ]

    EOF = Token.EOF
    STATIC=1
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
    BOOL=16
    STRING=17
    NULL=18
    SELF=19
    NEW=20
    OB=21
    CB=22
    EQ=23
    LB=24
    RB=25
    LP=26
    RP=27
    SM=28
    CM=29
    DOT=30
    ADD=31
    SUB=32
    DIV=33
    BS=34
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
    CONCATENATION=46
    MUL=47
    COLON=48
    EXTENDS=49
    FLOATLIT=50
    INTLIT=51
    BOOLLIT=52
    STRING_LITERAL=53
    ID=54
    WS=55
    NEWLINE=56
    LINE_COMMENT=57
    BLOCK_COMMENT=58
    ERROR_CHAR=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61

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
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.classdecl()
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 89
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(CSlangParser.ID)
            else:
                return self.getToken(CSlangParser.ID, i)

        def LB(self):
            return self.getToken(CSlangParser.LB, 0)

        def RB(self):
            return self.getToken(CSlangParser.RB, 0)

        def EXTENDS(self):
            return self.getToken(CSlangParser.EXTENDS, 0)

        def classmember(self):
            return self.getTypedRuleContext(CSlangParser.ClassmemberContext,0)


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
            self.state = 91
            self.match(CSlangParser.CLASS)
            self.state = 92
            self.match(CSlangParser.ID)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EXTENDS:
                self.state = 93
                self.match(CSlangParser.EXTENDS)
                self.state = 94
                self.match(CSlangParser.ID)


            self.state = 97
            self.match(CSlangParser.LB)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 98
                self.classmember()


            self.state = 101
            self.match(CSlangParser.RB)
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


        def classmember(self):
            return self.getTypedRuleContext(CSlangParser.ClassmemberContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classmember

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassmember" ):
                return visitor.visitClassmember(self)
            else:
                return visitor.visitChildren(self)




    def classmember(self):

        localctx = CSlangParser.ClassmemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classmember)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.construcdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 106
                self.attributedecl()
                self.state = 107
                self.classmember()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.methoddecl()
                self.state = 110
                self.classmember()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 112
                self.construcdecl()
                self.state = 113
                self.classmember()
                pass


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
            self.state = 117
            self.match(CSlangParser.FUNC)
            self.state = 118
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 119
            self.paramdecl()
            self.state = 120
            self.block_stmt()
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


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

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
        self.enterRule(localctx, 8, self.RULE_attributedecl)
        self._la = 0 # Token type
        try:
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 123
                self.attributelist()
                self.state = 124
                self.match(CSlangParser.COLON)
                self.state = 125
                self.mctype()

                self.state = 126
                self.match(CSlangParser.EQ)
                self.state = 127
                self.initlist()
                self.state = 129
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 132
                self.attributelist()
                self.state = 133
                self.match(CSlangParser.COLON)
                self.state = 134
                self.mctype()
                self.state = 135
                self.match(CSlangParser.SM)
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
        self.enterRule(localctx, 10, self.RULE_initlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.expression()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 140
                self.match(CSlangParser.CM)
                self.state = 141
                self.expression()
                self.state = 146
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
        self.enterRule(localctx, 12, self.RULE_methoddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(CSlangParser.FUNC)
            self.state = 148
            self.membername()
            self.state = 149
            self.paramdecl()
            self.state = 150
            self.match(CSlangParser.COLON)
            self.state = 151
            self.mctype()
            self.state = 152
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
        self.enterRule(localctx, 14, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(CSlangParser.LP)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.STATIC or _la==CSlangParser.ID:
                self.state = 155
                self.paramlist()


            self.state = 158
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

        def param(self):
            return self.getTypedRuleContext(CSlangParser.ParamContext,0)


        def CM(self):
            return self.getToken(CSlangParser.CM, 0)

        def paramlist(self):
            return self.getTypedRuleContext(CSlangParser.ParamlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = CSlangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramlist)
        try:
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.param()
                self.state = 161
                self.match(CSlangParser.CM)
                self.state = 162
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.param()
                pass


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
        self.enterRule(localctx, 18, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.attributelist()
            self.state = 168
            self.match(CSlangParser.COLON)
            self.state = 169
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


        def array_type(self):
            return self.getTypedRuleContext(CSlangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_mctype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMctype" ):
                return visitor.visitMctype(self)
            else:
                return visitor.visitChildren(self)




    def mctype(self):

        localctx = CSlangParser.MctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mctype)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.classtype()
                pass
            elif token in [CSlangParser.OB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 177
                self.array_type()
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

        def membername(self):
            return self.getTypedRuleContext(CSlangParser.MembernameContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_classtype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClasstype" ):
                return visitor.visitClasstype(self)
            else:
                return visitor.visitChildren(self)




    def classtype(self):

        localctx = CSlangParser.ClasstypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.membername()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(CSlangParser.OB, 0)

        def INTLIT(self):
            return self.getToken(CSlangParser.INTLIT, 0)

        def CB(self):
            return self.getToken(CSlangParser.CB, 0)

        def INT(self):
            return self.getToken(CSlangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSlangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(CSlangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(CSlangParser.STRING, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def getRuleIndex(self):
            return CSlangParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = CSlangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(CSlangParser.OB)
            self.state = 183
            self.match(CSlangParser.INTLIT)
            self.state = 184
            self.match(CSlangParser.CB)
            self.state = 185
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.INT) | (1 << CSlangParser.FLOAT) | (1 << CSlangParser.BOOL) | (1 << CSlangParser.STRING) | (1 << CSlangParser.ID))) != 0)):
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
            self.state = 187
            self.membername()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 188
                self.match(CSlangParser.CM)
                self.state = 189
                self.membername()
                self.state = 194
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
        self.enterRule(localctx, 28, self.RULE_expression)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.expression1()
                self.state = 196
                self.match(CSlangParser.CONCATENATION)
                self.state = 197
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
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
        self.enterRule(localctx, 30, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.expression2(0)
                self.state = 203
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.NOTEQUAL) | (1 << CSlangParser.LESS) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.LESSEQUAL) | (1 << CSlangParser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 204
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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
            self.state = 210
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 217
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 212
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 213
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.OR or _la==CSlangParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 214
                    self.expression3(0) 
                self.state = 219
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
            self.state = 221
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 228
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 223
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 224
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 225
                    self.expression4(0) 
                self.state = 230
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
            self.state = 232
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 234
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 235
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.DIV) | (1 << CSlangParser.BS) | (1 << CSlangParser.MOD) | (1 << CSlangParser.MUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 236
                    self.expression5() 
                self.state = 241
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
        self.enterRule(localctx, 38, self.RULE_expression5)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(CSlangParser.NOT)
                self.state = 243
                self.expression5()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.SUB, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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
        self.enterRule(localctx, 40, self.RULE_expression6)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(CSlangParser.SUB)
                self.state = 248
                self.expression6()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.expression8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                    self.state = 255
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 256
                    self.match(CSlangParser.OB)
                    self.state = 257
                    self.expression()
                    self.state = 258
                    self.match(CSlangParser.CB) 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.expression9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 268
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 269
                    self.match(CSlangParser.DOT)
                    self.state = 270
                    self.match(CSlangParser.ID)
                    self.state = 276
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 271
                        self.match(CSlangParser.LP)
                        self.state = 273
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                            self.state = 272
                            self.list_of_expression()


                        self.state = 275
                        self.match(CSlangParser.RP)

             
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def STATIC(self):
            return self.getToken(CSlangParser.STATIC, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def expression10(self):
            return self.getTypedRuleContext(CSlangParser.Expression10Context,0)


        def expression9(self):
            return self.getTypedRuleContext(CSlangParser.Expression9Context,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 284
                self.match(CSlangParser.ID)
                self.state = 285
                self.match(CSlangParser.DOT)
                self.state = 286
                self.match(CSlangParser.STATIC)
                pass

            elif la_ == 2:
                self.state = 287
                self.match(CSlangParser.STATIC)
                pass

            elif la_ == 3:
                self.state = 288
                self.match(CSlangParser.ID)
                self.state = 289
                self.match(CSlangParser.DOT)
                self.state = 290
                self.match(CSlangParser.STATIC)
                self.state = 291
                self.match(CSlangParser.LP)
                self.state = 292
                self.list_of_expression()
                self.state = 293
                self.match(CSlangParser.RP)
                pass

            elif la_ == 4:
                self.state = 295
                self.match(CSlangParser.STATIC)
                self.state = 296
                self.match(CSlangParser.LP)
                self.state = 297
                self.list_of_expression()
                self.state = 298
                self.match(CSlangParser.RP)
                pass

            elif la_ == 5:
                self.state = 300
                self.match(CSlangParser.ID)
                self.state = 301
                self.match(CSlangParser.DOT)
                self.state = 302
                self.match(CSlangParser.STATIC)
                self.state = 303
                self.match(CSlangParser.LP)
                self.state = 304
                self.match(CSlangParser.RP)
                pass

            elif la_ == 6:
                self.state = 305
                self.match(CSlangParser.STATIC)
                self.state = 306
                self.match(CSlangParser.LP)
                self.state = 307
                self.match(CSlangParser.RP)
                pass

            elif la_ == 7:
                self.state = 308
                self.expression10()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 326
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 311
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 312
                        self.match(CSlangParser.DOT)
                        self.state = 313
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 314
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 315
                        self.match(CSlangParser.DOT)
                        self.state = 316
                        self.match(CSlangParser.ID)
                        self.state = 317
                        self.match(CSlangParser.LP)
                        self.state = 318
                        self.list_of_expression()
                        self.state = 319
                        self.match(CSlangParser.RP)
                        pass

                    elif la_ == 3:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 321
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 322
                        self.match(CSlangParser.DOT)
                        self.state = 323
                        self.match(CSlangParser.ID)
                        self.state = 324
                        self.match(CSlangParser.LP)
                        self.state = 325
                        self.match(CSlangParser.RP)
                        pass

             
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_expression10)
        self._la = 0 # Token type
        try:
            self.state = 342
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(CSlangParser.NEW)
                self.state = 332
                self.match(CSlangParser.ID)
                self.state = 333
                self.match(CSlangParser.LP)
                self.state = 335
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 334
                    self.list_of_expression()


                self.state = 337
                self.match(CSlangParser.RP)
                self.state = 339
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 338
                    self.expression10()


                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
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

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


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
        self.enterRule(localctx, 50, self.RULE_operands)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(CSlangParser.LP)
                self.state = 345
                self.expression()
                self.state = 346
                self.match(CSlangParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(CSlangParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 349
                self.literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 350
                self.match(CSlangParser.SELF)
                self.state = 351
                self.match(CSlangParser.DOT)
                self.state = 352
                self.match(CSlangParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 353
                self.match(CSlangParser.SELF)
                self.state = 354
                self.match(CSlangParser.DOT)
                self.state = 355
                self.match(CSlangParser.ID)
                self.state = 356
                self.match(CSlangParser.LP)
                self.state = 357
                self.list_of_expression()
                self.state = 358
                self.match(CSlangParser.RP)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 360
                self.match(CSlangParser.SELF)
                self.state = 361
                self.match(CSlangParser.DOT)
                self.state = 362
                self.match(CSlangParser.ID)
                self.state = 363
                self.match(CSlangParser.LP)
                self.state = 364
                self.match(CSlangParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 365
                self.match(CSlangParser.NULL)
                pass


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
            self.state = 368
            self.expression()
            self.state = 373
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 369
                self.match(CSlangParser.CM)
                self.state = 370
                self.expression()
                self.state = 375
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

        def block_vardecl(self):
            return self.getTypedRuleContext(CSlangParser.Block_vardeclContext,0)


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
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.block_vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.assign_stmt()
                self.state = 378
                self.match(CSlangParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 380
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 381
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 382
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 383
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 384
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 385
                self.method_stm()
                self.state = 386
                self.match(CSlangParser.SM)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 388
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
        self.enterRule(localctx, 56, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(CSlangParser.LB)
            self.state = 392
            self.member_block()
            self.state = 393
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
        self.enterRule(localctx, 58, self.RULE_member_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SM) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 395
                self.statement()
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_vardeclContext(ParserRuleContext):
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


        def SM(self):
            return self.getToken(CSlangParser.SM, 0)

        def VAR(self):
            return self.getToken(CSlangParser.VAR, 0)

        def CONST(self):
            return self.getToken(CSlangParser.CONST, 0)

        def EQ(self):
            return self.getToken(CSlangParser.EQ, 0)

        def initlist(self):
            return self.getTypedRuleContext(CSlangParser.InitlistContext,0)


        def getRuleIndex(self):
            return CSlangParser.RULE_block_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_vardecl" ):
                return visitor.visitBlock_vardecl(self)
            else:
                return visitor.visitChildren(self)




    def block_vardecl(self):

        localctx = CSlangParser.Block_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 402
                self.attributelist()
                self.state = 403
                self.match(CSlangParser.COLON)
                self.state = 404
                self.mctype()

                self.state = 405
                self.match(CSlangParser.EQ)
                self.state = 406
                self.initlist()
                self.state = 408
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 411
                self.attributelist()
                self.state = 412
                self.match(CSlangParser.COLON)
                self.state = 413
                self.mctype()
                self.state = 414
                self.match(CSlangParser.SM)
                pass


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
        self.enterRule(localctx, 62, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 418
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.state = 419
                self.expression7(0)
                pass


            self.state = 422
            self.match(CSlangParser.ASSIGN)
            self.state = 423
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

        def block_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSlangParser.Block_stmtContext)
            else:
                return self.getTypedRuleContext(CSlangParser.Block_stmtContext,i)


        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


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
        try:
            self.state = 447
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.match(CSlangParser.IF)
                self.state = 426
                self.block_stmt()
                self.state = 427
                self.expression()
                self.state = 428
                self.block_stmt()
                self.state = 429
                self.match(CSlangParser.ELSE)
                self.state = 430
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.match(CSlangParser.IF)
                self.state = 433
                self.block_stmt()
                self.state = 434
                self.expression()
                self.state = 435
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 437
                self.match(CSlangParser.IF)
                self.state = 438
                self.expression()
                self.state = 439
                self.block_stmt()
                self.state = 440
                self.match(CSlangParser.ELSE)
                self.state = 441
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 443
                self.match(CSlangParser.IF)
                self.state = 444
                self.expression()
                self.state = 445
                self.block_stmt()
                pass


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
            self.state = 449
            self.match(CSlangParser.FOR)
            self.state = 450
            self.assign_stmt()
            self.state = 451
            self.match(CSlangParser.SM)
            self.state = 452
            self.expression()
            self.state = 453
            self.match(CSlangParser.SM)
            self.state = 454
            self.assign_stmt()
            self.state = 455
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
            self.state = 457
            self.match(CSlangParser.BREAK)
            self.state = 458
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
            self.state = 460
            self.match(CSlangParser.CONTINUE)
            self.state = 461
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
            self.state = 463
            self.match(CSlangParser.RETURN)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 464
                self.expression()


            self.state = 467
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

        def expression(self):
            return self.getTypedRuleContext(CSlangParser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(CSlangParser.DOT, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

        def LP(self):
            return self.getToken(CSlangParser.LP, 0)

        def list_of_expression(self):
            return self.getTypedRuleContext(CSlangParser.List_of_expressionContext,0)


        def RP(self):
            return self.getToken(CSlangParser.RP, 0)

        def STATIC(self):
            return self.getToken(CSlangParser.STATIC, 0)

        def SELF(self):
            return self.getToken(CSlangParser.SELF, 0)

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
        try:
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.expression()
                self.state = 471
                self.match(CSlangParser.DOT)
                self.state = 472
                self.match(CSlangParser.ID)
                self.state = 473
                self.match(CSlangParser.LP)
                self.state = 474
                self.list_of_expression()
                self.state = 475
                self.match(CSlangParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 477
                self.match(CSlangParser.ID)
                self.state = 478
                self.match(CSlangParser.DOT)
                self.state = 479
                self.match(CSlangParser.STATIC)
                self.state = 480
                self.match(CSlangParser.LP)
                self.state = 481
                self.list_of_expression()
                self.state = 482
                self.match(CSlangParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 484
                self.match(CSlangParser.STATIC)
                self.state = 485
                self.match(CSlangParser.LP)
                self.state = 486
                self.list_of_expression()
                self.state = 487
                self.match(CSlangParser.RP)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 489
                self.expression()
                self.state = 490
                self.match(CSlangParser.DOT)
                self.state = 491
                self.match(CSlangParser.ID)
                self.state = 492
                self.match(CSlangParser.LP)
                self.state = 493
                self.match(CSlangParser.RP)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 495
                self.match(CSlangParser.ID)
                self.state = 496
                self.match(CSlangParser.DOT)
                self.state = 497
                self.match(CSlangParser.STATIC)
                self.state = 498
                self.match(CSlangParser.LP)
                self.state = 499
                self.match(CSlangParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 500
                self.match(CSlangParser.STATIC)
                self.state = 501
                self.match(CSlangParser.LP)
                self.state = 502
                self.match(CSlangParser.RP)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 503
                self.match(CSlangParser.SELF)
                self.state = 504
                self.match(CSlangParser.DOT)
                self.state = 505
                self.match(CSlangParser.ID)
                self.state = 506
                self.match(CSlangParser.LP)
                self.state = 507
                self.list_of_expression()
                self.state = 508
                self.match(CSlangParser.RP)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 510
                self.match(CSlangParser.SELF)
                self.state = 511
                self.match(CSlangParser.DOT)
                self.state = 512
                self.match(CSlangParser.ID)
                self.state = 513
                self.match(CSlangParser.LP)
                self.state = 514
                self.match(CSlangParser.RP)
                pass


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
        self.enterRule(localctx, 76, self.RULE_literal)
        try:
            self.state = 522
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 520
                self.match(CSlangParser.BOOLLIT)
                pass
            elif token in [CSlangParser.OB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 521
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
        self.enterRule(localctx, 78, self.RULE_membername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
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
        self.enterRule(localctx, 80, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(CSlangParser.OB)
            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.NEW) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL))) != 0):
                self.state = 527
                self.elem()
                self.state = 532
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 528
                    self.match(CSlangParser.CM)
                    self.state = 529
                    self.elem()
                    self.state = 534
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 537
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


        def getRuleIndex(self):
            return CSlangParser.RULE_elem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElem" ):
                return visitor.visitElem(self)
            else:
                return visitor.visitChildren(self)




    def elem(self):

        localctx = CSlangParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 542
                self.match(CSlangParser.BOOLLIT)
                pass
            elif token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 5)
                self.state = 543
                self.match(CSlangParser.NEW)
                self.state = 544
                self.match(CSlangParser.ID)
                self.state = 545
                self.match(CSlangParser.LP)
                self.state = 547
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 546
                    self.list_of_expression()


                self.state = 549
                self.match(CSlangParser.RP)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expression2_sempred
        self._predicates[17] = self.expression3_sempred
        self._predicates[18] = self.expression4_sempred
        self._predicates[21] = self.expression7_sempred
        self._predicates[22] = self.expression8_sempred
        self._predicates[23] = self.expression9_sempred
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
         

    def expression9_sempred(self, localctx:Expression9Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 4)
         




