("""
Segunda versão da lista de compras

Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.

O programa deve permitir adicionar mais de uma unidade de um item.

O programa deve permitir:
- adicionar itens;
- remover itens;
- visualizar o dicionário de compras.

Mostrar mensagem de erro para opção inválida.

O programa deve ser case insensitive.""")

#solução👇:
from cores import *

dicionario_produtos = dict()

while True:
    opcao = str(input(f"""{Negrito}Digite uma opcão do menu:
                      1 - Adicionar Item✅;
                      2 - Remover Item❌;
                      3 - Vizualizar Lista Completa ⚠️👁️; e
                      4 - Sair do Sistema 🛒👋{Reset}""")).strip().capitalize()
    while not (opcao.isdigit()):
            print(f"{Vermelho}Termo Inválido!!❌ Digite um NÚMERO (int){Reset}")
            opcao = str(input(f"""{Negrito}Digite uma opcão do menu:
                      1 - Adicionar Item✅;
                      2 - Remover Item❌;
                      3 - Vizualizar Lista Completa ⚠️👁️; e
                      4 - Sair do Sistema 🛒👋{Reset}""")).strip().capitalize()
    opcao = int(opcao)
    if (opcao==1):
          adicionar_produto = str(input(f"{Negrito}Digite o nome de um produto: {Reset}")).capitalize()
          while not adicionar_produto.isalpha():
                 print(f"{Vermelho}Termo Inválido!!❌ Digite um NOME DE PRODUTO (str){Reset}")
                 adicionar_produto = str(input(f"{Negrito}Digite o nome de um produto: {Reset}")).capitalize()
          quantidade_produto = str(input(f"{Negrito}Digite quantos(as): '{adicionar_produto}' deseja adicionar?{Reset}")).strip()
          while not (quantidade_produto.isdigit()):
                 print(f"{Vermelho}Termo Inválido!!❌ Digite uma QUANTIDADE (int){Reset}")
                 quantidade_produto = str(input(f"{Negrito}Digite quantos(as): '{adicionar_produto}' deseja adicionar?{Reset}")).strip()
          dicionario_produtos[adicionar_produto] = int(quantidade_produto)
    elif (opcao==2):
          remover_produto = str(input(f"{Negrito}Digite o nome do Produto que quer remover: {Reset}")).strip().capitalize()
          if (remover_produto not in dicionario_produtos):
                print(f"{Vermelho}O produto: '{remover_produto}' NÃO ENCONTRA-SE no dicionário. Digite novamente{Reset}")
                continue
          else:
                dicionario_produtos.pop(remover_produto)
    elif (opcao==3):
          for indice_produto, (produto,qtd) in (enumerate(dicionario_produtos.items())):
                print(f"{Negrito}{indice_produto+1}º Produto: {produto} - Quantidade: {qtd}{Reset}")
    else:
          break
    
print(f"{Verde}Sistema encerrado com sucesso! 🛒✅{Reset} {AzulClaro}Volte sempre!👋{Reset}")
print(dicionario_produtos)