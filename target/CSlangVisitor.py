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


    # Visit a parse tree produced by CSlangParser#attributelist.
    def visitAttributelist(self, ctx:CSlangParser.AttributelistContext):
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


    # Visit a parse tree produced by CSlangParser#body.
    def visitBody(self, ctx:CSlangParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#bodydecl.
    def visitBodydecl(self, ctx:CSlangParser.BodydeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#mctype.
    def visitMctype(self, ctx:CSlangParser.MctypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#membername.
    def visitMembername(self, ctx:CSlangParser.MembernameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#call_stmt.
    def visitCall_stmt(self, ctx:CSlangParser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exprlist.
    def visitExprlist(self, ctx:CSlangParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#nonNULL_exprlist.
    def visitNonNULL_exprlist(self, ctx:CSlangParser.NonNULL_exprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#expr.
    def visitExpr(self, ctx:CSlangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp1.
    def visitExp1(self, ctx:CSlangParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp2.
    def visitExp2(self, ctx:CSlangParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp3.
    def visitExp3(self, ctx:CSlangParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operands.
    def visitOperands(self, ctx:CSlangParser.OperandsContext):
        return self.visitChildren(ctx)



del CSlangParser