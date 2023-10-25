from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
from AST import *

class ASTGeneration(CSlangVisitor):

    # comment is ANTLR code which need to generate AST
    # program: classdecl+ EOF;
    def visitProgram(self,ctx:CSlangParser.ProgramContext):
        return Program([self.visit(x) for x in ctx.classdecl()])
    
    
    # classdecl: CLASS ID (EXTENDS ID)? LB classmember? RB;
    def visitClassdecl(self,ctx:CSlangParser.ClassdeclContext):
        if ctx.EXTENDS():
            if ctx.classmember():
                memlist = self.visit(ctx.classmember())
            else:
                memlist = []
            return ClassDecl(Id(ctx.ID(1).getText()), memlist, Id(ctx.ID(0).getText()))
        else:
            if ctx.classmember():
                memlist = self.visit(ctx.classmember())
            else:
                memlist = []
            return ClassDecl(Id(ctx.ID(0).getText()), memlist)
    
    
    # classmember: attributedecl 
    #     | methoddecl 
    #     | construcdecl
    #     | attributedecl classmember
    #     | methoddecl classmember
    #     | construcdecl classmember;
    def visitClassmember(self,ctx:CSlangParser.ClassmemberContext):
        if ctx.getChildCount() == 1:
            if ctx.attributedecl():
                return self.visit(ctx.attributedecl())
            elif ctx.methoddecl():
                return self.visit(ctx.methoddecl())
            elif ctx.construcdecl():
                return self.visit(ctx.construcdecl())
        else:
            return self.visit(ctx.getChild(0)) + self.visit(ctx.classmember()) 
    
    
    # construcdecl: FUNC CONSTRUCTOR paramdecl block_stmt;
    def visitConstrucdecl(self,ctx:CSlangParser.ConstrucdeclContext):
        return MethodDecl(Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.paramdecl()), VoidType(), self.visit(ctx.block_stmt()))
    
    
    # attributedecl: attributedecl: (CONST | VAR) attributelist COLON mctype (EQ initlist){len($attributelist.text.split(',')) == len($initlist.text.split(','))}? SM | (CONST | VAR) attributelist COLON mctype SM;
    def visitAttributedecl(self,ctx:CSlangParser.AttributedeclContext):
        mctype = self.visit(ctx.mctype())
        variable_list = self.visit(ctx.attributelist())
        if ctx.VAR():
            if ctx.initlist():
                init_list = self.visit(ctx.initlist())
                return [AttributeDecl(VarDecl(variable_list[i], mctype, init_list[i])) for i in range(len(variable_list))]
            else:
                return [AttributeDecl(VarDecl(variable_list[i], mctype)) for i in range(len(variable_list))]
        else:
            if ctx.initlist():
                init_list = self.visit(ctx.initlist())
                return [AttributeDecl(ConstDecl(variable_list[i], mctype, init_list[i])) for i in range(len(variable_list))]
            else:
                return [AttributeDecl(ConstDecl(variable_list[i], mctype)) for i in range(len(variable_list))]


    # methoddecl: FUNC membername paramdecl COLON mctype block_stmt;
    # paramdecl: LP paramlist? RP;
    # paramlist: param (CM param)*;
    # param: attributelist COLON mctype; 

    def visitMethoddecl(self,ctx:CSlangParser.MethoddeclContext):
        return [MethodDecl(self.visit(ctx.membername()), self.visit(ctx.paramdecl()), self.visit(ctx.mctype()), self.visit(ctx.block_stmt()))]

    def visitParamdecl(self,ctx:CSlangParser.ParamdeclContext):
        if ctx.paramlist():
            return self.visit(ctx.paramlist())
        else:
            return []
    
    # paramlist: param CM paramlist | param;
    def visitParamlist(self,ctx:CSlangParser.ParamlistContext):
        if ctx.paramlist():
            return self.visit(ctx.param()) + self.visit(ctx.paramlist()) 
        else:
            return self.visit(ctx.param())
        
    
    def visitParam(self,ctx:CSlangParser.ParamContext):
        variable_list = self.visit(ctx.attributelist())
        mctype = self.visit(ctx.mctype())
        return [VarDecl(variable_list[i], mctype) for i in range(len(variable_list))]

    # attributelist: membername (CM membername)*;
    def visitAttributelist(self, ctx:CSlangParser.AttributelistContext):
        return [self.visit(x) for x in ctx.membername()]

    # membername: STATIC | ID;
    def visitMembername(self,ctx:CSlangParser.MembernameContext):
        if ctx.STATIC():
            return Id(ctx.STATIC().getText())
        else:
            return Id(ctx.ID().getText())
        
    #initlist: expression (CM expression)*;
    def visitInitlist(self,ctx:CSlangParser.InitlistContext):
        return [self.visit(x) for x in ctx.expression()]
    
    # mctype: INT | FLOAT | BOOL | STRING | VOID  | classtype | array_type;
    def visitMctype(self,ctx:CSlangParser.MctypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.BOOL():
            return BoolType()
        elif ctx.STRING():
            return StringType()
        elif ctx.VOID():
            return VoidType()
        elif ctx.classtype():
            return self.visit(ctx.classtype())
        else:
            return self.visit(ctx.array_type())
        
    # classtype: NEW ID LP RP;
    def visitClasstype(self,ctx:CSlangParser.ClasstypeContext):
        return ClassType(Id(ctx.ID().getText()))
    
    # array_type: OB INTLIT CB (INT | FLOAT | BOOL | STRING | ID);
    def visitArray_type(self,ctx:CSlangParser.Array_typeContext):
        if ctx.INT():
            type = IntType()
        elif ctx.FLOAT():
            type = FloatType()
        elif ctx.BOOL():
            type = BoolType()
        elif ctx.STRING():
            type = StringType()
        # elif ctx.ID():
        #     type = ClassType(Id(ctx.ID().getText()))
        return ArrayType(int(ctx.INTLIT().getText()), type)
    
    # expression: expression1 CONCATENATION expression1 | expression1;
    # expression1: expression2 (EQUAL | NOTEQUAL | LESS | GREATER | LESSEQUAL | GREATEREQUAL) expression2 | expression2;
    # expression2: expression2 (AND | OR) expression3 | expression3;
    # expression3: expression3 ( ADD | SUB) expression4 | expression4;
    # expression4: expression4 (MUL | DIV | MOD | BS) expression5 | expression5;
    # expression5: NOT expression5 | expression6;
    # expression6: SUB expression6 | expression7;
    # expression7: expression7 OB expression CB | expression8;
    # expression8: expression8 DOT ID (LP list_of_expression? RP)?| expression9;
    # expression9: expression9 DOT ID
        # | ID DOT STATIC
        # | STATIC
        # | expression9 DOT ID LP list_of_expression RP
        # | ID DOT STATIC LP list_of_expression RP
        # | STATIC LP list_of_expression RP
        # | expression10;
    # expression10: NEW ID LP (list_of_expression)? RP expression10? | operands;

    def visitExpression(self,ctx:CSlangParser.ExpressionContext):
        if ctx.CONCATENATION():
            return BinaryOp(ctx.CONCATENATION().getText(), self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)))
        else:
            return self.visit(ctx.expression1(0))
        
    def visitExpression1(self,ctx:CSlangParser.Expression1Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
        else:
            return self.visit(ctx.expression2(0))
        
    def visitExpression2(self,ctx:CSlangParser.Expression2Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        else:
            return self.visit(ctx.expression3())
        
    def visitExpression3(self,ctx:CSlangParser.Expression3Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        else:
            return self.visit(ctx.expression4())
    
    def visitExpression4(self,ctx:CSlangParser.Expression4Context):
        if ctx.getChildCount() == 3:
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
        else:
            return self.visit(ctx.expression5())
        
    def visitExpression5(self,ctx:CSlangParser.Expression5Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression5()))
        else:
            return self.visit(ctx.expression6())
    
    def visitExpression6(self,ctx:CSlangParser.Expression6Context):
        if ctx.getChildCount() == 2:
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expression6()))
        else:
            return self.visit(ctx.expression7())
        
    def visitExpression7(self,ctx:CSlangParser.Expression7Context):
        if ctx.getChildCount() == 4:
            return ArrayCell(self.visit(ctx.expression7()), self.visit(ctx.expression()))
        else:
            return self.visit(ctx.expression8())
    
    # expression8: expression8 DOT ID (LP list_of_expression? RP)?| expression9;
    def visitExpression8(self,ctx:CSlangParser.Expression8Context):
        if ctx.getChildCount() > 1:
            if ctx.list_of_expression():
                return CallExpr(self.visit(ctx.expression8()), Id(ctx.ID().getText()), self.visit(ctx.list_of_expression()))
            else:
                return CallExpr(self.visit(ctx.expression8()), Id(ctx.ID().getText()), [])
        else:
            return self.visit(ctx.expression9())
        
#    `expression9: expression9 DOT ID  	3 children 
# 			| ID DOT STATIC             3 children
# 			| STATIC                    1 children
# 			| expression9 DOT ID LP list_of_expression RP 6 children
# 			| ID DOT STATIC LP list_of_expression RP 6 children
# 			| STATIC LP list_of_expression RP 4 children
# 			| expression9 DOT ID LP RP 5 children
# 			| ID DOT STATIC LP RP 5 children
# 			| STATIC LP RP 3 children
# 			| expression10;`
    def visitExpression9(self,ctx:CSlangParser.Expression9Context):
        if ctx.getChildCount() == 1:
            # 1 children group:
            # STATIC
            # expression10
            if ctx.STATIC():
                return FieldAccess(None, Id(ctx.STATIC().getText()))
            return self.visit(ctx.expression10())
        elif ctx.getChildCount() == 3:
            # 3 children group:
            # expression9 DOT ID #FieldAccess
            # ID DOT STATIC #FieldAccess
            # STATIC LP RP #CallExp
            if ctx.ID():
                if ctx.STATIC():
                    return FieldAccess(Id(ctx.ID().getText()), Id(ctx.STATIC().getText()))
                else:
                    return FieldAccess(self.visit(ctx.expression9()), Id(ctx.ID().getText()))
            else:
                return CallExpr(None, Id(ctx.STATIC().getText()), [])
        elif ctx.getChildCount() == 4:
            # 4 children group:
            # STATIC LP list_of_expression RP #CallExp
            return CallExpr(None, Id(ctx.STATIC().getText()), self.visit(ctx.list_of_expression()))
        elif ctx.getChildCount() == 5:
            # 5 children group:
            # expression9 DOT ID LP RP #CallExpr
            # ID DOT STATIC LP RP #CallExpr
            if ctx.expression9():
                return CallExpr(self.visit(ctx.expression9()), Id(ctx.ID().getText()), [])
            return CallExpr(Id(ctx.ID().getText()), Id(ctx.STATIC().getText()), [])
        else:
            # 6 children group:
            # expression9 DOT ID LP list_of_expression RP #CallExpr
            # ID DOT STATIC LP list_of_expression RP #CallExpr
            if ctx.expression9():
                return CallExpr(self.visit(ctx.expression9()), Id(ctx.ID().getText()), self.visit(ctx.list_of_expression()))
            return CallExpr(Id(ctx.ID().getText()), Id(ctx.STATIC().getText()), self.visit(ctx.list_of_expression()))
        
    
    # expression10: NEW ID LP (list_of_expression)? RP expression10? | operands;
    def visitExpression10(self,ctx:CSlangParser.Expression10Context):
        if ctx.NEW():
            if ctx.list_of_expression():
                return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.list_of_expression()))
            else:
                return NewExpr(Id(ctx.ID().getText()), [])
        else:
            return self.visit(ctx.operands())
        
        
    # operands: LP expression RP | ID | literal | SELF DOT ID | NULL ;
    def visitOperands(self,ctx:CSlangParser.OperandsContext):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.SELF():
            return SelfLiteral()
        else:
            return NullLiteral()
        
    # list_of_expression: expression (CM expression)*;
    def visitList_of_expression(self,ctx:CSlangParser.List_of_expressionContext):
        return [self.visit(x) for x in ctx.expression()]
    
    # statement: 
    #     attributedecl
    #     | assign_stmt SM
    #     | if_stmt
    #     | for_stmt
    #     | break_stmt
    #     | continue_stmt
    #     | return_stmt
    #     | method_stm
    #     | block_stmt;

    def visitStatement(self,ctx:CSlangParser.StatementContext):
        return self.visit(ctx.getChild(0))
    
    # block_stmt: LB member_block RB;
    def visitBlock_stmt(self,ctx:CSlangParser.Block_stmtContext):
        return Block(self.visit(ctx.member_block()))
    
    # member_block: statement*;
    def visitMember_block(self,ctx:CSlangParser.Member_blockContext):
        return [self.visit(x) for x in ctx.statement()]
    
    # assign_stmt: (ID | expression7) ASSIGN expression;
    def visitAssign_stmt(self,ctx:CSlangParser.Assign_stmtContext):
        if ctx.ID():
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.expression()))
        else:
            return Assign(self.visit(ctx.expression7()), self.visit(ctx.expression()))
        
    # if_stmt: IF block_stmt expression block_stmt ELSE block_stmt
	# | IF block_stmt expression block_stmt
	# | IF expression block_stmt ELSE block_stmt
	# | IF expression block_stmt;
    #if [<pre-statement>]? <expression> <block statement> [else <block statement>]?

    def visitIf_stmt(self,ctx:CSlangParser.If_stmtContext):
        if ctx.getChildCount() == 6:
            # IF block_stmt expression block_stmt ELSE block_stmt
            return If(self.visit(ctx.expression()), self.visit(ctx.block_stmt(1)), self.visit(ctx.block_stmt(0)), self.visit(ctx.block_stmt(2)))
        elif ctx.getChildCount() == 5:
            # | IF expression block_stmt ELSE block_stmt
            return If(self.visit(ctx.expression()), self.visit(ctx.block_stmt(0)),None,self.visit(ctx.block_stmt(1)))
        elif ctx.getChildCount() == 4:
            # | IF block_stmt expression block_stmt
            return If(self.visit(ctx.expression()), self.visit(ctx.block_stmt(1)), self.visit(ctx.block_stmt(0)))
        else:
            # | IF expression block_stmt
            return If(self.visit(ctx.expression()), self.visit(ctx.block_stmt(0)))
        
    # for_stmt: FOR assign_stmt SM expression SM assign_stmt block_stmt;
    #for <init statement> ; <condition expression> ; <post statement> <block statement>
    def visitFor_stmt(self,ctx:CSlangParser.For_stmtContext):
        return For(self.visit(ctx.assign_stmt(0)), self.visit(ctx.expression()), self.visit(ctx.assign_stmt(1)), self.visit(ctx.block_stmt()))
    
    # break_stmt: BREAK SM;
    def visitBreak_stmt(self,ctx:CSlangParser.Break_stmtContext):
        return Break()
    
    # continue_stmt: CONTINUE SM;
    def visitContinue_stmt(self,ctx:CSlangParser.Continue_stmtContext):
        return Continue()
    
    # return_stmt: RETURN expression? SM;
    def visitReturn_stmt(self,ctx:CSlangParser.Return_stmtContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        else:
            return Return(None)
        
    # method_stm: | expression DOT ID LP list_of_expression RP
	# 		| ID DOT STATIC LP list_of_expression RP
	# 		| STATIC LP list_of_expression RP
	# 		| expression DOT ID LP RP
	# 		| ID DOT STATIC LP RP
	# 		| STATIC LP RP;
    def visitMethod_stm(self,ctx:CSlangParser.Method_stmContext):
        if ctx.getChildCount() == 3:
            # STATIC LP RP
            return CallStmt(None, Id(ctx.STATIC().getText()), [])
        elif ctx.getChildCount() == 4:
            # | STATIC LP list_of_expression RP
            return CallStmt(None, Id(ctx.STATIC().getText()), self.visit(ctx.list_of_expression()))
        elif ctx.getChildCount() == 5:
            # | expression DOT ID LP RP
            # | ID DOT STATIC LP RP
            if ctx.expression():
                return CallStmt(self.visit(ctx.expression()), Id(ctx.ID().getText()), [])
            return CallStmt(Id(ctx.ID().getText()), Id(ctx.STATIC().getText()), [])
        elif ctx.getChildCount() == 6:
            # | expression DOT ID LP list_of_expression RP
            # | ID DOT STATIC LP list_of_expression RP
            if ctx.expression():    
                return CallStmt(self.visit(ctx.expression()), Id(ctx.ID().getText()), self.visit(ctx.list_of_expression()))
            return CallStmt(Id(ctx.ID().getText()), Id(ctx.STATIC().getText()), self.visit(ctx.list_of_expression()))
        

    # literal:  INTLIT | FLOATLIT | STRING_LITERAL | BOOLLIT | array_literal;
    def visitLiteral(self,ctx:CSlangParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText())
        else:
            return self.visit(ctx.array_literal())
    
    # array_literal: OB (elem (CM elem)*)? CB;
    def visitArray_literal(self,ctx:CSlangParser.Array_literalContext):
        if ctx.elem():
            return ArrayLiteral([self.visit(x) for x in ctx.elem()])
        else:
            return ArrayLiteral([])
        
    # elem: INTLIT | FLOATLIT | STRING_LITERAL | BOOLLIT;
    def visitElem(self,ctx:CSlangParser.ElemContext):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRING_LITERAL():
            return StringLiteral(ctx.STRING_LITERAL().getText())
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText())
            



                
            
        
    

        

    
