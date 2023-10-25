import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("""abc""", "abc,<EOF>", 101))
    def test_float_literals(self):
        """test_float_literals"""
        self.assertTrue(TestLexer.test("9.0\t", "9.0,<EOF>", 102))
    def test_float_literals_2(self):
        """test_float_literals_2"""
        self.assertTrue(TestLexer.test("12e8\t", "12e8,<EOF>", 103))
    def test_float_literals_3(self):
        """test_float_literals_3"""
        self.assertTrue(TestLexer.test("1.\t", "1.,<EOF>", 104))
    def test_float_literals_4(self):
        """test_float_literals_4"""
        self.assertTrue(TestLexer.test("0.33E-3\t", "0.33E-3,<EOF>", 105))
    def test_float_literals_5(self):
        """test_float_literals_5"""
        self.assertTrue(TestLexer.test("128e+42\t", "128e+42,<EOF>", 106))
    def test_float_literals_6(self):
        """test_float_literals_6"""
        self.assertTrue(TestLexer.test(".12\t", ".,12,<EOF>", 107))
    def test_float_literals_7(self):
        """test_float_literals_7"""
        self.assertTrue(TestLexer.test("143e\t", "143,e,<EOF>", 108))
    def test_float_literals_8(self):
        """test_float_literals_8"""
        self.assertTrue(TestLexer.test("12e-8\t", "12e-8,<EOF>", 109))
    def test_string_literals_9(self):
        """test_string_literals_9"""
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t " """, "This is a string containing tab \\t "",<EOF>", 110))
    def test_string_literals_10(self):
        """test_string_literals_10"""
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, "He asked me: \\\"Where is John?\\\",<EOF>", 111))
    def test_array_literals_11(self):
        """test_array_literals"""
        self.assertTrue(TestLexer.test("[2.3, 4.2]", "[,2.3,,,4.2,],<EOF>", 112))
    def test_array_literals_12(self):
        """test_array_literals_12"""
        self.assertTrue(TestLexer.test("[2, 4]", "[,2,,,4,],<EOF>", 113))
    def test_array_literals_13(self):
        """test_array_literals_13"""
        self.assertTrue(TestLexer.test("[1.5]", "[,1.5,],<EOF>", 114))
    def test_simple_program_2(self):
        """Simple program 2"""
        input = """class Program {
      var x: int = 65;
      func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():int {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}"""
        expect = "class,Program,{,var,x,:,int,=,65,;,func,@fact,(,n,:,int,),:,int,{,if,n,==,0,{,return,1,;,},else,{,return,n,*,@fact,(,n,-,1,),;,},},func,@inc,(,n,,,delta,:,int,),:,void,{,n,:=,n,+,delta,;,return,n,;,},func,@main,(,),:,int,{,var,delta,:,int,=,@fact,(,3,),;,@inc,(,self,.,x,,,delta,),;,io,.,@writeInt,(,self,.,x,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))
    def test_class_15(self):
        input = """class ar5 { var a: [10]bool;}"""
        expect = "class,ar5,{,var,a,:,[,10,],bool,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))
    def test_string_15(self):
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" ""","He asked me: \\\"Where is John?\\\",<EOF>",117))
    def test_array_16(self):
        self.assertTrue(TestLexer.test("[true]", "[,true,],<EOF>", 118))
    def test_array_17(self):
        self.assertTrue(TestLexer.test("[false]", "[,false,],<EOF>", 119))
    def test_array_18(self):
        self.assertTrue(TestLexer.test("[true, false]", "[,true,,,false,],<EOF>", 120))
    def test_lexer_19(self):
        self.assertTrue(TestLexer.test("a[3+x.foo(2)] := a[b[2]] +3;", "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[,2,],],+,3,;,<EOF>", 121))
    def test_lexer_20(self):
        self.assertTrue(TestLexer.test("x.b()[2] := x.m()[3];", "x,.,b,(,),[,2,],:=,x,.,m,(,),[,3,],;,<EOF>", 122))
    def test_array_literals_21(self):
        """test_array_literals_13"""
        self.assertTrue(TestLexer.test("[[1.2,1.3], [1.2, 1.3]]", "[,[,1.2,,,1.3,],,,[,1.2,,,1.3,],],<EOF>", 123))
    def test_array_literals_22(self):
        """test_array_literals_13"""
        self.assertTrue(TestLexer.test("[3+1]", "[,3,+,1,],<EOF>", 124))
    def test_string_literals_23(self):
        """test_string_literals_23"""
        self.assertTrue(TestLexer.test("\"Hello,\"\" World!\"", "Hello,, World!,<EOF>", 125))

    def test_boolean_literals_24(self):
        """test_boolean_literals_24"""
        self.assertTrue(TestLexer.test("true false", "true,false,<EOF>", 126))

    def test_string_concatenation_25(self):
        """test_string_concatenation_25"""
        self.assertTrue(TestLexer.test("\"Hello,\"\" World!\"", "Hello,, World!,<EOF>", 127))

    def test_identifier_with_underscore_26(self):
        """test_identifier_with_underscore_26"""
        self.assertTrue(TestLexer.test("abc_def", "abc_def,<EOF>", 128))

    def test_assignment_statement_27(self):
        """test_assignment_statement_27"""
        self.assertTrue(TestLexer.test("x = 10;", "x,=,10,;,<EOF>", 129))

    def test_logical_operators_28(self):
        """test_logical_operators_28"""
        self.assertTrue(TestLexer.test("a && b || c", "a,&&,b,||,c,<EOF>", 130))

    def test_comment_29(self):
        """test_comment_29"""
        self.assertTrue(TestLexer.test("// This is a comment\nx = 5;", "x,=,5,;,<EOF>", 131))

    def test_multiple_statements_30(self):
        """test_multiple_statements_30"""
        self.assertTrue(TestLexer.test("x = 5; y = 10;", "x,=,5,;,y,=,10,;,<EOF>", 132))

    def test_function_call_31(self):
        """test_function_call_31"""
        self.assertTrue(TestLexer.test("foo(1, 2, 3);", "foo,(,1,,,2,,,3,),;,<EOF>", 133))

    def test_nested_function_calls_32(self):
        """test_nested_function_calls_32"""
        self.assertTrue(TestLexer.test("foo(bar(1), baz(2));", "foo,(,bar,(,1,),,,baz,(,2,),),;,<EOF>", 134))

    def test_for_loop_33(self):
        """test_for_loop_33"""
        self.assertTrue(TestLexer.test("for i := 1 to 10 do\n    writeln(i);", "for,i,:=,1,to,10,do,writeln,(,i,),;,<EOF>", 135))

    def test_while_loop_34(self):
        """test_while_loop_34"""
        self.assertTrue(TestLexer.test("while x < 10 do\n    x = x + 1;", "while,x,<,10,do,x,=,x,+,1,;,<EOF>", 136))

    def test_if_statement_35(self):
        """test_if_statement_35"""
        self.assertTrue(TestLexer.test("if x < 10 then\n    x = x + 1;\nelse\n    x = x - 1;", "if,x,<,10,then,x,=,x,+,1,;,else,x,=,x,-,1,;,<EOF>", 137))

    def test_comparison_operators_36(self):
        """test_comparison_operators_36"""
        self.assertTrue(TestLexer.test("x == y != z > w < q >= r <= s", "x,==,y,!=,z,>,w,<,q,>=,r,<=,s,<EOF>", 138))

    def test_array_indexing_37(self):
        """test_array_indexing_37"""
        self.assertTrue(TestLexer.test("arr[5]", "arr,[,5,],<EOF>", 139))

    def test_array_assignment_38(self):
        """test_array_assignment_38"""
        self.assertTrue(TestLexer.test("arr[5] = 42;", "arr,[,5,],=,42,;,<EOF>", 140))

    def test_empty_program_39(self):
        """test_empty_program_39"""
        self.assertTrue(TestLexer.test("", "<EOF>", 141))

    def test_function_declaration_40(self):
        """test_function_declaration_40"""
        self.assertTrue(TestLexer.test("func foo(a: int, b: int): int {\n    return a + b;\n}", "func,foo,(,a,:,int,,,b,:,int,),:,int,{,return,a,+,b,;,},<EOF>", 142))

    def test_variable_declaration_41(self):
        """test_variable_declaration_41"""
        self.assertTrue(TestLexer.test("var x, y, z: int;", "var,x,,,y,,,z,:,int,;,<EOF>", 143))

    def test_class_declaration_42(self):
        """test_class_declaration_42"""
        input = "class Person {\n    var name: string;\n    func sayHello(): void {\n        writeln(\"Hello, \", name);\n    }\n}"
        expect = "class,Person,{,var,name,:,string,;,func,sayHello,(,),:,void,{,writeln,(,Hello, ,,,name,),;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_unterminated_string_literal_43(self):
        """test_unterminated_string_literal_43"""
        self.assertTrue(TestLexer.test(""" "This is an unterminated string""", "Unclosed String: This is an unterminated string", 145))

    def test_unknown_operator_44(self):
        """test_unknown_operator_44"""
        self.assertTrue(TestLexer.test("x @@ y", "x,Error Token @", 146))

    def test_mixed_identifiers_45(self):
        """test_mixed_identifiers_45"""
        self.assertTrue(TestLexer.test("abc_123 foo_456", "abc_123,foo_456,<EOF>", 147))

    def test_invalid_characters_46(self):
        """test_invalid_characters_46"""
        self.assertTrue(TestLexer.test("x $ y", "x,Error Token $", 148))

    def test_invalid_float_literal_47(self):
        """test_invalid_float_literal_47"""
        self.assertTrue(TestLexer.test("12.3.4", "12.3,.,4,<EOF>", 149))

    def test_invalid_string_escape_sequence_48(self):
        """test_invalid_string_escape_sequence_48"""
        self.assertTrue(TestLexer.test(""" "Invalid escape sequence: \\q" """, "Illegal Escape In String: Invalid escape sequence: \\q", 150))
    def test_string_literals_151(self):
        """Test string literal with a tab character and spaces"""
        self.assertTrue(TestLexer.test(""" "Tab \\t Space \\t " """, "Tab \\t Space \\t ,<EOF>", 151))

    def test_string_literals_152(self):
        """Test string literal with a newline character (compile-time error)"""
        self.assertTrue(TestLexer.test("\"This string\nnhas a newline character.\"", "Unclosed String: This string", 152))

    def test_string_literals_153(self):
        """Test string literal with a carriage return character"""
        self.assertTrue(TestLexer.test(""" "Carriage\\rReturn" """, "Carriage\\rReturn,<EOF>", 153))

    def test_string_literals_154(self):
        """Test string literal with a formfeed character"""
        self.assertTrue(TestLexer.test("\"Form\\ffeed\"", "Form\\ffeed,<EOF>", 154))

    def test_string_literals_155(self):
        """Test string literal with a backspace character"""
        self.assertTrue(TestLexer.test("\"Back\\bspace\"", "Back\\bspace,<EOF>", 155))

    def test_string_literals_156(self):
        """Test string literal with a backslash character"""
        self.assertTrue(TestLexer.test("\"Back\\\\slash\"", "Back\\\\slash,<EOF>", 156))

    def test_string_literals_157(self):
        """Test string literal with double quotes and escape sequence"""
        self.assertTrue(TestLexer.test(""" "He said, \\"Hello!\\\"" """, "He said, \\\"Hello!\\\",<EOF>", 157))

    def test_string_literals_158(self):
        """Test string literal with single quotes and escape sequence"""
        self.assertTrue(TestLexer.test(""" "He said, \\\\'Hello!\\\\'" """, "He said, \\\\'Hello!\\\\',<EOF>", 158))

    def test_string_literals_159(self):
        """Test string literal with backslash character and text"""
        self.assertTrue(TestLexer.test("\"Back\\\\slash and text\"", "Back\\\\slash and text,<EOF>", 159))

    def test_string_literals_160(self):
        """Test string literal with backslash character and text"""
        self.assertTrue(TestLexer.test("\"Back\\\\slash and text\"", "Back\\\\slash and text,<EOF>", 160))
    def test_identifier_161(self):
        """Test identifier with letters and digits"""
        self.assertTrue(TestLexer.test("abc123", "abc123,<EOF>", 161))

    def test_identifier_162(self):
        """Test identifier with underscores and digits"""
        self.assertTrue(TestLexer.test("var_name_42", "var_name_42,<EOF>", 162))

    def test_keyword_163(self):
        """Test reserved keyword 'if'"""
        self.assertTrue(TestLexer.test("if x < 10 then", "if,x,<,10,then,<EOF>", 163))

    def test_operator_164(self):
        """Test arithmetic operator '*'"""
        self.assertTrue(TestLexer.test("x * y", "x,*,y,<EOF>", 164))

    def test_operator_165(self):
        """Test relational operator '<>'"""
        self.assertTrue(TestLexer.test("x <> y", "x,<,>,y,<EOF>", 165))

    def test_operator_166(self):
        """Test logical operator 'and'"""
        self.assertTrue(TestLexer.test("x and y", "x,and,y,<EOF>", 166))

    def test_operator_167(self):
        """Test assignment operator ':='"""
        self.assertTrue(TestLexer.test("x := 42", "x,:=,42,<EOF>", 167))

    def test_operator_168(self):
        """Test mixed operators"""
        self.assertTrue(TestLexer.test("x + y * 2", "x,+,y,*,2,<EOF>", 168))

    def test_comment_169(self):
        """Test single-line comment"""
        self.assertTrue(TestLexer.test("// This is a comment", "<EOF>", 169))

    def test_comment_170(self):
        """Test single-line comment with code"""
        self.assertTrue(TestLexer.test("// This is a comment\nx := 5;", "x,:=,5,;,<EOF>", 170))
    def test_class_declaration_171(self):
        """Test class declaration with a variable"""
        input = """class Person {
            var name: string;
        }"""
        expect = "class,Person,{,var,name,:,string,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_function_declaration_172(self):
        """Test function declaration with parameters"""
        input = """func add(a: int, b: int): int {
            return a + b;
        }"""
        expect = "func,add,(,a,:,int,,,b,:,int,),:,int,{,return,a,+,b,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_var_declaration_173(self):
        """Test variable declaration with multiple variables"""
        input = """var x, y, z: int;"""
        expect = "var,x,,,y,,,z,:,int,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_array_declaration_174(self):
        """Test array declaration"""
        input = """var arr: array [5] of int;"""
        expect = "var,arr,:,array,[,5,],of,int,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_if_statement_175(self):
        """Test if statement with else part"""
        input = """if x < 10 then
            y := y + 1;
        else
            y := y - 1;"""
        expect = "if,x,<,10,then,y,:=,y,+,1,;,else,y,:=,y,-,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_for_loop_176(self):
        """Test for loop"""
        input = """for i := 1 to 10 do
            writeln(i);"""
        expect = "for,i,:=,1,to,10,do,writeln,(,i,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_while_loop_177(self):
        """Test while loop"""
        input = """while x < 10 do
            x := x + 1;"""
        expect = "while,x,<,10,do,x,:=,x,+,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_function_call_178(self):
        """Test function call with arguments"""
        input = """foo(1, 2, 3);"""
        expect = "foo,(,1,,,2,,,3,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_nested_function_calls_179(self):
        """Test nested function calls"""
        input = """foo(bar(1), baz(2));"""
        expect = "foo,(,bar,(,1,),,,baz,(,2,),),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))

    def test_assignment_statement_180(self):
        """Test assignment statement"""
        input = """x := 42;"""
        expect = "x,:=,42,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 180))

    def test_logical_operators_181(self):
        """Test logical operators (AND, OR, NOT)"""
        input = "x && y || !z;"
        expect = "x,&&,y,||,!,z,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_comparison_operators_182(self):
        """Test comparison operators (==, !=, >, <, >=, <=)"""
        input = "x == y != z > w < q >= r <= s;"
        expect = "x,==,y,!=,z,>,w,<,q,>=,r,<=,s,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_array_indexing_183(self):
        """Test array indexing"""
        input = "arr[5];"
        expect = "arr,[,5,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_array_assignment_184(self):
        """Test array assignment"""
        input = "arr[5] := 42;"
        expect = "arr,[,5,],:=,42,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test_comment_185(self):
        """Test single-line comment"""
        input = "// This is a comment\nx := 5;"
        expect = "x,:=,5,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_multiple_statements_186(self):
        """Test multiple statements in a block"""
        input = "x := 5; y := 10;"
        expect = "x,:=,5,;,y,:=,10,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_empty_program_187(self):
        """Test an empty program"""
        input = ""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_invalid_characters_188(self):
        """Test invalid characters in the input"""
        input = "x $ y"
        expect = "x,Error Token $"
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_invalid_float_literal_189(self):
        """Test invalid floating-point literal"""
        input = "12.3.4"
        expect = "12.3,.,4,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_invalid_string_escape_sequence_190(self):
        """Test invalid string escape sequence"""
        input = "\"Invalid escape sequence: \\q\""
        expect = "Illegal Escape In String: Invalid escape sequence: \\q"
        self.assertTrue(TestLexer.test(input, expect, 190))
    def test_identifier_with_underscore_191(self):
        """Test an identifier with underscore"""
        input = "abc_def"
        expect = "abc_def,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_assignment_statement_192(self):
        """Test an assignment statement"""
        input = "x = 10;"
        expect = "x,=,10,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_function_call_193(self):
        """Test a function call"""
        input = "foo(1, 2, 3);"
        expect = "foo,(,1,,,2,,,3,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_nested_function_calls_194(self):
        """Test nested function calls"""
        input = "foo(bar(1), baz(2));"
        expect = "foo,(,bar,(,1,),,,baz,(,2,),),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_for_loop_195(self):
        """Test a for loop"""
        input = "for i := 1 to 10 do\n    writeln(i);"
        expect = "for,i,:=,1,to,10,do,writeln,(,i,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_while_loop_196(self):
        """Test a while loop"""
        input = "while x < 10 do\n    x = x + 1;"
        expect = "while,x,<,10,do,x,=,x,+,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_if_statement_197(self):
        """Test an if statement"""
        input = "if x < 10 then\n    x = x + 1;\nelse\n    x = x - 1;"
        expect = "if,x,<,10,then,x,=,x,+,1,;,else,x,=,x,-,1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_string_concatenation_198(self):
        """Test string concatenation"""
        input = "\"Hello,\" + \" World!\";"
        expect = "Hello,,+, World!,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))

    def test_identifier_with_underscore_199(self):
        """Test an identifier with underscore"""
        input = "abc_def"
        expect = "abc_def,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_assignment_statement_200(self):
        """Test an assignment statement"""
        input = "x = 10;"
        expect = "x,=,10,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 200))
    







