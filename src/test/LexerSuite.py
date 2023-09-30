import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 101))
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
        self.assertTrue(TestLexer.test("[2.3, 4.2]", "[2.3, 4.2],<EOF>", 112))
    def test_array_literals_12(self):
        """test_array_literals_12"""
        self.assertTrue(TestLexer.test("[2, 4]", "[2, 4],<EOF>", 113))
    def test_array_literals_13(self):
        """test_array_literals_13"""
        self.assertTrue(TestLexer.test("[1.5]", "[1.5],<EOF>", 114))
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
    def test_11(self):
        input = """class ar5 { var a: [10]bool;}"""
        expect = "class,ar5,{,var,a,:,[10]bool,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))
    def test_15(self):
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" ""","He asked me: \\\"Where is John?\\\",<EOF>",117))
    def test_16(self):
        self.assertTrue(TestLexer.test("[true]", "[true],<EOF>", 118))
    def test_17(self):
        self.assertTrue(TestLexer.test("[false]", "[false],<EOF>", 119))
    def test_18(self):
        self.assertTrue(TestLexer.test("[true, false]", "[true, false],<EOF>", 120))
    def test_19(self):
        self.assertTrue(TestLexer.test("a[3+x.foo(2)] := a[b[2]] +3;", "a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[2],],+,3,;,<EOF>", 121))
    def test_20(self):
        self.assertTrue(TestLexer.test("x.b[2] := x.m()[3];", "class,Program,{,func,@inc,(,n,,,delta,:,int,),:,void,{,x,.,b,[2],:=,x,.,m,(,),[3],;,a,[,3,+,x,.,foo,(,2,),],:=,a,[,b,[2],],+,3,;,return,n,;,},<EOF>", 122))

