# SemanticVisitor.py

from saida.LinguagemXListener import LinguagemXListener
from saida.LinguagemXParser import LinguagemXParser

class SemanticVisitor(LinguagemXListener):
    
    def __init__(self):
        self.tabela_simbolos = {}
        self.erros_semanticos = []
        
    # 1. Checagem e Registro da Declaração
    def enterDeclaracao(self, ctx: LinguagemXParser.DeclaracaoContext):
        # Obtém o tipo do primeiro filho (TIPO_INT, TIPO_REAL, etc.)
        tipo_ctx = ctx.getChild(0)
        tipo_var = tipo_ctx.getText() 
        # Obtém o nome da variável
        nome_var = ctx.ID().getText() 
        
        if nome_var in self.tabela_simbolos:
            erro = f"ERRO SEMÂNTICO na linha {ctx.start.line}: Variável '{nome_var}' já foi declarada."
            self.erros_semanticos.append(erro)
        else:
            self.tabela_simbolos[nome_var] = tipo_var
            
    # 2. Checagem de Uso de Variável na Atribuição (Verifica se a variável de destino existe)
    def exitAtribuicao(self, ctx: LinguagemXParser.AtribuicaoContext):
        nome_var = ctx.ID().getText()
        
        if nome_var not in self.tabela_simbolos:
            erro = f"ERRO SEMÂNTICO na linha {ctx.start.line}: Variável '{nome_var}' utilizada sem ser declarada."
            self.erros_semanticos.append(erro)
            
        # Lógica para checar compatibilidade de tipos viria aqui.
        pass