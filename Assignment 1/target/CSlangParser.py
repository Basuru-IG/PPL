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
        buf.write("\u01d5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\6\2f\n\2\r\2\16")
        buf.write("\2g\3\2\3\2\3\3\3\3\3\3\5\3o\n\3\3\3\3\3\7\3s\n\3\f\3")
        buf.write("\16\3v\13\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\5\6\u0085\n\6\3\7\3\7\5\7\u0089\n\7\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\n\3\n\5\n\u0093\n\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00a7\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\5\16\u00b2\n\16\3\16\3\16\3\17\3\17\3\17\7\17\u00b9")
        buf.write("\n\17\f\17\16\17\u00bc\13\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\5\21\u00c9\n\21\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\7\25\u00da\n\25\f\25\16\25\u00dd\13\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\5\26\u00e4\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\5\27\u00eb\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u00f3\n\30\f\30\16\30\u00f6\13\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\7\31\u00fe\n\31\f\31\16\31\u0101")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0109\n\32\f")
        buf.write("\32\16\32\u010c\13\32\3\33\3\33\3\33\5\33\u0111\n\33\3")
        buf.write("\34\3\34\3\34\5\34\u0116\n\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\7\35\u0120\n\35\f\35\16\35\u0123\13\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\5\36\u012d\n")
        buf.write("\36\3\36\5\36\u0130\n\36\7\36\u0132\n\36\f\36\16\36\u0135")
        buf.write("\13\36\3\37\3\37\5\37\u0139\n\37\3\37\3\37\3\37\5\37\u013e")
        buf.write("\n\37\3\37\5\37\u0141\n\37\3\37\5\37\u0144\n\37\3 \3 ")
        buf.write("\3 \3 \5 \u014a\n \3 \3 \5 \u014e\n \3 \5 \u0151\n \3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u015d\n!\3\"\3\"\3\"\7")
        buf.write("\"\u0162\n\"\f\"\16\"\u0165\13\"\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\5#\u0172\n#\3$\3$\3$\3$\3%\7%\u0179\n%\f")
        buf.write("%\16%\u017c\13%\3&\3&\5&\u0180\n&\3&\3&\3&\3\'\3\'\5\'")
        buf.write("\u0187\n\'\3\'\3\'\3\'\3\'\5\'\u018d\n\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\5+\u019f\n+\3+\3+\3")
        buf.write(",\3,\5,\u01a5\n,\3,\3,\3-\3-\3-\3-\3-\5-\u01ae\n-\3-\3")
        buf.write("-\3.\3.\5.\u01b4\n.\3.\3.\3.\5.\u01b9\n.\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\5/\u01c2\n/\3\60\3\60\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u01ca\n\61\f\61\16\61\u01cd\13\61\5\61\u01cf\n\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\2\7.\60\628:\63\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJL")
        buf.write("NPRTVXZ\\^`b\2\t\5\2\6\7\22\2388\3\2).\3\2\'(\3\2!\"\4")
        buf.write("\2#%\61\61\4\2\3\388\3\2\64\67\2\u01e2\2e\3\2\2\2\4k\3")
        buf.write("\2\2\2\6y\3\2\2\2\b|\3\2\2\2\n\u0084\3\2\2\2\f\u0088\3")
        buf.write("\2\2\2\16\u008a\3\2\2\2\20\u008d\3\2\2\2\22\u0092\3\2")
        buf.write("\2\2\24\u0096\3\2\2\2\26\u00a6\3\2\2\2\30\u00a8\3\2\2")
        buf.write("\2\32\u00af\3\2\2\2\34\u00b5\3\2\2\2\36\u00bd\3\2\2\2")
        buf.write(" \u00c8\3\2\2\2\"\u00ca\3\2\2\2$\u00cf\3\2\2\2&\u00d1")
        buf.write("\3\2\2\2(\u00d6\3\2\2\2*\u00e3\3\2\2\2,\u00ea\3\2\2\2")
        buf.write(".\u00ec\3\2\2\2\60\u00f7\3\2\2\2\62\u0102\3\2\2\2\64\u0110")
        buf.write("\3\2\2\2\66\u0115\3\2\2\28\u0117\3\2\2\2:\u0124\3\2\2")
        buf.write("\2<\u0143\3\2\2\2>\u0150\3\2\2\2@\u015c\3\2\2\2B\u015e")
        buf.write("\3\2\2\2D\u0171\3\2\2\2F\u0173\3\2\2\2H\u017a\3\2\2\2")
        buf.write("J\u017f\3\2\2\2L\u0184\3\2\2\2N\u018e\3\2\2\2P\u0196\3")
        buf.write("\2\2\2R\u0199\3\2\2\2T\u019c\3\2\2\2V\u01a4\3\2\2\2X\u01a8")
        buf.write("\3\2\2\2Z\u01b3\3\2\2\2\\\u01c1\3\2\2\2^\u01c3\3\2\2\2")
        buf.write("`\u01c5\3\2\2\2b\u01d2\3\2\2\2df\5\4\3\2ed\3\2\2\2fg\3")
        buf.write("\2\2\2ge\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\2\2\3j\3\3\2")
        buf.write("\2\2kl\7\4\2\2ln\5$\23\2mo\5\6\4\2nm\3\2\2\2no\3\2\2\2")
        buf.write("op\3\2\2\2pt\7\32\2\2qs\5\n\6\2rq\3\2\2\2sv\3\2\2\2tr")
        buf.write("\3\2\2\2tu\3\2\2\2uw\3\2\2\2vt\3\2\2\2wx\7\33\2\2x\5\3")
        buf.write("\2\2\2yz\7\63\2\2z{\5$\23\2{\7\3\2\2\2|}\7\n\2\2}~\7\f")
        buf.write("\2\2~\177\5\32\16\2\177\u0080\5F$\2\u0080\t\3\2\2\2\u0081")
        buf.write("\u0085\5\f\7\2\u0082\u0085\5\30\r\2\u0083\u0085\5\b\5")
        buf.write("\2\u0084\u0081\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\13\3\2\2\2\u0086\u0089\5\16\b\2\u0087\u0089")
        buf.write("\5\20\t\2\u0088\u0086\3\2\2\2\u0088\u0087\3\2\2\2\u0089")
        buf.write("\r\3\2\2\2\u008a\u008b\7\t\2\2\u008b\u008c\5\22\n\2\u008c")
        buf.write("\17\3\2\2\2\u008d\u008e\7\b\2\2\u008e\u008f\5\22\n\2\u008f")
        buf.write("\21\3\2\2\2\u0090\u0093\5\24\13\2\u0091\u0093\5\26\f\2")
        buf.write("\u0092\u0090\3\2\2\2\u0092\u0091\3\2\2\2\u0093\u0094\3")
        buf.write("\2\2\2\u0094\u0095\7\36\2\2\u0095\23\3\2\2\2\u0096\u0097")
        buf.write("\5(\25\2\u0097\u0098\7\62\2\2\u0098\u0099\5 \21\2\u0099")
        buf.write("\25\3\2\2\2\u009a\u009b\5^\60\2\u009b\u009c\7\37\2\2\u009c")
        buf.write("\u009d\5\26\f\2\u009d\u009e\7\37\2\2\u009e\u009f\5*\26")
        buf.write("\2\u009f\u00a7\3\2\2\2\u00a0\u00a1\5^\60\2\u00a1\u00a2")
        buf.write("\7\62\2\2\u00a2\u00a3\5 \21\2\u00a3\u00a4\7\31\2\2\u00a4")
        buf.write("\u00a5\5*\26\2\u00a5\u00a7\3\2\2\2\u00a6\u009a\3\2\2\2")
        buf.write("\u00a6\u00a0\3\2\2\2\u00a7\27\3\2\2\2\u00a8\u00a9\7\n")
        buf.write("\2\2\u00a9\u00aa\5^\60\2\u00aa\u00ab\5\32\16\2\u00ab\u00ac")
        buf.write("\7\62\2\2\u00ac\u00ad\5 \21\2\u00ad\u00ae\5F$\2\u00ae")
        buf.write("\31\3\2\2\2\u00af\u00b1\7\34\2\2\u00b0\u00b2\5\34\17\2")
        buf.write("\u00b1\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3")
        buf.write("\2\2\2\u00b3\u00b4\7\35\2\2\u00b4\33\3\2\2\2\u00b5\u00ba")
        buf.write("\5\36\20\2\u00b6\u00b7\7\37\2\2\u00b7\u00b9\5\36\20\2")
        buf.write("\u00b8\u00b6\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3")
        buf.write("\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\35\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00be\5(\25\2\u00be\u00bf\7\62\2\2\u00bf")
        buf.write("\u00c0\5 \21\2\u00c0\37\3\2\2\2\u00c1\u00c9\7\6\2\2\u00c2")
        buf.write("\u00c9\7\7\2\2\u00c3\u00c9\7\22\2\2\u00c4\u00c9\7\23\2")
        buf.write("\2\u00c5\u00c9\7\13\2\2\u00c6\u00c9\5\"\22\2\u00c7\u00c9")
        buf.write("\5&\24\2\u00c8\u00c1\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c8")
        buf.write("\u00c3\3\2\2\2\u00c8\u00c4\3\2\2\2\u00c8\u00c5\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9!\3\2\2")
        buf.write("\2\u00ca\u00cb\7\26\2\2\u00cb\u00cc\5$\23\2\u00cc\u00cd")
        buf.write("\7\34\2\2\u00cd\u00ce\7\35\2\2\u00ce#\3\2\2\2\u00cf\u00d0")
        buf.write("\78\2\2\u00d0%\3\2\2\2\u00d1\u00d2\7\27\2\2\u00d2\u00d3")
        buf.write("\7\65\2\2\u00d3\u00d4\7\30\2\2\u00d4\u00d5\t\2\2\2\u00d5")
        buf.write("\'\3\2\2\2\u00d6\u00db\5^\60\2\u00d7\u00d8\7\37\2\2\u00d8")
        buf.write("\u00da\5^\60\2\u00d9\u00d7\3\2\2\2\u00da\u00dd\3\2\2\2")
        buf.write("\u00db\u00d9\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc)\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00de\u00df\5,\27\2\u00df\u00e0")
        buf.write("\7\60\2\2\u00e0\u00e1\5,\27\2\u00e1\u00e4\3\2\2\2\u00e2")
        buf.write("\u00e4\5,\27\2\u00e3\u00de\3\2\2\2\u00e3\u00e2\3\2\2\2")
        buf.write("\u00e4+\3\2\2\2\u00e5\u00e6\5.\30\2\u00e6\u00e7\t\3\2")
        buf.write("\2\u00e7\u00e8\5.\30\2\u00e8\u00eb\3\2\2\2\u00e9\u00eb")
        buf.write("\5.\30\2\u00ea\u00e5\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write("-\3\2\2\2\u00ec\u00ed\b\30\1\2\u00ed\u00ee\5\60\31\2\u00ee")
        buf.write("\u00f4\3\2\2\2\u00ef\u00f0\f\4\2\2\u00f0\u00f1\t\4\2\2")
        buf.write("\u00f1\u00f3\5\60\31\2\u00f2\u00ef\3\2\2\2\u00f3\u00f6")
        buf.write("\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("/\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f8\b\31\1\2\u00f8")
        buf.write("\u00f9\5\62\32\2\u00f9\u00ff\3\2\2\2\u00fa\u00fb\f\4\2")
        buf.write("\2\u00fb\u00fc\t\5\2\2\u00fc\u00fe\5\62\32\2\u00fd\u00fa")
        buf.write("\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100\61\3\2\2\2\u0101\u00ff\3\2\2\2\u0102")
        buf.write("\u0103\b\32\1\2\u0103\u0104\5\64\33\2\u0104\u010a\3\2")
        buf.write("\2\2\u0105\u0106\f\4\2\2\u0106\u0107\t\6\2\2\u0107\u0109")
        buf.write("\5\64\33\2\u0108\u0105\3\2\2\2\u0109\u010c\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\63\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010d\u010e\7&\2\2\u010e\u0111\5\64\33")
        buf.write("\2\u010f\u0111\5\66\34\2\u0110\u010d\3\2\2\2\u0110\u010f")
        buf.write("\3\2\2\2\u0111\65\3\2\2\2\u0112\u0113\7\"\2\2\u0113\u0116")
        buf.write("\5\66\34\2\u0114\u0116\58\35\2\u0115\u0112\3\2\2\2\u0115")
        buf.write("\u0114\3\2\2\2\u0116\67\3\2\2\2\u0117\u0118\b\35\1\2\u0118")
        buf.write("\u0119\5:\36\2\u0119\u0121\3\2\2\2\u011a\u011b\f\4\2\2")
        buf.write("\u011b\u011c\7\27\2\2\u011c\u011d\5*\26\2\u011d\u011e")
        buf.write("\7\30\2\2\u011e\u0120\3\2\2\2\u011f\u011a\3\2\2\2\u0120")
        buf.write("\u0123\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u01229\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0125\b\36\1")
        buf.write("\2\u0125\u0126\5<\37\2\u0126\u0133\3\2\2\2\u0127\u0128")
        buf.write("\f\4\2\2\u0128\u0129\7 \2\2\u0129\u012f\78\2\2\u012a\u012c")
        buf.write("\7\34\2\2\u012b\u012d\5B\"\2\u012c\u012b\3\2\2\2\u012c")
        buf.write("\u012d\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130\7\35\2")
        buf.write("\2\u012f\u012a\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0132")
        buf.write("\3\2\2\2\u0131\u0127\3\2\2\2\u0132\u0135\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134;\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0136\u0137\78\2\2\u0137\u0139\7 \2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a\u0140\7\3\2\2\u013b\u013d\7\34\2\2\u013c\u013e")
        buf.write("\5B\"\2\u013d\u013c\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("\u013f\3\2\2\2\u013f\u0141\7\35\2\2\u0140\u013b\3\2\2")
        buf.write("\2\u0140\u0141\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0144")
        buf.write("\5> \2\u0143\u0138\3\2\2\2\u0143\u0142\3\2\2\2\u0144=")
        buf.write("\3\2\2\2\u0145\u0146\7\26\2\2\u0146\u0147\78\2\2\u0147")
        buf.write("\u0149\7\34\2\2\u0148\u014a\5B\"\2\u0149\u0148\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014d\7")
        buf.write("\35\2\2\u014c\u014e\5> \2\u014d\u014c\3\2\2\2\u014d\u014e")
        buf.write("\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u0151\5@!\2\u0150\u0145")
        buf.write("\3\2\2\2\u0150\u014f\3\2\2\2\u0151?\3\2\2\2\u0152\u0153")
        buf.write("\7\34\2\2\u0153\u0154\5*\26\2\u0154\u0155\7\35\2\2\u0155")
        buf.write("\u015d\3\2\2\2\u0156\u015d\78\2\2\u0157\u015d\5\\/\2\u0158")
        buf.write("\u0159\7\25\2\2\u0159\u015a\7 \2\2\u015a\u015d\78\2\2")
        buf.write("\u015b\u015d\7\24\2\2\u015c\u0152\3\2\2\2\u015c\u0156")
        buf.write("\3\2\2\2\u015c\u0157\3\2\2\2\u015c\u0158\3\2\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015dA\3\2\2\2\u015e\u0163\5*\26\2\u015f")
        buf.write("\u0160\7\37\2\2\u0160\u0162\5*\26\2\u0161\u015f\3\2\2")
        buf.write("\2\u0162\u0165\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164")
        buf.write("\3\2\2\2\u0164C\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0172")
        buf.write("\5\f\7\2\u0167\u0168\5J&\2\u0168\u0169\7\36\2\2\u0169")
        buf.write("\u0172\3\2\2\2\u016a\u0172\5L\'\2\u016b\u0172\5N(\2\u016c")
        buf.write("\u0172\5P)\2\u016d\u0172\5R*\2\u016e\u0172\5T+\2\u016f")
        buf.write("\u0172\5V,\2\u0170\u0172\5F$\2\u0171\u0166\3\2\2\2\u0171")
        buf.write("\u0167\3\2\2\2\u0171\u016a\3\2\2\2\u0171\u016b\3\2\2\2")
        buf.write("\u0171\u016c\3\2\2\2\u0171\u016d\3\2\2\2\u0171\u016e\3")
        buf.write("\2\2\2\u0171\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172E")
        buf.write("\3\2\2\2\u0173\u0174\7\32\2\2\u0174\u0175\5H%\2\u0175")
        buf.write("\u0176\7\33\2\2\u0176G\3\2\2\2\u0177\u0179\5D#\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bI\3\2\2\2\u017c\u017a\3\2\2")
        buf.write("\2\u017d\u0180\78\2\2\u017e\u0180\58\35\2\u017f\u017d")
        buf.write("\3\2\2\2\u017f\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181")
        buf.write("\u0182\7/\2\2\u0182\u0183\5*\26\2\u0183K\3\2\2\2\u0184")
        buf.write("\u0186\7\17\2\2\u0185\u0187\5F$\2\u0186\u0185\3\2\2\2")
        buf.write("\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\5")
        buf.write("*\26\2\u0189\u018c\5F$\2\u018a\u018b\7\20\2\2\u018b\u018d")
        buf.write("\5F$\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018dM")
        buf.write("\3\2\2\2\u018e\u018f\7\21\2\2\u018f\u0190\5J&\2\u0190")
        buf.write("\u0191\7\36\2\2\u0191\u0192\5*\26\2\u0192\u0193\7\36\2")
        buf.write("\2\u0193\u0194\5J&\2\u0194\u0195\5F$\2\u0195O\3\2\2\2")
        buf.write("\u0196\u0197\7\r\2\2\u0197\u0198\7\36\2\2\u0198Q\3\2\2")
        buf.write("\2\u0199\u019a\7\16\2\2\u019a\u019b\7\36\2\2\u019bS\3")
        buf.write("\2\2\2\u019c\u019e\7\5\2\2\u019d\u019f\5*\26\2\u019e\u019d")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a1\7\36\2\2\u01a1U\3\2\2\2\u01a2\u01a5\5X-\2\u01a3")
        buf.write("\u01a5\5Z.\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a7\7\36\2\2\u01a7W\3\2\2\2\u01a8")
        buf.write("\u01a9\5*\26\2\u01a9\u01aa\7 \2\2\u01aa\u01ab\78\2\2\u01ab")
        buf.write("\u01ad\7\34\2\2\u01ac\u01ae\5B\"\2\u01ad\u01ac\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\7")
        buf.write("\35\2\2\u01b0Y\3\2\2\2\u01b1\u01b2\78\2\2\u01b2\u01b4")
        buf.write("\7 \2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b6\7\3\2\2\u01b6\u01b8\7\34\2")
        buf.write("\2\u01b7\u01b9\5B\"\2\u01b8\u01b7\3\2\2\2\u01b8\u01b9")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\7\35\2\2\u01bb")
        buf.write("[\3\2\2\2\u01bc\u01c2\7\65\2\2\u01bd\u01c2\7\64\2\2\u01be")
        buf.write("\u01c2\7\67\2\2\u01bf\u01c2\7\66\2\2\u01c0\u01c2\5`\61")
        buf.write("\2\u01c1\u01bc\3\2\2\2\u01c1\u01bd\3\2\2\2\u01c1\u01be")
        buf.write("\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2")
        buf.write("]\3\2\2\2\u01c3\u01c4\t\7\2\2\u01c4_\3\2\2\2\u01c5\u01ce")
        buf.write("\7\27\2\2\u01c6\u01cb\5b\62\2\u01c7\u01c8\7\37\2\2\u01c8")
        buf.write("\u01ca\5b\62\2\u01c9\u01c7\3\2\2\2\u01ca\u01cd\3\2\2\2")
        buf.write("\u01cb\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01cf\3")
        buf.write("\2\2\2\u01cd\u01cb\3\2\2\2\u01ce\u01c6\3\2\2\2\u01ce\u01cf")
        buf.write("\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\7\30\2\2\u01d1")
        buf.write("a\3\2\2\2\u01d2\u01d3\t\b\2\2\u01d3c\3\2\2\2.gnt\u0084")
        buf.write("\u0088\u0092\u00a6\u00b1\u00ba\u00c8\u00db\u00e3\u00ea")
        buf.write("\u00f4\u00ff\u010a\u0110\u0115\u0121\u012c\u012f\u0133")
        buf.write("\u0138\u013d\u0140\u0143\u0149\u014d\u0150\u015c\u0163")
        buf.write("\u0171\u017a\u017f\u0186\u018c\u019e\u01a4\u01ad\u01b3")
        buf.write("\u01b8\u01c1\u01cb\u01ce")
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
    RULE_array_type = 18
    RULE_attributelist = 19
    RULE_expression = 20
    RULE_expression1 = 21
    RULE_expression2 = 22
    RULE_expression3 = 23
    RULE_expression4 = 24
    RULE_expression5 = 25
    RULE_expression6 = 26
    RULE_expression7 = 27
    RULE_expression8 = 28
    RULE_expression9 = 29
    RULE_expression10 = 30
    RULE_operands = 31
    RULE_list_of_expression = 32
    RULE_statement = 33
    RULE_block_stmt = 34
    RULE_member_block = 35
    RULE_assign_stmt = 36
    RULE_if_stmt = 37
    RULE_for_stmt = 38
    RULE_break_stmt = 39
    RULE_continue_stmt = 40
    RULE_return_stmt = 41
    RULE_method_stm = 42
    RULE_instance_method = 43
    RULE_static_method = 44
    RULE_literal = 45
    RULE_membername = 46
    RULE_array_literal = 47
    RULE_elem = 48

    ruleNames =  [ "program", "classdecl", "supperclass", "construcdecl", 
                   "classmember", "attributedecl", "var_attr", "const_attr", 
                   "attr_frag", "no_initlist", "initlist", "methoddecl", 
                   "paramdecl", "paramlist", "param", "mctype", "classtype", 
                   "classname", "array_type", "attributelist", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "expression8", 
                   "expression9", "expression10", "operands", "list_of_expression", 
                   "statement", "block_stmt", "member_block", "assign_stmt", 
                   "if_stmt", "for_stmt", "break_stmt", "continue_stmt", 
                   "return_stmt", "method_stm", "instance_method", "static_method", 
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
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 98
                self.classdecl()
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CSlangParser.CLASS):
                    break

            self.state = 103
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
            self.state = 105
            self.match(CSlangParser.CLASS)
            self.state = 106
            self.classname()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.EXTENDS:
                self.state = 107
                self.supperclass()


            self.state = 110
            self.match(CSlangParser.LB)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.FUNC))) != 0):
                self.state = 111
                self.classmember()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
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
            self.state = 119
            self.match(CSlangParser.EXTENDS)
            self.state = 120
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
            self.state = 122
            self.match(CSlangParser.FUNC)
            self.state = 123
            self.match(CSlangParser.CONSTRUCTOR)
            self.state = 124
            self.paramdecl()
            self.state = 125
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
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.methoddecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.var_attr()
                pass
            elif token in [CSlangParser.CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
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
            self.state = 136
            self.match(CSlangParser.VAR)
            self.state = 137
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
            self.state = 139
            self.match(CSlangParser.CONST)
            self.state = 140
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
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 142
                self.no_initlist()
                pass

            elif la_ == 2:
                self.state = 143
                self.initlist()
                pass


            self.state = 146
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
            self.state = 148
            self.attributelist()
            self.state = 149
            self.match(CSlangParser.COLON)
            self.state = 150
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
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.membername()
                self.state = 153
                self.match(CSlangParser.CM)
                self.state = 154
                self.initlist()
                self.state = 155
                self.match(CSlangParser.CM)
                self.state = 156
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.membername()
                self.state = 159
                self.match(CSlangParser.COLON)
                self.state = 160
                self.mctype()
                self.state = 161
                self.match(CSlangParser.EQ)
                self.state = 162
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
            self.state = 166
            self.match(CSlangParser.FUNC)
            self.state = 167
            self.membername()
            self.state = 168
            self.paramdecl()
            self.state = 169
            self.match(CSlangParser.COLON)
            self.state = 170
            self.mctype()
            self.state = 171
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
            self.state = 173
            self.match(CSlangParser.LP)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.STATIC or _la==CSlangParser.ID:
                self.state = 174
                self.paramlist()


            self.state = 177
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
            self.state = 179
            self.param()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 180
                self.match(CSlangParser.CM)
                self.state = 181
                self.param()
                self.state = 186
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
            self.state = 187
            self.attributelist()
            self.state = 188
            self.match(CSlangParser.COLON)
            self.state = 189
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
        self.enterRule(localctx, 30, self.RULE_mctype)
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(CSlangParser.INT)
                pass
            elif token in [CSlangParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.match(CSlangParser.FLOAT)
                pass
            elif token in [CSlangParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.match(CSlangParser.BOOL)
                pass
            elif token in [CSlangParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.match(CSlangParser.STRING)
                pass
            elif token in [CSlangParser.VOID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.match(CSlangParser.VOID)
                pass
            elif token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.classtype()
                pass
            elif token in [CSlangParser.OB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 197
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
            self.state = 200
            self.match(CSlangParser.NEW)
            self.state = 201
            self.classname()
            self.state = 202
            self.match(CSlangParser.LP)
            self.state = 203
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
            self.state = 205
            self.match(CSlangParser.ID)
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
        self.enterRule(localctx, 36, self.RULE_array_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(CSlangParser.OB)
            self.state = 208
            self.match(CSlangParser.INTLIT)
            self.state = 209
            self.match(CSlangParser.CB)
            self.state = 210
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
        self.enterRule(localctx, 38, self.RULE_attributelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.membername()
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 213
                self.match(CSlangParser.CM)
                self.state = 214
                self.membername()
                self.state = 219
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
        self.enterRule(localctx, 40, self.RULE_expression)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.expression1()
                self.state = 221
                self.match(CSlangParser.CONCATENATION)
                self.state = 222
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
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
        self.enterRule(localctx, 42, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.expression2(0)
                self.state = 228
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.EQUAL) | (1 << CSlangParser.NOTEQUAL) | (1 << CSlangParser.LESS) | (1 << CSlangParser.GREATER) | (1 << CSlangParser.LESSEQUAL) | (1 << CSlangParser.GREATEREQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
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
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 242
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 237
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 238
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.OR or _la==CSlangParser.AND):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 239
                    self.expression3(0) 
                self.state = 244
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
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 248
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 249
                    _la = self._input.LA(1)
                    if not(_la==CSlangParser.ADD or _la==CSlangParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 250
                    self.expression4(0) 
                self.state = 255
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 264
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 259
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 260
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.DIV) | (1 << CSlangParser.BS) | (1 << CSlangParser.MOD) | (1 << CSlangParser.MUL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 261
                    self.expression5() 
                self.state = 266
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
        self.enterRule(localctx, 50, self.RULE_expression5)
        try:
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(CSlangParser.NOT)
                self.state = 268
                self.expression5()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.SUB, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
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
        self.enterRule(localctx, 52, self.RULE_expression6)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(CSlangParser.SUB)
                self.state = 273
                self.expression6()
                pass
            elif token in [CSlangParser.STATIC, CSlangParser.NULL, CSlangParser.SELF, CSlangParser.NEW, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
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
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.expression8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 287
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                    self.state = 280
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 281
                    self.match(CSlangParser.OB)
                    self.state = 282
                    self.expression()
                    self.state = 283
                    self.match(CSlangParser.CB) 
                self.state = 289
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expression8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.expression9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSlangParser.Expression8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                    self.state = 293
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 294
                    self.match(CSlangParser.DOT)
                    self.state = 295
                    self.match(CSlangParser.ID)
                    self.state = 301
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                    if la_ == 1:
                        self.state = 296
                        self.match(CSlangParser.LP)
                        self.state = 298
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                            self.state = 297
                            self.list_of_expression()


                        self.state = 300
                        self.match(CSlangParser.RP)

             
                self.state = 307
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
        self.enterRule(localctx, 58, self.RULE_expression9)
        self._la = 0 # Token type
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CSlangParser.ID:
                    self.state = 308
                    self.match(CSlangParser.ID)
                    self.state = 309
                    self.match(CSlangParser.DOT)


                self.state = 312
                self.match(CSlangParser.STATIC)
                self.state = 318
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                if la_ == 1:
                    self.state = 313
                    self.match(CSlangParser.LP)
                    self.state = 315
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                        self.state = 314
                        self.list_of_expression()


                    self.state = 317
                    self.match(CSlangParser.RP)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
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
        self.enterRule(localctx, 60, self.RULE_expression10)
        self._la = 0 # Token type
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(CSlangParser.NEW)
                self.state = 324
                self.match(CSlangParser.ID)
                self.state = 325
                self.match(CSlangParser.LP)
                self.state = 327
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                    self.state = 326
                    self.list_of_expression()


                self.state = 329
                self.match(CSlangParser.RP)
                self.state = 331
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 330
                    self.expression10()


                pass
            elif token in [CSlangParser.NULL, CSlangParser.SELF, CSlangParser.OB, CSlangParser.LP, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL, CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
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
        self.enterRule(localctx, 62, self.RULE_operands)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.LP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(CSlangParser.LP)
                self.state = 337
                self.expression()
                self.state = 338
                self.match(CSlangParser.RP)
                pass
            elif token in [CSlangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.OB, CSlangParser.FLOATLIT, CSlangParser.INTLIT, CSlangParser.BOOLLIT, CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 341
                self.literal()
                pass
            elif token in [CSlangParser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self.match(CSlangParser.SELF)
                self.state = 343
                self.match(CSlangParser.DOT)
                self.state = 344
                self.match(CSlangParser.ID)
                pass
            elif token in [CSlangParser.NULL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 345
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
        self.enterRule(localctx, 64, self.RULE_list_of_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.expression()
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSlangParser.CM:
                self.state = 349
                self.match(CSlangParser.CM)
                self.state = 350
                self.expression()
                self.state = 355
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
        self.enterRule(localctx, 66, self.RULE_statement)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.attributedecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.assign_stmt()
                self.state = 358
                self.match(CSlangParser.SM)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 360
                self.if_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 361
                self.for_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 362
                self.break_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 363
                self.continue_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 364
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 365
                self.method_stm()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 366
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
        self.enterRule(localctx, 68, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(CSlangParser.LB)
            self.state = 370
            self.member_block()
            self.state = 371
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
        self.enterRule(localctx, 70, self.RULE_member_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.RETURN) | (1 << CSlangParser.CONST) | (1 << CSlangParser.VAR) | (1 << CSlangParser.BREAK) | (1 << CSlangParser.CONTINUE) | (1 << CSlangParser.IF) | (1 << CSlangParser.FOR) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 373
                self.statement()
                self.state = 378
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
        self.enterRule(localctx, 72, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 379
                self.match(CSlangParser.ID)
                pass

            elif la_ == 2:
                self.state = 380
                self.expression7(0)
                pass


            self.state = 383
            self.match(CSlangParser.ASSIGN)
            self.state = 384
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
        self.enterRule(localctx, 74, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(CSlangParser.IF)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.LB:
                self.state = 387
                self.block_stmt()


            self.state = 390
            self.expression()
            self.state = 391
            self.block_stmt()
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ELSE:
                self.state = 392
                self.match(CSlangParser.ELSE)
                self.state = 393
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
        self.enterRule(localctx, 76, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(CSlangParser.FOR)
            self.state = 397
            self.assign_stmt()
            self.state = 398
            self.match(CSlangParser.SM)
            self.state = 399
            self.expression()
            self.state = 400
            self.match(CSlangParser.SM)
            self.state = 401
            self.assign_stmt()
            self.state = 402
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
        self.enterRule(localctx, 78, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(CSlangParser.BREAK)
            self.state = 405
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
        self.enterRule(localctx, 80, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(CSlangParser.CONTINUE)
            self.state = 408
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
        self.enterRule(localctx, 82, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(CSlangParser.RETURN)
            self.state = 412
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 411
                self.expression()


            self.state = 414
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
        self.enterRule(localctx, 84, self.RULE_method_stm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 416
                self.instance_method()
                pass

            elif la_ == 2:
                self.state = 417
                self.static_method()
                pass


            self.state = 420
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
        self.enterRule(localctx, 86, self.RULE_instance_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.expression()
            self.state = 423
            self.match(CSlangParser.DOT)
            self.state = 424
            self.match(CSlangParser.ID)
            self.state = 425
            self.match(CSlangParser.LP)
            self.state = 427
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 426
                self.list_of_expression()


            self.state = 429
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
        self.enterRule(localctx, 88, self.RULE_static_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSlangParser.ID:
                self.state = 431
                self.match(CSlangParser.ID)
                self.state = 432
                self.match(CSlangParser.DOT)


            self.state = 435
            self.match(CSlangParser.STATIC)
            self.state = 436
            self.match(CSlangParser.LP)
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.STATIC) | (1 << CSlangParser.NULL) | (1 << CSlangParser.SELF) | (1 << CSlangParser.NEW) | (1 << CSlangParser.OB) | (1 << CSlangParser.LP) | (1 << CSlangParser.SUB) | (1 << CSlangParser.NOT) | (1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL) | (1 << CSlangParser.ID))) != 0):
                self.state = 437
                self.list_of_expression()


            self.state = 440
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
        self.enterRule(localctx, 90, self.RULE_literal)
        try:
            self.state = 447
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CSlangParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(CSlangParser.INTLIT)
                pass
            elif token in [CSlangParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
                self.match(CSlangParser.FLOATLIT)
                pass
            elif token in [CSlangParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 444
                self.match(CSlangParser.STRING_LITERAL)
                pass
            elif token in [CSlangParser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 445
                self.match(CSlangParser.BOOLLIT)
                pass
            elif token in [CSlangParser.OB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 446
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
        self.enterRule(localctx, 92, self.RULE_membername)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
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
        self.enterRule(localctx, 94, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(CSlangParser.OB)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CSlangParser.FLOATLIT) | (1 << CSlangParser.INTLIT) | (1 << CSlangParser.BOOLLIT) | (1 << CSlangParser.STRING_LITERAL))) != 0):
                self.state = 452
                self.elem()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CSlangParser.CM:
                    self.state = 453
                    self.match(CSlangParser.CM)
                    self.state = 454
                    self.elem()
                    self.state = 459
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 462
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
        self.enterRule(localctx, 96, self.RULE_elem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
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
        self._predicates[22] = self.expression2_sempred
        self._predicates[23] = self.expression3_sempred
        self._predicates[24] = self.expression4_sempred
        self._predicates[27] = self.expression7_sempred
        self._predicates[28] = self.expression8_sempred
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
         




