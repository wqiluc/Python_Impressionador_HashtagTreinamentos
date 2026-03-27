("""
Primeira versão da lista de compras

Escreva um programa que permita que um usuário crie uma lista de compras.

O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.

Estruture seu programa da seguinte forma:

1. Crie uma lista vazia para armazenar os itens da lista de compras.
2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
7. Se o usuário escolher sair, encerre o loop usando break.""")


# solução👇:
from cores import *

lista_produtos = list()

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
          lista_produtos.append(adicionar_produto)
    elif (opcao==2):
          remover_produto = str(input(f"{Negrito}Digite o nome do Produto que quer remover: {Reset}")).strip().capitalize()
          if remover_produto not in lista_produtos:
                print(f"{Vermelho}O produto: '{remover_produto}' NÃO ENCONTRA-SE na lista. Digite novamente{Reset}")
                continue
          else:
                lista_produtos.remove(remover_produto.capitalize())
    elif (opcao==3):
          for indice_produto, (produto) in (enumerate(lista_produtos)):
                print(f"{Negrito}{indice_produto+1}º Produto: {produto}{Reset}")
    else:
          break
    
print(f"{Verde}Sistema encerrado com sucesso! 🛒✅{Reset} {AzulClaro}Volte sempre!👋{Reset}")