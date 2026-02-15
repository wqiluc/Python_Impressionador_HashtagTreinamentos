("""
Terceira versão da lista de compras

Mantenha o programa com dicionário, mas use funções para organizar o código.

Crie funções:
- adicionar_item
- remover_item
- ver_lista
- mostrar_menu

O programa deve continuar funcionando da mesma forma.""")

#solução:👇
from cores import *

dicionario_produtos = dict()

def mostrar_menu():
    opcao = str(input(f"""{Negrito}Digite uma opcão do menu:
                      1 - Adicionar Item✅;
                      2 - Remover Item❌;
                      3 - Vizualizar Lista Completa ⚠️👁️; e
                      4 - Sair do Sistema 🛒👋{Reset}""")).strip()
    while not opcao.isdigit() or int(opcao) not in [1,2,3,4]:
        print(f"{Vermelho}Termo Inválido!!❌ Digite um NÚMERO entre 1 e 4{Reset}")
        opcao = str(input(f"""{Negrito}Digite uma opcão do menu:
                      1 - Adicionar Item✅;
                      2 - Remover Item❌;
                      3 - Vizualizar Lista Completa ⚠️👁️; e
                      4 - Sair do Sistema 🛒👋{Reset}""")).strip()
    return int(opcao)

def adicionar_item():
    adicionar_produto = str(input(f"{Negrito}Digite o nome de um produto: {Reset}")).strip().capitalize()
    while not adicionar_produto.isalpha():
        print(f"{Vermelho}Termo Inválido!!❌ Digite um NOME DE PRODUTO (str){Reset}")
        adicionar_produto = str(input(f"{Negrito}Digite o nome de um produto: {Reset}")).strip().capitalize()
    quantidade_produto = str(input(f"{Negrito}Digite quantos(as): '{adicionar_produto}' deseja adicionar?{Reset}")).strip()
    while not quantidade_produto.isdigit():
        print(f"{Vermelho}Termo Inválido!!❌ Digite uma QUANTIDADE (int){Reset}")
        quantidade_produto = str(input(f"{Negrito}Digite quantos(as): '{adicionar_produto}' deseja adicionar?{Reset}")).strip()
    dicionario_produtos[adicionar_produto] = int(quantidade_produto)

def remover_item():
    remover_produto = str(input(f"{Negrito}Digite o nome do Produto que quer remover: {Reset}")).strip().capitalize()
    if remover_produto not in dicionario_produtos:
        print(f"{Vermelho}O produto: '{remover_produto}' NÃO ENCONTRA-SE no dicionário. Digite novamente{Reset}")
        return
    dicionario_produtos.pop(remover_produto)

def ver_lista():
    for indice_produto, (produto,qtd) in enumerate(dicionario_produtos.items()):
        print(f"{Negrito}{indice_produto+1}º Produto: {produto} - Quantidade: {qtd}{Reset}")

while True:
    opcao = mostrar_menu()
    if opcao == 1:
        adicionar_item()
    elif opcao == 2:
        remover_item()
    elif opcao == 3:
        ver_lista()
    elif opcao == 4:
        break

print(f"{Verde}Sistema encerrado com sucesso! 🛒✅{Reset} {AzulClaro}Volte sempre!👋{Reset}")
print(dicionario_produtos)