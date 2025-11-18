# 💻 Projeto Compilador: Linguagem X (A3 - [Seu Período/Disciplina])

## 1. Introdução
Desenvolvimento de um compilador para a Linguagem X, uma DSL (Domain-Specific Language) imperativa projetada para cumprir todos os requisitos obrigatórios da avaliação. O compilador realiza as etapas de Análise Léxica, Sintática e Semântica (verificação de declaração de variáveis).

## 2. Decisões Técnicas
O projeto utiliza **ANTLR 4** para a geração das ferramentas de Lexer e Parser a partir da gramática `LinguagemX.g4`, com o runtime em **Python 3**.

### 2.1. Componentes Principais:
| Arquivo | Função |
| :--- | :--- |
| `LinguagemX.g4` | Gramática (Lexer e Parser) da Linguagem X. |
| `main.py` | Driver do compilador (Orquestra as análises). |
| `SemanticVisitor.py` | Implementa a Análise Semântica (Tabela de Símbolos e verificação de declaração). |
| `saida/` | Arquivos gerados pelo ANTLR (Listener, Lexer, Parser). |

## 3. Detalhamento da Linguagem
Todos os aspectos da sintaxe, tipos de dados e estruturas de controle estão documentados formalmente no relatório da linguagem.

👉 **[Acesse o Detalhamento Completo da Linguagem X (PDF/MD)](./arquivo)**

## 4. Como Compilar e Executar
Para rodar o compilador, execute o seguinte comando na pasta raiz do projeto, substituindo `<arquivo.lx>` pelo nome de um dos arquivos de teste:

```bash
python src/main.py testes/teste_sucesso_decl.lx
4.1. Requisitos
Java JRE/JDK

Python 3

pip install antlr4-python3-runtime

5. Comprovação da Funcionalidade
O compilador processou o arquivo de teste com sucesso na fase Semântica:
![Compilação Bem-Sucedida - Linguagem X](RELATORIO/Comprovação.png)
