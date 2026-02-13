("""
Primeira versão da previsão de vendas

Crie um programa que preveja vendas totais para cada produto.

1. Criar um dicionário vazio.
2. Loop infinito solicitando:
   - nome do produto;
   - vendas atuais;
   - taxa de crescimento.
3. Se digitar 'sair', encerrar o loop.
4. Calcular vendas previstas e salvar no dicionário.
5. Ao final, iterar e mostrar previsões.""")

# solução:👇
from cores import *

info_produto = [ ]

def escolher_opcao():
    opcao = str(input(f"""{Negrito}Digite:
                      1- Informar dados do Produto 🛍️;
                      2 - Sair do Sistema ❌{Reset}""")).strip()
    while not opcao.isdigit():
        print(f"{Vermelho}Termo Inválido!! Digite uma opcão [1 / 2]{Reset}")
        opcao = str(input(f"""{Negrito}Digite:
                      1- Informar dados do Produto 🛍️;
                      2 - Sair do Sistema ❌{Reset}""")).strip()
    return int(opcao)

def mostrar_dados_produto(opcao):
    try:
        if (opcao==1):
            produto = str(input(f"{Negrito}Digite o nome do Produto: {Reset}")).strip().capitalize()
            while not produto.isalpha():
                print(f"{Vermelho}Termo Inválido!! ❌ Digite o NOME do produto (str){Reset}")
                produto = str(input(f"{Negrito}Digite o nome do Produto: {Reset}")).strip().capitalize()
            produto = str(produto)

        vendas = str(input(f"{Negrito}Digite o nº de vendas do produto: '{produto}': {Reset}")).strip()
        while not vendas.isdigit():
             print(f"{Vermelho}Termo Inválido!! ❌ Digite o NÚMERO de vendas do produto: '{produto}' (int){Reset}")
             vendas = str(input(f"{Negrito}Digite o nº de vendas do produto: '{produto}': {Reset}")).strip()
        vendas = int(vendas)

        taxa_de_crescimento = str(input(f"{Negrito}Digite a taxa de crescimento (em %) do produto: '{produto}': {Reset}"))
        while not taxa_de_crescimento.isdigit():
            print(f"{Vermelho}Termo Inválido!! ❌ Digite A TAXA de vendas do produto: '{produto}' (int){Reset}")
            taxa_de_crescimento = str(input(f"{Negrito}Digite a taxa de crescimento (em %) do produto: '{produto}': {Reset}"))
        taxa_de_crescimento = int(taxa_de_crescimento)
        info_produto.append([produto,vendas,taxa_de_crescimento])
    except:
        print(ValueError)

while True:
    opcao_mostrar = escolher_opcao()
    if (opcao_mostrar==2):
        break
    mostrar_dados_produto(opcao_mostrar)

for indice_produto, (indice_tupla) in (enumerate(info_produto)):
    print(f"{Negrito}{indice_produto+1}º Produto:{Reset} {Amarelo}'{indice_tupla[0]}'{Reset}{Negrito} - Qtd. Vendas: {Reset}{Azul}{indice_tupla[1]}{Reset}{Negrito} - Porcentagem de Vendas: {indice_tupla[2]}{Reset}{Amarelo}%{Reset}")