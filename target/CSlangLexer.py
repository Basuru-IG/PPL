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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u0206\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3")
        buf.write("-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\63\6\63\u016d\n\63\r\63\16\63\u016e\3\63\3\63\3\63")
        buf.write("\7\63\u0174\n\63\f\63\16\63\u0177\13\63\3\63\7\63\u017a")
        buf.write("\n\63\f\63\16\63\u017d\13\63\3\63\3\63\6\63\u0181\n\63")
        buf.write("\r\63\16\63\u0182\3\63\5\63\u0186\n\63\3\63\6\63\u0189")
        buf.write("\n\63\r\63\16\63\u018a\3\63\3\63\5\63\u018f\n\63\3\64")
        buf.write("\6\64\u0192\n\64\r\64\16\64\u0193\3\65\3\65\5\65\u0198")
        buf.write("\n\65\3\65\6\65\u019b\n\65\r\65\16\65\u019c\3\66\3\66")
        buf.write("\3\67\3\67\7\67\u01a3\n\67\f\67\16\67\u01a6\13\67\38\6")
        buf.write("8\u01a9\n8\r8\168\u01aa\38\38\39\39\39\39\3:\3:\3:\3:")
        buf.write("\7:\u01b7\n:\f:\16:\u01ba\13:\3:\3:\3;\3;\3;\3;\7;\u01c2")
        buf.write("\n;\f;\16;\u01c5\13;\3;\3;\3;\3;\3;\3<\3<\3<\3=\3=\3>")
        buf.write("\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3")
        buf.write("P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3")
        buf.write("\u01c3\2Y\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\2k\2")
        buf.write("m\66o\67q8s9u:w;y<{=}\2\177\2\u0081\2\u0083\2\u0085\2")
        buf.write("\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1")
        buf.write("\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af")
        buf.write("\2\3\2\"\4\2GGgg\3\2//\3\2\62;\5\2C\\aac|\6\2\62;C\\a")
        buf.write("ac|\5\2\n\13\16\17\"\"\4\2\f\f\17\17\4\2CCcc\4\2DDdd\4")
        buf.write("\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\2\u01f9\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\3\u00b1\3\2\2\2\5\u00b6\3\2\2\2\7")
        buf.write("\u00b8\3\2\2\2\t\u00be\3\2\2\2\13\u00c5\3\2\2\2\r\u00c9")
        buf.write("\3\2\2\2\17\u00cf\3\2\2\2\21\u00d5\3\2\2\2\23\u00d9\3")
        buf.write("\2\2\2\25\u00de\3\2\2\2\27\u00e3\3\2\2\2\31\u00ef\3\2")
        buf.write("\2\2\33\u00f5\3\2\2\2\35\u00fe\3\2\2\2\37\u0101\3\2\2")
        buf.write("\2!\u0106\3\2\2\2#\u010a\3\2\2\2%\u010f\3\2\2\2\'\u0115")
        buf.write("\3\2\2\2)\u011a\3\2\2\2+\u0121\3\2\2\2-\u0126\3\2\2\2")
        buf.write("/\u012b\3\2\2\2\61\u012f\3\2\2\2\63\u0131\3\2\2\2\65\u0133")
        buf.write("\3\2\2\2\67\u0135\3\2\2\29\u0137\3\2\2\2;\u0139\3\2\2")
        buf.write("\2=\u013b\3\2\2\2?\u013d\3\2\2\2A\u013f\3\2\2\2C\u0141")
        buf.write("\3\2\2\2E\u0143\3\2\2\2G\u0145\3\2\2\2I\u0147\3\2\2\2")
        buf.write("K\u0149\3\2\2\2M\u014c\3\2\2\2O\u014f\3\2\2\2Q\u0152\3")
        buf.write("\2\2\2S\u0155\3\2\2\2U\u0157\3\2\2\2W\u0159\3\2\2\2Y\u015c")
        buf.write("\3\2\2\2[\u015f\3\2\2\2]\u0162\3\2\2\2_\u0164\3\2\2\2")
        buf.write("a\u0166\3\2\2\2c\u0168\3\2\2\2e\u018e\3\2\2\2g\u0191\3")
        buf.write("\2\2\2i\u0195\3\2\2\2k\u019e\3\2\2\2m\u01a0\3\2\2\2o\u01a8")
        buf.write("\3\2\2\2q\u01ae\3\2\2\2s\u01b2\3\2\2\2u\u01bd\3\2\2\2")
        buf.write("w\u01cb\3\2\2\2y\u01ce\3\2\2\2{\u01d0\3\2\2\2}\u01d2\3")
        buf.write("\2\2\2\177\u01d4\3\2\2\2\u0081\u01d6\3\2\2\2\u0083\u01d8")
        buf.write("\3\2\2\2\u0085\u01da\3\2\2\2\u0087\u01dc\3\2\2\2\u0089")
        buf.write("\u01de\3\2\2\2\u008b\u01e0\3\2\2\2\u008d\u01e2\3\2\2\2")
        buf.write("\u008f\u01e4\3\2\2\2\u0091\u01e6\3\2\2\2\u0093\u01e8\3")
        buf.write("\2\2\2\u0095\u01ea\3\2\2\2\u0097\u01ec\3\2\2\2\u0099\u01ee")
        buf.write("\3\2\2\2\u009b\u01f0\3\2\2\2\u009d\u01f2\3\2\2\2\u009f")
        buf.write("\u01f4\3\2\2\2\u00a1\u01f6\3\2\2\2\u00a3\u01f8\3\2\2\2")
        buf.write("\u00a5\u01fa\3\2\2\2\u00a7\u01fc\3\2\2\2\u00a9\u01fe\3")
        buf.write("\2\2\2\u00ab\u0200\3\2\2\2\u00ad\u0202\3\2\2\2\u00af\u0204")
        buf.write("\3\2\2\2\u00b1\u00b2\7d\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4")
        buf.write("\7f\2\2\u00b4\u00b5\7{\2\2\u00b5\4\3\2\2\2\u00b6\u00b7")
        buf.write("\7B\2\2\u00b7\6\3\2\2\2\u00b8\u00b9\7e\2\2\u00b9\u00ba")
        buf.write("\5\u0093J\2\u00ba\u00bb\5}?\2\u00bb\u00bc\5\u00a1Q\2\u00bc")
        buf.write("\u00bd\5\u00a1Q\2\u00bd\b\3\2\2\2\u00be\u00bf\7t\2\2\u00bf")
        buf.write("\u00c0\5\u0085C\2\u00c0\u00c1\5\u00a3R\2\u00c1\u00c2\5")
        buf.write("\u00a5S\2\u00c2\u00c3\5\u009fP\2\u00c3\u00c4\5\u0097L")
        buf.write("\2\u00c4\n\3\2\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\5\u0097")
        buf.write("L\2\u00c7\u00c8\5\u00a3R\2\u00c8\f\3\2\2\2\u00c9\u00ca")
        buf.write("\7h\2\2\u00ca\u00cb\5\u0093J\2\u00cb\u00cc\5\u0099M\2")
        buf.write("\u00cc\u00cd\5}?\2\u00cd\u00ce\5\u00a3R\2\u00ce\16\3\2")
        buf.write("\2\2\u00cf\u00d0\7e\2\2\u00d0\u00d1\5\u0099M\2\u00d1\u00d2")
        buf.write("\5\u0097L\2\u00d2\u00d3\5\u00a1Q\2\u00d3\u00d4\5\u00a3")
        buf.write("R\2\u00d4\20\3\2\2\2\u00d5\u00d6\7x\2\2\u00d6\u00d7\5")
        buf.write("}?\2\u00d7\u00d8\5\u009fP\2\u00d8\22\3\2\2\2\u00d9\u00da")
        buf.write("\7h\2\2\u00da\u00db\5\u00a5S\2\u00db\u00dc\5\u0097L\2")
        buf.write("\u00dc\u00dd\5\u0081A\2\u00dd\24\3\2\2\2\u00de\u00df\7")
        buf.write("x\2\2\u00df\u00e0\5\u0099M\2\u00e0\u00e1\5\u008dG\2\u00e1")
        buf.write("\u00e2\5\u0083B\2\u00e2\26\3\2\2\2\u00e3\u00e4\7e\2\2")
        buf.write("\u00e4\u00e5\5\u0099M\2\u00e5\u00e6\5\u0097L\2\u00e6\u00e7")
        buf.write("\5\u00a1Q\2\u00e7\u00e8\5\u00a3R\2\u00e8\u00e9\5\u009f")
        buf.write("P\2\u00e9\u00ea\5\u00a5S\2\u00ea\u00eb\5\u0081A\2\u00eb")
        buf.write("\u00ec\5\u00a3R\2\u00ec\u00ed\5\u0099M\2\u00ed\u00ee\5")
        buf.write("\u009fP\2\u00ee\30\3\2\2\2\u00ef\u00f0\7d\2\2\u00f0\u00f1")
        buf.write("\5\u009fP\2\u00f1\u00f2\5\u0085C\2\u00f2\u00f3\5}?\2\u00f3")
        buf.write("\u00f4\5\u0091I\2\u00f4\32\3\2\2\2\u00f5\u00f6\7e\2\2")
        buf.write("\u00f6\u00f7\5\u0099M\2\u00f7\u00f8\5\u0097L\2\u00f8\u00f9")
        buf.write("\5\u00a3R\2\u00f9\u00fa\5\u008dG\2\u00fa\u00fb\5\u0097")
        buf.write("L\2\u00fb\u00fc\5\u00a5S\2\u00fc\u00fd\5\u0085C\2\u00fd")
        buf.write("\34\3\2\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100\5\u0087D\2")
        buf.write("\u0100\36\3\2\2\2\u0101\u0102\7g\2\2\u0102\u0103\5\u0093")
        buf.write("J\2\u0103\u0104\5\u00a1Q\2\u0104\u0105\5\u0085C\2\u0105")
        buf.write(" \3\2\2\2\u0106\u0107\7h\2\2\u0107\u0108\5\u0099M\2\u0108")
        buf.write("\u0109\5\u009fP\2\u0109\"\3\2\2\2\u010a\u010b\7v\2\2\u010b")
        buf.write("\u010c\5\u009fP\2\u010c\u010d\5\u00a5S\2\u010d\u010e\5")
        buf.write("\u0085C\2\u010e$\3\2\2\2\u010f\u0110\7h\2\2\u0110\u0111")
        buf.write("\5}?\2\u0111\u0112\5\u0093J\2\u0112\u0113\5\u00a1Q\2\u0113")
        buf.write("\u0114\5\u0085C\2\u0114&\3\2\2\2\u0115\u0116\7d\2\2\u0116")
        buf.write("\u0117\5\u0099M\2\u0117\u0118\5\u0099M\2\u0118\u0119\5")
        buf.write("\u0093J\2\u0119(\3\2\2\2\u011a\u011b\7u\2\2\u011b\u011c")
        buf.write("\5\u00a3R\2\u011c\u011d\5\u009fP\2\u011d\u011e\5\u008d")
        buf.write("G\2\u011e\u011f\5\u0097L\2\u011f\u0120\5\u0089E\2\u0120")
        buf.write("*\3\2\2\2\u0121\u0122\7p\2\2\u0122\u0123\5\u00a5S\2\u0123")
        buf.write("\u0124\5\u0093J\2\u0124\u0125\5\u0093J\2\u0125,\3\2\2")
        buf.write("\2\u0126\u0127\7u\2\2\u0127\u0128\5\u0085C\2\u0128\u0129")
        buf.write("\5\u0093J\2\u0129\u012a\5\u0087D\2\u012a.\3\2\2\2\u012b")
        buf.write("\u012c\7p\2\2\u012c\u012d\5\u0085C\2\u012d\u012e\5\u00a9")
        buf.write("U\2\u012e\60\3\2\2\2\u012f\u0130\7?\2\2\u0130\62\3\2\2")
        buf.write("\2\u0131\u0132\7}\2\2\u0132\64\3\2\2\2\u0133\u0134\7\177")
        buf.write("\2\2\u0134\66\3\2\2\2\u0135\u0136\7*\2\2\u01368\3\2\2")
        buf.write("\2\u0137\u0138\7+\2\2\u0138:\3\2\2\2\u0139\u013a\7=\2")
        buf.write("\2\u013a<\3\2\2\2\u013b\u013c\7.\2\2\u013c>\3\2\2\2\u013d")
        buf.write("\u013e\7\60\2\2\u013e@\3\2\2\2\u013f\u0140\7-\2\2\u0140")
        buf.write("B\3\2\2\2\u0141\u0142\7/\2\2\u0142D\3\2\2\2\u0143\u0144")
        buf.write("\7\61\2\2\u0144F\3\2\2\2\u0145\u0146\7\'\2\2\u0146H\3")
        buf.write("\2\2\2\u0147\u0148\7#\2\2\u0148J\3\2\2\2\u0149\u014a\7")
        buf.write("~\2\2\u014a\u014b\7~\2\2\u014bL\3\2\2\2\u014c\u014d\7")
        buf.write("(\2\2\u014d\u014e\7(\2\2\u014eN\3\2\2\2\u014f\u0150\7")
        buf.write("?\2\2\u0150\u0151\7?\2\2\u0151P\3\2\2\2\u0152\u0153\7")
        buf.write("#\2\2\u0153\u0154\7?\2\2\u0154R\3\2\2\2\u0155\u0156\7")
        buf.write(">\2\2\u0156T\3\2\2\2\u0157\u0158\7@\2\2\u0158V\3\2\2\2")
        buf.write("\u0159\u015a\7>\2\2\u015a\u015b\7?\2\2\u015bX\3\2\2\2")
        buf.write("\u015c\u015d\7@\2\2\u015d\u015e\7?\2\2\u015eZ\3\2\2\2")
        buf.write("\u015f\u0160\7<\2\2\u0160\u0161\7?\2\2\u0161\\\3\2\2\2")
        buf.write("\u0162\u0163\7`\2\2\u0163^\3\2\2\2\u0164\u0165\7,\2\2")
        buf.write("\u0165`\3\2\2\2\u0166\u0167\7<\2\2\u0167b\3\2\2\2\u0168")
        buf.write("\u0169\7>\2\2\u0169\u016a\7/\2\2\u016ad\3\2\2\2\u016b")
        buf.write("\u016d\5k\66\2\u016c\u016b\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3")
        buf.write("\2\2\2\u0170\u0175\5? \2\u0171\u0174\5k\66\2\u0172\u0174")
        buf.write("\5i\65\2\u0173\u0171\3\2\2\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u018f\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u017a\5")
        buf.write("k\66\2\u0179\u0178\3\2\2\2\u017a\u017d\3\2\2\2\u017b\u0179")
        buf.write("\3\2\2\2\u017b\u017c\3\2\2\2\u017c\u017e\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017e\u0180\5? \2\u017f\u0181\5k\66\2\u0180")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0180\3\2\2\2")
        buf.write("\u0182\u0183\3\2\2\2\u0183\u0185\3\2\2\2\u0184\u0186\5")
        buf.write("i\65\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186\u018f")
        buf.write("\3\2\2\2\u0187\u0189\5k\66\2\u0188\u0187\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018c\3\2\2\2\u018c\u018d\5i\65\2\u018d\u018f\3")
        buf.write("\2\2\2\u018e\u016c\3\2\2\2\u018e\u017b\3\2\2\2\u018e\u0188")
        buf.write("\3\2\2\2\u018ff\3\2\2\2\u0190\u0192\5k\66\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194h\3\2\2\2\u0195\u0197\t\2\2\2\u0196")
        buf.write("\u0198\t\3\2\2\u0197\u0196\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198\u019a\3\2\2\2\u0199\u019b\5k\66\2\u019a\u0199\3")
        buf.write("\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019dj\3\2\2\2\u019e\u019f\t\4\2\2\u019fl\3\2")
        buf.write("\2\2\u01a0\u01a4\t\5\2\2\u01a1\u01a3\t\6\2\2\u01a2\u01a1")
        buf.write("\3\2\2\2\u01a3\u01a6\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5n\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7")
        buf.write("\u01a9\t\7\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01ad\b8\2\2\u01adp\3\2\2\2\u01ae\u01af\7")
        buf.write("\f\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\b9\2\2\u01b1r\3")
        buf.write("\2\2\2\u01b2\u01b3\7\61\2\2\u01b3\u01b4\7\61\2\2\u01b4")
        buf.write("\u01b8\3\2\2\2\u01b5\u01b7\n\b\2\2\u01b6\u01b5\3\2\2\2")
        buf.write("\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3")
        buf.write("\2\2\2\u01b9\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc")
        buf.write("\b:\2\2\u01bct\3\2\2\2\u01bd\u01be\7\61\2\2\u01be\u01bf")
        buf.write("\7,\2\2\u01bf\u01c3\3\2\2\2\u01c0\u01c2\13\2\2\2\u01c1")
        buf.write("\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c3\u01c1\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01c3\3")
        buf.write("\2\2\2\u01c6\u01c7\7,\2\2\u01c7\u01c8\7\61\2\2\u01c8\u01c9")
        buf.write("\3\2\2\2\u01c9\u01ca\b;\2\2\u01cav\3\2\2\2\u01cb\u01cc")
        buf.write("\13\2\2\2\u01cc\u01cd\b<\3\2\u01cdx\3\2\2\2\u01ce\u01cf")
        buf.write("\13\2\2\2\u01cfz\3\2\2\2\u01d0\u01d1\13\2\2\2\u01d1|\3")
        buf.write("\2\2\2\u01d2\u01d3\t\t\2\2\u01d3~\3\2\2\2\u01d4\u01d5")
        buf.write("\t\n\2\2\u01d5\u0080\3\2\2\2\u01d6\u01d7\t\13\2\2\u01d7")
        buf.write("\u0082\3\2\2\2\u01d8\u01d9\t\f\2\2\u01d9\u0084\3\2\2\2")
        buf.write("\u01da\u01db\t\2\2\2\u01db\u0086\3\2\2\2\u01dc\u01dd\t")
        buf.write("\r\2\2\u01dd\u0088\3\2\2\2\u01de\u01df\t\16\2\2\u01df")
        buf.write("\u008a\3\2\2\2\u01e0\u01e1\t\17\2\2\u01e1\u008c\3\2\2")
        buf.write("\2\u01e2\u01e3\t\20\2\2\u01e3\u008e\3\2\2\2\u01e4\u01e5")
        buf.write("\t\21\2\2\u01e5\u0090\3\2\2\2\u01e6\u01e7\t\22\2\2\u01e7")
        buf.write("\u0092\3\2\2\2\u01e8\u01e9\t\23\2\2\u01e9\u0094\3\2\2")
        buf.write("\2\u01ea\u01eb\t\24\2\2\u01eb\u0096\3\2\2\2\u01ec\u01ed")
        buf.write("\t\25\2\2\u01ed\u0098\3\2\2\2\u01ee\u01ef\t\26\2\2\u01ef")
        buf.write("\u009a\3\2\2\2\u01f0\u01f1\t\27\2\2\u01f1\u009c\3\2\2")
        buf.write("\2\u01f2\u01f3\t\30\2\2\u01f3\u009e\3\2\2\2\u01f4\u01f5")
        buf.write("\t\31\2\2\u01f5\u00a0\3\2\2\2\u01f6\u01f7\t\32\2\2\u01f7")
        buf.write("\u00a2\3\2\2\2\u01f8\u01f9\t\33\2\2\u01f9\u00a4\3\2\2")
        buf.write("\2\u01fa\u01fb\t\34\2\2\u01fb\u00a6\3\2\2\2\u01fc\u01fd")
        buf.write("\t\35\2\2\u01fd\u00a8\3\2\2\2\u01fe\u01ff\t\36\2\2\u01ff")
        buf.write("\u00aa\3\2\2\2\u0200\u0201\t\37\2\2\u0201\u00ac\3\2\2")
        buf.write("\2\u0202\u0203\t \2\2\u0203\u00ae\3\2\2\2\u0204\u0205")
        buf.write("\t!\2\2\u0205\u00b0\3\2\2\2\22\2\u016e\u0173\u0175\u017b")
        buf.write("\u0182\u0185\u018a\u018e\u0193\u0197\u019c\u01a4\u01aa")
        buf.write("\u01b8\u01c3\4\b\2\2\3<\2")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
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
    TRUE = 17
    FALSE = 18
    BOOL = 19
    STRING = 20
    NULL = 21
    SELF = 22
    NEW = 23
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
    EXP = 46
    MUL = 47
    COLON = 48
    EXTENDS = 49
    FLOATLIT = 50
    INTLIT = 51
    ID = 52
    WS = 53
    NEWLINE = 54
    LINE_COMMENT = 55
    BLOCK_COMMENT = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'body'", "'@'", "'='", "'{'", "'}'", "'('", "')'", "';'", "','", 
            "'.'", "'+'", "'-'", "'/'", "'%'", "'!'", "'||'", "'&&'", "'=='", 
            "'!='", "'<'", "'>'", "'<='", "'>='", "':='", "'^'", "'*'", 
            "':'", "'<-'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "RETURN", "INT", "FLOAT", "CONST", "VAR", "FUNC", "VOID", 
            "CONSTRUCTOR", "BREAK", "CONTINUE", "IF", "ELSE", "FOR", "TRUE", 
            "FALSE", "BOOL", "STRING", "NULL", "SELF", "NEW", "EQ", "LB", 
            "RB", "LP", "RP", "SM", "CM", "DOT", "ADD", "SUB", "DIV", "MOD", 
            "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", "LESS", "GREATER", 
            "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "EXP", "MUL", "COLON", 
            "EXTENDS", "FLOATLIT", "INTLIT", "ID", "WS", "NEWLINE", "LINE_COMMENT", 
            "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "CLASS", "RETURN", "INT", "FLOAT", "CONST", 
                  "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", "CONTINUE", 
                  "IF", "ELSE", "FOR", "TRUE", "FALSE", "BOOL", "STRING", 
                  "NULL", "SELF", "NEW", "EQ", "LB", "RB", "LP", "RP", "SM", 
                  "CM", "DOT", "ADD", "SUB", "DIV", "MOD", "NOT", "OR", 
                  "AND", "EQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", 
                  "GREATEREQUAL", "ASSIGN", "EXP", "MUL", "COLON", "EXTENDS", 
                  "FLOATLIT", "INTLIT", "EXPONENT", "DIGIT", "ID", "WS", 
                  "NEWLINE", "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "A", "B", "C", "D", 
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

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
            actions[58] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


