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
   