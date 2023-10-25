import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test_class_with_method_decl(self):
        "Test with method decl"
        input = """class main{ func a(): void {}}"""
        expect = str(Program([ClassDecl(Id("main"),[MethodDecl(Id("a"),[],VoidType(),Block([]))])]))
        self.assertTrue(TestAST.test(input,expect,303))

    def test_class_with_more_method_decl(self):
        "Test with more method decl"
        input = """class main{
        func foo  (a: int, b: float):void {}

        func @main():void{
            io.printInt(4);
        }}"""
        expect = """Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[Param(Id(a),IntType),Param(Id(b),FloatType)],VoidType,Block([])),MethodDecl(Id(@main),[],VoidType,Block([Call(Id(io),Id(printInt),[IntLit(4)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,304))

    def test_return_stm(self):
        "Test return statement"
        input = """class main{func foo():void {return @count;}}"""
        expect = """Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[],VoidType,Block([Return(FieldAccess(Id(@count)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
   
    def test_return_stm_2(self):
        "Test return statement"
        input = """class main{func foo():void {return;}}"""
        expect = """Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[],VoidType,Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))

    def test_var_decl_stm(self):
        """More complex program"""
        input = """class main {
            var  a, b, c: int = 3, 4, 6;
            var b:int;
        }"""
        expect = """Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(a),IntType,IntLit(3))),AttributeDecl(VarDecl(Id(b),IntType,IntLit(4))),AttributeDecl(VarDecl(Id(c),IntType,IntLit(6))),AttributeDecl(VarDecl(Id(b),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,307))

    def test_complex_class(self):
        input = """class Q {
            var numbers: [10]int;
            func @findSmallest(): int {
                var min,b: int ;
                
                return min;
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Q"),[
                    AttributeDecl(VarDecl(Id("numbers"),ArrayType(10,IntType()))),
                    MethodDecl(Id("@findSmallest"),[],IntType(),Block([
                        VarDecl(Id("min"),IntType()),
                        VarDecl(Id("b"),IntType()),
                        Return(Id("min"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,308))

    def test_complex_class_2(self):
        input = """class Q {
            var numbers: [10]int;
            func @findSmallest(): int {
                var min: int = numbers[0];
                
                return min;
            }
        }"""
        expect = "Program([ClassDecl(Id(Q),[AttributeDecl(VarDecl(Id(numbers),ArrayType(10,IntType))),MethodDecl(Id(@findSmallest),[],IntType,Block([VarDecl(Id(min),IntType,ArrayCell(Id(numbers),IntLit(0))),Return(Id(min))]))])])"
        self.assertTrue(TestAST.test(input,expect,309))

    def test_complex_class_3(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Q"),[
                    AttributeDecl(VarDecl(Id("numbers"),ArrayType(10,IntType()))),
                    MethodDecl(Id("@findSmallest"),[],IntType(),Block([
                        VarDecl(Id("min"),IntType(),ArrayCell(Id("numbers"),IntLiteral(0))),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("<",ArrayCell(Id("numbers"),Id("i")),Id("min")),Block([
                                Assign(Id("min"),ArrayCell(Id("numbers"),Id("i")))
                            ]))
                        ])),
                        Return(Id("min"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,310))

    def test_class_with_one_decl_2(self):
        "Test class with more complex decl"
        input = """
        class main {
            var a : [2]float = [1.2,1.0];
        }
        """
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),ArrayType(2,FloatType()),ArrayLiteral([FloatLiteral(1.2),FloatLiteral(1.0)])))])]))
        self.assertTrue(TestAST.test(input,expect,311))

    def test_complex_class_4(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("P"),[
                    AttributeDecl(VarDecl(Id("count"),IntType())),
                    MethodDecl(Id("@generateFibonacci"),[],ArrayType(10,IntType()),Block([
                        VarDecl(Id("fib"),ArrayType(10,IntType())),
                        Assign(ArrayCell(Id("fib"),IntLiteral(0)),IntLiteral(0)),
                        Assign(ArrayCell(Id("fib"),IntLiteral(1)),IntLiteral(1)),
                        For(Assign(Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            Assign(ArrayCell(Id("fib"),Id("i")),BinaryOp("+",ArrayCell(Id("fib"),BinaryOp("-",Id("i"),IntLiteral(1))),ArrayCell(Id("fib"),BinaryOp("-",Id("i"),IntLiteral(2)))))
                        ])),
                        Return(Id("fib"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,312))

    def test_complex_class_5(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Q"),[
                    AttributeDecl(VarDecl(Id("numbers"),ArrayType(10,IntType()))),
                    MethodDecl(Id("@findSmallest"),[],IntType(),Block([
                        VarDecl(Id("min"),IntType(),ArrayCell(Id("numbers"),IntLiteral(0))),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("<",ArrayCell(Id("numbers"),Id("i")),Id("min")),Block([
                                Assign(Id("min"),ArrayCell(Id("numbers"),Id("i")))
                            ]))
                        ])),
                        Return(Id("min"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,313))

    def test_complex_class_5(self):
        input = """class Q {
            var numbers: [10]int;
            func @findSmallest(): int {
                var min: int = numbers[0];
                for i := 1; i < 10; i := i + 1 {
                    if numbers[i] < min {
                        min := numbers[i];
                    }
                }
                return @min;
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Q"),[
                    AttributeDecl(VarDecl(Id("numbers"),ArrayType(10,IntType()))),
                    MethodDecl(Id("@findSmallest"),[],IntType(),Block([
                        VarDecl(Id("min"),IntType(),ArrayCell(Id("numbers"),IntLiteral(0))),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("<",ArrayCell(Id("numbers"),Id("i")),Id("min")),Block([
                                Assign(Id("min"),ArrayCell(Id("numbers"),Id("i")))
                            ]))
                        ])),
                        Return(FieldAccess(None,Id("@min")))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,314))

    def test_complex_class_6(self):
        input = """class Q {
            var numbers: [10]int;
            func @findSmallest(): int {
                var min: int = numbers[0];
                for i := 1; i < 10; i := i + 1 {
                    if numbers[i] < min {
                        min := numbers[i];
                    }
                }
                return @min;
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Q"),[
                    AttributeDecl(VarDecl(Id("numbers"),ArrayType(10,IntType()))),
                    MethodDecl(Id("@findSmallest"),[],IntType(),Block([
                        VarDecl(Id("min"),IntType(),ArrayCell(Id("numbers"),IntLiteral(0))),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("<",ArrayCell(Id("numbers"),Id("i")),Id("min")),Block([
                                Assign(Id("min"),ArrayCell(Id("numbers"),Id("i")))
                            ]))
                        ])),
                        Return(FieldAccess(None,Id("@min")))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,315))

    def test_complex_class_7(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("R"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("x"),IntType(),IntLiteral(5)),
                        VarDecl(Id("y"),IntType(),IntLiteral(10)),
                        If(BinaryOp("<",Id("x"),Id("y")),Block([
                            CallStmt(Id("io"),Id("@writeString"),[StringLiteral("x is less than y")])
                        ]),None,Block([
                            CallStmt(Id("io"),Id("@writeString"),[StringLiteral("x is greater than or equal to y")])
                        ]))
                    ])
                    )
                ])
            ]
            )
        )
        self.assertTrue(TestAST.test(input,expect,316))

    def test_complex_class_8(self):
        input = """class Q {
            var numbers: [10]int;
            func @findSmallest(): int {
                var min,b: int ;
                
                return min;
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Q"),[
                    AttributeDecl(VarDecl(Id("numbers"),ArrayType(10,IntType()))),
                    MethodDecl(Id("@findSmallest"),[],IntType(),Block([
                        VarDecl(Id("min"),IntType()),
                        VarDecl(Id("b"),IntType()),
                        Return(Id("min"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,317))


