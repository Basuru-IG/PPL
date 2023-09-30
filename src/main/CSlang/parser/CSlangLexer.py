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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u01f1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5")
        buf.write("\2\u0096\n\2\3\3\3\3\6\3\u009a\n\3\r\3\16\3\u009b\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write(".\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\66\5\66\u0158\n")
        buf.write("\66\3\66\6\66\u015b\n\66\r\66\16\66\u015c\3\66\3\66\3")
        buf.write("\66\7\66\u0162\n\66\f\66\16\66\u0165\13\66\3\66\5\66\u0168")
        buf.write("\n\66\3\66\6\66\u016b\n\66\r\66\16\66\u016c\3\66\3\66")
        buf.write("\6\66\u0171\n\66\r\66\16\66\u0172\3\66\5\66\u0176\n\66")
        buf.write("\3\66\5\66\u0179\n\66\3\66\6\66\u017c\n\66\r\66\16\66")
        buf.write("\u017d\3\66\3\66\5\66\u0182\n\66\3\67\6\67\u0185\n\67")
        buf.write("\r\67\16\67\u0186\38\38\58\u018b\n8\39\39\79\u018f\n9")
        buf.write("\f9\169\u0192\139\39\39\39\3:\3:\5:\u0199\n:\3:\6:\u019c")
        buf.write("\n:\r:\16:\u019d\3;\3;\3<\3<\7<\u01a4\n<\f<\16<\u01a7")
        buf.write("\13<\3=\6=\u01aa\n=\r=\16=\u01ab\3=\3=\3>\3>\3>\3>\3?")
        buf.write("\3?\3?\3?\7?\u01b8\n?\f?\16?\u01bb\13?\3?\3?\3@\3@\3@")
        buf.write("\3@\7@\u01c3\n@\f@\16@\u01c6\13@\3@\3@\3@\3@\3@\3A\3A")
        buf.write("\3A\3B\3B\7B\u01d2\nB\fB\16B\u01d5\13B\3B\5B\u01d8\nB")
        buf.write("\3B\3B\3C\3C\7C\u01de\nC\fC\16C\u01e1\13C\3C\3C\3C\3D")
        buf.write("\3D\5D\u01e8\nD\3E\3E\3E\3F\3F\3F\5F\u01f0\nF\3\u01c4")
        buf.write("\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\2%\2\'\23)\24+\25-\26/\27")
        buf.write("\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%")
        buf.write("M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67")
        buf.write("q8s\2u\2w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087\2\u0089")
        buf.write("\2\u008b\2\3\2\r\6\2\62;C\\aac|\4\2GGgg\4\2--//\3\2\62")
        buf.write(";\5\2C\\aac|\5\2\13\13\16\17\"\"\4\2\f\f\17\17\6\3\n\f")
        buf.write("\16\17$$^^\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\3\2^^\2")
        buf.write("\u0207\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\3\u008d")
        buf.write("\3\2\2\2\5\u0097\3\2\2\2\7\u009d\3\2\2\2\t\u00a3\3\2\2")
        buf.write("\2\13\u00aa\3\2\2\2\r\u00ae\3\2\2\2\17\u00b4\3\2\2\2\21")
        buf.write("\u00ba\3\2\2\2\23\u00be\3\2\2\2\25\u00c3\3\2\2\2\27\u00c8")
        buf.write("\3\2\2\2\31\u00d4\3\2\2\2\33\u00da\3\2\2\2\35\u00e3\3")
        buf.write("\2\2\2\37\u00e6\3\2\2\2!\u00eb\3\2\2\2#\u00ef\3\2\2\2")
        buf.write("%\u00f4\3\2\2\2\'\u00fa\3\2\2\2)\u00ff\3\2\2\2+\u0106")
        buf.write("\3\2\2\2-\u010b\3\2\2\2/\u0110\3\2\2\2\61\u0114\3\2\2")
        buf.write("\2\63\u0116\3\2\2\2\65\u0118\3\2\2\2\67\u011a\3\2\2\2")
        buf.write("9\u011c\3\2\2\2;\u011e\3\2\2\2=\u0120\3\2\2\2?\u0122\3")
        buf.write("\2\2\2A\u0124\3\2\2\2C\u0126\3\2\2\2E\u0128\3\2\2\2G\u012a")
        buf.write("\3\2\2\2I\u012c\3\2\2\2K\u012e\3\2\2\2M\u0130\3\2\2\2")
        buf.write("O\u0132\3\2\2\2Q\u0134\3\2\2\2S\u0137\3\2\2\2U\u013a\3")
        buf.write("\2\2\2W\u013d\3\2\2\2Y\u0140\3\2\2\2[\u0142\3\2\2\2]\u0144")
        buf.write("\3\2\2\2_\u0147\3\2\2\2a\u014a\3\2\2\2c\u014d\3\2\2\2")
        buf.write("e\u014f\3\2\2\2g\u0151\3\2\2\2i\u0153\3\2\2\2k\u0181\3")
        buf.write("\2\2\2m\u0184\3\2\2\2o\u018a\3\2\2\2q\u018c\3\2\2\2s\u0196")
        buf.write("\3\2\2\2u\u019f\3\2\2\2w\u01a1\3\2\2\2y\u01a9\3\2\2\2")
        buf.write("{\u01af\3\2\2\2}\u01b3\3\2\2\2\177\u01be\3\2\2\2\u0081")
        buf.write("\u01cc\3\2\2\2\u0083\u01cf\3\2\2\2\u0085\u01db\3\2\2\2")
        buf.write("\u0087\u01e7\3\2\2\2\u0089\u01e9\3\2\2\2\u008b\u01ef\3")
        buf.write("\2\2\2\u008d\u008e\5\61\31\2\u008e\u008f\5m\67\2\u008f")
        buf.write("\u0095\5\63\32\2\u0090\u0096\5\13\6\2\u0091\u0096\5\r")
        buf.write("\7\2\u0092\u0096\5\'\24\2\u0093\u0096\5)\25\2\u0094\u0096")
        buf.write("\5w<\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096")
        buf.write("\4\3\2\2\2\u0097\u0099\7B\2\2\u0098\u009a\t\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u0099\3\2\2\2")
        buf.write("\u009b\u009c\3\2\2\2\u009c\6\3\2\2\2\u009d\u009e\7e\2")
        buf.write("\2\u009e\u009f\7n\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1\7")
        buf.write("u\2\2\u00a1\u00a2\7u\2\2\u00a2\b\3\2\2\2\u00a3\u00a4\7")
        buf.write("t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7w\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7p\2\2\u00a9\n")
        buf.write("\3\2\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\f\3\2\2\2\u00ae\u00af\7h\2\2\u00af\u00b0")
        buf.write("\7n\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3")
        buf.write("\7v\2\2\u00b3\16\3\2\2\2\u00b4\u00b5\7e\2\2\u00b5\u00b6")
        buf.write("\7q\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\20\3\2\2\2\u00ba\u00bb\7x\2\2\u00bb\u00bc")
        buf.write("\7c\2\2\u00bc\u00bd\7t\2\2\u00bd\22\3\2\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\u00c0\7w\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7e\2\2\u00c2\24\3\2\2\2\u00c3\u00c4\7x\2\2\u00c4\u00c5")
        buf.write("\7q\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7f\2\2\u00c7\26")
        buf.write("\3\2\2\2\u00c8\u00c9\7e\2\2\u00c9\u00ca\7q\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\u00cc\7u\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce")
        buf.write("\7t\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1")
        buf.write("\7v\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7t\2\2\u00d3\30")
        buf.write("\3\2\2\2\u00d4\u00d5\7d\2\2\u00d5\u00d6\7t\2\2\u00d6\u00d7")
        buf.write("\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7m\2\2\u00d9\32")
        buf.write("\3\2\2\2\u00da\u00db\7e\2\2\u00db\u00dc\7q\2\2\u00dc\u00dd")
        buf.write("\7p\2\2\u00dd\u00de\7v\2\2\u00de\u00df\7k\2\2\u00df\u00e0")
        buf.write("\7p\2\2\u00e0\u00e1\7w\2\2\u00e1\u00e2\7g\2\2\u00e2\34")
        buf.write("\3\2\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7h\2\2\u00e5\36")
        buf.write("\3\2\2\2\u00e6\u00e7\7g\2\2\u00e7\u00e8\7n\2\2\u00e8\u00e9")
        buf.write("\7u\2\2\u00e9\u00ea\7g\2\2\u00ea \3\2\2\2\u00eb\u00ec")
        buf.write("\7h\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee\7t\2\2\u00ee\"")
        buf.write("\3\2\2\2\u00ef\u00f0\7v\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2")
        buf.write("\7w\2\2\u00f2\u00f3\7g\2\2\u00f3$\3\2\2\2\u00f4\u00f5")
        buf.write("\7h\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8")
        buf.write("\7u\2\2\u00f8\u00f9\7g\2\2\u00f9&\3\2\2\2\u00fa\u00fb")
        buf.write("\7d\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7q\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe(\3\2\2\2\u00ff\u0100\7u\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7t\2\2\u0102\u0103\7k\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\u0105\7i\2\2\u0105*\3\2\2\2\u0106\u0107")
        buf.write("\7p\2\2\u0107\u0108\7w\2\2\u0108\u0109\7n\2\2\u0109\u010a")
        buf.write("\7n\2\2\u010a,\3\2\2\2\u010b\u010c\7u\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010d\u010e\7n\2\2\u010e\u010f\7h\2\2\u010f.\3")
        buf.write("\2\2\2\u0110\u0111\7p\2\2\u0111\u0112\7g\2\2\u0112\u0113")
        buf.write("\7y\2\2\u0113\60\3\2\2\2\u0114\u0115\7]\2\2\u0115\62\3")
        buf.write("\2\2\2\u0116\u0117\7_\2\2\u0117\64\3\2\2\2\u0118\u0119")
        buf.write("\7?\2\2\u0119\66\3\2\2\2\u011a\u011b\7}\2\2\u011b8\3\2")
        buf.write("\2\2\u011c\u011d\7\177\2\2\u011d:\3\2\2\2\u011e\u011f")
        buf.write("\7*\2\2\u011f<\3\2\2\2\u0120\u0121\7+\2\2\u0121>\3\2\2")
        buf.write("\2\u0122\u0123\7=\2\2\u0123@\3\2\2\2\u0124\u0125\7.\2")
        buf.write("\2\u0125B\3\2\2\2\u0126\u0127\7\60\2\2\u0127D\3\2\2\2")
        buf.write("\u0128\u0129\7-\2\2\u0129F\3\2\2\2\u012a\u012b\7/\2\2")
        buf.write("\u012bH\3\2\2\2\u012c\u012d\7\61\2\2\u012dJ\3\2\2\2\u012e")
        buf.write("\u012f\7^\2\2\u012fL\3\2\2\2\u0130\u0131\7\'\2\2\u0131")
        buf.write("N\3\2\2\2\u0132\u0133\7#\2\2\u0133P\3\2\2\2\u0134\u0135")
        buf.write("\7~\2\2\u0135\u0136\7~\2\2\u0136R\3\2\2\2\u0137\u0138")
        buf.write("\7(\2\2\u0138\u0139\7(\2\2\u0139T\3\2\2\2\u013a\u013b")
        buf.write("\7?\2\2\u013b\u013c\7?\2\2\u013cV\3\2\2\2\u013d\u013e")
        buf.write("\7#\2\2\u013e\u013f\7?\2\2\u013fX\3\2\2\2\u0140\u0141")
        buf.write("\7>\2\2\u0141Z\3\2\2\2\u0142\u0143\7@\2\2\u0143\\\3\2")
        buf.write("\2\2\u0144\u0145\7>\2\2\u0145\u0146\7?\2\2\u0146^\3\2")
        buf.write("\2\2\u0147\u0148\7@\2\2\u0148\u0149\7?\2\2\u0149`\3\2")
        buf.write("\2\2\u014a\u014b\7<\2\2\u014b\u014c\7?\2\2\u014cb\3\2")
        buf.write("\2\2\u014d\u014e\7`\2\2\u014ed\3\2\2\2\u014f\u0150\7,")
        buf.write("\2\2\u0150f\3\2\2\2\u0151\u0152\7<\2\2\u0152h\3\2\2\2")
        buf.write("\u0153\u0154\7>\2\2\u0154\u0155\7/\2\2\u0155j\3\2\2\2")
        buf.write("\u0156\u0158\7/\2\2\u0157\u0156\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u015a\3\2\2\2\u0159\u015b\5u;\2\u015a\u0159")
        buf.write("\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015d\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0163\5C\"\2")
        buf.write("\u015f\u0162\5u;\2\u0160\u0162\5s:\2\u0161\u015f\3\2\2")
        buf.write("\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0182\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0166\u0168\7/\2\2\u0167\u0166\3\2\2\2")
        buf.write("\u0167\u0168\3\2\2\2\u0168\u016a\3\2\2\2\u0169\u016b\5")
        buf.write("u;\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016e\3\2\2\2\u016e")
        buf.write("\u0170\5C\"\2\u016f\u0171\5u;\2\u0170\u016f\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0175\3\2\2\2\u0174\u0176\5s:\2\u0175\u0174\3\2")
        buf.write("\2\2\u0175\u0176\3\2\2\2\u0176\u0182\3\2\2\2\u0177\u0179")
        buf.write("\7/\2\2\u0178\u0177\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u017b\3\2\2\2\u017a\u017c\5u;\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017e\u017f\3\2\2\2\u017f\u0180\5s:\2\u0180\u0182\3\2")
        buf.write("\2\2\u0181\u0157\3\2\2\2\u0181\u0167\3\2\2\2\u0181\u0178")
        buf.write("\3\2\2\2\u0182l\3\2\2\2\u0183\u0185\5u;\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187n\3\2\2\2\u0188\u018b\5#\22\2\u0189")
        buf.write("\u018b\5%\23\2\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2")
        buf.write("\u018bp\3\2\2\2\u018c\u0190\7$\2\2\u018d\u018f\5\u0087")
        buf.write("D\2\u018e\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0193\3\2\2\2\u0192")
        buf.write("\u0190\3\2\2\2\u0193\u0194\7$\2\2\u0194\u0195\b9\2\2\u0195")
        buf.write("r\3\2\2\2\u0196\u0198\t\3\2\2\u0197\u0199\t\4\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2")
        buf.write("\u019a\u019c\5u;\2\u019b\u019a\3\2\2\2\u019c\u019d\3\2")
        buf.write("\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019et\3")
        buf.write("\2\2\2\u019f\u01a0\t\5\2\2\u01a0v\3\2\2\2\u01a1\u01a5")
        buf.write("\t\6\2\2\u01a2\u01a4\t\2\2\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a7\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6x\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a8\u01aa\t\7\2")
        buf.write("\2\u01a9\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad")
        buf.write("\u01ae\b=\3\2\u01aez\3\2\2\2\u01af\u01b0\7\f\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b2\b>\3\2\u01b2|\3\2\2\2\u01b3")
        buf.write("\u01b4\7\61\2\2\u01b4\u01b5\7\61\2\2\u01b5\u01b9\3\2\2")
        buf.write("\2\u01b6\u01b8\n\b\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb")
        buf.write("\3\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01bc\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\b?\3\2")
        buf.write("\u01bd~\3\2\2\2\u01be\u01bf\7\61\2\2\u01bf\u01c0\7,\2")
        buf.write("\2\u01c0\u01c4\3\2\2\2\u01c1\u01c3\13\2\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c7\u01c8\7,\2\2\u01c8\u01c9\7\61\2\2\u01c9\u01ca\3")
        buf.write("\2\2\2\u01ca\u01cb\b@\3\2\u01cb\u0080\3\2\2\2\u01cc\u01cd")
        buf.write("\13\2\2\2\u01cd\u01ce\bA\4\2\u01ce\u0082\3\2\2\2\u01cf")
        buf.write("\u01d3\7$\2\2\u01d0\u01d2\5\u0087D\2\u01d1\u01d0\3\2\2")
        buf.write("\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4")
        buf.write("\3\2\2\2\u01d4\u01d7\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6")
        buf.write("\u01d8\t\t\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2")
        buf.write("\u01d9\u01da\bB\5\2\u01da\u0084\3\2\2\2\u01db\u01df\7")
        buf.write("$\2\2\u01dc\u01de\5\u0087D\2\u01dd\u01dc\3\2\2\2\u01de")
        buf.write("\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2")
        buf.write("\u01e0\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e3\5")
        buf.write("\u008bF\2\u01e3\u01e4\bC\6\2\u01e4\u0086\3\2\2\2\u01e5")
        buf.write("\u01e8\n\n\2\2\u01e6\u01e8\5\u0089E\2\u01e7\u01e5\3\2")
        buf.write("\2\2\u01e7\u01e6\3\2\2\2\u01e8\u0088\3\2\2\2\u01e9\u01ea")
        buf.write("\7^\2\2\u01ea\u01eb\t\13\2\2\u01eb\u008a\3\2\2\2\u01ec")
        buf.write("\u01ed\7^\2\2\u01ed\u01f0\n\13\2\2\u01ee\u01f0\n\f\2\2")
        buf.write("\u01ef\u01ec\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0\u008c\3")
        buf.write("\2\2\2\36\2\u0095\u009b\u0157\u015c\u0161\u0163\u0167")
        buf.write("\u016c\u0172\u0175\u0178\u017d\u0181\u0186\u018a\u0190")
        buf.write("\u0198\u019d\u01a5\u01ab\u01b9\u01c4\u01d3\u01d7\u01df")
        buf.write("\u01e7\u01ef\7\39\2\b\2\2\3A\3\3B\4\3C\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY = 1
    STATIC = 2
    CLASS = 3
    RETURN = 4
    INT = 5
    FLOAT = 6
    CONST = 7
    VAR = 8
    FUNC = 9
    VOID = 10
    CONSTRUCTOR = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSE = 15
    FOR = 16
    BOOL = 17
    STRING = 18
    NULL = 19
    SELF = 20
    NEW = 21
    OB = 22
    CB = 23
    EQ = 24
    LB = 25
    RB = 26
    LP = 27
    RP = 28
    SM = 29
    CM = 30
    DOT = 31
    ADD = 32
    SUB = 33
    DIV = 34
    BS = 35
    MOD = 36
    NOT = 37
    OR = 38
    AND = 39
    EQUAL = 40
    NOTEQUAL = 41
    LESS = 42
    GREATER = 43
    LESSEQUAL = 44
    GREATEREQUAL = 45
    ASSIGN = 46
    CONCATENATION = 47
    MUL = 48
    COLON = 49
    EXTENDS = 50
    FLOATLIT = 51
    INTLIT = 52
    BOOLLIT = 53
    STRING_LITERAL = 54
    ID = 55
    WS = 56
    NEWLINE = 57
    LINE_COMMENT = 58
    BLOCK_COMMENT = 59
    ERROR_CHAR = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62

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
            "ARRAY", "STATIC", "CLASS", "RETURN", "INT", "FLOAT", "CONST", 
            "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "BOOL", "STRING", "NULL", "SELF", "NEW", "OB", 
            "CB", "EQ", "LB", "RB", "LP", "RP", "SM", "CM", "DOT", "ADD", 
            "SUB", "DIV", "BS", "MOD", "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", 
            "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "CONCATENATION", 
            "MUL", "COLON", "EXTENDS", "FLOATLIT", "INTLIT", "BOOLLIT", 
            "STRING_LITERAL", "ID", "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ARRAY", "STATIC", "CLASS", "RETURN", "INT", "FLOAT", 
                  "CONST", "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "BOOL", 
                  "STRING", "NULL", "SELF", "NEW", "OB", "CB", "EQ", "LB", 
                  "RB", "LP", "RP", "SM", "CM", "DOT", "ADD", "SUB", "DIV", 
                  "BS", "MOD", "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", 
                  "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", 
                  "CONCATENATION", "MUL", "COLON", "EXTENDS", "FLOATLIT", 
                  "INTLIT", "BOOLLIT", "STRING_LITERAL", "EXPONENT", "DIGIT", 
                  "ID", "WS", "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL" ]

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
            actions[55] = self.STRING_LITERAL_action 
            actions[63] = self.ERROR_CHAR_action 
            actions[64] = self.UNCLOSE_STRING_action 
            actions[65] = self.ILLEGAL_ESCAPE_action 
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
            	
     


