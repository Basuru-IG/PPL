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

    def test_complex_class_9(self):
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
        self.assertTrue(TestAST.test(input,expect,318))

    def test_complex_class_10(self):
        input = """
        class ComplexExpressions {
            func complexMethod(): int {
                return (1 + 2) * (3 - 4) / (5 + 6) % 7;
            }
            
            func callComplex(): void {
                var result: int;
                result := self.complexMethod();
                io.@writeInt(result);
            }
        }"""
        expect = str(
            Program(
                [
                    ClassDecl(Id("ComplexExpressions"),[
                            MethodDecl(Id("complexMethod"),[],IntType(),Block(
                                    [
                                        Return(
                                            BinaryOp("%",
                                                BinaryOp( "/",
                                                    BinaryOp(
                                                        "*",
                                                        BinaryOp(
                                                            "+",
                                                            IntLiteral(1),
                                                            IntLiteral(2),
                                                        ),
                                                        BinaryOp(
                                                            "-",
                                                            IntLiteral(3),
                                                            IntLiteral(4),
                                                        ),
                                                    ),
                                                    BinaryOp(
                                                        "+",
                                                        IntLiteral(5),
                                                        IntLiteral(6),
                                                    ),
                                                ),
                                                IntLiteral(7),
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            MethodDecl(Id("callComplex"),[],VoidType(),Block([
                                        VarDecl(Id("result"), IntType()),
                                        Assign(
                                            Id("result"),
                                            CallExpr(
                                                SelfLiteral(), Id("complexMethod"), []
                                            ),
                                        ),
                                        CallStmt(
                                            Id("io"), Id("@writeInt"), [Id("result")]
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_complex_class_11(self):
        input = """class HNode {
                        var value: int;
                        var pnext: HNode;
                        
                        func constructor(value: int, pnext: HNode) {
                            self.value := value;
                            self.pnext := pnext;
                        }
                    }

                    class List {
                        var head: HNode;
                        
                        func constructor(head: HNode) {
                            self.head := head;
                        }
                        
                        func addNode(value: int): void {
                            var newN: HNode = new HNode(value, self.head);
                            self.head := newN;
                        }
                        
                        func search(value: int): bool {
                            for pcurrent := self.head; pcurrent != null; pcurrent := pcurrent.pnext {
                                if pcurrent.value == value {
                                    return true;
                                }
                            }
                            return false;
                        }
                        
                        func printlist(): void {
                            for pcurrent := self.head; pcurrent != null; pcurrent := pcurrent.pnext {
                                io.@writeInt(pcurrent.value);
                            }
                        }
                    }"""
        expect = "Program([ClassDecl(Id(HNode),[AttributeDecl(VarDecl(Id(value),IntType)),AttributeDecl(VarDecl(Id(pnext),ClassType(Id(HNode)))),MethodDecl(Id(constructor),[Param(Id(value),IntType),Param(Id(pnext),ClassType(Id(HNode)))],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(value)),Id(value)),AssignStmt(FieldAccess(Self(),Id(pnext)),Id(pnext))]))]),ClassDecl(Id(List),[AttributeDecl(VarDecl(Id(head),ClassType(Id(HNode)))),MethodDecl(Id(constructor),[Param(Id(head),ClassType(Id(HNode)))],VoidType,Block([AssignStmt(FieldAccess(Self(),Id(head)),Id(head))])),MethodDecl(Id(addNode),[Param(Id(value),IntType)],VoidType,Block([VarDecl(Id(newN),ClassType(Id(HNode)),NewExpr(Id(HNode),[Id(value),FieldAccess(Self(),Id(head))])),AssignStmt(FieldAccess(Self(),Id(head)),Id(newN))])),MethodDecl(Id(search),[Param(Id(value),IntType)],BoolType,Block([For(AssignStmt(Id(pcurrent),FieldAccess(Self(),Id(head))),BinaryOp(!=,Id(pcurrent),NullLiteral()),AssignStmt(Id(pcurrent),FieldAccess(Id(pcurrent),Id(pnext))),Block([If(BinaryOp(==,FieldAccess(Id(pcurrent),Id(value)),Id(value)),Block([Return(BooleanLit(True))]))])]),Return(BooleanLit(False))])),MethodDecl(Id(printlist),[],VoidType,Block([For(AssignStmt(Id(pcurrent),FieldAccess(Self(),Id(head))),BinaryOp(!=,Id(pcurrent),NullLiteral()),AssignStmt(Id(pcurrent),FieldAccess(Id(pcurrent),Id(pnext))),Block([Call(Id(io),Id(@writeInt),[FieldAccess(Id(pcurrent),Id(value))])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 320))
    
    def test_complex_class_12(self):
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
        self.assertTrue(TestAST.test(input,expect,321))

    def test_complex_class_13(self):
        input = """class S {
            var n: int;
            func @isEven(): bool {
                if n % 2 == 0 {
                    return true;
                }
                return false;
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("S"),[
                    AttributeDecl(VarDecl(Id("n"),IntType())),
                    MethodDecl(Id("@isEven"),[],BoolType(),Block([
                        If(BinaryOp("==",BinaryOp("%",Id("n"),IntLiteral(2)),IntLiteral(0)),Block([
                            Return(BooleanLiteral(True))
                        ])),
                        Return(BooleanLiteral(False))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,322))

    def test_complex_class_14(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(1))),
                    AttributeDecl(VarDecl(Id("b"),IntType(),IntLiteral(2))),
                    MethodDecl(Id("@main"),[],ClassType(Id("arr")),Block([
                        If(BinaryOp(">",Id("a"),Id("b")),Block([
                            Assign(Id("a"),BinaryOp("*",Id("a"),IntLiteral(2)))
                        ]),None,Block([
                            Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,323))

    def test_complex_class_15(self):
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
        self.assertTrue(TestAST.test(input,expect,324))

    def test_complex_class_16(self):
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
                            Assign(ArrayCell(Id("fib"),Id("i")),BinaryOp("+",ArrayCell(Id("fib"),BinaryOp("-",Id("i"),IntLiteral(1))),ArrayCell(Id("fib"),BinaryOp("-",Id("i"),IntLiteral
                            (2)))))
                        ])),
                        Return(Id("fib"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,325))

    def test_complex_class_17(self):
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
        expect = str(Program( 
            [
                ClassDecl(Id("O"),[
                    AttributeDecl(VarDecl(Id("grades"),ArrayType(5,FloatType()))),
                    MethodDecl(Id("@calculateGradeAverage"),[],FloatType(),Block([
                        VarDecl(Id("total"),FloatType(),FloatLiteral(0.0)),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            Assign(Id("total"),BinaryOp("+",Id("total"),ArrayCell(Id("grades"),Id("i"))))
                        ])),
                        Return(BinaryOp("/",Id("total"),FloatLiteral(5.0)))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test_complex_class_18(self):
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
        self.assertTrue(TestAST.test(input,expect,327))

    def test_complex_class_19(self):
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
        self.assertTrue(TestAST.test(input,expect,328))

    def test_complex_class_20(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("L"),[
                    AttributeDecl(VarDecl(Id("n"),IntType())),
                    MethodDecl(Id("@isPrime"),[],BoolType(),Block([
                        If(BinaryOp("<=",Id("n"),IntLiteral(1)),Block([
                            Return(BooleanLiteral(False))
                        ])),
                        For(Assign(Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),Id("n")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("==",BinaryOp("%",Id("n"),Id("i")),IntLiteral(0)),Block([
                                Return(BooleanLiteral(False))
                            ]))
                        ])),
                        Return(BooleanLiteral(True))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,329))

    def test_complex_class_21(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("K"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("x"),IntType(),IntLiteral(1)),
                        VarDecl(Id("y"),IntType(),IntLiteral(2)),
                        VarDecl(Id("z"),IntType(),IntLiteral(3)),
                        VarDecl(Id("sum"),IntType(),BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z"))),
                        If(BinaryOp(">=",Id("sum"),IntLiteral(5)),Block([
                            CallStmt(Id("io"),Id("@writeString"),[StringLiteral("Sum is greater than or equal to 5")])
                        ]),None,Block([
                            CallStmt(Id("io"),Id("@writeString"),[StringLiteral("Sum is less than 5")])
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        
        self.assertTrue(TestAST.test(input,expect,330))

    def test_complex_class_22(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("J"),[
                    AttributeDecl(VarDecl(Id("total"),IntType())),
                    MethodDecl(Id("@sumOfEvenNumbers"),[],VoidType(),Block([
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([
                                Assign(Id("total"),BinaryOp("+",Id("total"),Id("i")))
                            ]))
                        ])),
                        CallStmt(Id("io"),Id("@writeInt"),[Id("total")])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,331))

    def test_complex_class_23(self):
        input = """class I {
            var numbers: [5]int;
            func @initializeArray(): void {
                for i := 0; i < 5; i := i + 1 {
                    numbers[i] := i * 2;
                }
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("I"),[
                    AttributeDecl(VarDecl(Id("numbers"),ArrayType(5,IntType()))),
                    MethodDecl(Id("@initializeArray"),[],VoidType(),Block([
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            Assign(ArrayCell(Id("numbers"),Id("i")),BinaryOp("*",Id("i"),IntLiteral(2)))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        
        self.assertTrue(TestAST.test(input,expect,332))

    def test_complex_class_24(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("H"),[
                    AttributeDecl(VarDecl(Id("isValid"),BoolType(),BooleanLiteral(True))),
                    MethodDecl(Id("@toggleFlag"),[],VoidType(),Block([
                        If(Id("isValid"),Block([
                            Assign(Id("isValid"),BooleanLiteral(False))
                        ]),None,Block([
                            Assign(Id("isValid"),BooleanLiteral(True))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,333))

    def test_complex_class_25(self):
        input = """class G {
            func @main(): void {
                var sum: int = 0;
                for i := 1; i <= 100; i := i + 1 {
                    sum := sum + i;
                }
                io.@writeInt(sum);
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("G"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("sum"),IntType(),IntLiteral(0)),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(100)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("i")))
                        ])),
                        CallStmt(Id("io"),Id("@writeInt"),[Id("sum")])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,334))

    def test_complex_class_26(self):
        input = """class F {
            var counter: int;
            func @countToTen(): void {
                counter := 1;
            }
        }"""
        expect = str(Program( 
            [
                ClassDecl(Id("F"),[
                    AttributeDecl(VarDecl(Id("counter"),IntType())),
                    MethodDecl(Id("@countToTen"),[],VoidType(),Block([
                        Assign(Id("counter"),IntLiteral(1))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,335))

    def test_complex_class_27(self):
        input = """class E {
            const PI: float = 3.14159265359;
            func @calculateArea(radius: float): float {
                return PI * radius * radius;
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("E"),[
                    AttributeDecl(ConstDecl(Id("PI"),FloatType(),FloatLiteral(3.14159265359))),
                    MethodDecl(Id("@calculateArea"),[VarDecl(Id("radius"),FloatType())],FloatType(),Block([
                        Return(BinaryOp("*",BinaryOp("*",Id("PI"),Id("radius")),Id("radius")))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,336))

    def test_complex_class_28(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("total"),IntType()),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            Assign(Id("total"),BinaryOp("+",Id("total"),Id("i"))),
                            If(BinaryOp("==",Id("i"),IntLiteral(3)),Block([
                                Break()
                            ]))
                        ])),
                        CallStmt(Id("io"),Id("@writeInt"),[Id("total")])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,337))

    def test_complex_class_29(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("count"),IntType()),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([
                                Assign(Id("count"),BinaryOp("+",Id("count"),IntLiteral(1)))
                            ]))
                        ])),
                        CallStmt(Id("io"),Id("@writeInt"),[Id("count")])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,338))

    def test_complex_class_30(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("result"),IntType()),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([
                                Assign(Id("result"),BinaryOp("*",Id("i"),IntLiteral(2))),
                                CallStmt(Id("io"),Id("@writeInt"),[Id("result")])
                            ]),None,Block([
                                Assign(Id("result"),BinaryOp("*",Id("i"),IntLiteral(3))),
                                CallStmt(Id("io"),Id("@writeInt"),[Id("result")])
                            ]))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,339))

    def test_complex_class_31(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType()),
                        If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([
                            Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                        ])),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,340))

    def test_complex_class_32(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType()),
                        If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([
                            Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),
                            If(BinaryOp(">",Id("x"),IntLiteral(5)),Block([
                                Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))
                            ]))
                        ]),None,Block([
                            Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))
                        ])),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,341))

    def test_complex_class_33(self):
        """Test a program with variables and functions"""
        input = """class Program {
            var x: int;
            func @fact(n: int):int {
                if n == 0 {return 1;}
                else {return n * @fact(n - 1);}
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    AttributeDecl(VarDecl(Id("x"),IntType())),
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )   
        self.assertTrue(TestAST.test(input,expect,342))

    def test_complex_class_34(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@fnc"),[],IntType(),Block([
                        VarDecl(Id("delta"),ArrayType(10,ClassType(Id("delta")))),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeStr"),[Id("i")])
                        ])),
                        Return(ArrayCell(Id("arr"),IntLiteral(5)))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,343))
    
    def test_complex_class_35(self):
        input = """class Test { 
        var x: int = 5 * 3 + 2 * !true;
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(3)),BinaryOp("*",IntLiteral(2),UnaryOp("!",BooleanLiteral(True))))))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,344))

    def test_complex_class_36(self):
        input = """class Test { 
        var x: int = 5 * 3 + 2 * !true;
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(3)),BinaryOp("*",IntLiteral(2),UnaryOp("!",BooleanLiteral(True))))))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,345))

    def test_complex_class_37(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    AttributeDecl(VarDecl(Id("max"),IntType())),
                    MethodDecl(Id("@findMax"),[VarDecl(Id("numbers"),ArrayType(10,IntType()))],IntType(),Block([
                        Assign(Id("max"),ArrayCell(Id("numbers"),IntLiteral(0))),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp(">",ArrayCell(Id("numbers"),Id("i")),Id("max")),Block([
                                Assign(Id("max"),ArrayCell(Id("numbers"),Id("i")))
                            ]))
                        ])),
                        Return(Id("max"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,346))

    def test_complex_class_38(self):
        input = """class Loop {
            func @main(): void {
                var sum: int = 0;
                for i := 1; i <= 100; i := i + 1 {
                    sum := sum + i;
                }
                io.@writeInt(sum);
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("sum"),IntType(),IntLiteral(0)),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(100)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            Assign(Id("sum"),BinaryOp("+",Id("sum"),Id("i")))
                        ])),
                        CallStmt(Id("io"),Id("@writeInt"),[Id("sum")])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,347))

    def test_complex_class_39(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    AttributeDecl(VarDecl(Id("prime"),BoolType())),
                    MethodDecl(Id("@isPrime"),[VarDecl(Id("num"),IntType())],BoolType(),Block([
                        Assign(Id("prime"),BooleanLiteral(True)),
                        For(Assign(Id("i"),IntLiteral(2)),BinaryOp("<",Id("i"),Id("num")),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("==",BinaryOp("%",Id("num"),Id("i")),IntLiteral(0)),Block([
                                Assign(Id("prime"),BooleanLiteral(False))
                            ]))
                        ])),
                        Return(Id("prime"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test_complex_class_40(self):
        input = """
            class HNode {
                var value: int;
                var pnext: HNode;
                
                func constructor(value: int, pnext: HNode) {
                    self.value := value;
                    self.pnext := pnext;
                }
            }

            class HLList {
                var head: HNode;
                func constructor(head: HNode) {
                    self.head := head;
                }
                func addNode(value: int): void {
                    var newHNode: HNode = new HNode(value, self.head);
                    self.head := newHNode;
                }
                func search(value: int): bool {
                    for pcurrent := self.head; pcurrent != null; pcurrent := pcurrent.pnext {
                        if pcurrent.value == value {
                            return true;
                        }
                    }
                    return false;
                }
                func printlist(): void {
                    for pcurrent := self.head; pcurrent != null; pcurrent := pcurrent.pnext {
                        io.@writeInt(pcurrent.value);
                    }
                }
            }"""
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("HNode"),
                        [
                            AttributeDecl(VarDecl(Id("value"), IntType())),
                            AttributeDecl(VarDecl(Id("pnext"), ClassType(Id("HNode")))),
                            MethodDecl(
                                Id("constructor"),
                                [
                                    VarDecl(Id("value"), IntType()),
                                    VarDecl(Id("pnext"), ClassType(Id("HNode"))),
                                ],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            FieldAccess(SelfLiteral(), Id("value")),
                                            Id("value"),
                                        ),
                                        Assign(
                                            FieldAccess(SelfLiteral(), Id("pnext")),
                                            Id("pnext"),
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    ClassDecl(
                        Id("HLList"),
                        [
                            AttributeDecl(VarDecl(Id("head"), ClassType(Id("HNode")))),
                            MethodDecl(
                                Id("constructor"),
                                [VarDecl(Id("head"), ClassType(Id("HNode")))],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            FieldAccess(SelfLiteral(), Id("head")),
                                            Id("head"),
                                        ),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("addNode"),
                                [VarDecl(Id("value"), IntType())],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("newHNode"),
                                            ClassType(Id("HNode")),
                                            NewExpr(
                                                Id("HNode"),
                                                [
                                                    Id("value"),
                                                    FieldAccess(
                                                        SelfLiteral(), Id("head")
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assign(
                                            FieldAccess(SelfLiteral(), Id("head")),
                                            Id("newHNode"),
                                        ),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("search"),
                                [VarDecl(Id("value"), IntType())],
                                BoolType(),
                                Block(
                                    [
                                        For(
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(SelfLiteral(), Id("head")),
                                            ),
                                            BinaryOp(
                                                "!=", Id("pcurrent"), NullLiteral()
                                            ),
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(Id("pcurrent"), Id("pnext")),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        BinaryOp(
                                                            "==",
                                                            FieldAccess(
                                                                Id("pcurrent"),
                                                                Id("value"),
                                                            ),
                                                            Id("value"),
                                                        ),
                                                        Block(
                                                            [
                                                                Return(
                                                                    BooleanLiteral(True)
                                                                )
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ),
                                        Return(BooleanLiteral(False)),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("printlist"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(SelfLiteral(), Id("head")),
                                            ),
                                            BinaryOp(
                                                "!=", Id("pcurrent"), NullLiteral()
                                            ),
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(Id("pcurrent"), Id("pnext")),
                                            ),
                                            Block(
                                                [
                                                    CallStmt(
                                                        Id("io"),
                                                        Id("@writeInt"),
                                                        [
                                                            FieldAccess(
                                                                Id("pcurrent"),
                                                                Id("value"),
                                                            )
                                                        ],
                                                    )
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_complex_class_41(self):
        input = """
            class HNode {
                var value: int;
                var pnext: HNode;
                
                func constructor(value: int, pnext: HNode) {
                    self.value := value;
                    self.pnext := pnext;
                }
            }

            class HLList {
                var head: HNode;
                func constructor(head: HNode) {
                    self.head := head;
                }
                func addNode(value: int): void {
                    var newHNode: HNode = new HNode(value, self.head);
                    self.head := newHNode;
                }
                func search(value: int): bool {
                    for pcurrent := self.head; pcurrent != null; pcurrent := pcurrent.pnext {
                        if pcurrent.value == value {
                            return true;
                        }
                    }
                    return false;
                }
                func printlist(): void {
                    for pcurrent := self.head; pcurrent != null; pcurrent := pcurrent.pnext {
                        io.@writeInt(pcurrent.value);
                    }
                }
            }"""
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("HNode"),
                        [
                            AttributeDecl(VarDecl(Id("value"), IntType())),
                            AttributeDecl(VarDecl(Id("pnext"), ClassType(Id("HNode")))),
                            MethodDecl(
                                Id("constructor"),
                                [
                                    VarDecl(Id("value"), IntType()),
                                    VarDecl(Id("pnext"), ClassType(Id("HNode"))),
                                ],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            FieldAccess(SelfLiteral(), Id("value")),
                                            Id("value"),
                                        ),
                                        Assign (
                                            FieldAccess(SelfLiteral(), Id("pnext")),
                                            Id("pnext"),
                                        ), 
                                    ],
                                ),
                            ),
                        ],
                    ),
                    ClassDecl(
                        Id("HLList"),
                        [
                            AttributeDecl(VarDecl(Id("head"), ClassType(Id("HNode")))),
                            MethodDecl(
                                Id("constructor"),
                                [VarDecl(Id("head"), ClassType(Id("HNode")))],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            FieldAccess(SelfLiteral(), Id("head")),
                                            Id("head"),
                                        ),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("addNode"),
                                [VarDecl(Id("value"), IntType())],
                                VoidType(),
                                Block(
                                    [
                                        VarDecl(
                                            Id("newHNode"),
                                            ClassType(Id("HNode")),
                                            NewExpr(
                                                Id("HNode"),
                                                [
                                                    Id("value"),
                                                    FieldAccess(
                                                        SelfLiteral(), Id("head")
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assign(
                                            FieldAccess(SelfLiteral(), Id("head")),
                                            Id("newHNode"),
                                        ),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("search"),
                                [VarDecl(Id("value"), IntType())],
                                BoolType(),
                                Block(
                                    [
                                        For(
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(SelfLiteral(), Id("head")),
                                            ),
                                            BinaryOp(
                                                "!=", Id("pcurrent"), NullLiteral()
                                            ),
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(Id("pcurrent"), Id("pnext")),
                                            ),
                                            Block(
                                                [
                                                    If(
                                                        BinaryOp(
                                                            "==",
                                                            FieldAccess(
                                                                Id("pcurrent"),
                                                                Id("value"),
                                                            ),
                                                            Id("value"),
                                                        ),
                                                        Block(
                                                            [
                                                                Return(
                                                                    BooleanLiteral(True)
                                                                )
                                                            ]
                                                        ),
                                                    )
                                                ]
                                            ),
                                        ),
                                        Return(BooleanLiteral(False)),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("printlist"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        For(
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(SelfLiteral(), Id("head")),
                                            ),
                                            BinaryOp(
                                                "!=", Id("pcurrent"), NullLiteral()
                                            ),
                                            Assign(
                                                Id("pcurrent"),
                                                FieldAccess(Id("pcurrent"), Id("pnext")),
                                            ),
                                            Block(
                                                [
                                                    CallStmt(
                                                        Id("io"),
                                                        Id("@writeInt"),
                                                        [
                                                            FieldAccess(
                                                                Id("pcurrent"),
                                                                Id("value"),
                                                            )
                                                        ],
                                                    )
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    ),
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_complex_class_42(self):
        input = """
    class Ass   {
        var x: int;
        
        func cal(a: int, b: int): void {
            x := a + b;
            y := x * a;
            self.printR();
        }
        
        func printR(): void {
            io.@writeInt(x);
        }
    }
        """
        expect = str(
            Program(
                [
                    ClassDecl(
                        Id("Ass"),
                        [
                            AttributeDecl(VarDecl(Id("x"), IntType())),
                            MethodDecl(
                                Id("cal"),
                                [
                                    VarDecl(Id("a"), IntType()),
                                    VarDecl(Id("b"), IntType()),
                                ],
                                VoidType(),
                                Block(
                                    [
                                        Assign(
                                            Id("x"), BinaryOp("+", Id("a"), Id("b"))
                                        ),
                                        Assign(
                                            Id("y"), BinaryOp("*", Id("x"), Id("a"))
                                        ),
                                        CallStmt(SelfLiteral(), Id("printR"), []),
                                    ]
                                ),
                            ),
                            MethodDecl(
                                Id("printR"),
                                [],
                                VoidType(),
                                Block(
                                    [
                                        CallStmt(Id("io"), Id("@writeInt"), [Id("x")])
                                    ]
                                ),
                            ),
                        ],
                    )
                ]
            )
        )
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_complex_class_43(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("arr"),ArrayType(10,IntType())),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeInt"),[Id("i")])
                        ])),
                        Return(ArrayCell(Id("arr"),IntLiteral(5)))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,352))

    
    def test_complex_class_44(self):
        input = """class Program {
            func @main():int {
                var arr: [10]int;
                for i := 0; i < 10; i := i + 1 {
                }
                return arr[5];
            }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("arr"),ArrayType(10,IntType())),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([])),
                        Return(ArrayCell(Id("arr"),IntLiteral(5)))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,353))

    def test_complex_class_45(self):
        input = """class Program {
            func @main():int {
                return 0;
            }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        Return(IntLiteral(0))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,354))

    def test_complex_class_46(self):
        input = """class Program {
            var x: int;
            func @main():int {
                x := 0;
                return x;
            }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    AttributeDecl(VarDecl(Id("x"),IntType())),
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        Assign(Id("x"),IntLiteral(0)),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,355))

    def test_complex_class_47(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(IntLiteral(0))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,356))

    def test_complex_class_48(self):
        input = """class Program {
        func  @inc( n, delta: int):void {
            x.b()[4+55] := x.m()[3];
            a[3+x.foo(2)] := a[b[2+1]] +3;
            return n;
        }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@inc"),[VarDecl(Id("n"),IntType()),VarDecl(Id("delta"),IntType())],VoidType(),Block([
                        Assign(ArrayCell(CallExpr(Id("x"),Id("b"),[]),BinaryOp("+",IntLiteral(4),IntLiteral(55))),ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(3))),
                        Assign(ArrayCell(Id("a"),BinaryOp("+",IntLiteral(3),CallExpr(Id("x"),Id("foo"),[IntLiteral(2)]))),BinaryOp("+",ArrayCell(Id("a"),ArrayCell(Id("b"),BinaryOp("+",IntLiteral(2),IntLiteral(1)))),IntLiteral(3))),
                        Return(Id("n"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,357))

    def test_complex_class_49(self):
        input = """class Program2 { var x: int = new X(); func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}} func @inc( n, delta: int):void { n := n + delta; return n; } func @main():int { var delta: int = @fact(3); @inc(self.x, delta); io.@writeInt(self.x); }}"""
        expect = str(Program(
            [
                ClassDecl(Id("Program2"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),NewExpr(Id("X"),[]))),
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    ),
                    MethodDecl(Id("@inc"),[VarDecl(Id("n"),IntType()),VarDecl(Id("delta"),IntType())],VoidType(),Block([
                        Assign(Id("n"),BinaryOp("+",Id("n"),Id("delta"))),
                        Return(Id("n"))
                    ])
                    ),
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("delta"),IntType(),CallExpr(None,Id("@fact"),[IntLiteral(3)])),
                        CallStmt(None,Id("@inc"),[FieldAccess(SelfLiteral(),Id("x")),Id("delta")]),
                        CallStmt(Id("io"),Id("@writeInt"),[FieldAccess(SelfLiteral(),Id("x"))])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,358))

    def test_complex_class_50(self):
        input = """class Program2 { var x: int = 65; func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}} func @inc( n, delta: int):void { n := n + delta; return n; } func @main():int { var delta: int = @fact(3); @inc(self.x, delta); io.@writeInt(self.x); }}"""
        expect = str(Program(
            [
                ClassDecl(Id("Program2"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),IntLiteral(65))),
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    ),
                    MethodDecl(Id("@inc"),[VarDecl(Id("n"),IntType()),VarDecl(Id("delta"),IntType())],VoidType(),Block([
                        Assign(Id("n"),BinaryOp("+",Id("n"),Id("delta"))),
                        Return(Id("n"))
                    ])
                    ),
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("delta"),IntType(),CallExpr(None,Id("@fact"),[IntLiteral(3)])),
                        CallStmt(None,Id("@inc"),[FieldAccess(SelfLiteral(),Id("x")),Id("delta")]),
                        CallStmt(Id("io"),Id("@writeInt"),[FieldAccess(SelfLiteral(),Id("x"))])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,359))

    def test_complex_class_51(self):
        input = """class ar5 { var a: [10]bool;}"""
        expect = str(Program(
            [
                ClassDecl(Id("ar5"),[
                    AttributeDecl(VarDecl(Id("a"),ArrayType(10,BoolType())))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,360))

    def test_complex_class_52(self):
        input = """class Shape <- Retangle {func constructor() {return self.length * self.width; } }"""
        expect = str(Program(
            [
                ClassDecl(Id("Retangle"),[
                    MethodDecl(Id("constructor"),[],None,Block([
                        Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))
                    ])
                    )
                ],Id("Shape"))
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,361))

    def test_complex_class_53(self):
        input = """class Shape <- Retangle {func getArea():int {return self.length * self.width; } }"""
        expect = str(Program(
            [
                ClassDecl(Id("Retangle"),[
                    MethodDecl(Id("getArea"),[],IntType(),Block([
                        Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))
                    ])
                    )
                ],Id("Shape"))
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,362))

    def test_complex_class_54(self):
        input = """class Sms {func @main():void {io.@writeInt(Shape.@numOfShape);}var length, width: int; func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = str(Program(
            [
                ClassDecl(Id("Sms"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        CallStmt(Id("io"),Id("@writeInt"),[FieldAccess(Id("Shape"),Id("@numOfShape"))])
                    ])
                    ),
                    AttributeDecl(VarDecl(Id("length"),IntType())),
                    AttributeDecl(VarDecl(Id("width"),IntType())),
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,363))

    def test_complex_class_55(self):
        input = """class funcc {func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = str(Program(
            [
                ClassDecl(Id("funcc"),[
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,364))

    def test_complex_class_56(self):
        input = """class Ss {func @fact(n: int):int{ if n == [3.0, 3, 12.3e-1] {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = str(Program(
            [
                ClassDecl(Id("Ss"),[
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),ArrayLiteral([FloatLiteral(3.0),IntLiteral(3),FloatLiteral(1.23)])),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,365))

    def test_complex_class_57(self):
        input = """class Ss {func @fact(n: int):int{ if n == 0 {return 1;} else {return n * @fact(n - 1);}}}"""
        expect = str(Program(
            [
                ClassDecl(Id("Ss"),[
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,366))

    def test_complex_class_58(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    AttributeDecl(VarDecl(Id("x"),IntType())),
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    ),
                    MethodDecl(Id("@inc"),[VarDecl(Id("n"),IntType()),VarDecl(Id("delta"),IntType())],VoidType(),Block([
                        Assign(Id("n"),BinaryOp("+",Id("n"),Id("delta"))),
                        Return(Id("n"))
                    ])
                    ),
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("delta"),IntType(),CallExpr(None,Id("@fact"),[IntLiteral(3)])),
                        CallStmt(None,Id("@inc"),[FieldAccess(SelfLiteral(),Id("x")),Id("delta")]),
                        CallStmt(Id("io"),Id("@writeInt"),[FieldAccess(SelfLiteral(),Id("x"))])
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,367))

    def test_complex_class_59(self):
        input = """class A{
            /* This is a block comment so // has no meaning here */
            //This is a line comment so /* has no meaning here
            }"""
        expect = str(Program(
            [
                ClassDecl(Id("A"),[])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,368))

    def test_complex_class_60(self):
        input = """class A{
            /* This is a block comment so // has no meaning here */
            //This is a line comment so /* has no meaning here
            }"""
        expect = str(Program(
            [
                ClassDecl(Id("A"),[])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,369))

    def test_complex_class_61(self):
        input = """class A{
            var @x, @y : int = 0, 0;
            /* This is a block comment, that
            may span in many lines*/
            //this is a line comment  @x, @y : int = 0, 0;
            }"""
        expect = str(Program(
            [
                ClassDecl(Id("A"),[
                    AttributeDecl(VarDecl(Id("@x"),IntType(),IntLiteral(0))),
                    AttributeDecl(VarDecl(Id("@y"),IntType(),IntLiteral(0)))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,370))

    def test_complex_class_62(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("sum"),IntType(),IntLiteral(0)),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeInt"),[Id("i")])
                        ])),
                        Return(Id("sum"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,371))

    def test_complex_class_63(self):
        input = """class Program {
            func @main():int {
                var i: int = 0;
                return i;
            }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("i"),IntType(),IntLiteral(0)),
                        Return(Id("i"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,372))

    def test_complex_class_64(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("a"),IntType()),
                        VarDecl(Id("b"),IntType()),
                        VarDecl(Id("c"),IntType()),
                        Assign(Id("a"),IntLiteral(1)),
                        Assign(Id("b"),IntLiteral(2)),
                        Assign(Id("c"),BinaryOp("+",Id("a"),Id("b"))),
                        Return(Id("c"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,373))

    def test_complex_class_65(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType(),IntLiteral(5)),
                        VarDecl(Id("y"),IntType(),IntLiteral(10)),
                        If(BinaryOp("<",Id("x"),Id("y")),Block([
                            Return(Id("x"))
                        ]),None,Block([
                            Return(Id("y"))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,374))

    def test_complex_class_66(self):
        input = """class Program {
            func @main():int {
                var a, b, c: int = 1, 2, 3;
                return a + b + c;
            }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("a"),IntType(),IntLiteral(1)),
                        VarDecl(Id("b"),IntType(),IntLiteral(2)),
                        VarDecl(Id("c"),IntType(),IntLiteral(3)),
                        Return(BinaryOp("+",BinaryOp("+",Id("a"),Id("b")),Id("c")))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,375))

    def test_complex_class_67(self):
        input = input = """class Program {
            func @main():int {
                var x: int;
                x := -5;
                return x;
            }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType()),
                        Assign(Id("x"),UnaryOp("-",IntLiteral(5))),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,376))

    def test_complex_class_68(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("arr"),ArrayType(10,IntType())),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeInt"),[Id("i")])
                        ])),
                        Return(ArrayCell(Id("arr"),IntLiteral(5)))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,377))

    def test_complex_class_69(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType(),IntLiteral(5)),
                        VarDecl(Id("y"),IntType(),IntLiteral(10)),
                        If(BinaryOp("<",Id("x"),Id("y")),Block([
                            CallStmt(None,Id("@writeln"),[StringLiteral("x is less than y")])
                        ]),None,Block([
                            CallStmt(None,Id("@writeln"),[StringLiteral("x is greater than or equal to y")])
                            ])),
                        Return(IntLiteral(0))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,378))
    
    def test_complex_class_70(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType(),IntLiteral(5)),
                        VarDecl(Id("y"),IntType(),IntLiteral(10)),
                        If(BinaryOp("<",Id("x"),Id("y")),Block([
                            Assign(Id("x"),BinaryOp("*",Id("x"),IntLiteral(2)))
                        ]),None,Block([
                            Assign(Id("x"),BinaryOp("/",Id("x"),IntLiteral(2)))
                        ])),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,379))

    def test_complex_class_71(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType(),IntLiteral(5)),
                        VarDecl(Id("y"),IntType(),IntLiteral(10)),
                        If(BinaryOp("<",Id("x"),Id("y")),Block([
                            If(BinaryOp(">",Id("y"),IntLiteral(15)),Block([
                                Assign(Id("x"),BinaryOp("*",Id("x"),IntLiteral(2)))
                            ]),None,Block([
                                Assign(Id("x"),BinaryOp("/",Id("x"),IntLiteral(2)))
                            ]))
                        ]),None,Block([
                            Assign(Id("x"),IntLiteral(0))
                        ])),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,380))

    def test_complex_class_72(self):
        input = """class Program {
            func @main():int {
                var x: int = 5;
                var y: int = 10;
                return x;
            }
        }
        """
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType(),IntLiteral(5)),
                        VarDecl(Id("y"),IntType(),IntLiteral(10)),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,381))

    def test_complex_class_73(self):
        input = """class Test {
            func @main():int {
                return 1.2;
            }
            }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        Return(FloatLiteral(1.2))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,382))

    def test_complex_class_74(self):
        input = """class Test { var x: int = 5 * 3 + 2 && 3; }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),BinaryOp("&&",BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(3)),IntLiteral(2)),IntLiteral(3))))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,383))

    def test_complex_class_75(self):
        input = """class Test { var x: int = 5 * 3 + 2 || 3; }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),BinaryOp("||",BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(3)),IntLiteral(2)),IntLiteral(3))))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,384))

    def test_complex_class_76(self):
        input = """class Test { var x: int = 10.5; }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),FloatLiteral(10.5)))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,385))

    def test_complex_class_77(self):
        input = """class Test { 
        var x: int = 5 * 3 + 2 * !false;
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(3)),BinaryOp("*",IntLiteral(2),UnaryOp("!",BooleanLiteral(False))))))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,386))

    def test_complex_class_78(self):
        input = """class Test { 
        var x: int = 5 * 3 + 2 * !true;
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Test"),[
                    AttributeDecl(VarDecl(Id("x"),IntType(),BinaryOp("+",BinaryOp("*",IntLiteral(5),IntLiteral(3)),BinaryOp("*",IntLiteral(2),UnaryOp("!",BooleanLiteral(True))))))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,387))

    def test_complex_class_79(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@fnc"),[],IntType(),Block([
                        VarDecl(Id("delta"),ArrayType(10,ClassType(Id("delta")))),
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeStr"),[Id("i")])
                        ])),
                        Return(ArrayCell(Id("arr"),IntLiteral(5)))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,388))

    def test_complex_class_80(self):
        input = """class Program {
            const a, b, c: int = 3, 4, 6;
            var x, y, z: int;
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    AttributeDecl(ConstDecl(Id("a"),IntType(),IntLiteral(3))),
                    AttributeDecl(ConstDecl(Id("b"),IntType(),IntLiteral(4))),
                    AttributeDecl(ConstDecl(Id("c"),IntType(),IntLiteral(6))),
                    AttributeDecl(VarDecl(Id("x"),IntType())),
                    AttributeDecl(VarDecl(Id("y"),IntType())),
                    AttributeDecl(VarDecl(Id("z"),IntType()))
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,389))

    def test_complex_class_81(self):
        input = """class Program {
            var x: int;
            func @fact(n: int):int {
                if n == 0 {return 1;}
                else {return n * @fact(n - 1);}
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    AttributeDecl(VarDecl(Id("x"),IntType())),
                    MethodDecl(Id("@fact"),[VarDecl(Id("n"),IntType())],IntType(),Block([
                        If(BinaryOp("==",Id("n"),IntLiteral(0)),Block([
                            Return(IntLiteral(1))
                        ]),None,Block([
                            Return(BinaryOp("*",Id("n"),CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,390))

    def test_complex_class_82(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType()),
                        If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([
                            Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1))),
                            If(BinaryOp(">",Id("x"),IntLiteral(5)),Block([
                                Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))
                            ]),None,None)
                        ]),None,Block([
                            Assign(Id("x"),BinaryOp("-",Id("x"),IntLiteral(1)))
                        ])),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,391))

    def test_complex_class_83(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType()),
                        If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([
                            Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                        ]),None,None),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,392))

    def test_complex_class_84(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType()),
                        If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([
                            Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                        ]),None,None),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,393))

    def test_complex_class_85(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Program"),[
                    MethodDecl(Id("@main"),[],IntType(),Block([
                        VarDecl(Id("x"),IntType()),
                        If(BinaryOp("<",Id("x"),IntLiteral(10)),Block([
                            Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))
                        ]),None,None),
                        Return(Id("x"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,394))

    def test_complex_class_86(self):
        input = """class Loop {
            func @main(): void {
                for i := 0; i < 5; i := i + 1 {
                    io.@writeInt(i);
                }
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        For(Assign(Id("i"),IntLiteral(0)),BinaryOp("<",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeInt"),[Id("i")])
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,395))

    def test_complex_class_87(self):
        input = """class Loop {
            func @main(): void {
                for j := 10; j > 0; j := j - 1 {
                    io.@writeInt(j);
                }
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        For(Assign(Id("j"),IntLiteral(10)),BinaryOp(">",Id("j"),IntLiteral(0)),Assign(Id("j"),BinaryOp("-",Id("j"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeInt"),[Id("j")])
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,396)) 

    def test_complex_class_88(self):
        input = """class Loop {
            func @main(): void {
                for a := 5; a > 1; a := a - 1 {
                    io.@writeInt(a);
                }
            }
        }"""
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        For(Assign(Id("a"),IntLiteral(5)),BinaryOp(">",Id("a"),IntLiteral(1)),Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),Block([
                            CallStmt(Id("io"),Id("@writeInt"),[Id("a")])
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,397))

    def test_complex_class_89(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    AttributeDecl(VarDecl(Id("max"),IntType())),
                    MethodDecl(Id("@findMax"),[VarDecl(Id("numbers"),ArrayType(10,IntType()))],IntType(),Block([
                        Assign(Id("max"),ArrayCell(Id("numbers"),IntLiteral(0))),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(10)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp(">",ArrayCell(Id("numbers"),Id("i")),Id("max")),Block([
                                Assign(Id("max"),ArrayCell(Id("numbers"),Id("i")))
                            ]),None,None)
                        ])),
                        Return(Id("max"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,398))

    def test_complex_class_90(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("Loop"),[
                    MethodDecl(Id("@main"),[],VoidType(),Block([
                        VarDecl(Id("result"),IntType()),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<=",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),Block([
                                Assign(Id("result"),BinaryOp("*",Id("i"),IntLiteral(2))),
                                CallStmt(Id("io"),Id("@writeInt"),[Id("result")])
                            ]),None,Block([
                                Assign(Id("result"),BinaryOp("*",Id("i"),IntLiteral(3))),
                                CallStmt(Id("io"),Id("@writeInt"),[Id("result")])
                            ]))
                        ]))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,399))

    def test_complex_class_91(self):
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
        expect = str(Program(
            [
                ClassDecl(Id("M"),[
                    AttributeDecl(VarDecl(Id("data"),ArrayType(5,IntType()))),
                    MethodDecl(Id("@findMax"),[],IntType(),Block([
                        VarDecl(Id("max"),IntType(),ArrayCell(Id("data"),IntLiteral(0))),
                        For(Assign(Id("i"),IntLiteral(1)),BinaryOp("<",Id("i"),IntLiteral(5)),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),Block([
                            If(BinaryOp(">",ArrayCell(Id("data"),Id("i")),Id("max")),Block([
                                Assign(Id("max"),ArrayCell(Id("data"),Id("i")))
                            ]),None,None)
                        ])),
                        Return(Id("max"))
                    ])
                    )
                ])
            ]
            )
            )
        self.assertTrue(TestAST.test(input,expect,400))