from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    # comment is ANTLR code which need to generate AST
    # program: classdecl+ EOF;
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])
    # classdecl: CLASS ID (EXTENDS ID)? LB (classmember)* RB;
    def visitClassdecl(self,ctx:CSlangParser.ClassdeclContext):
        if ctx.EXTENDS():
            if ctx.classmember():
                memlist = self.visit(ctx.classmember())
            else:
                memlist = []
            return ClassDecl(Id(ctx.ID(0).getText()), memlist, Id(ctx.ID(1).getText()))
        else:
            if ctx.classmember():
                memlist = self.visit(ctx.classmember())
            else:
                memlist = []
            return ClassDecl(Id(ctx.ID(0).getText()), memlist)
    #classmember: attributedecl | methoddecl | construcdecl;
    def visitClassmember(self,ctx:CSlangParser.ClassmemberContext):
        return self.visitChildren(ctx)
    # construcdecl: FUNC CONSTRUCTOR paramdecl block_stmt;
    def visitConstrucdecl(self,ctx:CSlangParser.ConstrucdeclContext):
        return MethodDecl(Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.paramdecl()), VoidType(), self.visit(ctx.block_stmt()))
    # attributedecl: var_attr | const_attr;
    def visitAttributedecl(self,ctx:CSlangParser.AttributedeclContext):
        if ctx.VAR():
            return AttributeDecl(self.visit(ctx.attr_frag()))
        else:
            return AttributeDecl(self.visit(ctx.attr_frag()))
    
    # var_attr: VAR attr_frag;
    # const_attr: CONST attr_frag;

    # attr_frag: (no_initlist | initlist) SM;
    # no_initlist: attributelist COLON mctype;
    # initlist: membername CM initlist CM expression 
    #     | membername COLON mctype EQ expression;
    #attributelist: membername (CM membername)*;
    def visitVar_attr(self,ctx:CSlangParser.Var_attrContext):
        attr_list = self.visit(ctx.attr_frag())
        return [(VarDecl(x[0],x[1]) if x[2] == None else VarDecl(x[0],x[1],x[2])) for x in attr_list]

    def visitConst_attr(self,ctx:CSlangParser.Const_attrContext):
        attr_list = self.visit(ctx.attr_frag())
        return [ConstDecl(x[0],x[1],x[2]) for x in attr_list]
    
    def visitAttr_frag(self,ctx:CSlangParser.Attr_fragContext):
        if ctx.no_initlist():
            att_list = self.visit(ctx.no_initlist())
            return [(item[0],item[1],None) for item in att_list]
        else:
            return self.visit(ctx.initlist())
    def visitNo_initlist(self,ctx:CSlangParser.No_initlistContext):
        memberList = self.visit(ctx.attributelist())
        mctype = self.visit(ctx.mctype())
        return [(x,mctype) for x in memberList]
    def visitInitlist(self,ctx:CSlangParser.InitlistContext):
        pass
    def visitAttributelist(self,ctx:CSlangParser.AttributelistContext):
        return [Id(x.getText()) for x in ctx.membername()]
        # if ctx.getChildCount()==1: return [Id(ctx.ID().getText())]
        # return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
    # membername: STATIC | ID;
    def visitMembername(self,ctx:CSlangParser.MembernameContext):
        if ctx.STATIC():
            return Id(ctx.STATIC().getText())
        else:
            return Id(ctx.ID().getText())