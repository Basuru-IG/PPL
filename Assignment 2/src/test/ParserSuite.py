import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
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
        expect = "Error on line 1 col 27: ,"
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
    def test_simple_program_with_comment_2(self):
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
    def test_advance_program(self):
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
    def test_program(self):
        """Simple program"""
        input = """class A{func @main():int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
        
    def test_program_2(self):
        """Simple program 2"""
        input = """class Program{ const a, b, c: int = 3, 4, 6;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_program_3(self):
        input = """class SS { var x: int =           65 ;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
        
    def test_program_4(self):
        input = """class Ss {func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))
    
    def test_program_5(self):
        input = """class Ss {func @fact(n: int):int{ if n == [3.0, 3, 12.3e-1] {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test_program_6(self):
        input = """class funcc {func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_program_7(self):
        input = """class aSs {var length, width: int; func @fact  (          n: int):int{            if n == 0 {return 1;          } else {return 
        n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
        
    def test_program_8(self):
        input = """class Sms {func @main():void {io.@writeInt(Shape.@numOfShape);}var length, width: int; func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
        
    def test_program_9(self):
        input = """class Shape <- Retangle {func getArea():int {return self.length * self.width; } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test_program_10(self):
        input = """class Shape <- Retangle {func constructor() {return self.length * self.width; } }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_program_11(self):
        input = """class ar5 { var a: [10]bool;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        
    def test_program_12(self):
        input = """class Program2 { var x: int = 65; func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}} func @inc( n, delta: int):void { n := n + delta; return n; } func @main():int { var delta: int = @fact(3); @inc(self.x, delta); io.@writeInt(self.x); }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))
    def test_program_13(self):
        input = """class Program2 { var x: int = new X(); func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}} func @inc( n, delta: int):void { n := n + delta; return n; } func @main():int { var delta: int = @fact(3); @inc(self.x, delta); io.@writeInt(self.x); }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test_simple_program_24(self):
        input = """class Program {
        func  @inc( n, delta: int):void {
            x.b()[4+55] := x.m()[3];
            a[3+x.foo(2)] := a[b[2+1]] +3;
            return n;
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test_simple_program_225(self):
        input = """class Program {
            func @main():int {
                if x < 10 {
                    return 1;
                }
                else {
                    return 0;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_simple_program_226(self):
        input = """class Program {
            var x: int;
            func @main():int {
                x := 0;
                return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_simple_program_227(self):
        input = """class Program {
            func @main():int {
                return 0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_simple_program_228(self):
        input = """class Program {
            func @main():int {
                var arr: [10]int;
                for i := 0; i < 10; i := i + 1 {
io.@writeInt(i);
}
                return arr[5];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_simple_program_229(self):
        input = """class Program {
            func @main():int {
                var sum: int = 0;
                for i := 0; i < 10; i := i + 1 {
io.@writeInt(i);
}
                return sum;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_simple_program_230(self):
        input = """class Program {
            func @main():int {
                var i: int = 0;
                return i;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_simple_program_231(self):
        input = """class Program {
            func @main():int {
                var a, b, c: int;
                a := 1;
                b := 2;
                c := a + b;
                return c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_simple_program_232(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                if x < y {
                    return x;
                }
                else {
                    return y;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_simple_program_233(self):
        input = """class Program {
            func @main():int {
                var a, b, c: int = 1, 2, 3;
                return a + b + c;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_simple_program_234(self):
        input = """class Program {
            func @main():int {
                var x: int;
                x := foo(); 
                return x;
            }
        }
        """
        expect = "Error on line 4 col 24: ("
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_simple_program_235(self):
        input = """class Program {
            func @main():int {
                var arr: [10]int;
                for i := 0; i < 10; i := i + 1 {
                    io.@writeInt(i);
                }
                return arr[5];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_simple_program_236(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                if x < y {
                    writeln("x is less than y");
                }
                else {
                    writeln("x is greater than or equal to y");
                }
                return 0;
            }
        }
        """
        expect = "Error on line 6 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_simple_program_237(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                if x < y {
                    @writeln("x is less than y");
                }
                else {
                    @writeln("x is greater than or equal to y");
                }
                return 0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_simple_program_238(self):
        input = """class Program {
            func @main():int {
                var x: int;
                x := -5;
                return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_simple_program_239(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                if x < y {
                    x := x * 2;
                }
                else {
                    x := x / 2;
                }
                return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_simple_program_240(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                if x < y {
                    if y > 15 {
                        x := x * 2;
                    }
                    else {
                        x := x / 2;
                    }
                }
                else {
                    x := 0;
                }
                return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_simple_program_241(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_simple_program_242(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                dfsdf sdfsdfs;
                return x;
            }
        }
        """
        expect = "Error on line 5 col 22: sdfsdfs"
        self.assertTrue(TestParser.test(input, expect, 242))
    def test_test_simple_program_243(self):
        input = """class Test {
            func @main():int {
                return 1.2;
            }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
    def test_simple_program_244(self):
        input = """class Test { var x: int = 5 * 3 + 2 && 3; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_simple_program_245(self):
        input = """class Test { var x: int = 5 * 3 + 2 || 3; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
    
    def test_simple_program_246(self):
        input = """class Test { var x: int = 5 * 3 + 2 +; }"""
        expect = "Error on line 1 col 37: ;"
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_simple_program_247(self):
        input = """class Test { func @main():int { return 5 * (3 + 2; } }"""
        expect = "Error on line 1 col 49: ;"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_simple_program_248(self):
        input = """class Test { var x: int = 10.5; }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_simple_program_249(self):
        input = """class Test { 
        func @main():void {
            x := x + + 1;
        }
        }"""
        expect = "Error on line 3 col 21: +"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_simple_program_250(self):
        input = """class Test { 
        var x: int = 5 * 3 + 2 * !false;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    
    def test_simple_program_251(self):
        input = """class Test { 
        var x: int = 5 * 3 + 2 * !true;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_simple_program_252(self):
        input = """class Program {
            func @fnc():int {
                var delta: [10]delta;
                for i := 0; i < 10; i := i + 1 {
                    io.@writeStr(i);
                }
                return arr[5];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_program_253(self):
        """Test a program with constant declaration and assignment"""
        input = """class Program {
            const a, b, c: int = 3, 4, 6;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_program_254(self):
        """Test a program with empty function"""
        input = """class Program {
            func @main():int {}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_program_255(self):
        """Test a program with multiple variables and constant declaration and assignment"""
        input = """class Program {
            const a, b, c: int = 3, 4, 6;
            var x, y, z: int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_program_256(self):
        """Test a program with variables and functions"""
        input = """class Program {
            var x: int;
            func @fact(n: int):int {
                if n == 0 {return 1;}
                else {return n * @fact(n - 1);}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_program_257(self):
        """Test a program with nested if-else statements"""
        input = """class Program {
            func @main():int {
                var x: int;
                if x < 10 {
                    x := x + 1;
                    if x > 5 {
                        x := x - 1;
                    }
                }
                else {
                    x := x - 1;
                }
                return x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_program_258(self):
        """Test a program with block comments"""
        input = """class Program {
            /* This is a block comment */
            func @main():int {
                var x: int;
                if x < 10 {
                    x := x + 1;
                }
                return x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_program_259(self):
        """Test a program with line comments"""
        input = """class Program {
            func @main():int {
                // This is a line comment
                var x: int;
                if x < 10 {
                    x := x + 1;
                }
                return x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_program_260(self):
        """Test a program with a mix of block and line comments"""
        input = """class Program {
            /* This is a block comment */
            func @main():int {
                // This is a line comment
                var x: int;
                if x < 10 {
                    x := x + 1;
                }
                return x;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_for_statement_261(self):
        input = """class Loop {
            func @main(): void {
                for i := 0; i < 5; i := i + 1 {
                    io.@writeInt(i);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_for_statement_262(self):
        input = """class Loop {
            func @main(): void {
                for j := 10; j > 0; j := j - 1 {
                    io.@writeInt(j);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_for_statement_263(self):
        input = """class Loop {
            func @main(): void {
                for k := 1; k <= 10; k := k + 2 {
                    io.@writeInt(k);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_for_statement_264(self):
        input = """class Loop {
            func @main(): void {
                for n := 5; n >= 0; n := n - 1 {
                    io.@writeInt(n);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_for_statement_265(self):
        input = """class Loop {
            func @main(): void {
                for x := 100; x > 90; x := x - 1 {
                    io.@writeInt(x);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_for_statement_266(self):
        input = """class Loop {
            func @main(): void {
                for i := 1; i <= 3; i := i * 2 {
                    io.@writeInt(i);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_for_statement_267(self):
        input = """class Loop {
            func @main(): void {
                for a := 5; a > 1; a := a - 1 {
                    io.@writeInt(a);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_for_statement_268(self):
        input = """class Loop {
            func @main(): void {
                for b := 2; b < 20; b := b * 2 {
                    io.@writeInt(b);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_for_statement_269(self):
        input = """class Loop {
            func @main(): void {
                for c := 0; c < 10; c := c + 1 {
                    io.@writeInt(c);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_for_statement_270(self):
        input = """class Loop {
            func @main(): void {
                for x := 5; x <= 25; x := x + 5 {
                    io.@writeInt(x);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
    def test_for_if_statements_271(self):
        input = """class Loop {
            var sum: int;
            func @calculateSum(): int {
                sum := 0;
                for i := 1; i <= 10; i := i + 1 {
                    if i % 2 == 0 {
                        sum := sum + i;
                    }
                }
                return sum;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_for_if_statements_272(self):
        input = """class Loop {
            var max: int;
            func @findMax(numbers: [10]int): int {
                max := numbers[0];
                for i := 1; i < 10; i := i + 1 {
                    if numbers[i] > max {
                        max := numbers[i];
                    }
                }
                return max;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_for_if_statements_273(self):
        input = """class Loop {
            var prime: bool;
            func @isPrime(num: int): bool {
                prime := true;
                for i := 2; i < num; i := i + 1 {
                    if num % i == 0 {
                        prime := false;
                    }
                }
                return prime;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_for_if_statements_274(self):
        input = """class Loop {
            var max: int;
            func @findMax(arr: [10]int): int {
                max := arr[0];
                for i := 1; i < 10; i := i + 1 {
                    if arr[i] > max {
                        max := arr[i];
                    }
                }
                return max;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_for_if_statements_275(self):
        input = """class Loop {
            func @main(): void {
                var result: int;
                for i := 1; i <= 5; i := i + 1 {
                    if i % 2 == 0 {
                        result := i * 2;
                        io.@writeInt(result);
                    }
                    else {
                        result := i * 3;
                        io.@writeInt(result);
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_for_if_statements_276(self):
        input = """class Loop {
            var isPositive: bool;
            func @checkPositive(num: int): bool {
                if num > 0 {
                    isPositive := 1;
                }
                else {
                    isPositive := 0;
                }
                return isPositive;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_for_if_statements_277(self):
        input = """class Loop {
            func @main(): void {
                var count: int;
                for i := 0; i < 10; i := i + 1 {
                    if i % 2 == 0 {
                        count := count + 1;
                    }
                }
                io.@writeInt(count);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_for_if_statements_278(self):
        input = """class Loop {
            func @main(): void {
                var total: int;
                for i := 1; i <= 5; i := i + 1 {
                    total := total + i;
                    if i == 3 {
                        break;
                    }
                }
                io.@writeInt(total);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_for_if_statements_279(self):
        input = """class Loop {
            func @main(): void {
                var result: int;
                for i := 1; i <= 5; i := i + 1 {
                    if i == 3 {
                        continue;
                    }
                    result := result + i;
                }
                io.@writeInt(result);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_for_if_statements_280(self):
        input = """class Loop {
            var numbers: [10]int;
            func @initializeArray(): void {
                for i := 0; i < 10; i := i + 1 {
                    numbers[i] := i * 2;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_advanced_program_281(self):
        input = """class A {
            var delta: int = 3;
            func @main(): int {
                return delta * 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_advanced_program_282(self):
        input = """class B {
            var a, b, c: int = 1, 2, 3;
            func @sum(): int {
                return a + b + c;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_advanced_program_283(self):
        input = """class C {
            var x, y, z: float = 1.0, 2.5, 3.5e-2;
            func @average(): float {
                return (x + y + z) / 3.0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_advanced_program_284(self):
        input = """class D {
            func @main(): void {
                var result: string = "Hello, World!";
                io.@writeString(result);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_advanced_program_285(self):
        input = """class E {
            const PI: float = 3.14159265359;
            func @calculateArea(radius: float): float {
                return PI * radius * radius;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_advanced_program_286(self):
        input = """class F {
            var counter: int;
            func @countToTen(): void {
                counter := 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_advanced_program_287(self):
        input = """class G {
            func @main(): void {
                var sum: int = 0;
                for i := 1; i <= 100; i := i + 1 {
                    sum := sum + i;
                }
                io.@writeInt(sum);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_advanced_program_288(self):
        input = """class H {
            var isValid: bool = true;
            func @toggleFlag(): void {
                if isValid {
                    isValid := false;
                }
                else {
                    isValid := true;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_advanced_program_289(self):
        input = """class I {
            var numbers: [5]int;
            func @initializeArray(): void {
                for i := 0; i < 5; i := i + 1 {
                    numbers[i] := i * 2;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_advanced_program_290(self):
        input = """class J {
            var total: int;
            func @sumOfEvenNumbers(): void {
                for i := 1; i <= 10; i := i + 1 {
                    if i % 2 == 0 {
                        total := total + i;
                    }
                }
                io.@writeInt(total);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
    def test_advanced_program_291(self):
        input = """class K {
            func @main(): void {
                var x, y, z: int = 1, 2, 3;
                var sum: int = x + y + z;
                if sum >= 5 {
                    io.@writeString("Sum is greater than or equal to 5");
                }
                else {
                    io.@writeString("Sum is less than 5");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_advanced_program_292(self):
        input = """class L {
            var n: int;
            func @isPrime(): bool {
                if n <= 1 {
                    return false;
                }
                for i := 2; i < n; i := i + 1 {
                    if n % i == 0 {
                        return false;
                    }
                }
                return true;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_advanced_program_293(self):
        input = """class M {
            var data: [5]int;
            func @findMax(): int {
                var max: int = data[0];
                for i := 1; i < 5; i := i + 1 {
                    if data[i] > max {
                        max := data[i];
                    }
                }
                return max;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_advanced_program_294(self):
        input = """class N {
            var values: [10]float;
            func @calculateAverage(): float {
                var sum: float = 0.0;
                for i := 0; i < 10; i := i + 1 {
                    sum := sum + values[i];
                }
                return sum / 10.0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_advanced_program_295(self):
        input = """class O {
            var grades: [5]float;
            func @calculateGradeAverage(): float {
                var total: float = 0.0;
                for i := 0; i < 5; i := i + 1 {
                    total := total + grades[i];
                }
                return total / 5.0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_advanced_program_296(self):
        input = """class P {
            var count: int;
            func @generateFibonacci(): [10]int {
                var fib: [10]int;
                fib[0] := 0;
                fib[1] := 1;
                for i := 2; i < 10; i := i + 1 {
                    fib[i] := fib[i - 1] + fib[i - 2];
                }
                return fib;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_advanced_program_297(self):
        input = """class Q {
            var numbers: [10]int;
            func @findSmallest(): int {
                var min: int = numbers[0];
                for i := 1; i < 10; i := i + 1 {
                    if numbers[i] < min {
                        min := numbers[i];
                    }
                }
                return min;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_advanced_program_298(self):
        input = """class R {
            func @main(): void {
                var x, y: int = 5, 10;
                if x < y {
                    io.@writeString("x is less than y");
                }
                else {
                    io.@writeString("x is greater than or equal to y");
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_advanced_program_299(self):
        input = """class S {
            var n: int;
            func @isEven(): bool {
                if n % 2 == 0 {
                    return true;
                }
                return false;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_advanced_program_300(self):
        input = """class Test {
        var a, b: int = 1, 2;
        func @main():arr {
            if a > b {
                a := a * 2;
            } else {
                b := b + 1;
            }
        }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

    def test_advanced_program_320(self):
        input ="""
    class ComplexExpressions {
        func complexMethod(): int {
            return (1 + 2) * (3 - 4) / (5 + 6) % 7;
        }
        
        func callComplex(): void {
            var result: int;
            result := self.complexMethod();
            io.@writeInt(result);
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 405))



        