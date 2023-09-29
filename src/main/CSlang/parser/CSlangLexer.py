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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u028f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\5\2\u00d2\n\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\7\66")
        buf.write("\u0194\n\66\f\66\16\66\u0197\13\66\5\66\u0199\n\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\5\67\u01a1\n\67\38\58\u01a4")
        buf.write("\n8\38\68\u01a7\n8\r8\168\u01a8\38\38\38\78\u01ae\n8\f")
        buf.write("8\168\u01b1\138\38\58\u01b4\n8\38\68\u01b7\n8\r8\168\u01b8")
        buf.write("\38\38\68\u01bd\n8\r8\168\u01be\38\58\u01c2\n8\38\58\u01c5")
        buf.write("\n8\38\68\u01c8\n8\r8\168\u01c9\38\38\58\u01ce\n8\39\6")
        buf.write("9\u01d1\n9\r9\169\u01d2\3:\3:\5:\u01d7\n:\3;\3;\7;\u01db")
        buf.write("\n;\f;\16;\u01de\13;\3;\3;\3;\3<\3<\5<\u01e5\n<\3<\6<")
        buf.write("\u01e8\n<\r<\16<\u01e9\3=\3=\3>\3>\3>\3>\7>\u01f2\n>\f")
        buf.write(">\16>\u01f5\13>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\7?\u0202")
        buf.write("\n?\f?\16?\u0205\13?\3?\3?\3?\3?\3?\3@\3@\7@\u020e\n@")
        buf.write("\f@\16@\u0211\13@\3A\6A\u0214\nA\rA\16A\u0215\3A\3A\3")
        buf.write("B\3B\3B\3B\3C\3C\3C\3C\7C\u0222\nC\fC\16C\u0225\13C\3")
        buf.write("C\3C\3D\3D\3D\3D\7D\u022d\nD\fD\16D\u0230\13D\3D\3D\3")
        buf.write("D\3D\3D\3E\3E\3E\3F\3F\7F\u023c\nF\fF\16F\u023f\13F\3")
        buf.write("F\5F\u0242\nF\3F\3F\3G\3G\7G\u0248\nG\fG\16G\u024b\13")
        buf.write("G\3G\3G\3G\3H\3H\5H\u0252\nH\3I\3I\3I\3J\3J\3J\5J\u025a")
        buf.write("\nJ\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3")
        buf.write("S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3")
        buf.write("\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3b\3b\3c\3c\3d\3")
        buf.write("d\3\u022e\2e\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\67m8o9q:s;u<w\2y\2{=}>\177?\u0081@\u0083A\u0085B\u0087")
        buf.write("C\u0089D\u008bE\u008dF\u008f\2\u0091\2\u0093\2\u0095\2")
        buf.write("\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1")
        buf.write("\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf")
        buf.write("\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\3\2(\4\2GGgg\4\2--")
        buf.write("//\3\2\62;\4\2\f\f\17\17\4\2,,\61\61\3\2\61\61\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\n\13\16\17\"\"\6\3\n\f\16\17$")
        buf.write("$^^\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\3\2^^\4\2CCcc")
        buf.write("\4\2DDdd\4\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2K")
        buf.write("Kkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4")
        buf.write("\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXx")
        buf.write("x\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u0295\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\3\u00c9\3\2\2\2\5\u00d3\3\2\2\2\7\u00d9\3\2\2\2\t\u00e0")
        buf.write("\3\2\2\2\13\u00e4\3\2\2\2\r\u00ea\3\2\2\2\17\u00f0\3\2")
        buf.write("\2\2\21\u00f4\3\2\2\2\23\u00f9\3\2\2\2\25\u00fe\3\2\2")
        buf.write("\2\27\u010a\3\2\2\2\31\u0110\3\2\2\2\33\u0119\3\2\2\2")
        buf.write("\35\u011c\3\2\2\2\37\u0121\3\2\2\2!\u0125\3\2\2\2#\u012a")
        buf.write("\3\2\2\2%\u0130\3\2\2\2\'\u0135\3\2\2\2)\u013c\3\2\2\2")
        buf.write("+\u0141\3\2\2\2-\u0146\3\2\2\2/\u014a\3\2\2\2\61\u014c")
        buf.write("\3\2\2\2\63\u014e\3\2\2\2\65\u0150\3\2\2\2\67\u0152\3")
        buf.write("\2\2\29\u0154\3\2\2\2;\u0156\3\2\2\2=\u0158\3\2\2\2?\u015a")
        buf.write("\3\2\2\2A\u015c\3\2\2\2C\u015e\3\2\2\2E\u0160\3\2\2\2")
        buf.write("G\u0162\3\2\2\2I\u0164\3\2\2\2K\u0166\3\2\2\2M\u0168\3")
        buf.write("\2\2\2O\u016a\3\2\2\2Q\u016c\3\2\2\2S\u016f\3\2\2\2U\u0172")
        buf.write("\3\2\2\2W\u0175\3\2\2\2Y\u0178\3\2\2\2[\u017a\3\2\2\2")
        buf.write("]\u017c\3\2\2\2_\u017f\3\2\2\2a\u0182\3\2\2\2c\u0185\3")
        buf.write("\2\2\2e\u0187\3\2\2\2g\u0189\3\2\2\2i\u018b\3\2\2\2k\u018e")
        buf.write("\3\2\2\2m\u01a0\3\2\2\2o\u01cd\3\2\2\2q\u01d0\3\2\2\2")
        buf.write("s\u01d6\3\2\2\2u\u01d8\3\2\2\2w\u01e2\3\2\2\2y\u01eb\3")
        buf.write("\2\2\2{\u01ed\3\2\2\2}\u01f8\3\2\2\2\177\u020b\3\2\2\2")
        buf.write("\u0081\u0213\3\2\2\2\u0083\u0219\3\2\2\2\u0085\u021d\3")
        buf.write("\2\2\2\u0087\u0228\3\2\2\2\u0089\u0236\3\2\2\2\u008b\u0239")
        buf.write("\3\2\2\2\u008d\u0245\3\2\2\2\u008f\u0251\3\2\2\2\u0091")
        buf.write("\u0253\3\2\2\2\u0093\u0259\3\2\2\2\u0095\u025b\3\2\2\2")
        buf.write("\u0097\u025d\3\2\2\2\u0099\u025f\3\2\2\2\u009b\u0261\3")
        buf.write("\2\2\2\u009d\u0263\3\2\2\2\u009f\u0265\3\2\2\2\u00a1\u0267")
        buf.write("\3\2\2\2\u00a3\u0269\3\2\2\2\u00a5\u026b\3\2\2\2\u00a7")
        buf.write("\u026d\3\2\2\2\u00a9\u026f\3\2\2\2\u00ab\u0271\3\2\2\2")
        buf.write("\u00ad\u0273\3\2\2\2\u00af\u0275\3\2\2\2\u00b1\u0277\3")
        buf.write("\2\2\2\u00b3\u0279\3\2\2\2\u00b5\u027b\3\2\2\2\u00b7\u027d")
        buf.write("\3\2\2\2\u00b9\u027f\3\2\2\2\u00bb\u0281\3\2\2\2\u00bd")
        buf.write("\u0283\3\2\2\2\u00bf\u0285\3\2\2\2\u00c1\u0287\3\2\2\2")
        buf.write("\u00c3\u0289\3\2\2\2\u00c5\u028b\3\2\2\2\u00c7\u028d\3")
        buf.write("\2\2\2\u00c9\u00ca\5\61\31\2\u00ca\u00cb\5q9\2\u00cb\u00d1")
        buf.write("\5\63\32\2\u00cc\u00d2\5\t\5\2\u00cd\u00d2\5\13\6\2\u00ce")
        buf.write("\u00d2\5%\23\2\u00cf\u00d2\5\'\24\2\u00d0\u00d2\5\177")
        buf.write("@\2\u00d1\u00cc\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d1\u00ce")
        buf.write("\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write("\4\3\2\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5\5\u00abV\2\u00d5")
        buf.write("\u00d6\5\u0095K\2\u00d6\u00d7\5\u00b9]\2\u00d7\u00d8\5")
        buf.write("\u00b9]\2\u00d8\6\3\2\2\2\u00d9\u00da\7t\2\2\u00da\u00db")
        buf.write("\5\u009dO\2\u00db\u00dc\5\u00bb^\2\u00dc\u00dd\5\u00bd")
        buf.write("_\2\u00dd\u00de\5\u00b7\\\2\u00de\u00df\5\u00afX\2\u00df")
        buf.write("\b\3\2\2\2\u00e0\u00e1\7k\2\2\u00e1\u00e2\5\u00afX\2\u00e2")
        buf.write("\u00e3\5\u00bb^\2\u00e3\n\3\2\2\2\u00e4\u00e5\7h\2\2\u00e5")
        buf.write("\u00e6\5\u00abV\2\u00e6\u00e7\5\u00b1Y\2\u00e7\u00e8\5")
        buf.write("\u0095K\2\u00e8\u00e9\5\u00bb^\2\u00e9\f\3\2\2\2\u00ea")
        buf.write("\u00eb\7e\2\2\u00eb\u00ec\5\u00b1Y\2\u00ec\u00ed\5\u00af")
        buf.write("X\2\u00ed\u00ee\5\u00b9]\2\u00ee\u00ef\5\u00bb^\2\u00ef")
        buf.write("\16\3\2\2\2\u00f0\u00f1\7x\2\2\u00f1\u00f2\5\u0095K\2")
        buf.write("\u00f2\u00f3\5\u00b7\\\2\u00f3\20\3\2\2\2\u00f4\u00f5")
        buf.write("\7h\2\2\u00f5\u00f6\5\u00bd_\2\u00f6\u00f7\5\u00afX\2")
        buf.write("\u00f7\u00f8\5\u0099M\2\u00f8\22\3\2\2\2\u00f9\u00fa\7")
        buf.write("x\2\2\u00fa\u00fb\5\u00b1Y\2\u00fb\u00fc\5\u00a5S\2\u00fc")
        buf.write("\u00fd\5\u009bN\2\u00fd\24\3\2\2\2\u00fe\u00ff\7e\2\2")
        buf.write("\u00ff\u0100\5\u00b1Y\2\u0100\u0101\5\u00afX\2\u0101\u0102")
        buf.write("\5\u00b9]\2\u0102\u0103\5\u00bb^\2\u0103\u0104\5\u00b7")
        buf.write("\\\2\u0104\u0105\5\u00bd_\2\u0105\u0106\5\u0099M\2\u0106")
        buf.write("\u0107\5\u00bb^\2\u0107\u0108\5\u00b1Y\2\u0108\u0109\5")
        buf.write("\u00b7\\\2\u0109\26\3\2\2\2\u010a\u010b\7d\2\2\u010b\u010c")
        buf.write("\5\u00b7\\\2\u010c\u010d\5\u009dO\2\u010d\u010e\5\u0095")
        buf.write("K\2\u010e\u010f\5\u00a9U\2\u010f\30\3\2\2\2\u0110\u0111")
        buf.write("\7e\2\2\u0111\u0112\5\u00b1Y\2\u0112\u0113\5\u00afX\2")
        buf.write("\u0113\u0114\5\u00bb^\2\u0114\u0115\5\u00a5S\2\u0115\u0116")
        buf.write("\5\u00afX\2\u0116\u0117\5\u00bd_\2\u0117\u0118\5\u009d")
        buf.write("O\2\u0118\32\3\2\2\2\u0119\u011a\7k\2\2\u011a\u011b\5")
        buf.write("\u009fP\2\u011b\34\3\2\2\2\u011c\u011d\7g\2\2\u011d\u011e")
        buf.write("\5\u00abV\2\u011e\u011f\5\u00b9]\2\u011f\u0120\5\u009d")
        buf.write("O\2\u0120\36\3\2\2\2\u0121\u0122\7h\2\2\u0122\u0123\5")
        buf.write("\u00b1Y\2\u0123\u0124\5\u00b7\\\2\u0124 \3\2\2\2\u0125")
        buf.write("\u0126\7v\2\2\u0126\u0127\5\u00b7\\\2\u0127\u0128\5\u00bd")
        buf.write("_\2\u0128\u0129\5\u009dO\2\u0129\"\3\2\2\2\u012a\u012b")
        buf.write("\7h\2\2\u012b\u012c\5\u0095K\2\u012c\u012d\5\u00abV\2")
        buf.write("\u012d\u012e\5\u00b9]\2\u012e\u012f\5\u009dO\2\u012f$")
        buf.write("\3\2\2\2\u0130\u0131\7d\2\2\u0131\u0132\5\u00b1Y\2\u0132")
        buf.write("\u0133\5\u00b1Y\2\u0133\u0134\5\u00abV\2\u0134&\3\2\2")
        buf.write("\2\u0135\u0136\7u\2\2\u0136\u0137\5\u00bb^\2\u0137\u0138")
        buf.write("\5\u00b7\\\2\u0138\u0139\5\u00a5S\2\u0139\u013a\5\u00af")
        buf.write("X\2\u013a\u013b\5\u00a1Q\2\u013b(\3\2\2\2\u013c\u013d")
        buf.write("\7p\2\2\u013d\u013e\5\u00bd_\2\u013e\u013f\5\u00abV\2")
        buf.write("\u013f\u0140\5\u00abV\2\u0140*\3\2\2\2\u0141\u0142\7u")
        buf.write("\2\2\u0142\u0143\5\u009dO\2\u0143\u0144\5\u00abV\2\u0144")
        buf.write("\u0145\5\u009fP\2\u0145,\3\2\2\2\u0146\u0147\7p\2\2\u0147")
        buf.write("\u0148\5\u009dO\2\u0148\u0149\5\u00c1a\2\u0149.\3\2\2")
        buf.write("\2\u014a\u014b\7B\2\2\u014b\60\3\2\2\2\u014c\u014d\7]")
        buf.write("\2\2\u014d\62\3\2\2\2\u014e\u014f\7_\2\2\u014f\64\3\2")
        buf.write("\2\2\u0150\u0151\7?\2\2\u0151\66\3\2\2\2\u0152\u0153\7")
        buf.write("}\2\2\u01538\3\2\2\2\u0154\u0155\7\177\2\2\u0155:\3\2")
        buf.write("\2\2\u0156\u0157\7*\2\2\u0157<\3\2\2\2\u0158\u0159\7+")
        buf.write("\2\2\u0159>\3\2\2\2\u015a\u015b\7=\2\2\u015b@\3\2\2\2")
        buf.write("\u015c\u015d\7.\2\2\u015dB\3\2\2\2\u015e\u015f\7\60\2")
        buf.write("\2\u015fD\3\2\2\2\u0160\u0161\7-\2\2\u0161F\3\2\2\2\u0162")
        buf.write("\u0163\7/\2\2\u0163H\3\2\2\2\u0164\u0165\7\61\2\2\u0165")
        buf.write("J\3\2\2\2\u0166\u0167\7^\2\2\u0167L\3\2\2\2\u0168\u0169")
        buf.write("\7\'\2\2\u0169N\3\2\2\2\u016a\u016b\7#\2\2\u016bP\3\2")
        buf.write("\2\2\u016c\u016d\7~\2\2\u016d\u016e\7~\2\2\u016eR\3\2")
        buf.write("\2\2\u016f\u0170\7(\2\2\u0170\u0171\7(\2\2\u0171T\3\2")
        buf.write("\2\2\u0172\u0173\7?\2\2\u0173\u0174\7?\2\2\u0174V\3\2")
        buf.write("\2\2\u0175\u0176\7#\2\2\u0176\u0177\7?\2\2\u0177X\3\2")
        buf.write("\2\2\u0178\u0179\7>\2\2\u0179Z\3\2\2\2\u017a\u017b\7@")
        buf.write("\2\2\u017b\\\3\2\2\2\u017c\u017d\7>\2\2\u017d\u017e\7")
        buf.write("?\2\2\u017e^\3\2\2\2\u017f\u0180\7@\2\2\u0180\u0181\7")
        buf.write("?\2\2\u0181`\3\2\2\2\u0182\u0183\7<\2\2\u0183\u0184\7")
        buf.write("?\2\2\u0184b\3\2\2\2\u0185\u0186\7`\2\2\u0186d\3\2\2\2")
        buf.write("\u0187\u0188\7,\2\2\u0188f\3\2\2\2\u0189\u018a\7<\2\2")
        buf.write("\u018ah\3\2\2\2\u018b\u018c\7>\2\2\u018c\u018d\7/\2\2")
        buf.write("\u018dj\3\2\2\2\u018e\u0198\5\61\31\2\u018f\u0195\5m\67")
        buf.write("\2\u0190\u0191\5A!\2\u0191\u0192\5m\67\2\u0192\u0194\3")
        buf.write("\2\2\2\u0193\u0190\3\2\2\2\u0194\u0197\3\2\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0199\3\2\2\2\u0197")
        buf.write("\u0195\3\2\2\2\u0198\u018f\3\2\2\2\u0198\u0199\3\2\2\2")
        buf.write("\u0199\u019a\3\2\2\2\u019a\u019b\5\63\32\2\u019bl\3\2")
        buf.write("\2\2\u019c\u01a1\5q9\2\u019d\u01a1\5o8\2\u019e\u01a1\5")
        buf.write("u;\2\u019f\u01a1\5s:\2\u01a0\u019c\3\2\2\2\u01a0\u019d")
        buf.write("\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("n\3\2\2\2\u01a2\u01a4\7/\2\2\u01a3\u01a2\3\2\2\2\u01a3")
        buf.write("\u01a4\3\2\2\2\u01a4\u01a6\3\2\2\2\u01a5\u01a7\5y=\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01af\5")
        buf.write("C\"\2\u01ab\u01ae\5y=\2\u01ac\u01ae\5w<\2\u01ad\u01ab")
        buf.write("\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01ce\3\2\2\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b2\u01b4\7/\2\2\u01b3\u01b2\3")
        buf.write("\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b7")
        buf.write("\5y=\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba")
        buf.write("\u01bc\5C\"\2\u01bb\u01bd\5y=\2\u01bc\u01bb\3\2\2\2\u01bd")
        buf.write("\u01be\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c1\3\2\2\2\u01c0\u01c2\5w<\2\u01c1\u01c0\3\2")
        buf.write("\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01ce\3\2\2\2\u01c3\u01c5")
        buf.write("\7/\2\2\u01c4\u01c3\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("\u01c7\3\2\2\2\u01c6\u01c8\5y=\2\u01c7\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01cc\5w<\2\u01cc\u01ce\3\2")
        buf.write("\2\2\u01cd\u01a3\3\2\2\2\u01cd\u01b3\3\2\2\2\u01cd\u01c4")
        buf.write("\3\2\2\2\u01cep\3\2\2\2\u01cf\u01d1\5y=\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3r\3\2\2\2\u01d4\u01d7\5!\21\2\u01d5")
        buf.write("\u01d7\5#\22\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2")
        buf.write("\u01d7t\3\2\2\2\u01d8\u01dc\7$\2\2\u01d9\u01db\5\u008f")
        buf.write("H\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e0\7$\2\2\u01e0\u01e1\b;\2\2\u01e1")
        buf.write("v\3\2\2\2\u01e2\u01e4\t\2\2\2\u01e3\u01e5\t\3\2\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e7\3\2\2\2")
        buf.write("\u01e6\u01e8\5y=\2\u01e7\u01e6\3\2\2\2\u01e8\u01e9\3\2")
        buf.write("\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01eax\3")
        buf.write("\2\2\2\u01eb\u01ec\t\4\2\2\u01ecz\3\2\2\2\u01ed\u01ee")
        buf.write("\7\61\2\2\u01ee\u01ef\7\61\2\2\u01ef\u01f3\3\2\2\2\u01f0")
        buf.write("\u01f2\n\5\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f5\3\2\2\2")
        buf.write("\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3")
        buf.write("\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f7\b>\3\2\u01f7|\3")
        buf.write("\2\2\2\u01f8\u01f9\7\61\2\2\u01f9\u01fa\7,\2\2\u01fa\u0203")
        buf.write("\3\2\2\2\u01fb\u0202\n\6\2\2\u01fc\u01fd\7,\2\2\u01fd")
        buf.write("\u01fe\7\61\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0202\n\7\2")
        buf.write("\2\u0200\u0202\5}?\2\u0201\u01fb\3\2\2\2\u0201\u01fc\3")
        buf.write("\2\2\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205")
        buf.write("\u0203\3\2\2\2\u0206\u0207\7,\2\2\u0207\u0208\7\61\2\2")
        buf.write("\u0208\u0209\3\2\2\2\u0209\u020a\b?\3\2\u020a~\3\2\2\2")
        buf.write("\u020b\u020f\t\b\2\2\u020c\u020e\t\t\2\2\u020d\u020c\3")
        buf.write("\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u0080\3\2\2\2\u0211\u020f\3\2\2\2\u0212")
        buf.write("\u0214\t\n\2\2\u0213\u0212\3\2\2\2\u0214\u0215\3\2\2\2")
        buf.write("\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0217\3")
        buf.write("\2\2\2\u0217\u0218\bA\3\2\u0218\u0082\3\2\2\2\u0219\u021a")
        buf.write("\7\f\2\2\u021a\u021b\3\2\2\2\u021b\u021c\bB\3\2\u021c")
        buf.write("\u0084\3\2\2\2\u021d\u021e\7\61\2\2\u021e\u021f\7\61\2")
        buf.write("\2\u021f\u0223\3\2\2\2\u0220\u0222\n\5\2\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2\u0223")
        buf.write("\u0224\3\2\2\2\u0224\u0226\3\2\2\2\u0225\u0223\3\2\2\2")
        buf.write("\u0226\u0227\bC\3\2\u0227\u0086\3\2\2\2\u0228\u0229\7")
        buf.write("\61\2\2\u0229\u022a\7,\2\2\u022a\u022e\3\2\2\2\u022b\u022d")
        buf.write("\13\2\2\2\u022c\u022b\3\2\2\2\u022d\u0230\3\2\2\2\u022e")
        buf.write("\u022f\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0231\3\2\2\2")
        buf.write("\u0230\u022e\3\2\2\2\u0231\u0232\7,\2\2\u0232\u0233\7")
        buf.write("\61\2\2\u0233\u0234\3\2\2\2\u0234\u0235\bD\3\2\u0235\u0088")
        buf.write("\3\2\2\2\u0236\u0237\13\2\2\2\u0237\u0238\bE\4\2\u0238")
        buf.write("\u008a\3\2\2\2\u0239\u023d\7$\2\2\u023a\u023c\5\u008f")
        buf.write("H\2\u023b\u023a\3\2\2\2\u023c\u023f\3\2\2\2\u023d\u023b")
        buf.write("\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u0241\3\2\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u0240\u0242\t\13\2\2\u0241\u0240\3\2\2")
        buf.write("\2\u0242\u0243\3\2\2\2\u0243\u0244\bF\5\2\u0244\u008c")
        buf.write("\3\2\2\2\u0245\u0249\7$\2\2\u0246\u0248\5\u008fH\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247\3\2\2\2")
        buf.write("\u0249\u024a\3\2\2\2\u024a\u024c\3\2\2\2\u024b\u0249\3")
        buf.write("\2\2\2\u024c\u024d\5\u0093J\2\u024d\u024e\bG\6\2\u024e")
        buf.write("\u008e\3\2\2\2\u024f\u0252\n\f\2\2\u0250\u0252\5\u0091")
        buf.write("I\2\u0251\u024f\3\2\2\2\u0251\u0250\3\2\2\2\u0252\u0090")
        buf.write("\3\2\2\2\u0253\u0254\7^\2\2\u0254\u0255\t\r\2\2\u0255")
        buf.write("\u0092\3\2\2\2\u0256\u0257\7^\2\2\u0257\u025a\n\r\2\2")
        buf.write("\u0258\u025a\n\16\2\2\u0259\u0256\3\2\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u025a\u0094\3\2\2\2\u025b\u025c\t\17\2\2\u025c")
        buf.write("\u0096\3\2\2\2\u025d\u025e\t\20\2\2\u025e\u0098\3\2\2")
        buf.write("\2\u025f\u0260\t\21\2\2\u0260\u009a\3\2\2\2\u0261\u0262")
        buf.write("\t\22\2\2\u0262\u009c\3\2\2\2\u0263\u0264\t\2\2\2\u0264")
        buf.write("\u009e\3\2\2\2\u0265\u0266\t\23\2\2\u0266\u00a0\3\2\2")
        buf.write("\2\u0267\u0268\t\24\2\2\u0268\u00a2\3\2\2\2\u0269\u026a")
        buf.write("\t\25\2\2\u026a\u00a4\3\2\2\2\u026b\u026c\t\26\2\2\u026c")
        buf.write("\u00a6\3\2\2\2\u026d\u026e\t\27\2\2\u026e\u00a8\3\2\2")
        buf.write("\2\u026f\u0270\t\30\2\2\u0270\u00aa\3\2\2\2\u0271\u0272")
        buf.write("\t\31\2\2\u0272\u00ac\3\2\2\2\u0273\u0274\t\32\2\2\u0274")
        buf.write("\u00ae\3\2\2\2\u0275\u0276\t\33\2\2\u0276\u00b0\3\2\2")
        buf.write("\2\u0277\u0278\t\34\2\2\u0278\u00b2\3\2\2\2\u0279\u027a")
        buf.write("\t\35\2\2\u027a\u00b4\3\2\2\2\u027b\u027c\t\36\2\2\u027c")
        buf.write("\u00b6\3\2\2\2\u027d\u027e\t\37\2\2\u027e\u00b8\3\2\2")
        buf.write("\2\u027f\u0280\t \2\2\u0280\u00ba\3\2\2\2\u0281\u0282")
        buf.write("\t!\2\2\u0282\u00bc\3\2\2\2\u0283\u0284\t\"\2\2\u0284")
        buf.write("\u00be\3\2\2\2\u0285\u0286\t#\2\2\u0286\u00c0\3\2\2\2")
        buf.write("\u0287\u0288\t$\2\2\u0288\u00c2\3\2\2\2\u0289\u028a\t")
        buf.write("%\2\2\u028a\u00c4\3\2\2\2\u028b\u028c\t&\2\2\u028c\u00c6")
        buf.write("\3\2\2\2\u028d\u028e\t\'\2\2\u028e\u00c8\3\2\2\2#\2\u00d1")
        buf.write("\u0195\u0198\u01a0\u01a3\u01a8\u01ad\u01af\u01b3\u01b8")
        buf.write("\u01be\u01c1\u01c4\u01c9\u01cd\u01d2\u01d6\u01dc\u01e4")
        buf.write("\u01e9\u01f3\u0201\u0203\u020f\u0215\u0223\u022e\u023d")
        buf.write("\u0241\u0249\u0251\u0259\7\3;\2\b\2\2\3E\3\3F\4\3G\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY = 1
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
    TRUE = 16
    FALSE = 17
    BOOL = 18
    STRING = 19
    NULL = 20
    SELF = 21
    NEW = 22
    AC = 23
    OB = 24
    CB = 25
    EQ = 26
    LB = 27
    RB = 28
    LP = 29
    RP = 30
    SM = 31
    CM = 32
    DOT = 33
    ADD = 34
    SUB = 35
    DIV = 36
    BS = 37
    MOD = 38
    NOT = 39
    OR = 40
    AND = 41
    EQUAL = 42
    NOTEQUAL = 43
    LESS = 44
    GREATER = 45
    LESSEQUAL = 46
    GREATEREQUAL = 47
    ASSIGN = 48
    CONCATENATION = 49
    MUL = 50
    COLON = 51
    EXTENDS = 52
    ARRAYLIT = 53
    ARRAY_ELEMENT = 54
    FLOATLIT = 55
    INTLIT = 56
    BOOLLIT = 57
    STRING_LITERAL = 58
    LineComment = 59
    BlockComment = 60
    ID = 61
    WS = 62
    NEWLINE = 63
    LINE_COMMENT = 64
    BLOCK_COMMENT = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'@'", "'['", "']'", "'='", "'{'", "'}'", "'('", "')'", "';'", 
            "','", "'.'", "'+'", "'-'", "'/'", "'\\'", "'%'", "'!'", "'||'", 
            "'&&'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "':='", 
            "'^'", "'*'", "':'", "'<-'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "ARRAY", "CLASS", "RETURN", "INT", "FLOAT", "CONST", "VAR", 
            "FUNC", "VOID", "CONSTRUCTOR", "BREAK", "CONTINUE", "IF", "ELSE", 
            "FOR", "TRUE", "FALSE", "BOOL", "STRING", "NULL", "SELF", "NEW", 
            "AC", "OB", "CB", "EQ", "LB", "RB", "LP", "RP", "SM", "CM", 
            "DOT", "ADD", "SUB", "DIV", "BS", "MOD", "NOT", "OR", "AND", 
            "EQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", 
            "ASSIGN", "CONCATENATION", "MUL", "COLON", "EXTENDS", "ARRAYLIT", 
            "ARRAY_ELEMENT", "FLOATLIT", "INTLIT", "BOOLLIT", "STRING_LITERAL", 
            "LineComment", "BlockComment", "ID", "WS", "NEWLINE", "LINE_COMMENT", 
            "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ARRAY", "CLASS", "RETURN", "INT", "FLOAT", "CONST", "VAR", 
                  "FUNC", "VOID", "CONSTRUCTOR", "BREAK", "CONTINUE", "IF", 
                  "ELSE", "FOR", "TRUE", "FALSE", "BOOL", "STRING", "NULL", 
                  "SELF", "NEW", "AC", "OB", "CB", "EQ", "LB", "RB", "LP", 
                  "RP", "SM", "CM", "DOT", "ADD", "SUB", "DIV", "BS", "MOD", 
                  "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", "LESS", "GREATER", 
                  "LESSEQUAL", "GREATEREQUAL", "ASSIGN", "CONCATENATION", 
                  "MUL", "COLON", "EXTENDS", "ARRAYLIT", "ARRAY_ELEMENT", 
                  "FLOATLIT", "INTLIT", "BOOLLIT", "STRING_LITERAL", "EXPONENT", 
                  "DIGIT", "LineComment", "BlockComment", "ID", "WS", "NEWLINE", 
                  "LINE_COMMENT", "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z" ]

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
            actions[57] = self.STRING_LITERAL_action 
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
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
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


