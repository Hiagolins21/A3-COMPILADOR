# Generated from LinguagemX.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,25,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,39,8,0,10,0,12,0,42,9,0,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,5,2,56,8,2,10,2,
        12,2,59,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,76,8,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,91,8,6,1,7,1,7,1,7,1,7,1,7,1,7,5,7,99,8,7,10,7,12,7,102,
        9,7,1,7,1,7,1,7,1,7,5,7,108,8,7,10,7,12,7,111,9,7,1,7,3,7,114,8,
        7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,122,8,8,10,8,12,8,125,9,8,1,8,1,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,139,8,9,10,9,12,9,142,
        9,9,1,9,1,9,1,9,0,1,0,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,1,3,156,
        0,20,1,0,0,0,2,51,1,0,0,0,4,57,1,0,0,0,6,62,1,0,0,0,8,75,1,0,0,0,
        10,77,1,0,0,0,12,90,1,0,0,0,14,92,1,0,0,0,16,115,1,0,0,0,18,128,
        1,0,0,0,20,21,6,0,-1,0,21,22,3,2,1,0,22,40,1,0,0,0,23,24,10,6,0,
        0,24,25,5,13,0,0,25,39,3,0,0,7,26,27,10,5,0,0,27,28,5,14,0,0,28,
        39,3,0,0,6,29,30,10,4,0,0,30,31,5,11,0,0,31,39,3,0,0,5,32,33,10,
        3,0,0,33,34,5,12,0,0,34,39,3,0,0,4,35,36,10,2,0,0,36,37,5,15,0,0,
        37,39,3,0,0,3,38,23,1,0,0,0,38,26,1,0,0,0,38,29,1,0,0,0,38,32,1,
        0,0,0,38,35,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,
        1,1,0,0,0,42,40,1,0,0,0,43,52,5,21,0,0,44,52,5,23,0,0,45,52,5,22,
        0,0,46,52,5,24,0,0,47,48,5,17,0,0,48,49,3,0,0,0,49,50,5,18,0,0,50,
        52,1,0,0,0,51,43,1,0,0,0,51,44,1,0,0,0,51,45,1,0,0,0,51,46,1,0,0,
        0,51,47,1,0,0,0,52,3,1,0,0,0,53,56,3,6,3,0,54,56,3,8,4,0,55,53,1,
        0,0,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,
        60,1,0,0,0,59,57,1,0,0,0,60,61,5,0,0,1,61,5,1,0,0,0,62,63,7,0,0,
        0,63,64,5,21,0,0,64,65,5,16,0,0,65,7,1,0,0,0,66,67,3,10,5,0,67,68,
        5,16,0,0,68,76,1,0,0,0,69,70,3,12,6,0,70,71,5,16,0,0,71,76,1,0,0,
        0,72,76,3,14,7,0,73,76,3,16,8,0,74,76,3,18,9,0,75,66,1,0,0,0,75,
        69,1,0,0,0,75,72,1,0,0,0,75,73,1,0,0,0,75,74,1,0,0,0,76,9,1,0,0,
        0,77,78,5,21,0,0,78,79,5,10,0,0,79,80,3,0,0,0,80,11,1,0,0,0,81,82,
        5,8,0,0,82,83,5,17,0,0,83,84,5,21,0,0,84,91,5,18,0,0,85,86,5,9,0,
        0,86,87,5,17,0,0,87,88,3,0,0,0,88,89,5,18,0,0,89,91,1,0,0,0,90,81,
        1,0,0,0,90,85,1,0,0,0,91,13,1,0,0,0,92,93,5,4,0,0,93,94,5,17,0,0,
        94,95,3,0,0,0,95,96,5,18,0,0,96,100,5,19,0,0,97,99,3,8,4,0,98,97,
        1,0,0,0,99,102,1,0,0,0,100,98,1,0,0,0,100,101,1,0,0,0,101,103,1,
        0,0,0,102,100,1,0,0,0,103,113,5,20,0,0,104,105,5,5,0,0,105,109,5,
        19,0,0,106,108,3,8,4,0,107,106,1,0,0,0,108,111,1,0,0,0,109,107,1,
        0,0,0,109,110,1,0,0,0,110,112,1,0,0,0,111,109,1,0,0,0,112,114,5,
        20,0,0,113,104,1,0,0,0,113,114,1,0,0,0,114,15,1,0,0,0,115,116,5,
        6,0,0,116,117,5,17,0,0,117,118,3,0,0,0,118,119,5,18,0,0,119,123,
        5,19,0,0,120,122,3,8,4,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,
        1,0,0,0,123,124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,
        5,20,0,0,127,17,1,0,0,0,128,129,5,7,0,0,129,130,5,17,0,0,130,131,
        3,10,5,0,131,132,5,16,0,0,132,133,3,0,0,0,133,134,5,16,0,0,134,135,
        3,10,5,0,135,136,5,16,0,0,136,140,5,19,0,0,137,139,3,8,4,0,138,137,
        1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,143,
        1,0,0,0,142,140,1,0,0,0,143,144,5,20,0,0,144,19,1,0,0,0,12,38,40,
        51,55,57,75,90,100,109,113,123,140
    ]

class LinguagemXParser ( Parser ):

    grammarFileName = "LinguagemX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'inteiro'", "'real'", "'texto'", "'se'", 
                     "'senao'", "'enquanto'", "'para'", "'leia'", "'escreva'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "<INVALID>", "';'", 
                     "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "TIPO_INT", "TIPO_REAL", "TIPO_TEXTO", 
                      "IF", "ELSE", "WHILE", "FOR", "LEIA", "ESCREVA", "ATRIB", 
                      "SOMA", "SUB", "MULT", "DIV", "OP_REL", "PONTO_VIRGULA", 
                      "ABRE_PARENTESES", "FECHA_PARENTESES", "ABRE_CHAVE", 
                      "FECHA_CHAVE", "ID", "NUM_DEC", "NUM_INT", "TEXTO_LITERAL", 
                      "WS" ]

    RULE_expressao = 0
    RULE_termo = 1
    RULE_programa = 2
    RULE_declaracao = 3
    RULE_comando = 4
    RULE_atribuicao = 5
    RULE_io = 6
    RULE_se_senao = 7
    RULE_loop_while = 8
    RULE_loop_for = 9

    ruleNames =  [ "expressao", "termo", "programa", "declaracao", "comando", 
                   "atribuicao", "io", "se_senao", "loop_while", "loop_for" ]

    EOF = Token.EOF
    TIPO_INT=1
    TIPO_REAL=2
    TIPO_TEXTO=3
    IF=4
    ELSE=5
    WHILE=6
    FOR=7
    LEIA=8
    ESCREVA=9
    ATRIB=10
    SOMA=11
    SUB=12
    MULT=13
    DIV=14
    OP_REL=15
    PONTO_VIRGULA=16
    ABRE_PARENTESES=17
    FECHA_PARENTESES=18
    ABRE_CHAVE=19
    FECHA_CHAVE=20
    ID=21
    NUM_DEC=22
    NUM_INT=23
    TEXTO_LITERAL=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LinguagemXParser.RULE_expressao

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OpMultDivContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,i)

        def MULT(self):
            return self.getToken(LinguagemXParser.MULT, 0)
        def DIV(self):
            return self.getToken(LinguagemXParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpMultDiv" ):
                listener.enterOpMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpMultDiv" ):
                listener.exitOpMultDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpMultDiv" ):
                return visitor.visitOpMultDiv(self)
            else:
                return visitor.visitChildren(self)


    class OpSomaSubContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,i)

        def SOMA(self):
            return self.getToken(LinguagemXParser.SOMA, 0)
        def SUB(self):
            return self.getToken(LinguagemXParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpSomaSub" ):
                listener.enterOpSomaSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpSomaSub" ):
                listener.exitOpSomaSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpSomaSub" ):
                return visitor.visitOpSomaSub(self)
            else:
                return visitor.visitChildren(self)


    class ExpressaoTermoContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termo(self):
            return self.getTypedRuleContext(LinguagemXParser.TermoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressaoTermo" ):
                listener.enterExpressaoTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressaoTermo" ):
                listener.exitExpressaoTermo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressaoTermo" ):
                return visitor.visitExpressaoTermo(self)
            else:
                return visitor.visitChildren(self)


    class OpRelacionalContext(ExpressaoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.ExpressaoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,i)

        def OP_REL(self):
            return self.getToken(LinguagemXParser.OP_REL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpRelacional" ):
                listener.enterOpRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpRelacional" ):
                listener.exitOpRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpRelacional" ):
                return visitor.visitOpRelacional(self)
            else:
                return visitor.visitChildren(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LinguagemXParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expressao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = LinguagemXParser.ExpressaoTermoContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 21
            self.termo()
            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = LinguagemXParser.OpMultDivContext(self, LinguagemXParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 23
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 24
                        self.match(LinguagemXParser.MULT)
                        self.state = 25
                        self.expressao(7)
                        pass

                    elif la_ == 2:
                        localctx = LinguagemXParser.OpMultDivContext(self, LinguagemXParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 26
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 27
                        self.match(LinguagemXParser.DIV)
                        self.state = 28
                        self.expressao(6)
                        pass

                    elif la_ == 3:
                        localctx = LinguagemXParser.OpSomaSubContext(self, LinguagemXParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        self.match(LinguagemXParser.SOMA)
                        self.state = 31
                        self.expressao(5)
                        pass

                    elif la_ == 4:
                        localctx = LinguagemXParser.OpSomaSubContext(self, LinguagemXParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        self.match(LinguagemXParser.SUB)
                        self.state = 34
                        self.expressao(4)
                        pass

                    elif la_ == 5:
                        localctx = LinguagemXParser.OpRelacionalContext(self, LinguagemXParser.ExpressaoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                        self.state = 35
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 36
                        self.match(LinguagemXParser.OP_REL)
                        self.state = 37
                        self.expressao(3)
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LinguagemXParser.RULE_termo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TermoIDContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LinguagemXParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoID" ):
                listener.enterTermoID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoID" ):
                listener.exitTermoID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoID" ):
                return visitor.visitTermoID(self)
            else:
                return visitor.visitChildren(self)


    class TermoTextoContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TEXTO_LITERAL(self):
            return self.getToken(LinguagemXParser.TEXTO_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoTexto" ):
                listener.enterTermoTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoTexto" ):
                listener.exitTermoTexto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoTexto" ):
                return visitor.visitTermoTexto(self)
            else:
                return visitor.visitChildren(self)


    class TermoParentesesContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ABRE_PARENTESES(self):
            return self.getToken(LinguagemXParser.ABRE_PARENTESES, 0)
        def expressao(self):
            return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,0)

        def FECHA_PARENTESES(self):
            return self.getToken(LinguagemXParser.FECHA_PARENTESES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoParenteses" ):
                listener.enterTermoParenteses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoParenteses" ):
                listener.exitTermoParenteses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoParenteses" ):
                return visitor.visitTermoParenteses(self)
            else:
                return visitor.visitChildren(self)


    class TermoNumDecContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM_DEC(self):
            return self.getToken(LinguagemXParser.NUM_DEC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoNumDec" ):
                listener.enterTermoNumDec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoNumDec" ):
                listener.exitTermoNumDec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoNumDec" ):
                return visitor.visitTermoNumDec(self)
            else:
                return visitor.visitChildren(self)


    class TermoNumIntContext(TermoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LinguagemXParser.TermoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM_INT(self):
            return self.getToken(LinguagemXParser.NUM_INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermoNumInt" ):
                listener.enterTermoNumInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermoNumInt" ):
                listener.exitTermoNumInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermoNumInt" ):
                return visitor.visitTermoNumInt(self)
            else:
                return visitor.visitChildren(self)



    def termo(self):

        localctx = LinguagemXParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_termo)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = LinguagemXParser.TermoIDContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(LinguagemXParser.ID)
                pass
            elif token in [23]:
                localctx = LinguagemXParser.TermoNumIntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.match(LinguagemXParser.NUM_INT)
                pass
            elif token in [22]:
                localctx = LinguagemXParser.TermoNumDecContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.match(LinguagemXParser.NUM_DEC)
                pass
            elif token in [24]:
                localctx = LinguagemXParser.TermoTextoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.match(LinguagemXParser.TEXTO_LITERAL)
                pass
            elif token in [17]:
                localctx = LinguagemXParser.TermoParentesesContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.match(LinguagemXParser.ABRE_PARENTESES)
                self.state = 48
                self.expressao(0)
                self.state = 49
                self.match(LinguagemXParser.FECHA_PARENTESES)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LinguagemXParser.EOF, 0)

        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.DeclaracaoContext,i)


        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.ComandoContext,i)


        def getRuleIndex(self):
            return LinguagemXParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LinguagemXParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2098142) != 0):
                self.state = 55
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3]:
                    self.state = 53
                    self.declaracao()
                    pass
                elif token in [4, 6, 7, 8, 9, 21]:
                    self.state = 54
                    self.comando()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(LinguagemXParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LinguagemXParser.ID, 0)

        def PONTO_VIRGULA(self):
            return self.getToken(LinguagemXParser.PONTO_VIRGULA, 0)

        def TIPO_INT(self):
            return self.getToken(LinguagemXParser.TIPO_INT, 0)

        def TIPO_REAL(self):
            return self.getToken(LinguagemXParser.TIPO_REAL, 0)

        def TIPO_TEXTO(self):
            return self.getToken(LinguagemXParser.TIPO_TEXTO, 0)

        def getRuleIndex(self):
            return LinguagemXParser.RULE_declaracao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao" ):
                return visitor.visitDeclaracao(self)
            else:
                return visitor.visitChildren(self)




    def declaracao(self):

        localctx = LinguagemXParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 63
            self.match(LinguagemXParser.ID)
            self.state = 64
            self.match(LinguagemXParser.PONTO_VIRGULA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(LinguagemXParser.AtribuicaoContext,0)


        def PONTO_VIRGULA(self):
            return self.getToken(LinguagemXParser.PONTO_VIRGULA, 0)

        def io(self):
            return self.getTypedRuleContext(LinguagemXParser.IoContext,0)


        def se_senao(self):
            return self.getTypedRuleContext(LinguagemXParser.Se_senaoContext,0)


        def loop_while(self):
            return self.getTypedRuleContext(LinguagemXParser.Loop_whileContext,0)


        def loop_for(self):
            return self.getTypedRuleContext(LinguagemXParser.Loop_forContext,0)


        def getRuleIndex(self):
            return LinguagemXParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComando" ):
                return visitor.visitComando(self)
            else:
                return visitor.visitChildren(self)




    def comando(self):

        localctx = LinguagemXParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comando)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.atribuicao()
                self.state = 67
                self.match(LinguagemXParser.PONTO_VIRGULA)
                pass
            elif token in [8, 9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.io()
                self.state = 70
                self.match(LinguagemXParser.PONTO_VIRGULA)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.se_senao()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.loop_while()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 5)
                self.state = 74
                self.loop_for()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LinguagemXParser.ID, 0)

        def ATRIB(self):
            return self.getToken(LinguagemXParser.ATRIB, 0)

        def expressao(self):
            return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LinguagemXParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = LinguagemXParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(LinguagemXParser.ID)
            self.state = 78
            self.match(LinguagemXParser.ATRIB)
            self.state = 79
            self.expressao(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEIA(self):
            return self.getToken(LinguagemXParser.LEIA, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(LinguagemXParser.ABRE_PARENTESES, 0)

        def ID(self):
            return self.getToken(LinguagemXParser.ID, 0)

        def FECHA_PARENTESES(self):
            return self.getToken(LinguagemXParser.FECHA_PARENTESES, 0)

        def ESCREVA(self):
            return self.getToken(LinguagemXParser.ESCREVA, 0)

        def expressao(self):
            return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LinguagemXParser.RULE_io

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIo" ):
                listener.enterIo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIo" ):
                listener.exitIo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo" ):
                return visitor.visitIo(self)
            else:
                return visitor.visitChildren(self)




    def io(self):

        localctx = LinguagemXParser.IoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_io)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(LinguagemXParser.LEIA)
                self.state = 82
                self.match(LinguagemXParser.ABRE_PARENTESES)
                self.state = 83
                self.match(LinguagemXParser.ID)
                self.state = 84
                self.match(LinguagemXParser.FECHA_PARENTESES)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(LinguagemXParser.ESCREVA)
                self.state = 86
                self.match(LinguagemXParser.ABRE_PARENTESES)
                self.state = 87
                self.expressao(0)
                self.state = 88
                self.match(LinguagemXParser.FECHA_PARENTESES)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Se_senaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LinguagemXParser.IF, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(LinguagemXParser.ABRE_PARENTESES, 0)

        def expressao(self):
            return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,0)


        def FECHA_PARENTESES(self):
            return self.getToken(LinguagemXParser.FECHA_PARENTESES, 0)

        def ABRE_CHAVE(self, i:int=None):
            if i is None:
                return self.getTokens(LinguagemXParser.ABRE_CHAVE)
            else:
                return self.getToken(LinguagemXParser.ABRE_CHAVE, i)

        def FECHA_CHAVE(self, i:int=None):
            if i is None:
                return self.getTokens(LinguagemXParser.FECHA_CHAVE)
            else:
                return self.getToken(LinguagemXParser.FECHA_CHAVE, i)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.ComandoContext,i)


        def ELSE(self):
            return self.getToken(LinguagemXParser.ELSE, 0)

        def getRuleIndex(self):
            return LinguagemXParser.RULE_se_senao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSe_senao" ):
                listener.enterSe_senao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSe_senao" ):
                listener.exitSe_senao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSe_senao" ):
                return visitor.visitSe_senao(self)
            else:
                return visitor.visitChildren(self)




    def se_senao(self):

        localctx = LinguagemXParser.Se_senaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_se_senao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(LinguagemXParser.IF)
            self.state = 93
            self.match(LinguagemXParser.ABRE_PARENTESES)
            self.state = 94
            self.expressao(0)
            self.state = 95
            self.match(LinguagemXParser.FECHA_PARENTESES)
            self.state = 96
            self.match(LinguagemXParser.ABRE_CHAVE)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2098128) != 0):
                self.state = 97
                self.comando()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 103
            self.match(LinguagemXParser.FECHA_CHAVE)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 104
                self.match(LinguagemXParser.ELSE)
                self.state = 105
                self.match(LinguagemXParser.ABRE_CHAVE)
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2098128) != 0):
                    self.state = 106
                    self.comando()
                    self.state = 111
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 112
                self.match(LinguagemXParser.FECHA_CHAVE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LinguagemXParser.WHILE, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(LinguagemXParser.ABRE_PARENTESES, 0)

        def expressao(self):
            return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,0)


        def FECHA_PARENTESES(self):
            return self.getToken(LinguagemXParser.FECHA_PARENTESES, 0)

        def ABRE_CHAVE(self):
            return self.getToken(LinguagemXParser.ABRE_CHAVE, 0)

        def FECHA_CHAVE(self):
            return self.getToken(LinguagemXParser.FECHA_CHAVE, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.ComandoContext,i)


        def getRuleIndex(self):
            return LinguagemXParser.RULE_loop_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_while" ):
                listener.enterLoop_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_while" ):
                listener.exitLoop_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_while" ):
                return visitor.visitLoop_while(self)
            else:
                return visitor.visitChildren(self)




    def loop_while(self):

        localctx = LinguagemXParser.Loop_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_loop_while)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(LinguagemXParser.WHILE)
            self.state = 116
            self.match(LinguagemXParser.ABRE_PARENTESES)
            self.state = 117
            self.expressao(0)
            self.state = 118
            self.match(LinguagemXParser.FECHA_PARENTESES)
            self.state = 119
            self.match(LinguagemXParser.ABRE_CHAVE)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2098128) != 0):
                self.state = 120
                self.comando()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(LinguagemXParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(LinguagemXParser.FOR, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(LinguagemXParser.ABRE_PARENTESES, 0)

        def atribuicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.AtribuicaoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.AtribuicaoContext,i)


        def PONTO_VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(LinguagemXParser.PONTO_VIRGULA)
            else:
                return self.getToken(LinguagemXParser.PONTO_VIRGULA, i)

        def expressao(self):
            return self.getTypedRuleContext(LinguagemXParser.ExpressaoContext,0)


        def ABRE_CHAVE(self):
            return self.getToken(LinguagemXParser.ABRE_CHAVE, 0)

        def FECHA_CHAVE(self):
            return self.getToken(LinguagemXParser.FECHA_CHAVE, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LinguagemXParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LinguagemXParser.ComandoContext,i)


        def getRuleIndex(self):
            return LinguagemXParser.RULE_loop_for

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_for" ):
                listener.enterLoop_for(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_for" ):
                listener.exitLoop_for(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_for" ):
                return visitor.visitLoop_for(self)
            else:
                return visitor.visitChildren(self)




    def loop_for(self):

        localctx = LinguagemXParser.Loop_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_loop_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(LinguagemXParser.FOR)
            self.state = 129
            self.match(LinguagemXParser.ABRE_PARENTESES)
            self.state = 130
            self.atribuicao()
            self.state = 131
            self.match(LinguagemXParser.PONTO_VIRGULA)
            self.state = 132
            self.expressao(0)
            self.state = 133
            self.match(LinguagemXParser.PONTO_VIRGULA)
            self.state = 134
            self.atribuicao()
            self.state = 135
            self.match(LinguagemXParser.PONTO_VIRGULA)
            self.state = 136
            self.match(LinguagemXParser.ABRE_CHAVE)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2098128) != 0):
                self.state = 137
                self.comando()
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 143
            self.match(LinguagemXParser.FECHA_CHAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




