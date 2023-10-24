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
        buf.write("\u01f8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\6\2V\n\2\r\2\16\2W\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\5\3`\n\3\3\3\3\3\5\3d\n\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4t")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u008a\n\6\3\7\3\7\3")
        buf.write("\7\7\7\u008f\n\7\f\7\16\7\u0092\13\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\5\t\u009d\n\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u00a6\n\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\5\f\u00b3\n\f\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\7\17\u00c2\n\17\f")
        buf.write("\17\16\17\u00c5\13\17\3\20\3\20\3\20\3\20\3\20\5\20\u00cc")
        buf.write("\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00d3\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\7\22\u00db\n\22\f\22\16\22\u00de")
        buf.write("\13\22\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00e6\n\23\f")
        buf.write("\23\16\23\u00e9\13\23\3\24\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u00f1\n\24\f\24\16\24\u00f4\13\24\3\25\3\25\3\25\5")
        buf.write("\25\u00f9\n\25\3\26\3\26\3\26\5\26\u00fe\n\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0108\n\27\f\27\16")
        buf.write("\27\u010b\13\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0115\n\30\3\30\5\30\u0118\n\30\7\30\u011a\n\30")
        buf.write("\f\30\16\30\u011d\13\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u0139")
        buf.write("\n\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\7\31\u014a\n\31\f\31\16\31\u014d")
        buf.write("\13\31\3\32\3\32\3\32\3\32\5\32\u0153\n\32\3\32\3\32\5")
        buf.write("\32\u0157\n\32\3\32\5\32\u015a\n\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0166\n\33\3\34\3")
        buf.write("\34\3\34\7\34\u016b\n\34\f\34\16\34\u016e\13\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u017d\n\35\3\36\3\36\3\36\3\36\3\37\7\37\u0184")
        buf.write("\n\37\f\37\16\37\u0187\13\37\3 \3 \5 \u018b\n \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\5!\u01a6\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3%\3%\5%\u01b8\n%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u01de\n&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\5\'\u01e5\n\'\3(\3(\3)\3)\3)\3)\7)")
        buf.write("\u01ed\n)\f)\16)\u01f0\13)\5)\u01f2\n)\3)\3)\3*\3*\3*")
        buf.write("\2\b\"$&,.\60+\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\n\3\2\b\t\5\2\6")
        buf.write("\7\22\2388\3\2).\3\2\'(\3\2!\"\4\2#%\61\61\4\2\3\388\3")
        buf.write("\2\64\67\2\u0217\2U\3\2\2\2\4[\3\2\2\2\6s\3\2\2\2\bu\3")
        buf.write("\2\2\2\n\u0089\3\2\2\2\f\u008b\3\2\2\2\16\u0093\3\2\2")
        buf.write("\2\20\u009a\3\2\2\2\22\u00a5\3\2\2\2\24\u00a7\3\2\2\2")
        buf.write("\26\u00b2\3\2\2\2\30\u00b4\3\2\2\2\32\u00b9\3\2\2\2\34")
        buf.write("\u00be\3\2\2\2\36\u00cb\3\2\2\2 \u00d2\3\2\2\2\"\u00d4")
        buf.write("\3\2\2\2$\u00df\3\2\2\2&\u00ea\3\2\2\2(\u00f8\3\2\2\2")
        buf.write("*\u00fd\3\2\2\2,\u00ff\3\2\2\2.\u010c\3\2\2\2\60\u0138")
        buf.write("\3\2\2\2\62\u0159\3\2\2\2\64\u0165\3\2\2\2\66\u0167\3")
        buf.write("\2\2\28\u017c\3\2\2\2:\u017e\3\2\2\2<\u0185\3\2\2\2>\u018a")
        buf.write("\3\2\2\2@\u01a5\3\2\2\2B\u01a7\3\2\2\2D\u01af\3\2\2\2")
        buf.write("F\u01b2\3\2\2\2H\u01b5\3\2\2\2J\u01dd\3\2\2\2L\u01e4\3")
        buf.write("\2\2\2N\u01e6\3\2\2\2P\u01e8\3\2\2\2R\u01f5\3\2\2\2TV")
        buf.write("\5\4\3\2UT\3\2\2\2VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XY\3\2")
        buf.write("\2\2YZ\7\2\2\3Z\3\3\2\2\2[\\\7\4\2\2\\_\78\2\2]^\7\63")
        buf.write("\2\2^`\78\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ac\7\32\2\2")
        buf.write("bd\5\6\4\2cb\3\2\2\2cd\3\2\2\2de\3\2\2\2ef\7\33\2\2f\5")
        buf.write("\3\2\2\2gt\5\n\6\2ht\5\16\b\2it\5\b\5\2jk\5\n\6\2kl\5")
        buf.write("\6\4\2lt\3\2\2\2mn\5\16\b\2no\5\6\4\2ot\3\2\2\2pq\5\b")
        buf.write("\5\2qr\5\6\4\2rt\3\2\2\2sg\3\2\2\2sh\3\2\2\2si\3\2\2\2")
        buf.write("sj\3\2\2\2sm\3\2\2\2sp\3\2\2\2t\7\3\2\2\2uv\7\n\2\2vw")
        buf.write("\7\f\2\2wx\5\20\t\2xy\5:\36\2y\t\3\2\2\2z{\t\2\2\2{|\5")
        buf.write("\34\17\2|}\7\62\2\2}~\5\26\f\2~\177\7\31\2\2\177\u0080")
        buf.write("\5\f\7\2\u0080\u0081\3\2\2\2\u0081\u0082\7\36\2\2\u0082")
        buf.write("\u008a\3\2\2\2\u0083\u0084\t\2\2\2\u0084\u0085\5\34\17")
        buf.write("\2\u0085\u0086\7\62\2\2\u0086\u0087\5\26\f\2\u0087\u0088")
        buf.write("\7\36\2\2\u0088\u008a\3\2\2\2\u0089z\3\2\2\2\u0089\u0083")
        buf.write("\3\2\2\2\u008a\13\3\2\2\2\u008b\u0090\5\36\20\2\u008c")
        buf.write("\u008d\7\37\2\2\u008d\u008f\5\36\20\2\u008e\u008c\3\2")
        buf.write("\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\r\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094")
        buf.write("\7\n\2\2\u0094\u0095\5N(\2\u0095\u0096\5\20\t\2\u0096")
        buf.write("\u0097\7\62\2\2\u0097\u0098\5\26\f\2\u0098\u0099\5:\36")
        buf.write("\2\u0099\17\3\2\2\2\u009a\u009c\7\34\2\2\u009b\u009d\5")
        buf.write("\22\n\2\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u009e\3\2\2\2\u009e\u009f\7\35\2\2\u009f\21\3\2\2\2\u00a0")
        buf.write("\u00a1\5\24\13\2\u00a1\u00a2\7\37\2\2\u00a2\u00a3\5\22")
        buf.write("\n\2\u00a3\u00a6\3\2\2\2\u00a4\u00a6\5\24\13\2\u00a5\u00a0")
        buf.write("\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\23\3\2\2\2\u00a7\u00a8")
        buf.write("\5\34\17\2\u00a8\u00a9\7\62\2\2\u00a9\u00aa\5\26\f\2\u00aa")
        buf.write("\25\3\2\2\2\u00ab\u00b3\7\6\2\2\u00ac\u00b3\7\7\2\2\u00ad")
        buf.write("\u00b3\7\22\2\2\u00ae\u00b3\7\23\2\2\u00af\u00b3\7\13")
        buf.write("\2\2\u00b0\u00b3\5\30\r\2\u00b1\u00b3\5\32\16\2\u00b2")
        buf.write("\u00ab\3\2\2\2\u00b2\u00ac\3\2\2\2\u00b2\u00ad\3\2\2\2")
        buf.write("\u00b2\u00ae\3\2\2\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\27\3\2\2\2\u00b4\u00b5")
        buf.write("\7\26\2\2\u00b5\u00b6\78\2\2\u00b6\u00b7\7\34\2\2\u00b7")
        buf.write("\u00b8\7\35\2\2\u00b8\31\3\2\2\2\u00b9\u00ba\7\27\2\2")
        buf.write("\u00ba\u00bb\7\65\2\2\u00bb\u00bc\7\30\2\2\u00bc\u00bd")
        buf.write("\t\3\2\2\u00bd\33\3\2\2\2\u00be\u00c3\5N(\2\u00bf\u00c0")
        buf.write("\7\37\2\2\u00c0\u00c2\5N(\2\u00c1\u00bf\3\2\2\2\u00c2")
        buf.write("\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\35\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c6\u00c7\5 \21")
        buf.write("\2\u00c7\u00c8\7\60\2\2\u00c8\u00c9\5 \21\2\u00c9\u00cc")
        buf.write("\3\2\2\2\u00ca\u00cc\5 \21\2\u00cb\u00c6\3\2\2\2\u00cb")
        buf.write("\u00ca\3\2\2\2\u00cc\37\3\2\2\2\u00cd\u00ce\5\"\22\2\u00ce")
        buf.write("\u00cf\t\4\2\2\u00cf\u00d0\5\"\22\2\u00d0\u00d3\3\2\2")
        buf.write("\2\u00d1\u00d3\5\"\22\2\u00d2\u00cd\3\2\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d3!\3\2\2\2\u00d4\u00d5\b\22\1\2\u00d5\u00d6")
        buf.write("\5$\23\2\u00d6\u00dc\3\2\2\2\u00d7\u00d8\f\4\2\2\u00d8")
        buf.write("\u00d9\t\5\2\2\u00d9\u00db\5$\23\2\u00da\u00d7\3\2\2\2")
        buf.write("\u00db\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3")
        buf.write("\2\2\2\u00dd#\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0")
        buf.write("\b\23\1\2\u00e0\u00e1\5&\24\2\u00e1\u00e7\3\2\2\2\u00e2")
        buf.write("\u00e3\f\4\2\2\u00e3\u00e4\t\6\2\2\u00e4\u00e6\5&\24\2")
        buf.write("\u00e5\u00e2\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3")
        buf.write("\2\2\2\u00e7\u00e8\3\2\2\2\u00e8%\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00ea\u00eb\b\24\1\2\u00eb\u00ec\5(\25\2\u00ec")
        buf.write("\u00f2\3\2\2\2\u00ed\u00ee\f\4\2\2\u00ee\u00ef\t\7\2\2")
        buf.write("\u00ef\u00f1\5(\25\2\u00f0\u00ed\3\2\2\2\u00f1\u00f4\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\'")
        buf.write("\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\7&\2\2\u00f6")
        buf.write("\u00f9\5(\25\2\u00f7\u00f9\5*\26\2\u00f8\u00f5\3\2\2\2")
        buf.write("\u00f8\u00f7\3\2\2\2\u00f9)\3\2\2\2\u00fa\u00fb\7\"\2")
        buf.write("\2\u00fb\u00fe\5*\26\2\u00fc\u00fe\5,\27\2\u00fd\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe+\3\2\2\2\u00ff\u0100")
        buf.write("\b\27\1\2\u0100\u0101\5.\30\2\u0101\u0109\3\2\2\2\u0102")
        buf.write("\u0103\f\4\2\2\u0103\u0104\7\27\2\2\u0104\u0105\5\36\20")
        buf.write("\2\u0105\u0106\7\30\2\2\u0106\u0108\3\2\2\2\u0107\u0102")
        buf.write("\3\2\2\2\u0108\u010b\3\2\2\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a-\3\2\2\2\u010b\u0109\3\2\2\2\u010c")
        buf.write("\u010d\b\30\1\2\u010d\u010e\5\60\31\2\u010e\u011b\3\2")
        buf.write("\2\2\u010f\u0110\f\4\2\2\u0110\u0111\7 \2\2\u0111\u0117")
        buf.write("\78\2\2\u0112\u0114\7\34\2\2\u0113\u0115\5\66\34\2\u0114")
        buf.write("\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0118\7\35\2\2\u0117\u0112\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118\u011a\3\2\2\2\u0119\u010f\3\2\2\2\u011a")
        buf.write("\u011d\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c/\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\b\31\1")
        buf.write("\2\u011f\u0120\78\2\2\u0120\u0121\7 \2\2\u0121\u0139\7")
        buf.write("\3\2\2\u0122\u0139\7\3\2\2\u0123\u0124\78\2\2\u0124\u0125")
        buf.write("\7 \2\2\u0125\u0126\7\3\2\2\u0126\u0127\7\34\2\2\u0127")
        buf.write("\u0128\5\66\34\2\u0128\u0129\7\35\2\2\u0129\u0139\3\2")
        buf.write("\2\2\u012a\u012b\7\3\2\2\u012b\u012c\7\34\2\2\u012c\u012d")
        buf.write("\5\66\34\2\u012d\u012e\7\35\2\2\u012e\u0139\3\2\2\2\u012f")
        buf.write("\u0130\78\2\2\u0130\u0131\7 \2\2\u0131\u0132\7\3\2\2\u0132")
        buf.write("\u0133\7\34\2\2\u0133\u0139\7\35\2\2\u0134\u0135\7\3\2")
        buf.write("\2\u0135\u0136\7\34\2\2\u0136\u0139\7\35\2\2\u0137\u0139")
        buf.write("\5\62\32\2\u0138\u011e\3\2\2\2\u0138\u0122\3\2\2\2\u0138")
        buf.write("\u0123\3\2\2\2\u0138\u012a\3\2\2\2\u0138\u012f\3\2\2\2")
        buf.write("\u0138\u0134\3\2\2\2\u0138\u0137\3\2\2\2\u0139\u014b\3")
        buf.write("\2\2\2\u013a\u013b\f\f\2\2\u013b\u013c\7 \2\2\u013c\u014a")
        buf.write("\78\2\2\u013d\u013e\f\t\2\2\u013e\u013f\7 \2\2\u013f\u0140")
        buf.write("\78\2\2\u0140\u0141\7\34\2\2\u0141\u0142\5\66\34\2\u0142")
        buf.write("\u0143\7\35\2\2\u0143\u014a\3\2\2\2\u0144\u0145\f\6\2")
        buf.write("\2\u0145\u0146\7 \2\2\u0146\u0147\78\2\2\u0147\u0148\7")
        buf.write("\34\2\2\u0148\u014a\7\35\2\2\u0149\u013a\3\2\2\2\u0149")
        buf.write("\u013d\3\2\2\2\u0149\u0144\3\2\2\2\u014a\u014d\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\61\3\2")
        buf.write("\2\2\u014d\u014b\3\2\2\2\u014e\u014f\7\26\2\2\u014f\u0150")
        buf.write("\78\2\2\u0150\u0152\7\34\2\2\u0151\u0153\5\66\34\2\u0152")
        buf.write("\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0154\3\2\2\2")
        buf.write("\u0154\u0156\7\35\2\2\u0155\u0157\5\62\32\2\u0156\u0155")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u015a\3\2\2\2\u0158")
        buf.write("\u015a\5\64\33\2\u0159\u014e\3\2\2\2\u0159\u0158\3\2\2")
        buf.write("\2\u015a\63\3\2\2\2\u015b\u015c\7\34\2\2\u015c\u015d\5")
        buf.write("\36\20\2\u015d\u015e\7\35\2\2\u015e\u0166\3\2\2\2\u015f")
        buf.write("\u0166\78\2\2\u0160\u0166\5L\'\2\u0161\u0162\7\25\2\2")
        buf.write("\u0162\u0163\7 \2\2\u0163\u0166\78\2\2\u0164\u0166\7\24")
        buf.write("\2\2\u0165\u015b\3\2\2\2\u0165\u015f\3\2\2\2\u0165\u0160")
        buf.write("\3\2\2\2\u0165\u0161\3\2\2\2\u0165\u0164\3\2\2\2\u0166")
        buf.write("\65\3\2\2\2\u0167\u016c\5\36\20\2\u0168\u0169\7\37\2\2")
        buf.write("\u0169\u016b\5\36\20\2\u016a\u0168\3\2\2\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\67\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u017d\5\n\6\2\u0170")
        buf.write("\u0171\5> \2\u0171\u0172\7\36\2\2\u0172\u017d\3\2\2\2")
        buf.write("\u0173\u017d\5@!\2\u0174\u017d\5B\"\2\u0175\u017d\5D#")
        buf.write("\2\u0176\u017d\5F$\2\u0177\u017d\5H%\2\u0178\u0179\5J")
        buf.write("&\2\u0179\u017a\7\36\2\2\u017a\u017d\3\2\2\2\u017b\u017d")
        buf.write("\5:\36\2\u017c\u016f\3\2\2\2\u017c\u0170\3\2\2\2\u017c")
        buf.write("\u0173\3\2\2\2\u017c\u0174\3\2\2\2\u017c\u0175\3\2\2\2")
        buf.write("\u017c\u0176\3\2\2\2\u017c\u0177\3\2\2\2\u017c\u0178\3")
        buf.write("\2\2\2\u017c\u017b\3\2\2\2\u017d9\3\2\2\2\u017e\u017f")
        buf.write("\7\32\2\2\u017f\u0180\5<\37\2\u0180\u0181\7\33\2\2\u0181")
        buf.write(";\3\2\2\2\u0182\u0184\58\35\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186=\3\2\2\2\u0187\u0185\3\2\2\2\u0188\u018b\78\2\2")
        buf.write("\u0189\u018b\5,\27\2\u018a\u0188\3\2\2\2\u018a\u0189\3")
        buf.write("\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d\7/\2\2\u018d\u018e")
        buf.write("\5\36\20\2\u018e?\3\2\2\2\u018f\u0190\7\17\2\2\u0190\u0191")
        buf.write("\5:\36\2\u0191\u0192\5\36\20\2\u0192\u0193\5:\36\2\u0193")
        buf.write("\u0194\7\20\2\2\u0194\u0195\5:\36\2\u0195\u01a6\3\2\2")
        buf.write("\2\u0196\u0197\7\17\2\2\u0197\u0198\5:\36\2\u0198\u0199")
        buf.write("\5\36\20\2\u0199\u019a\5:\36\2\u019a\u01a6\3\2\2\2\u019b")
        buf.write("\u019c\7\17\2\2\u019c\u019d\5\36\20\2\u019d\u019e\5:\36")
        buf.write("\2\u019e\u019f\7\20\2\2\u019f\u01a0\5:\36\2\u01a0\u01a6")
        buf.write("\3\2\2\2\u01a1\u01a2\7\17\2\2\u01a2\u01a3\5\36\20\2\u01a3")
        buf.write("\u01a4\5:\36\2\u01a4\u01a6\3\2\2\2\u01a5\u018f\3\2\2\2")
        buf.write("\u01a5\u0196\3\2\2\2\u01a5\u019b\3\2\2\2\u01a5\u01a1\3")
        buf.write("\2\2\2\u01a6A\3\2\2\2\u01a7\u01a8\7\21\2\2\u01a8\u01a9")
        buf.write("\5> \2\u01a9\u01aa\7\36\2\2\u01aa\u01ab\5\36\20\2\u01ab")
        buf.write("\u01ac\7\36\2\2\u01ac\u01ad\5> \2\u01ad\u01ae\5:\36\2")
        buf.write("\u01aeC\3\2\2\2\u01af\u01b0\7\r\2\2\u01b0\u01b1\7\36\2")
        buf.write("\2\u01b1E\3\2\2\2\u01b2\u01b3\7\16\2\2\u01b3\u01b4\7\36")
        buf.write("\2\2\u01b4G\3\2\2\2\u01b5\u01b7\7\5\2\2\u01b6\u01b8\5")
        buf.write("\36\20\2\u01b7\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\7\36\2\2\u01baI\3\2\2\2\u01bb")
        buf.write("\u01de\3\2\2\2\u01bc\u01bd\5\36\20\2\u01bd\u01be\7 \2")
        buf.write("\2\u01be\u01bf\78\2\2\u01bf\u01c0\7\34\2\2\u01c0\u01c1")
        buf.write("\5\66\34\2\u01c1\u01c2\7\35\2\2\u01c2\u01de\3\2\2\2\u01c3")
        buf.write("\u01c4\78\2\2\u01c4\u01c5\7 \2\2\u01c5\u01c6\7\3\2\2\u01c6")
        buf.write("\u01c7\7\34\2\2\u01c7\u01c8\5\66\34\2\u01c8\u01c9\7\35")
        buf.write("\2\2\u01c9\u01de\3\2\2\2\u01ca\u01cb\7\3\2\2\u01cb\u01cc")
        buf.write("\7\34\2\2\u01cc\u01cd\5\66\34\2\u01cd\u01ce\7\35\2\2\u01ce")
        buf.write("\u01de\3\2\2\2\u01cf\u01d0\5\36\20\2\u01d0\u01d1\7 \2")
        buf.write("\2\u01d1\u01d2\78\2\2\u01d2\u01d3\7\34\2\2\u01d3\u01d4")
        buf.write("\7\35\2\2\u01d4\u01de\3\2\2\2\u01d5\u01d6\78\2\2\u01d6")
        buf.write("\u01d7\7 \2\2\u01d7\u01d8\7\3\2\2\u01d8\u01d9\7\34\2\2")
        buf.write("\u01d9\u01de\7\35\2\2\u01da\u01db\7\3\2\2\u01db\u01dc")
        buf.write("\7\34\2\2\u01dc\u01de\7\35\2\2\u01dd\u01bb\3\2\2\2\u01dd")
        buf.write("\u01bc\3\2\2\2\u01dd\u01c3\3\2\2\2\u01dd\u01ca\3\2\2\2")
        buf.write("\u01dd\u01cf\3\2\2\2\u01dd\u01d5\3\2\2\2\u01dd\u01da\3")
        buf.write("\2\2\2\u01deK\3\2\2\2\u01df\u01e5\7\65\2\2\u01e0\u01e5")
        buf.write("\7\64\2\2\u01e1\u01e5\7\67\2\2\u01e2\u01e5\7\66\2\2\u01e3")
        buf.write("\u01e5\5P)\2\u01e4\u01df\3\2\2\2\u01e4\u01e0\3\2\2\2\u01e4")
        buf.write("\u01e1\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e3\3\2\2\2")
        buf.write("\u01e5M\3\2\2\2\u01e6\u01e7\t\b\2\2\u01e7O\3\2\2\2\u01e8")
        buf.write("\u01f1\7\27\2\2\u01e9\u01ee\5R*\2\u01ea\u01eb\7\37\2\2")
        buf.write("\u01eb\u01ed\5R*\2\u01ec\u01ea\3\2\2\2\u01ed\u01f0\3\2")
        buf.write("\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f2")
        buf.write("\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01e9\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\7\30\2")
        buf.write("\2\u01f4Q\3\2\2\2\u01f5\u01f6\t\t\2\2\u01f6S\3\2\2\2(")
        buf.write("W_cs\u0089\u0090\u009c\u00a5\u00b2\u00c3\u00cb\u00d2\u00dc")
        buf.write("\u00e7\u00f2\u00f8\u00fd\u0109\u0114\u0117\u011b\u0138")
        buf.write("\u0149\u014b\u0152\u0156\u0159\u0165\u016c\u017c\u0185")
        buf.write("\u018a\u01a5\u01b7\u01dd\u01e4\u01ee\u01f1")
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
    RULE_assign_stmt = 30
    RULE_if_stmt = 31
    RULE_for_stmt = 32
    RULE_break_stmt = 33
    RULE_continue_stmt = 34
    RULE_return_stmt = 35
    RULE_method_stm = 36
    RULE_literal = 37
    RULE_membername = 38
    RULE_array_literal = 39
    RULE_elem = 40

    ruleNames =  [ "program", "classdecl", "classmember", "construcdecl", 
                   "attributedecl", "initlist", "methoddecl", "paramdecl", 
                   "paramlist", "param", "mctype", "classtype", "array_type", 
                   "attributelist", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "expression8", "expression9", "expression10", 
                   "operands", "list_of_expression", "statement", "block_stmt", 
                   "member_block", "assign_stmt", "if_stmt", "for_stmt", 
                   "break_stmt", "continue_stmt", "return_stmt", "method_stm", 
                   "literal", "membername", "array_literal", "elem" ]

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
            self.state = 83 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.classdecl()
                self.state = 85 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 87
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
            self.state = 89
            self.match(CSlangParser.CLASS)
            self.state = 90
            self.match(CSlangParser.ID)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EXTENDS:
                self.state = 91
                self.match(CSlangParser.EXTENDS)
                self.state = 92
                self.match(CSlangParser.ID)


            self.state = 95
            self.match(CSlangParser.LB)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 96
                self.classmember()


            self.state = 99
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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.construcdecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 104
                self.attributedecl()
                self.state = 105
                self.classmember()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 107
                self.methoddecl()
                self.state = 108
                self.classmember()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 110
                self.construcdecl()
                self.state = 111
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
            self.state = 115
            self.match(CSlangParser.FUNC)
            self.state = 116
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 117
            self.paramdecl()
            self.state = 118
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
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 121
                self.attributelist()
                self.state = 122
                self.match(CSlangParser.COLON)
                self.state = 123
                self.mctype()

                self.state = 124
                self.match(CSlangParser.EQ)
                self.state = 125
                self.initlist()
                self.state = 127
                self.match(CSlangParser.SM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                _la = self._input.LA(1)
                if not(_la==CSlangParser.CONST or _la==CSlangParser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 130
                self.attributelist()
                self.state = 131
                self.match(CSlangParser.COLON)
                self.state = 132
                self.mctype()
                self.state = 133
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
            self.state = 137
            self.expression()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 138
                self.match(CSlangParser.CM)
                self.state = 139
                self.expression()
                self.state = 144
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
            self.state = 145
            self.match(CSlangParser.FUNC)
            self.state = 146
            self.membername()
            self.state = 147
            self.paramdecl()
            self.state = 148
            self.match(CSlangParser.COLON)
            self.state = 149
            self.mctype()
            self.state = 150
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
            self.state = 152
            self.match(CSlangParser.LP)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.STATIC or _la==CSlangParser.ID:
                self.state = 153
                self.paramlist()


            self.state = 156
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
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.param()
                self.state = 159
                self.match(CSlangParser.CM)
                self.state = 160
                self.paramlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
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
            self.state = 165
            self.attributelist()
            self.state = 166
            self.match(CSlangParser.COLON)
            self.state = 167
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
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 172
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 173
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 6)
                self.state = 174
                self.classtype()
                pass
            elif token in [CSlangParser.OB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 175
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

        def NEW(self):
            return self.getToken(CSlangParser.NEW, 0)

        def ID(self):
            return self.getToken(CSlangParser.ID, 0)

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
        self.enterRule(localctx, 22, self.RULE_classtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(CSlangParser.NEW)
            self.state = 179
            self.match(CSlangParser.ID)
            self.state = 180
            self.match(CSlangParser.LP)
            self.state = 181
            self.match(CSlangParser.RP)
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
            self.state = 183
            self.match(CSlangParser.OB)
            self.state = 184
            self.match(CSlangParser.INTLIT)
            self.state = 185
            self.match(CSlangParser.CB)
            self.state = 186
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
            self.state = 188
            self.membername()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 189
                self.match(CSlangParser.CM)
                self.state = 190
                self.membername()
                self.state = 195
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
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.expression1()
                self.state = 197
                self.match(CSlangParser.CONCATENATION)
                self.state = 198
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
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
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.expression2(0)
                self.state = 204
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.NOTEQUAL) | (1 << CSlangParser.LESS) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.LESSEQUAL) | (1 << CSlangParser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 205
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
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
            self.state = 211
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 218
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 213
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 214
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.OR or _la==CSlangParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 215
                    self.expression3(0) 
                self.state = 220
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
            self.state = 222
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 224
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 225
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 226
                    self.expression4(0) 
                self.state = 231
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
            self.state = 233
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 240
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 235
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 236
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.DIV) | (1 << CSlangParser.BS) | (1 << CSlangParser.MOD) | (1 << CSlangParser.MUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 237
                    self.expression5() 
                self.state = 242
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
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(CSlangParser.NOT)
                self.state = 244
                self.expression5()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.SUB, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(CSlangParser.SUB)
                self.state = 249
                self.expression6()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
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
            self.state = 254
            self.expression8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                    self.state = 256
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 257
                    self.match(CSlangParser.OB)
                    self.state = 258
                    self.expression()
                    self.state = 259
                    self.match(CSlangParser.CB) 
                self.state = 265
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
            self.state = 267
            self.expression9(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 281
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 269
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 270
                    self.match(CSlangParser.DOT)
                    self.state = 271
                    self.match(CSlangParser.ID)
                    self.state = 277
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        self.state = 272
                        self.match(CSlangParser.LP)
                        self.state = 274
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                            self.state = 273
                            self.list_of_expression()


                        self.state = 276
                        self.match(CSlangParser.RP)

             
                self.state = 283
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
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 285
                self.match(CSlangParser.ID)
                self.state = 286
                self.match(CSlangParser.DOT)
                self.state = 287
                self.match(CSlangParser.STATIC)
                pass

            elif la_ == 2:
                self.state = 288
                self.match(CSlangParser.STATIC)
                pass

            elif la_ == 3:
                self.state = 289
                self.match(CSlangParser.ID)
                self.state = 290
                self.match(CSlangParser.DOT)
                self.state = 291
                self.match(CSlangParser.STATIC)
                self.state = 292
                self.match(CSlangParser.LP)
                self.state = 293
                self.list_of_expression()
                self.state = 294
                self.match(CSlangParser.RP)
                pass

            elif la_ == 4:
                self.state = 296
                self.match(CSlangParser.STATIC)
                self.state = 297
                self.match(CSlangParser.LP)
                self.state = 298
                self.list_of_expression()
                self.state = 299
                self.match(CSlangParser.RP)
                pass

            elif la_ == 5:
                self.state = 301
                self.match(CSlangParser.ID)
                self.state = 302
                self.match(CSlangParser.DOT)
                self.state = 303
                self.match(CSlangParser.STATIC)
                self.state = 304
                self.match(CSlangParser.LP)
                self.state = 305
                self.match(CSlangParser.RP)
                pass

            elif la_ == 6:
                self.state = 306
                self.match(CSlangParser.STATIC)
                self.state = 307
                self.match(CSlangParser.LP)
                self.state = 308
                self.match(CSlangParser.RP)
                pass

            elif la_ == 7:
                self.state = 309
                self.expression10()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 327
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                    if la_ == 1:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 312
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 313
                        self.match(CSlangParser.DOT)
                        self.state = 314
                        self.match(CSlangParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 315
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 316
                        self.match(CSlangParser.DOT)
                        self.state = 317
                        self.match(CSlangParser.ID)
                        self.state = 318
                        self.match(CSlangParser.LP)
                        self.state = 319
                        self.list_of_expression()
                        self.state = 320
                        self.match(CSlangParser.RP)
                        pass

                    elif la_ == 3:
                        localctx = CSlangParser.Expression9Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression9)
                        self.state = 322
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 323
                        self.match(CSlangParser.DOT)
                        self.state = 324
                        self.match(CSlangParser.ID)
                        self.state = 325
                        self.match(CSlangParser.LP)
                        self.state = 326
                        self.match(CSlangParser.RP)
                        pass

             
                self.state = 331
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
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(CSlangParser.NEW)
                self.state = 333
                self.match(CSlangParser.ID)
                self.state = 334
                self.match(CSlangParser.LP)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 335
                    self.list_of_expression()


                self.state = 338
                self.match(CSlangParser.RP)
                self.state = 340
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                if la_ == 1:
                    self.state = 339
                    self.expression10()


                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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
        self.enterRule(localctx, 50, self.RULE_operands)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(CSlangParser.LP)
                self.state = 346
                self.expression()
                self.state = 347
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.OB, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.match(CSlangParser.SELF)
                self.state = 352
                self.match(CSlangParser.DOT)
                self.state = 353
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 354
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
            self.state = 357
            self.expression()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 358
                self.match(CSlangParser.CM)
                self.state = 359
                self.expression()
                self.state = 364
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
        self.enterRule(localctx, 54, self.RULE_statement)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.assign_stmt()
                self.state = 367
                self.match(CSlangParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 369
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 370
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 371
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 372
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 373
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 374
                self.method_stm()
                self.state = 375
                self.match(CSlangParser.SM)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 377
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
            self.state = 380
            self.match(CSlangParser.LB)
            self.state = 381
            self.member_block()
            self.state = 382
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
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SM) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 384
                self.statement()
                self.state = 389
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
        self.enterRule(localctx, 60, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 390
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.state = 391
                self.expression7(0)
                pass


            self.state = 394
            self.match(CSlangParser.ASSIGN)
            self.state = 395
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
        self.enterRule(localctx, 62, self.RULE_if_stmt)
        try:
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(CSlangParser.IF)
                self.state = 398
                self.block_stmt()
                self.state = 399
                self.expression()
                self.state = 400
                self.block_stmt()
                self.state = 401
                self.match(CSlangParser.ELSE)
                self.state = 402
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(CSlangParser.IF)
                self.state = 405
                self.block_stmt()
                self.state = 406
                self.expression()
                self.state = 407
                self.block_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 409
                self.match(CSlangParser.IF)
                self.state = 410
                self.expression()
                self.state = 411
                self.block_stmt()
                self.state = 412
                self.match(CSlangParser.ELSE)
                self.state = 413
                self.block_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 415
                self.match(CSlangParser.IF)
                self.state = 416
                self.expression()
                self.state = 417
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
        self.enterRule(localctx, 64, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(CSlangParser.FOR)
            self.state = 422
            self.assign_stmt()
            self.state = 423
            self.match(CSlangParser.SM)
            self.state = 424
            self.expression()
            self.state = 425
            self.match(CSlangParser.SM)
            self.state = 426
            self.assign_stmt()
            self.state = 427
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
        self.enterRule(localctx, 66, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(CSlangParser.BREAK)
            self.state = 430
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
        self.enterRule(localctx, 68, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(CSlangParser.CONTINUE)
            self.state = 433
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
        self.enterRule(localctx, 70, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(CSlangParser.RETURN)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 436
                self.expression()


            self.state = 439
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

        def getRuleIndex(self):
            return CSlangParser.RULE_method_stm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_stm" ):
                return visitor.visitMethod_stm(self)
            else:
                return visitor.visitChildren(self)




    def method_stm(self):

        localctx = CSlangParser.Method_stmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_method_stm)
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.expression()
                self.state = 443
                self.match(CSlangParser.DOT)
                self.state = 444
                self.match(CSlangParser.ID)
                self.state = 445
                self.match(CSlangParser.LP)
                self.state = 446
                self.list_of_expression()
                self.state = 447
                self.match(CSlangParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
                self.match(CSlangParser.ID)
                self.state = 450
                self.match(CSlangParser.DOT)
                self.state = 451
                self.match(CSlangParser.STATIC)
                self.state = 452
                self.match(CSlangParser.LP)
                self.state = 453
                self.list_of_expression()
                self.state = 454
                self.match(CSlangParser.RP)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 456
                self.match(CSlangParser.STATIC)
                self.state = 457
                self.match(CSlangParser.LP)
                self.state = 458
                self.list_of_expression()
                self.state = 459
                self.match(CSlangParser.RP)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 461
                self.expression()
                self.state = 462
                self.match(CSlangParser.DOT)
                self.state = 463
                self.match(CSlangParser.ID)
                self.state = 464
                self.match(CSlangParser.LP)
                self.state = 465
                self.match(CSlangParser.RP)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 467
                self.match(CSlangParser.ID)
                self.state = 468
                self.match(CSlangParser.DOT)
                self.state = 469
                self.match(CSlangParser.STATIC)
                self.state = 470
                self.match(CSlangParser.LP)
                self.state = 471
                self.match(CSlangParser.RP)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 472
                self.match(CSlangParser.STATIC)
                self.state = 473
                self.match(CSlangParser.LP)
                self.state = 474
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
        self.enterRule(localctx, 74, self.RULE_literal)
        try:
            self.state = 482
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 478
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 479
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 480
                self.match(CSlangParser.BOOLLIT)
                pass
            elif token in [CSlangParser.OB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 481
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
        self.enterRule(localctx, 76, self.RULE_membername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
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
        self.enterRule(localctx, 78, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(CSlangParser.OB)
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL))) != 0):
                self.state = 487
                self.elem()
                self.state = 492
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 488
                    self.match(CSlangParser.CM)
                    self.state = 489
                    self.elem()
                    self.state = 494
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 497
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
        self.enterRule(localctx, 80, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
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
         




