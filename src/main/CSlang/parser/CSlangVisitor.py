# Generated from main/CSlang/parser/CSlang.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classdecl.
    def visitClassdecl(self, ctx:CSlangParser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#supperclass.
    def visitSupperclass(self, ctx:CSlangParser.SupperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classname.
    def visitClassname(self, ctx:CSlangParser.ClassnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#construcdecl.
    def visitConstrucdecl(self, ctx:CSlangParser.ConstrucdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classmember.
    def visitClassmember(self, ctx:CSlangParser.ClassmemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributedecl.
    def visitAttributedecl(self, ctx:CSlangParser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#initlist.
    def visitInitlist(self, ctx:CSlangParser.InitlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#methoddecl.
    def visitMethoddecl(self, ctx:CSlangParser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramdecl.
    def visitParamdecl(self, ctx:CSlangParser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#paramlist.
    def visitParamlist(self, ctx:CSlangParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#param.
    def visitParam(self, ctx:CSlangParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#mctype.
    def visitMctype(self, ctx:CSlangParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributelist.
    def visitAttributelist(self, ctx:CSlangParser.AttributelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#membername.
    def visitMembername(self, ctx:CSlangParser.MembernameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr1.
    def visitExpr1(self, ctx:CSlangParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr2.
    def visitExpr2(self, ctx:CSlangParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr3.
    def visitExpr3(self, ctx:CSlangParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr4.
    def visitExpr4(self, ctx:CSlangParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr5.
    def visitExpr5(self, ctx:CSlangParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr6.
    def visitExpr6(self, ctx:CSlangParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr7.
    def visitExpr7(self, ctx:CSlangParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr8.
    def visitExpr8(self, ctx:CSlangParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr9.
    def visitExpr9(self, ctx:CSlangParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr10.
    def visitExpr10(self, ctx:CSlangParser.Expr10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr11.
    def visitExpr11(self, ctx:CSlangParser.Expr11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#list_of_expr.
    def visitList_of_expr(self, ctx:CSlangParser.List_of_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#statement.
    def visitStatement(self, ctx:CSlangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#block_stmt.
    def visitBlock_stmt(self, ctx:CSlangParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#member_block.
    def visitMember_block(self, ctx:CSlangParser.Member_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assign_stmt.
    def visitAssign_stmt(self, ctx:CSlangParser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#if_stmt.
    def visitIf_stmt(self, ctx:CSlangParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#for_stmt.
    def visitFor_stmt(self, ctx:CSlangParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#break_stmt.
    def visitBreak_stmt(self, ctx:CSlangParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continue_stmt.
    def visitContinue_stmt(self, ctx:CSlangParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#return_stmt.
    def visitReturn_stmt(self, ctx:CSlangParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#method_stm.
    def visitMethod_stm(self, ctx:CSlangParser.Method_stmContext):
        return self.visitChildren(ctx)



del CSlangParser