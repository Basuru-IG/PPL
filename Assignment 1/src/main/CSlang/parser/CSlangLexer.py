# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01e5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\6\2\u008e\n\2\r\2\16\2\u008f\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,")
        buf.write("\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\5\65\u014c\n\65")
        buf.write("\3\65\6\65\u014f\n\65\r\65\16\65\u0150\3\65\3\65\3\65")
        buf.write("\7\65\u0156\n\65\f\65\16\65\u0159\13\65\3\65\5\65\u015c")
        buf.write("\n\65\3\65\6\65\u015f\n\65\r\65\16\65\u0160\3\65\3\65")
        buf.write("\6\65\u0165\n\65\r\65\16\65\u0166\3\65\5\65\u016a\n\65")
        buf.write("\3\65\5\65\u016d\n\65\3\65\6\65\u0170\n\65\r\65\16\65")
        buf.write("\u0171\3\65\3\65\5\65\u0176\n\65\3\66\6\66\u0179\n\66")
        buf.write("\r\66\16\66\u017a\3\67\3\67\5\67\u017f\n\67\38\38\78\u0183")
        buf.write("\n8\f8\168\u0186\138\38\38\38\39\39\59\u018d\n9\39\69")
        buf.write("\u0190\n9\r9\169\u0191\3:\3:\3;\3;\7;\u0198\n;\f;\16;")
        buf.write("\u019b\13;\3<\6<\u019e\n<\r<\16<\u019f\3<\3<\3=\3=\3=")
        buf.write("\3=\3>\3>\3>\3>\7>\u01ac\n>\f>\16>\u01af\13>\3>\3>\3?")
        buf.write("\3?\3?\3?\7?\u01b7\n?\f?\16?\u01ba\13?\3?\3?\3?\3?\3?")
        buf.write("\3@\3@\3@\3A\3A\7A\u01c6\nA\fA\16A\u01c9\13A\3A\5A\u01cc")
        buf.write("\nA\3A\3A\3B\3B\7B\u01d2\nB\fB\16B\u01d5\13B\3B\3B\3B")
        buf.write("\3C\3C\5C\u01dc\nC\3D\3D\3D\3E\3E\3E\5E\u01e4\nE\3\u01b8")
        buf.write("\2F\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\2#\2%\22\'\23)\24+\25-\26/\27")
        buf.write("\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%")
        buf.write("M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67")
        buf.write("q\2s\2u8w9y:{;}<\177=\u0081>\u0083?\u0085\2\u0087\2\u0089")
        buf.write("\2\3\2\r\6\2\62;C\\aac|\4\2GGgg\4\2--//\3\2\62;\5\2C\\")
        buf.write("aac|\5\2\13\13\16\17\"\"\4\2\f\f\17\17\6\3\n\f\16\17$")
        buf.write("$^^\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\3\2^^\2\u01f7")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\3\u008b\3\2\2\2\5\u0091\3\2\2")
        buf.write("\2\7\u0097\3\2\2\2\t\u009e\3\2\2\2\13\u00a2\3\2\2\2\r")
        buf.write("\u00a8\3\2\2\2\17\u00ae\3\2\2\2\21\u00b2\3\2\2\2\23\u00b7")
        buf.write("\3\2\2\2\25\u00bc\3\2\2\2\27\u00c8\3\2\2\2\31\u00ce\3")
        buf.write("\2\2\2\33\u00d7\3\2\2\2\35\u00da\3\2\2\2\37\u00df\3\2")
        buf.write("\2\2!\u00e3\3\2\2\2#\u00e8\3\2\2\2%\u00ee\3\2\2\2\'\u00f3")
        buf.write("\3\2\2\2)\u00fa\3\2\2\2+\u00ff\3\2\2\2-\u0104\3\2\2\2")
        buf.write("/\u0108\3\2\2\2\61\u010a\3\2\2\2\63\u010c\3\2\2\2\65\u010e")
        buf.write("\3\2\2\2\67\u0110\3\2\2\29\u0112\3\2\2\2;\u0114\3\2\2")
        buf.write("\2=\u0116\3\2\2\2?\u0118\3\2\2\2A\u011a\3\2\2\2C\u011c")
        buf.write("\3\2\2\2E\u011e\3\2\2\2G\u0120\3\2\2\2I\u0122\3\2\2\2")
        buf.write("K\u0124\3\2\2\2M\u0126\3\2\2\2O\u0128\3\2\2\2Q\u012b\3")
        buf.write("\2\2\2S\u012e\3\2\2\2U\u0131\3\2\2\2W\u0134\3\2\2\2Y\u0136")
        buf.write("\3\2\2\2[\u0138\3\2\2\2]\u013b\3\2\2\2_\u013e\3\2\2\2")
        buf.write("a\u0141\3\2\2\2c\u0143\3\2\2\2e\u0145\3\2\2\2g\u0147\3")
        buf.write("\2\2\2i\u0175\3\2\2\2k\u0178\3\2\2\2m\u017e\3\2\2\2o\u0180")
        buf.write("\3\2\2\2q\u018a\3\2\2\2s\u0193\3\2\2\2u\u0195\3\2\2\2")
        buf.write("w\u019d\3\2\2\2y\u01a3\3\2\2\2{\u01a7\3\2\2\2}\u01b2\3")
        buf.write("\2\2\2\177\u01c0\3\2\2\2\u0081\u01c3\3\2\2\2\u0083\u01cf")
        buf.write("\3\2\2\2\u0085\u01db\3\2\2\2\u0087\u01dd\3\2\2\2\u0089")
        buf.write("\u01e3\3\2\2\2\u008b\u008d\7B\2\2\u008c\u008e\t\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u008d\3")
        buf.write("\2\2\2\u008f\u0090\3\2\2\2\u0090\4\3\2\2\2\u0091\u0092")
        buf.write("\7e\2\2\u0092\u0093\7n\2\2\u0093\u0094\7c\2\2\u0094\u0095")
        buf.write("\7u\2\2\u0095\u0096\7u\2\2\u0096\6\3\2\2\2\u0097\u0098")
        buf.write("\7t\2\2\u0098\u0099\7g\2\2\u0099\u009a\7v\2\2\u009a\u009b")
        buf.write("\7w\2\2\u009b\u009c\7t\2\2\u009c\u009d\7p\2\2\u009d\b")
        buf.write("\3\2\2\2\u009e\u009f\7k\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\n\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4")
        buf.write("\7n\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7c\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\f\3\2\2\2\u00a8\u00a9\7e\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7u\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\16\3\2\2\2\u00ae\u00af\7x\2\2\u00af\u00b0")
        buf.write("\7c\2\2\u00b0\u00b1\7t\2\2\u00b1\20\3\2\2\2\u00b2\u00b3")
        buf.write("\7h\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6")
        buf.write("\7e\2\2\u00b6\22\3\2\2\2\u00b7\u00b8\7x\2\2\u00b8\u00b9")
        buf.write("\7q\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7f\2\2\u00bb\24")
        buf.write("\3\2\2\2\u00bc\u00bd\7e\2\2\u00bd\u00be\7q\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7e\2\2\u00c4\u00c5")
        buf.write("\7v\2\2\u00c5\u00c6\7q\2\2\u00c6\u00c7\7t\2\2\u00c7\26")
        buf.write("\3\2\2\2\u00c8\u00c9\7d\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7g\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd\7m\2\2\u00cd\30")
        buf.write("\3\2\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0\7q\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3\7k\2\2\u00d3\u00d4")
        buf.write("\7p\2\2\u00d4\u00d5\7w\2\2\u00d5\u00d6\7g\2\2\u00d6\32")
        buf.write("\3\2\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7h\2\2\u00d9\34")
        buf.write("\3\2\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd")
        buf.write("\7u\2\2\u00dd\u00de\7g\2\2\u00de\36\3\2\2\2\u00df\u00e0")
        buf.write("\7h\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2\7t\2\2\u00e2 \3")
        buf.write("\2\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6")
        buf.write("\7w\2\2\u00e6\u00e7\7g\2\2\u00e7\"\3\2\2\2\u00e8\u00e9")
        buf.write("\7h\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec")
        buf.write("\7u\2\2\u00ec\u00ed\7g\2\2\u00ed$\3\2\2\2\u00ee\u00ef")
        buf.write("\7d\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2&\3\2\2\2\u00f3\u00f4\7u\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7k\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7i\2\2\u00f9(\3\2\2\2\u00fa\u00fb")
        buf.write("\7p\2\2\u00fb\u00fc\7w\2\2\u00fc\u00fd\7n\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe*\3\2\2\2\u00ff\u0100\7u\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101\u0102\7n\2\2\u0102\u0103\7h\2\2\u0103,\3")
        buf.write("\2\2\2\u0104\u0105\7p\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7y\2\2\u0107.\3\2\2\2\u0108\u0109\7]\2\2\u0109\60\3\2")
        buf.write("\2\2\u010a\u010b\7_\2\2\u010b\62\3\2\2\2\u010c\u010d\7")
        buf.write("?\2\2\u010d\64\3\2\2\2\u010e\u010f\7}\2\2\u010f\66\3\2")
        buf.write("\2\2\u0110\u0111\7\177\2\2\u01118\3\2\2\2\u0112\u0113")
        buf.write("\7*\2\2\u0113:\3\2\2\2\u0114\u0115\7+\2\2\u0115<\3\2\2")
        buf.write("\2\u0116\u0117\7=\2\2\u0117>\3\2\2\2\u0118\u0119\7.\2")
        buf.write("\2\u0119@\3\2\2\2\u011a\u011b\7\60\2\2\u011bB\3\2\2\2")
        buf.write("\u011c\u011d\7-\2\2\u011dD\3\2\2\2\u011e\u011f\7/\2\2")
        buf.write("\u011fF\3\2\2\2\u0120\u0121\7\61\2\2\u0121H\3\2\2\2\u0122")
        buf.write("\u0123\7^\2\2\u0123J\3\2\2\2\u0124\u0125\7\'\2\2\u0125")
        buf.write("L\3\2\2\2\u0126\u0127\7#\2\2\u0127N\3\2\2\2\u0128\u0129")
        buf.write("\7~\2\2\u0129\u012a\7~\2\2\u012aP\3\2\2\2\u012b\u012c")
        buf.write("\7(\2\2\u012c\u012d\7(\2\2\u012dR\3\2\2\2\u012e\u012f")
        buf.write("\7?\2\2\u012f\u0130\7?\2\2\u0130T\3\2\2\2\u0131\u0132")
        buf.write("\7#\2\2\u0132\u0133\7?\2\2\u0133V\3\2\2\2\u0134\u0135")
        buf.write("\7>\2\2\u0135X\3\2\2\2\u0136\u0137\7@\2\2\u0137Z\3\2\2")
        buf.write("\2\u0138\u0139\7>\2\2\u0139\u013a\7?\2\2\u013a\\\3\2\2")
        buf.write("\2\u013b\u013c\7@\2\2\u013c\u013d\7?\2\2\u013d^\3\2\2")
        buf.write("\2\u013e\u013f\7<\2\2\u013f\u0140\7?\2\2\u0140`\3\2\2")
        buf.write("\2\u0141\u0142\7`\2\2\u0142b\3\2\2\2\u0143\u0144\7,\2")
        buf.write("\2\u0144d\3\2\2\2\u0145\u0146\7<\2\2\u0146f\3\2\2\2\u0147")
        buf.write("\u0148\7>\2\2\u0148\u0149\7/\2\2\u0149h\3\2\2\2\u014a")
        buf.write("\u014c\7/\2\2\u014b\u014a\3\2\2\2\u014b\u014c\3\2\2\2")
        buf.write("\u014c\u014e\3\2\2\2\u014d\u014f\5s:\2\u014e\u014d\3\2")
        buf.write("\2\2\u014f\u0150\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0157\5A!\2\u0153\u0156")
        buf.write("\5s:\2\u0154\u0156\5q9\2\u0155\u0153\3\2\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0176\3\2\2\2\u0159\u0157\3\2\2\2")
        buf.write("\u015a\u015c\7/\2\2\u015b\u015a\3\2\2\2\u015b\u015c\3")
        buf.write("\2\2\2\u015c\u015e\3\2\2\2\u015d\u015f\5s:\2\u015e\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0164\5A!\2\u0163")
        buf.write("\u0165\5s:\2\u0164\u0163\3\2\2\2\u0165\u0166\3\2\2\2\u0166")
        buf.write("\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0169\3\2\2\2")
        buf.write("\u0168\u016a\5q9\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2")
        buf.write("\2\2\u016a\u0176\3\2\2\2\u016b\u016d\7/\2\2\u016c\u016b")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3\2\2\2\u016e")
        buf.write("\u0170\5s:\2\u016f\u016e\3\2\2\2\u0170\u0171\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0174\5q9\2\u0174\u0176\3\2\2\2\u0175\u014b\3\2")
        buf.write("\2\2\u0175\u015b\3\2\2\2\u0175\u016c\3\2\2\2\u0176j\3")
        buf.write("\2\2\2\u0177\u0179\5s:\2\u0178\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u017b\3\2\2\2\u017b")
        buf.write("l\3\2\2\2\u017c\u017f\5!\21\2\u017d\u017f\5#\22\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017fn\3\2\2\2\u0180")
        buf.write("\u0184\7$\2\2\u0181\u0183\5\u0085C\2\u0182\u0181\3\2\2")
        buf.write("\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187")
        buf.write("\u0188\7$\2\2\u0188\u0189\b8\2\2\u0189p\3\2\2\2\u018a")
        buf.write("\u018c\t\3\2\2\u018b\u018d\t\4\2\2\u018c\u018b\3\2\2\2")
        buf.write("\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2\u018e\u0190\5")
        buf.write("s:\2\u018f\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u018f")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192r\3\2\2\2\u0193\u0194")
        buf.write("\t\5\2\2\u0194t\3\2\2\2\u0195\u0199\t\6\2\2\u0196\u0198")
        buf.write("\t\2\2\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019av\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019c\u019e\t\7\2\2\u019d\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3")
        buf.write("\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\b<\3\2\u01a2x\3")
        buf.write("\2\2\2\u01a3\u01a4\7\f\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6")
        buf.write("\b=\3\2\u01a6z\3\2\2\2\u01a7\u01a8\7\61\2\2\u01a8\u01a9")
        buf.write("\7\61\2\2\u01a9\u01ad\3\2\2\2\u01aa\u01ac\n\b\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01b1\b>\3\2\u01b1|\3\2\2\2\u01b2\u01b3\7")
        buf.write("\61\2\2\u01b3\u01b4\7,\2\2\u01b4\u01b8\3\2\2\2\u01b5\u01b7")
        buf.write("\13\2\2\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01bb\3\2\2\2")
        buf.write("\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7,\2\2\u01bc\u01bd\7")
        buf.write("\61\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\b?\3\2\u01bf~")
        buf.write("\3\2\2\2\u01c0\u01c1\13\2\2\2\u01c1\u01c2\b@\4\2\u01c2")
        buf.write("\u0080\3\2\2\2\u01c3\u01c7\7$\2\2\u01c4\u01c6\5\u0085")
        buf.write("C\2\u01c5\u01c4\3\2\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5")
        buf.write("\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9")
        buf.write("\u01c7\3\2\2\2\u01ca\u01cc\t\t\2\2\u01cb\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01ce\bA\5\2\u01ce\u0082\3")
        buf.write("\2\2\2\u01cf\u01d3\7$\2\2\u01d0\u01d2\5\u0085C\2\u01d1")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2")
        buf.write("\u01d3\u01d4\3\2\2\2\u01d4\u01d6\3\2\2\2\u01d5\u01d3\3")
        buf.write("\2\2\2\u01d6\u01d7\5\u0089E\2\u01d7\u01d8\bB\6\2\u01d8")
        buf.write("\u0084\3\2\2\2\u01d9\u01dc\n\n\2\2\u01da\u01dc\5\u0087")
        buf.write("D\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2\u01dc\u0086")
        buf.write("\3\2\2\2\u01dd\u01de\7^\2\2\u01de\u01df\t\13\2\2\u01df")
        buf.write("\u0088\3\2\2\2\u01e0\u01e1\7^\2\2\u01e1\u01e4\n\13\2\2")
        buf.write("\u01e2\u01e4\n\f\2\2\u01e3\u01e0\3\2\2\2\u01e3\u01e2\3")
        buf.write("\2\2\2\u01e4\u008a\3\2\2\2\35\2\u008f\u014b\u0150\u0155")
        buf.write("\u0157\u015b\u0160\u0166\u0169\u016c\u0171\u0175\u017a")
        buf.write("\u017e\u0184\u018c\u0191\u0199\u019f\u01ad\u01b8\u01c7")
        buf.write("\u01cb\u01d3\u01db\u01e3\7\38\2\b\2\2\3@\3\3A\4\3B\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STATIC = 1
    CLASS = 2
    RETURN = 3
    INT = 4
    FLOAT = 5
    CONST = 6
    VAR = 7
    FUNC = 8
    VOID = 9
    CONSTRUCTOR = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSE = 14
    FOR = 15
    BOOL = 16
    STRING = 17
    NULL = 18
    SELF = 19
    NEW = 20
    OB = 21
    CB = 22
    EQ = 23
    LB = 24
    RB = 25
    LP = 26
    RP = 27
    SM = 28
    CM = 29
    DOT = 30
    ADD = 31
    SUB = 32
    DIV = 33
    BS = 34
    MOD = 35
    NOT = 36
    OR = 37
    AND = 38
    EQUAL = 39
    NOTEQUAL = 40
    LESS = 41
    GREATER = 42
    LESSEQUAL = 43
    GREATEREQUAL = 44
    ASSIGN = 45
    CONCATENATION = 46
    MUL = 47
    COLON = 48
    EXTENDS = 49
    FLOATLIT = 50
    INTLIT = 51
    BOOLLIT = 52
    STRING_LITERAL = 53
    ID = 54
    WS = 55
    NEWLINE = 56
    LINE_COMMENT = 57
    BLOCK_COMMENT = 58
    ERROR_CHAR = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'return'", "'int'", "'float'", "'const'", "'var'", 
            "'func'", "'void'", "'constructor'", "'break'", "'continue'", 
            "'if'", "'else'", "'for'", "'bool'", "'string'", "'null'", "'self'", 
            "'new'", "'['", "']'", "'='", "'{'", "'}'", "'('", "')'", "';'", 
            "','", "'.'", "'+'", "'-'", "'/'", "'\\'", "'%'", "'!'", "'||'", 
            "'&&'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "':='", 
            "'^'", "'*'", "':'", "'<-'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "STATIC", "CLASS", "RETURN", "INT", "FLOAT", "CONST", "VAR", 
            "FUNC", "VOID", "CONSTRUCTOR", "BREAK", "CONTINUE", "IF", "ELSE", 
            "FOR", "BOOL", "STRING", "NULL", "SELF", "NEW", "OB", "CB", 
            "EQ", "LB", "RB", "LP", "RP", "SM", "CM", "DOT", "ADD", "SUB", 
            "DIV", "BS", "MOD", "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", 
            "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "CONCATENATION", 
            "MUL", "COLON", "EXTENDS", "FLOATLIT", "INTLIT", "BOOLLIT", 
            "STRING_LITERAL", "ID", "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "STATIC", "CLASS", "RETURN", "INT", "FLOAT", "CONST", 
                  "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "BOOL", "STRING", 
                  "NULL", "SELF", "NEW", "OB", "CB", "EQ", "LB", "RB", "LP", 
                  "RP", "SM", "CM", "DOT", "ADD", "SUB", "DIV", "BS", "MOD", 
                  "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", "LESS", "GREATER", 
                  "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "CONCATENATION", 
                  "MUL", "COLON", "EXTENDS", "FLOATLIT", "INTLIT", "BOOLLIT", 
                  "STRING_LITERAL", "EXPONENT", "DIGIT", "ID", "WS", "NEWLINE", 
                  "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL" ]

    grammarFileName = "CSlang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[54] = self.STRING_LITERAL_action 
            actions[62] = self.ERROR_CHAR_action 
            actions[63] = self.UNCLOSE_STRING_action 
            actions[64] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '\"', '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


