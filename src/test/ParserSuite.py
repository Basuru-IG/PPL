import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """class Program{ const asdgsgsdgsd, b, c: int = 321, 4, 6;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test_simple_program_2(self):
        """Simple program 2"""
        input = """class Program {func @main():int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test_simple_program_3(self):
        """Simple program 3"""
        input = """class Program{var  a, b, c, d: int = 3, 4, 6;}"""
        expect = "Error on line 1 col 44: ;"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test_simple_program_4(self):
        """Simple program 4"""
        input = """class A{var delta: int = 3., 5;}"""
        expect = "Error on line 1 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test_simple_program_5(self):
        """Simple program 5"""
        input = """class A{const My1stCons, My2ndCons: int = 1 + 5, 2;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_simple_program_6(self):
        """Simple program 6"""
        input = """class A{var @x, @y : int = 0, 0;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))
    def test_simple_program_with_comment(self):
        """Simple program with comment"""
        input = """class A{
            var @x, @y : int = 0, 0;
            /* This is a block comment, that
            may span in many lines*/
            //this is a line comment  @x, @y : int = 0, 0;
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_program_2(self):
        """Simple program with comment"""
        input = """class A{
            /* This is a block comment so // has no meaning here */
            //This is a line comment so /* has no meaning here
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))
    def test_simple_program_with_comment_3(self):
        """Simple program with comment"""
        input = """class A{
            /* This is a block comment so // has no meaning here */
            //This is a line comment so /* has no meaning here
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))
    def test_program_3(self):
        """Simple program with comment"""
        input = """class Program {
      var x: int ;
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_simple_program(self):
        """Simple program"""
        input = """class A{func @main():int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
    def test_2(self):
        input = """class Program{ const a, b, c: int = 3, 4, 6;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_3(self):
        input = """class SS { var x: int =           65 ;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        
    def test_4(self):
        input = """class Ss {func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def test_5(self):
        input = """class Ss {func @fact(n: int):int{ if n == [3.0, 3, 12.3e-1] {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test_6(self):
        input = """class funcc {func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_7(self):
        input = """class aSs {var length, width: int; func @fact  (          n: int):int{            if n == 0 {return 1;          } else {return 
        n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    def test_8(self):
        input = """class Sms {func @main():void {io.@writeInt(Shape.@numOfShape);}var length, width: int; func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        
    def test_9(self):
        input = """class Shape <- Retangle {func getArea():int {return self.length * self.width; } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test_10(self):
        input = """class Shape <- Retangle {func constructor() {return self.length * self.width; } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_11(self):
        input = """class ar5 { var a: [10]bool;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        
    def test_12(self):
        input = """class Program2 { var x: int = 65; func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}} func @inc( n, delta: int):void { n := n + delta; return n; } func @main():int { var delta: int = @fact(3); @inc(self.x, delta); io.@writeInt(self.x); }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_13(self):
        input = """class Program2 { var x: int = new X(); func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}} func @inc( n, delta: int):void { n := n + delta; return n; } func @main():int { var delta: int = @fact(3); @inc(self.x, delta); io.@writeInt(self.x); }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_24(self):
        input = """class Program {
        func  @inc( n, delta: int):void {
            x.b[2] := x.m()[3];
            a[3+x.foo(2)] := a[b[2]] +3;
            return n;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    