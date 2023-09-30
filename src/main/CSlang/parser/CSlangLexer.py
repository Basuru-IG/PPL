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
        buf.write("\u029b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\u00d6\n\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,")
        buf.write("\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\7\67\u0199\n\67\f\67\16\67\u019c")
        buf.write("\13\67\3\67\3\67\38\38\38\38\38\38\38\58\u01a7\n8\39\3")
        buf.write("9\39\39\59\u01ad\n9\3:\5:\u01b0\n:\3:\6:\u01b3\n:\r:\16")
        buf.write(":\u01b4\3:\3:\3:\7:\u01ba\n:\f:\16:\u01bd\13:\3:\5:\u01c0")
        buf.write("\n:\3:\6:\u01c3\n:\r:\16:\u01c4\3:\3:\6:\u01c9\n:\r:\16")
        buf.write(":\u01ca\3:\5:\u01ce\n:\3:\5:\u01d1\n:\3:\6:\u01d4\n:\r")
        buf.write(":\16:\u01d5\3:\3:\5:\u01da\n:\3;\6;\u01dd\n;\r;\16;\u01de")
        buf.write("\3<\3<\5<\u01e3\n<\3=\3=\7=\u01e7\n=\f=\16=\u01ea\13=")
        buf.write("\3=\3=\3=\3>\3>\5>\u01f1\n>\3>\6>\u01f4\n>\r>\16>\u01f5")
        buf.write("\3?\3?\3@\3@\3@\3@\7@\u01fe\n@\f@\16@\u0201\13@\3@\3@")
        buf.write("\3A\3A\3A\3A\3A\3A\3A\3A\3A\7A\u020e\nA\fA\16A\u0211\13")
        buf.write("A\3A\3A\3A\3A\3A\3B\3B\7B\u021a\nB\fB\16B\u021d\13B\3")
        buf.write("C\6C\u0220\nC\rC\16C\u0221\3C\3C\3D\3D\3D\3D\3E\3E\3E")
        buf.write("\3E\7E\u022e\nE\fE\16E\u0231\13E\3E\3E\3F\3F\3F\3F\7F")
        buf.write("\u0239\nF\fF\16F\u023c\13F\3F\3F\3F\3F\3F\3G\3G\3G\3H")
        buf.write("\3H\7H\u0248\nH\fH\16H\u024b\13H\3H\5H\u024e\nH\3H\3H")
        buf.write("\3I\3I\7I\u0254\nI\fI\16I\u0257\13I\3I\3I\3I\3J\3J\5J")
        buf.write("\u025e\nJ\3K\3K\3K\3L\3L\3L\5L\u0266\nL\3M\3M\3N\3N\3")
        buf.write("O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3")
        buf.write("X\3X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3")
        buf.write("`\3a\3a\3b\3b\3c\3c\3d\3d\3e\3e\3f\3f\3\u023a\2g\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o\2q\2s9u:w;")
        buf.write("y<{\2}\2\177=\u0081>\u0083?\u0085@\u0087A\u0089B\u008b")
        buf.write("C\u008dD\u008fE\u0091F\u0093\2\u0095\2\u0097\2\u0099\2")
        buf.write("\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7")
        buf.write("\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5")
        buf.write("\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf\2\u00c1\2\u00c3")
        buf.write("\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\3\2(\4\2GGgg\4\2--")
        buf.write("//\3\2\62;\4\2\f\f\17\17\4\2,,\61\61\3\2\61\61\5\2C\\")
        buf.write("aac|\6\2\62;C\\aac|\5\2\13\13\16\17\"\"\6\3\n\f\16\17")
        buf.write("$$^^\6\2\n\f\16\17$$^^\t\2$$^^ddhhppttvv\3\2^^\4\2CCc")
        buf.write("c\4\2DDdd\4\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2")
        buf.write("KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4")
        buf.write("\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXx")
        buf.write("x\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u029f\2\3\3\2\2")
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
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2")
        buf.write("w\3\2\2\2\2y\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\3\u00cd\3\2\2\2\5\u00d7\3\2\2\2\7\u00da\3\2\2")
        buf.write("\2\t\u00e0\3\2\2\2\13\u00e7\3\2\2\2\r\u00eb\3\2\2\2\17")
        buf.write("\u00f1\3\2\2\2\21\u00f7\3\2\2\2\23\u00fb\3\2\2\2\25\u0100")
        buf.write("\3\2\2\2\27\u0105\3\2\2\2\31\u0111\3\2\2\2\33\u0117\3")
        buf.write("\2\2\2\35\u0120\3\2\2\2\37\u0123\3\2\2\2!\u0128\3\2\2")
        buf.write("\2#\u012c\3\2\2\2%\u0131\3\2\2\2\'\u0137\3\2\2\2)\u013c")
        buf.write("\3\2\2\2+\u0143\3\2\2\2-\u0148\3\2\2\2/\u014d\3\2\2\2")
        buf.write("\61\u0151\3\2\2\2\63\u0153\3\2\2\2\65\u0155\3\2\2\2\67")
        buf.write("\u0157\3\2\2\29\u0159\3\2\2\2;\u015b\3\2\2\2=\u015d\3")
        buf.write("\2\2\2?\u015f\3\2\2\2A\u0161\3\2\2\2C\u0163\3\2\2\2E\u0165")
        buf.write("\3\2\2\2G\u0167\3\2\2\2I\u0169\3\2\2\2K\u016b\3\2\2\2")
        buf.write("M\u016d\3\2\2\2O\u016f\3\2\2\2Q\u0171\3\2\2\2S\u0173\3")
        buf.write("\2\2\2U\u0176\3\2\2\2W\u0179\3\2\2\2Y\u017c\3\2\2\2[\u017f")
        buf.write("\3\2\2\2]\u0181\3\2\2\2_\u0183\3\2\2\2a\u0186\3\2\2\2")
        buf.write("c\u0189\3\2\2\2e\u018c\3\2\2\2g\u018e\3\2\2\2i\u0190\3")
        buf.write("\2\2\2k\u0192\3\2\2\2m\u0195\3\2\2\2o\u01a6\3\2\2\2q\u01ac")
        buf.write("\3\2\2\2s\u01d9\3\2\2\2u\u01dc\3\2\2\2w\u01e2\3\2\2\2")
        buf.write("y\u01e4\3\2\2\2{\u01ee\3\2\2\2}\u01f7\3\2\2\2\177\u01f9")
        buf.write("\3\2\2\2\u0081\u0204\3\2\2\2\u0083\u0217\3\2\2\2\u0085")
        buf.write("\u021f\3\2\2\2\u0087\u0225\3\2\2\2\u0089\u0229\3\2\2\2")
        buf.write("\u008b\u0234\3\2\2\2\u008d\u0242\3\2\2\2\u008f\u0245\3")
        buf.write("\2\2\2\u0091\u0251\3\2\2\2\u0093\u025d\3\2\2\2\u0095\u025f")
        buf.write("\3\2\2\2\u0097\u0265\3\2\2\2\u0099\u0267\3\2\2\2\u009b")
        buf.write("\u0269\3\2\2\2\u009d\u026b\3\2\2\2\u009f\u026d\3\2\2\2")
        buf.write("\u00a1\u026f\3\2\2\2\u00a3\u0271\3\2\2\2\u00a5\u0273\3")
        buf.write("\2\2\2\u00a7\u0275\3\2\2\2\u00a9\u0277\3\2\2\2\u00ab\u0279")
        buf.write("\3\2\2\2\u00ad\u027b\3\2\2\2\u00af\u027d\3\2\2\2\u00b1")
        buf.write("\u027f\3\2\2\2\u00b3\u0281\3\2\2\2\u00b5\u0283\3\2\2\2")
        buf.write("\u00b7\u0285\3\2\2\2\u00b9\u0287\3\2\2\2\u00bb\u0289\3")
        buf.write("\2\2\2\u00bd\u028b\3\2\2\2\u00bf\u028d\3\2\2\2\u00c1\u028f")
        buf.write("\3\2\2\2\u00c3\u0291\3\2\2\2\u00c5\u0293\3\2\2\2\u00c7")
        buf.write("\u0295\3\2\2\2\u00c9\u0297\3\2\2\2\u00cb\u0299\3\2\2\2")
        buf.write("\u00cd\u00ce\5\63\32\2\u00ce\u00cf\5u;\2\u00cf\u00d5\5")
        buf.write("\65\33\2\u00d0\u00d6\5\13\6\2\u00d1\u00d6\5\r\7\2\u00d2")
        buf.write("\u00d6\5\'\24\2\u00d3\u00d6\5)\25\2\u00d4\u00d6\5\u0083")
        buf.write("B\2\u00d5\u00d0\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d5\u00d2")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("\4\3\2\2\2\u00d7\u00d8\5\61\31\2\u00d8\u00d9\5\u0083B")
        buf.write("\2\u00d9\6\3\2\2\2\u00da\u00db\7e\2\2\u00db\u00dc\5\u00af")
        buf.write("X\2\u00dc\u00dd\5\u0099M\2\u00dd\u00de\5\u00bd_\2\u00de")
        buf.write("\u00df\5\u00bd_\2\u00df\b\3\2\2\2\u00e0\u00e1\7t\2\2\u00e1")
        buf.write("\u00e2\5\u00a1Q\2\u00e2\u00e3\5\u00bf`\2\u00e3\u00e4\5")
        buf.write("\u00c1a\2\u00e4\u00e5\5\u00bb^\2\u00e5\u00e6\5\u00b3Z")
        buf.write("\2\u00e6\n\3\2\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\5\u00b3")
        buf.write("Z\2\u00e9\u00ea\5\u00bf`\2\u00ea\f\3\2\2\2\u00eb\u00ec")
        buf.write("\7h\2\2\u00ec\u00ed\5\u00afX\2\u00ed\u00ee\5\u00b5[\2")
        buf.write("\u00ee\u00ef\5\u0099M\2\u00ef\u00f0\5\u00bf`\2\u00f0\16")
        buf.write("\3\2\2\2\u00f1\u00f2\7e\2\2\u00f2\u00f3\5\u00b5[\2\u00f3")
        buf.write("\u00f4\5\u00b3Z\2\u00f4\u00f5\5\u00bd_\2\u00f5\u00f6\5")
        buf.write("\u00bf`\2\u00f6\20\3\2\2\2\u00f7\u00f8\7x\2\2\u00f8\u00f9")
        buf.write("\5\u0099M\2\u00f9\u00fa\5\u00bb^\2\u00fa\22\3\2\2\2\u00fb")
        buf.write("\u00fc\7h\2\2\u00fc\u00fd\5\u00c1a\2\u00fd\u00fe\5\u00b3")
        buf.write("Z\2\u00fe\u00ff\5\u009dO\2\u00ff\24\3\2\2\2\u0100\u0101")
        buf.write("\7x\2\2\u0101\u0102\5\u00b5[\2\u0102\u0103\5\u00a9U\2")
        buf.write("\u0103\u0104\5\u009fP\2\u0104\26\3\2\2\2\u0105\u0106\7")
        buf.write("e\2\2\u0106\u0107\5\u00b5[\2\u0107\u0108\5\u00b3Z\2\u0108")
        buf.write("\u0109\5\u00bd_\2\u0109\u010a\5\u00bf`\2\u010a\u010b\5")
        buf.write("\u00bb^\2\u010b\u010c\5\u00c1a\2\u010c\u010d\5\u009dO")
        buf.write("\2\u010d\u010e\5\u00bf`\2\u010e\u010f\5\u00b5[\2\u010f")
        buf.write("\u0110\5\u00bb^\2\u0110\30\3\2\2\2\u0111\u0112\7d\2\2")
        buf.write("\u0112\u0113\5\u00bb^\2\u0113\u0114\5\u00a1Q\2\u0114\u0115")
        buf.write("\5\u0099M\2\u0115\u0116\5\u00adW\2\u0116\32\3\2\2\2\u0117")
        buf.write("\u0118\7e\2\2\u0118\u0119\5\u00b5[\2\u0119\u011a\5\u00b3")
        buf.write("Z\2\u011a\u011b\5\u00bf`\2\u011b\u011c\5\u00a9U\2\u011c")
        buf.write("\u011d\5\u00b3Z\2\u011d\u011e\5\u00c1a\2\u011e\u011f\5")
        buf.write("\u00a1Q\2\u011f\34\3\2\2\2\u0120\u0121\7k\2\2\u0121\u0122")
        buf.write("\5\u00a3R\2\u0122\36\3\2\2\2\u0123\u0124\7g\2\2\u0124")
        buf.write("\u0125\5\u00afX\2\u0125\u0126\5\u00bd_\2\u0126\u0127\5")
        buf.write("\u00a1Q\2\u0127 \3\2\2\2\u0128\u0129\7h\2\2\u0129\u012a")
        buf.write("\5\u00b5[\2\u012a\u012b\5\u00bb^\2\u012b\"\3\2\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\5\u00bb^\2\u012e\u012f\5\u00c1")
        buf.write("a\2\u012f\u0130\5\u00a1Q\2\u0130$\3\2\2\2\u0131\u0132")
        buf.write("\7h\2\2\u0132\u0133\5\u0099M\2\u0133\u0134\5\u00afX\2")
        buf.write("\u0134\u0135\5\u00bd_\2\u0135\u0136\5\u00a1Q\2\u0136&")
        buf.write("\3\2\2\2\u0137\u0138\7d\2\2\u0138\u0139\5\u00b5[\2\u0139")
        buf.write("\u013a\5\u00b5[\2\u013a\u013b\5\u00afX\2\u013b(\3\2\2")
        buf.write("\2\u013c\u013d\7u\2\2\u013d\u013e\5\u00bf`\2\u013e\u013f")
        buf.write("\5\u00bb^\2\u013f\u0140\5\u00a9U\2\u0140\u0141\5\u00b3")
        buf.write("Z\2\u0141\u0142\5\u00a5S\2\u0142*\3\2\2\2\u0143\u0144")
        buf.write("\7p\2\2\u0144\u0145\5\u00c1a\2\u0145\u0146\5\u00afX\2")
        buf.write("\u0146\u0147\5\u00afX\2\u0147,\3\2\2\2\u0148\u0149\7u")
        buf.write("\2\2\u0149\u014a\5\u00a1Q\2\u014a\u014b\5\u00afX\2\u014b")
        buf.write("\u014c\5\u00a3R\2\u014c.\3\2\2\2\u014d\u014e\7p\2\2\u014e")
        buf.write("\u014f\5\u00a1Q\2\u014f\u0150\5\u00c5c\2\u0150\60\3\2")
        buf.write("\2\2\u0151\u0152\7B\2\2\u0152\62\3\2\2\2\u0153\u0154\7")
        buf.write("]\2\2\u0154\64\3\2\2\2\u0155\u0156\7_\2\2\u0156\66\3\2")
        buf.write("\2\2\u0157\u0158\7?\2\2\u01588\3\2\2\2\u0159\u015a\7}")
        buf.write("\2\2\u015a:\3\2\2\2\u015b\u015c\7\177\2\2\u015c<\3\2\2")
        buf.write("\2\u015d\u015e\7*\2\2\u015e>\3\2\2\2\u015f\u0160\7+\2")
        buf.write("\2\u0160@\3\2\2\2\u0161\u0162\7=\2\2\u0162B\3\2\2\2\u0163")
        buf.write("\u0164\7.\2\2\u0164D\3\2\2\2\u0165\u0166\7\60\2\2\u0166")
        buf.write("F\3\2\2\2\u0167\u0168\7-\2\2\u0168H\3\2\2\2\u0169\u016a")
        buf.write("\7/\2\2\u016aJ\3\2\2\2\u016b\u016c\7\61\2\2\u016cL\3\2")
        buf.write("\2\2\u016d\u016e\7^\2\2\u016eN\3\2\2\2\u016f\u0170\7\'")
        buf.write("\2\2\u0170P\3\2\2\2\u0171\u0172\7#\2\2\u0172R\3\2\2\2")
        buf.write("\u0173\u0174\7~\2\2\u0174\u0175\7~\2\2\u0175T\3\2\2\2")
        buf.write("\u0176\u0177\7(\2\2\u0177\u0178\7(\2\2\u0178V\3\2\2\2")
        buf.write("\u0179\u017a\7?\2\2\u017a\u017b\7?\2\2\u017bX\3\2\2\2")
        buf.write("\u017c\u017d\7#\2\2\u017d\u017e\7?\2\2\u017eZ\3\2\2\2")
        buf.write("\u017f\u0180\7>\2\2\u0180\\\3\2\2\2\u0181\u0182\7@\2\2")
        buf.write("\u0182^\3\2\2\2\u0183\u0184\7>\2\2\u0184\u0185\7?\2\2")
        buf.write("\u0185`\3\2\2\2\u0186\u0187\7@\2\2\u0187\u0188\7?\2\2")
        buf.write("\u0188b\3\2\2\2\u0189\u018a\7<\2\2\u018a\u018b\7?\2\2")
        buf.write("\u018bd\3\2\2\2\u018c\u018d\7`\2\2\u018df\3\2\2\2\u018e")
        buf.write("\u018f\7,\2\2\u018fh\3\2\2\2\u0190\u0191\7<\2\2\u0191")
        buf.write("j\3\2\2\2\u0192\u0193\7>\2\2\u0193\u0194\7/\2\2\u0194")
        buf.write("l\3\2\2\2\u0195\u0196\5\63\32\2\u0196\u019a\5q9\2\u0197")
        buf.write("\u0199\5o8\2\u0198\u0197\3\2\2\2\u0199\u019c\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2")
        buf.write("\u019c\u019a\3\2\2\2\u019d\u019e\5\65\33\2\u019en\3\2")
        buf.write("\2\2\u019f\u01a0\5C\"\2\u01a0\u01a1\5q9\2\u01a1\u01a7")
        buf.write("\3\2\2\2\u01a2\u01a3\5C\"\2\u01a3\u01a4\7\"\2\2\u01a4")
        buf.write("\u01a5\5q9\2\u01a5\u01a7\3\2\2\2\u01a6\u019f\3\2\2\2\u01a6")
        buf.write("\u01a2\3\2\2\2\u01a7p\3\2\2\2\u01a8\u01ad\5u;\2\u01a9")
        buf.write("\u01ad\5s:\2\u01aa\u01ad\5y=\2\u01ab\u01ad\5w<\2\u01ac")
        buf.write("\u01a8\3\2\2\2\u01ac\u01a9\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ab\3\2\2\2\u01adr\3\2\2\2\u01ae\u01b0\7/\2\2")
        buf.write("\u01af\u01ae\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b2\3")
        buf.write("\2\2\2\u01b1\u01b3\5}?\2\u01b2\u01b1\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01bb\5E#\2\u01b7\u01ba\5}?\2\u01b8")
        buf.write("\u01ba\5{>\2\u01b9\u01b7\3\2\2\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01da\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c0\7")
        buf.write("/\2\2\u01bf\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c2")
        buf.write("\3\2\2\2\u01c1\u01c3\5}?\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c8\5E#\2\u01c7\u01c9\5}?\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ce\5")
        buf.write("{>\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01da")
        buf.write("\3\2\2\2\u01cf\u01d1\7/\2\2\u01d0\u01cf\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d3\3\2\2\2\u01d2\u01d4\5}?\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2")
        buf.write("\u01d5\u01d6\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\5")
        buf.write("{>\2\u01d8\u01da\3\2\2\2\u01d9\u01af\3\2\2\2\u01d9\u01bf")
        buf.write("\3\2\2\2\u01d9\u01d0\3\2\2\2\u01dat\3\2\2\2\u01db\u01dd")
        buf.write("\5}?\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01dc")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01dfv\3\2\2\2\u01e0\u01e3")
        buf.write("\5#\22\2\u01e1\u01e3\5%\23\2\u01e2\u01e0\3\2\2\2\u01e2")
        buf.write("\u01e1\3\2\2\2\u01e3x\3\2\2\2\u01e4\u01e8\7$\2\2\u01e5")
        buf.write("\u01e7\5\u0093J\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2")
        buf.write("\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb")
        buf.write("\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec\7$\2\2\u01ec")
        buf.write("\u01ed\b=\2\2\u01edz\3\2\2\2\u01ee\u01f0\t\2\2\2\u01ef")
        buf.write("\u01f1\t\3\2\2\u01f0\u01ef\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f3\3\2\2\2\u01f2\u01f4\5}?\2\u01f3\u01f2\3\2")
        buf.write("\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6")
        buf.write("\3\2\2\2\u01f6|\3\2\2\2\u01f7\u01f8\t\4\2\2\u01f8~\3\2")
        buf.write("\2\2\u01f9\u01fa\7\61\2\2\u01fa\u01fb\7\61\2\2\u01fb\u01ff")
        buf.write("\3\2\2\2\u01fc\u01fe\n\5\2\2\u01fd\u01fc\3\2\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u0200\3\2\2\2")
        buf.write("\u0200\u0202\3\2\2\2\u0201\u01ff\3\2\2\2\u0202\u0203\b")
        buf.write("@\3\2\u0203\u0080\3\2\2\2\u0204\u0205\7\61\2\2\u0205\u0206")
        buf.write("\7,\2\2\u0206\u020f\3\2\2\2\u0207\u020e\n\6\2\2\u0208")
        buf.write("\u0209\7,\2\2\u0209\u020a\7\61\2\2\u020a\u020b\3\2\2\2")
        buf.write("\u020b\u020e\n\7\2\2\u020c\u020e\5\u0081A\2\u020d\u0207")
        buf.write("\3\2\2\2\u020d\u0208\3\2\2\2\u020d\u020c\3\2\2\2\u020e")
        buf.write("\u0211\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u0210\u0212\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0213\7")
        buf.write(",\2\2\u0213\u0214\7\61\2\2\u0214\u0215\3\2\2\2\u0215\u0216")
        buf.write("\bA\3\2\u0216\u0082\3\2\2\2\u0217\u021b\t\b\2\2\u0218")
        buf.write("\u021a\t\t\2\2\u0219\u0218\3\2\2\2\u021a\u021d\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u0084\3")
        buf.write("\2\2\2\u021d\u021b\3\2\2\2\u021e\u0220\t\n\2\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224\bC\3\2")
        buf.write("\u0224\u0086\3\2\2\2\u0225\u0226\7\f\2\2\u0226\u0227\3")
        buf.write("\2\2\2\u0227\u0228\bD\3\2\u0228\u0088\3\2\2\2\u0229\u022a")
        buf.write("\7\61\2\2\u022a\u022b\7\61\2\2\u022b\u022f\3\2\2\2\u022c")
        buf.write("\u022e\n\5\2\2\u022d\u022c\3\2\2\2\u022e\u0231\3\2\2\2")
        buf.write("\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232\3")
        buf.write("\2\2\2\u0231\u022f\3\2\2\2\u0232\u0233\bE\3\2\u0233\u008a")
        buf.write("\3\2\2\2\u0234\u0235\7\61\2\2\u0235\u0236\7,\2\2\u0236")
        buf.write("\u023a\3\2\2\2\u0237\u0239\13\2\2\2\u0238\u0237\3\2\2")
        buf.write("\2\u0239\u023c\3\2\2\2\u023a\u023b\3\2\2\2\u023a\u0238")
        buf.write("\3\2\2\2\u023b\u023d\3\2\2\2\u023c\u023a\3\2\2\2\u023d")
        buf.write("\u023e\7,\2\2\u023e\u023f\7\61\2\2\u023f\u0240\3\2\2\2")
        buf.write("\u0240\u0241\bF\3\2\u0241\u008c\3\2\2\2\u0242\u0243\13")
        buf.write("\2\2\2\u0243\u0244\bG\4\2\u0244\u008e\3\2\2\2\u0245\u0249")
        buf.write("\7$\2\2\u0246\u0248\5\u0093J\2\u0247\u0246\3\2\2\2\u0248")
        buf.write("\u024b\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2")
        buf.write("\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024e\t")
        buf.write("\13\2\2\u024d\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write("\u0250\bH\5\2\u0250\u0090\3\2\2\2\u0251\u0255\7$\2\2\u0252")
        buf.write("\u0254\5\u0093J\2\u0253\u0252\3\2\2\2\u0254\u0257\3\2")
        buf.write("\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0258")
        buf.write("\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u0259\5\u0097L\2\u0259")
        buf.write("\u025a\bI\6\2\u025a\u0092\3\2\2\2\u025b\u025e\n\f\2\2")
        buf.write("\u025c\u025e\5\u0095K\2\u025d\u025b\3\2\2\2\u025d\u025c")
        buf.write("\3\2\2\2\u025e\u0094\3\2\2\2\u025f\u0260\7^\2\2\u0260")
        buf.write("\u0261\t\r\2\2\u0261\u0096\3\2\2\2\u0262\u0263\7^\2\2")
        buf.write("\u0263\u0266\n\r\2\2\u0264\u0266\n\16\2\2\u0265\u0262")
        buf.write("\3\2\2\2\u0265\u0264\3\2\2\2\u0266\u0098\3\2\2\2\u0267")
        buf.write("\u0268\t\17\2\2\u0268\u009a\3\2\2\2\u0269\u026a\t\20\2")
        buf.write("\2\u026a\u009c\3\2\2\2\u026b\u026c\t\21\2\2\u026c\u009e")
        buf.write("\3\2\2\2\u026d\u026e\t\22\2\2\u026e\u00a0\3\2\2\2\u026f")
        buf.write("\u0270\t\2\2\2\u0270\u00a2\3\2\2\2\u0271\u0272\t\23\2")
        buf.write("\2\u0272\u00a4\3\2\2\2\u0273\u0274\t\24\2\2\u0274\u00a6")
        buf.write("\3\2\2\2\u0275\u0276\t\25\2\2\u0276\u00a8\3\2\2\2\u0277")
        buf.write("\u0278\t\26\2\2\u0278\u00aa\3\2\2\2\u0279\u027a\t\27\2")
        buf.write("\2\u027a\u00ac\3\2\2\2\u027b\u027c\t\30\2\2\u027c\u00ae")
        buf.write("\3\2\2\2\u027d\u027e\t\31\2\2\u027e\u00b0\3\2\2\2\u027f")
        buf.write("\u0280\t\32\2\2\u0280\u00b2\3\2\2\2\u0281\u0282\t\33\2")
        buf.write("\2\u0282\u00b4\3\2\2\2\u0283\u0284\t\34\2\2\u0284\u00b6")
        buf.write("\3\2\2\2\u0285\u0286\t\35\2\2\u0286\u00b8\3\2\2\2\u0287")
        buf.write("\u0288\t\36\2\2\u0288\u00ba\3\2\2\2\u0289\u028a\t\37\2")
        buf.write("\2\u028a\u00bc\3\2\2\2\u028b\u028c\t \2\2\u028c\u00be")
        buf.write("\3\2\2\2\u028d\u028e\t!\2\2\u028e\u00c0\3\2\2\2\u028f")
        buf.write("\u0290\t\"\2\2\u0290\u00c2\3\2\2\2\u0291\u0292\t#\2\2")
        buf.write("\u0292\u00c4\3\2\2\2\u0293\u0294\t$\2\2\u0294\u00c6\3")
        buf.write("\2\2\2\u0295\u0296\t%\2\2\u0296\u00c8\3\2\2\2\u0297\u0298")
        buf.write("\t&\2\2\u0298\u00ca\3\2\2\2\u0299\u029a\t\'\2\2\u029a")
        buf.write("\u00cc\3\2\2\2#\2\u00d5\u019a\u01a6\u01ac\u01af\u01b4")
        buf.write("\u01b9\u01bb\u01bf\u01c4\u01ca\u01cd\u01d0\u01d5\u01d9")
        buf.write("\u01de\u01e2\u01e8\u01f0\u01f5\u01ff\u020d\u020f\u021b")
        buf.write("\u0221\u022f\u023a\u0249\u024d\u0255\u025d\u0265\7\3=")
        buf.write("\2\b\2\2\3G\3\3H\4\3I\5")
        return buf.getvalue()


class CSlangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ARRAY = 1
    MEMBERl = 2
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
    AC = 24
    OB = 25
    CB = 26
    EQ = 27
    LB = 28
    RB = 29
    LP = 30
    RP = 31
    SM = 32
    CM = 33
    DOT = 34
    ADD = 35
    SUB = 36
    DIV = 37
    BS = 38
    MOD = 39
    NOT = 40
    OR = 41
    AND = 42
    EQUAL = 43
    NOTEQUAL = 44
    LESS = 45
    GREATER = 46
    LESSEQUAL = 47
    GREATEREQUAL = 48
    ASSIGN = 49
    CONCATENATION = 50
    MUL = 51
    COLON = 52
    EXTENDS = 53
    ARRAYLIT = 54
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
            "ARRAY", "MEMBERl", "CLASS", "RETURN", "INT", "FLOAT", "CONST", 
            "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", "CONTINUE", "IF", 
            "ELSE", "FOR", "TRUE", "FALSE", "BOOL", "STRING", "NULL", "SELF", 
            "NEW", "AC", "OB", "CB", "EQ", "LB", "RB", "LP", "RP", "SM", 
            "CM", "DOT", "ADD", "SUB", "DIV", "BS", "MOD", "NOT", "OR", 
            "AND", "EQUAL", "NOTEQUAL", "LESS", "GREATER", "LESSEQUAL", 
            "GREATEREQUAL", "ASSIGN", "CONCATENATION", "MUL", "COLON", "EXTENDS", 
            "ARRAYLIT", "FLOATLIT", "INTLIT", "BOOLLIT", "STRING_LITERAL", 
            "LineComment", "BlockComment", "ID", "WS", "NEWLINE", "LINE_COMMENT", 
            "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ARRAY", "MEMBERl", "CLASS", "RETURN", "INT", "FLOAT", 
                  "CONST", "VAR", "FUNC", "VOID", "CONSTRUCTOR", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "FOR", "TRUE", "FALSE", "BOOL", 
                  "STRING", "NULL", "SELF", "NEW", "AC", "OB", "CB", "EQ", 
                  "LB", "RB", "LP", "RP", "SM", "CM", "DOT", "ADD", "SUB", 
                  "DIV", "BS", "MOD", "NOT", "OR", "AND", "EQUAL", "NOTEQUAL", 
                  "LESS", "GREATER", "LESSEQUAL", "GREATEREQUAL", "ASSIGN", 
                  "CONCATENATION", "MUL", "COLON", "EXTENDS", "ARRAYLIT", 
                  "ARRAYLIST", "ELEM", "FLOATLIT", "INTLIT", "BOOLLIT", 
                  "STRING_LITERAL", "EXPONENT", "DIGIT", "LineComment", 
                  "BlockComment", "ID", "WS", "NEWLINE", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "A", "B", "C", "D", 
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
            actions[59] = self.STRING_LITERAL_action 
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
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
            	
     


