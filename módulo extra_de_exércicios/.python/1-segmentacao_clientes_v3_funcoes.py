("""
Terceira versão da segmentação de clientes

Organizar usando funções:

- solicitar_nome_cliente;
- solicitar_total_compras;
- atribuir_segmento; e
- print_segmento_por_cliente.

Armazenar nomes em letras minúsculas.""")

# solução:
from cores import *

clientes = list()

def menu():
    opcao = str(input(f"{Negrito}Deseja cadastrar um cliente? [S/N]: {Reset}")).strip().upper()
    while (opcao not in ["S","N"]):
        print(f"{Vermelho}Termo Inválido!! Digite apenas [S/N]{Reset}")
        opcao = str(input(f"{Negrito}Deseja cadastrar um cliente? [S/N]: {Reset}")).strip().upper()
    if (opcao == "N"):
        return
    cadastrar_cliente()

def cadastrar_cliente():
    indice_cliente = tuple()

    nome_cliente = str(input(f"{Negrito}Digite o NOME do cliente: {Reset}")).strip().capitalize()
    while not (nome_cliente.replace(" ","",10).isalpha()):
        print(f"{Vermelho}Termo Inválido!! Digite O NOME do cliente (str){Reset}")
        nome_cliente = str(input(f"{Negrito}Digite o NOME do cliente: {Reset}")).strip().capitalize()

    total_compras_cliente = str(input(f"{Negrito}Digite o total de compras feitas pelo cliente: '{nome_cliente}': {Reset}")).strip()
    while not (total_compras_cliente.isdigit()):
        print(f"{Vermelho}Termo Inválido!! Digite o TOTAL DE COMPRAS do cliente: '{nome_cliente}'{Reset}")
        total_compras_cliente = str(input(f"{Negrito}Digite o total de compras feitas pelo cliente: '{nome_cliente}': {Reset}")).strip()
    total_compras_cliente = int(total_compras_cliente)

    indice_cliente += (total_compras_cliente,nome_cliente)
    clientes.append(indice_cliente)

    menu()

menu()
print(clientes)