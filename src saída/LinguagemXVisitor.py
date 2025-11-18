# Generated from LinguagemX.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LinguagemXParser import LinguagemXParser
else:
    from LinguagemXParser import LinguagemXParser

# This class defines a complete generic visitor for a parse tree produced by LinguagemXParser.

class LinguagemXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LinguagemXParser#OpMultDiv.
    def visitOpMultDiv(self, ctx:LinguagemXParser.OpMultDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#OpSomaSub.
    def visitOpSomaSub(self, ctx:LinguagemXParser.OpSomaSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#ExpressaoTermo.
    def visitExpressaoTermo(self, ctx:LinguagemXParser.ExpressaoTermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#OpRelacional.
    def visitOpRelacional(self, ctx:LinguagemXParser.OpRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#TermoID.
    def visitTermoID(self, ctx:LinguagemXParser.TermoIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#TermoNumInt.
    def visitTermoNumInt(self, ctx:LinguagemXParser.TermoNumIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#TermoNumDec.
    def visitTermoNumDec(self, ctx:LinguagemXParser.TermoNumDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#TermoTexto.
    def visitTermoTexto(self, ctx:LinguagemXParser.TermoTextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#TermoParenteses.
    def visitTermoParenteses(self, ctx:LinguagemXParser.TermoParentesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#programa.
    def visitPrograma(self, ctx:LinguagemXParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#declaracao.
    def visitDeclaracao(self, ctx:LinguagemXParser.DeclaracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#comando.
    def visitComando(self, ctx:LinguagemXParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#atribuicao.
    def visitAtribuicao(self, ctx:LinguagemXParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#io.
    def visitIo(self, ctx:LinguagemXParser.IoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#se_senao.
    def visitSe_senao(self, ctx:LinguagemXParser.Se_senaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#loop_while.
    def visitLoop_while(self, ctx:LinguagemXParser.Loop_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LinguagemXParser#loop_for.
    def visitLoop_for(self, ctx:LinguagemXParser.Loop_forContext):
        return self.visitChildren(ctx)



del LinguagemXParser