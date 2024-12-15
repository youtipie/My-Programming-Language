# Generated from Quill.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .QuillParser import QuillParser
else:
    from QuillParser import QuillParser

# This class defines a complete listener for a parse tree produced by QuillParser.
class QuillListener(ParseTreeListener):

    # Enter a parse tree produced by QuillParser#program.
    def enterProgram(self, ctx:QuillParser.ProgramContext):
        pass

    # Exit a parse tree produced by QuillParser#program.
    def exitProgram(self, ctx:QuillParser.ProgramContext):
        pass


    # Enter a parse tree produced by QuillParser#statementList.
    def enterStatementList(self, ctx:QuillParser.StatementListContext):
        pass

    # Exit a parse tree produced by QuillParser#statementList.
    def exitStatementList(self, ctx:QuillParser.StatementListContext):
        pass


    # Enter a parse tree produced by QuillParser#statement.
    def enterStatement(self, ctx:QuillParser.StatementContext):
        pass

    # Exit a parse tree produced by QuillParser#statement.
    def exitStatement(self, ctx:QuillParser.StatementContext):
        pass


    # Enter a parse tree produced by QuillParser#declaration.
    def enterDeclaration(self, ctx:QuillParser.DeclarationContext):
        pass

    # Exit a parse tree produced by QuillParser#declaration.
    def exitDeclaration(self, ctx:QuillParser.DeclarationContext):
        pass


    # Enter a parse tree produced by QuillParser#ident.
    def enterIdent(self, ctx:QuillParser.IdentContext):
        pass

    # Exit a parse tree produced by QuillParser#ident.
    def exitIdent(self, ctx:QuillParser.IdentContext):
        pass


    # Enter a parse tree produced by QuillParser#declarationExpression.
    def enterDeclarationExpression(self, ctx:QuillParser.DeclarationExpressionContext):
        pass

    # Exit a parse tree produced by QuillParser#declarationExpression.
    def exitDeclarationExpression(self, ctx:QuillParser.DeclarationExpressionContext):
        pass


    # Enter a parse tree produced by QuillParser#assign.
    def enterAssign(self, ctx:QuillParser.AssignContext):
        pass

    # Exit a parse tree produced by QuillParser#assign.
    def exitAssign(self, ctx:QuillParser.AssignContext):
        pass


    # Enter a parse tree produced by QuillParser#ifStatement.
    def enterIfStatement(self, ctx:QuillParser.IfStatementContext):
        pass

    # Exit a parse tree produced by QuillParser#ifStatement.
    def exitIfStatement(self, ctx:QuillParser.IfStatementContext):
        pass


    # Enter a parse tree produced by QuillParser#ifTail.
    def enterIfTail(self, ctx:QuillParser.IfTailContext):
        pass

    # Exit a parse tree produced by QuillParser#ifTail.
    def exitIfTail(self, ctx:QuillParser.IfTailContext):
        pass


    # Enter a parse tree produced by QuillParser#forStatement.
    def enterForStatement(self, ctx:QuillParser.ForStatementContext):
        pass

    # Exit a parse tree produced by QuillParser#forStatement.
    def exitForStatement(self, ctx:QuillParser.ForStatementContext):
        pass


    # Enter a parse tree produced by QuillParser#rangeExpr.
    def enterRangeExpr(self, ctx:QuillParser.RangeExprContext):
        pass

    # Exit a parse tree produced by QuillParser#rangeExpr.
    def exitRangeExpr(self, ctx:QuillParser.RangeExprContext):
        pass


    # Enter a parse tree produced by QuillParser#whileStatement.
    def enterWhileStatement(self, ctx:QuillParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by QuillParser#whileStatement.
    def exitWhileStatement(self, ctx:QuillParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by QuillParser#inp.
    def enterInp(self, ctx:QuillParser.InpContext):
        pass

    # Exit a parse tree produced by QuillParser#inp.
    def exitInp(self, ctx:QuillParser.InpContext):
        pass


    # Enter a parse tree produced by QuillParser#out.
    def enterOut(self, ctx:QuillParser.OutContext):
        pass

    # Exit a parse tree produced by QuillParser#out.
    def exitOut(self, ctx:QuillParser.OutContext):
        pass


    # Enter a parse tree produced by QuillParser#expression.
    def enterExpression(self, ctx:QuillParser.ExpressionContext):
        pass

    # Exit a parse tree produced by QuillParser#expression.
    def exitExpression(self, ctx:QuillParser.ExpressionContext):
        pass


    # Enter a parse tree produced by QuillParser#relOp.
    def enterRelOp(self, ctx:QuillParser.RelOpContext):
        pass

    # Exit a parse tree produced by QuillParser#relOp.
    def exitRelOp(self, ctx:QuillParser.RelOpContext):
        pass


    # Enter a parse tree produced by QuillParser#arithmExpression.
    def enterArithmExpression(self, ctx:QuillParser.ArithmExpressionContext):
        pass

    # Exit a parse tree produced by QuillParser#arithmExpression.
    def exitArithmExpression(self, ctx:QuillParser.ArithmExpressionContext):
        pass


    # Enter a parse tree produced by QuillParser#term.
    def enterTerm(self, ctx:QuillParser.TermContext):
        pass

    # Exit a parse tree produced by QuillParser#term.
    def exitTerm(self, ctx:QuillParser.TermContext):
        pass


    # Enter a parse tree produced by QuillParser#exponent.
    def enterExponent(self, ctx:QuillParser.ExponentContext):
        pass

    # Exit a parse tree produced by QuillParser#exponent.
    def exitExponent(self, ctx:QuillParser.ExponentContext):
        pass


    # Enter a parse tree produced by QuillParser#factor.
    def enterFactor(self, ctx:QuillParser.FactorContext):
        pass

    # Exit a parse tree produced by QuillParser#factor.
    def exitFactor(self, ctx:QuillParser.FactorContext):
        pass


    # Enter a parse tree produced by QuillParser#constant.
    def enterConstant(self, ctx:QuillParser.ConstantContext):
        pass

    # Exit a parse tree produced by QuillParser#constant.
    def exitConstant(self, ctx:QuillParser.ConstantContext):
        pass


    # Enter a parse tree produced by QuillParser#declarationKeyword.
    def enterDeclarationKeyword(self, ctx:QuillParser.DeclarationKeywordContext):
        pass

    # Exit a parse tree produced by QuillParser#declarationKeyword.
    def exitDeclarationKeyword(self, ctx:QuillParser.DeclarationKeywordContext):
        pass


    # Enter a parse tree produced by QuillParser#sign.
    def enterSign(self, ctx:QuillParser.SignContext):
        pass

    # Exit a parse tree produced by QuillParser#sign.
    def exitSign(self, ctx:QuillParser.SignContext):
        pass


    # Enter a parse tree produced by QuillParser#type.
    def enterType(self, ctx:QuillParser.TypeContext):
        pass

    # Exit a parse tree produced by QuillParser#type.
    def exitType(self, ctx:QuillParser.TypeContext):
        pass


    # Enter a parse tree produced by QuillParser#rangeOp.
    def enterRangeOp(self, ctx:QuillParser.RangeOpContext):
        pass

    # Exit a parse tree produced by QuillParser#rangeOp.
    def exitRangeOp(self, ctx:QuillParser.RangeOpContext):
        pass


    # Enter a parse tree produced by QuillParser#intNumb.
    def enterIntNumb(self, ctx:QuillParser.IntNumbContext):
        pass

    # Exit a parse tree produced by QuillParser#intNumb.
    def exitIntNumb(self, ctx:QuillParser.IntNumbContext):
        pass


    # Enter a parse tree produced by QuillParser#floatNumb.
    def enterFloatNumb(self, ctx:QuillParser.FloatNumbContext):
        pass

    # Exit a parse tree produced by QuillParser#floatNumb.
    def exitFloatNumb(self, ctx:QuillParser.FloatNumbContext):
        pass


    # Enter a parse tree produced by QuillParser#unsignedInt.
    def enterUnsignedInt(self, ctx:QuillParser.UnsignedIntContext):
        pass

    # Exit a parse tree produced by QuillParser#unsignedInt.
    def exitUnsignedInt(self, ctx:QuillParser.UnsignedIntContext):
        pass


    # Enter a parse tree produced by QuillParser#unsignedFloat.
    def enterUnsignedFloat(self, ctx:QuillParser.UnsignedFloatContext):
        pass

    # Exit a parse tree produced by QuillParser#unsignedFloat.
    def exitUnsignedFloat(self, ctx:QuillParser.UnsignedFloatContext):
        pass


    # Enter a parse tree produced by QuillParser#boolConst.
    def enterBoolConst(self, ctx:QuillParser.BoolConstContext):
        pass

    # Exit a parse tree produced by QuillParser#boolConst.
    def exitBoolConst(self, ctx:QuillParser.BoolConstContext):
        pass



del QuillParser