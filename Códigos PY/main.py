# main.py

import sys
from antlr4 import *
from saida.LinguagemXLexer import LinguagemXLexer
from saida.LinguagemXParser import LinguagemXParser
from SemanticVisitor import SemanticVisitor
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import ParseTreeWalker

# Classe para capturar erros sintáticos
class LexerParserErrorListener(ErrorListener):
    def __init__(self, errors):
        super(LexerParserErrorListener, self).__init__()
        self.errors = errors

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Obtém o texto do token inesperado
        token_text = offendingSymbol.text if offendingSymbol and offendingSymbol.text is not None else 'EOF'
        error_msg = f"ERRO SINTÁTICO na linha {line}, coluna {column}: Token inesperado '{token_text}'"
        self.errors.append(error_msg)

if __name__ == '__main__':
    print("--- Iniciando Compilador ---")
    
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.lx>")
        sys.exit(1)

    input_file = sys.argv[1]
    errors = []
    
    try:
        # 1. ANÁLISE LÉXICA E SINTÁTICA
        input_stream = FileStream(input_file, encoding='utf-8')
        lexer = LinguagemXLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = LinguagemXParser(stream)
        
        # Configurar o listener de erro
        parser.removeErrorListeners()
        parser.addErrorListener(LexerParserErrorListener(errors))
        
        tree = parser.programa()
        
        if errors:
            print("\n--- COMPILAÇÃO FALHOU (Erros Sintáticos) ---")
            for error in errors[:5]: 
                print(error)
            if len(errors) > 5:
                print(f"... e mais {len(errors) - 5} erros.")
            sys.exit(1)
        
        print("Análise Sintática OK. Iniciando Análise Semântica...")
        
        # 2. ANÁLISE SEMÂNTICA
        semantic_visitor = SemanticVisitor()
        walker = ParseTreeWalker()
        walker.walk(semantic_visitor, tree)
        
        if semantic_visitor.erros_semanticos:
            print("\n--- COMPILAÇÃO FALHOU (Erros Semânticos) ---")
            for error in semantic_visitor.erros_semanticos:
                print(error)
            sys.exit(1)

        # 3. SUCESSO
        print("\n✅ CÓDIGO CORRETO: Compilação concluída com sucesso.")
        
    except FileNotFoundError:
        print(f"\nERRO: Arquivo de entrada '{input_file}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        # Captura erros de runtime do ANTLR, como falta da pasta 'saida'
        print(f"\nERRO INESPERADO durante a compilação. Certifique-se de que a pasta 'saida' foi gerada: {e}")
        sys.exit(1)