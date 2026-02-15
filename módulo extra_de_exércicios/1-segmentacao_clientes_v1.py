("""
Primeira versão da segmentação de clientes

Segmentos:
- Bronze até 1000
- Prata até 5000
- Ouro acima de 5000

1. Dicionário vazio.
2. Loop solicitando nome e compras.
3. Se digitar 'sair', encerrar.
4. Atribuir segmento.
5. Ao final imprimir cliente e segmento.""")

# solução
from cores import *

dicionario_cliente = dict()
clientes = list()

while True:
    opcao = str(input(f"{Negrito}Deseja cadastrar um cliente? [S/N]: {Reset}")).strip().upper()
    while opcao not in ["S","N"]:
        print(f"{Vermelho}Termo Inválido!! Digite apenas [S/N]{Reset}")
        opcao = str(input(f"{Negrito}Deseja cadastrar um cliente? [S/N]: {Reset}")).strip().upper()
    if opcao == "N":
        break

    nome_cliente = str(input(f"{Negrito}Digite o NOME do cliente: {Reset}")).strip().capitalize()
    while not nome_cliente.replace(" ","",10).isalpha():
        print(f"{Vermelho}Termo Inválido!! Digite O NOME do cliente (str){Reset}")
        nome_cliente = str(input(f"{Negrito}Digite o NOME do cliente: {Reset}")).strip().capitalize()

    total_compras_cliente = str(input(f"{Negrito}Digite o total de compras feitas pelo cliente: '{nome_cliente}': {Reset}")).strip()
    while not total_compras_cliente.isdigit():
        print(f"{Vermelho}Termo Inválido!! Digite o TOTAL DE COMPRAS do cliente: '{nome_cliente}'{Reset}")
        total_compras_cliente = str(input(f"{Negrito}Digite o total de compras feitas pelo cliente: '{nome_cliente}': {Reset}")).strip()
    total_compras_cliente = int(total_compras_cliente)

    dicionario_cliente["Nome do Cliente"] = nome_cliente
    dicionario_cliente["Total de Compras do Cliente"] = total_compras_cliente
    clientes.append(dicionario_cliente.copy())

for indice_cliente, (indice_dicionario) in enumerate(clientes):
    print(f"{Negrito}{indice_cliente+1}º Cliente - Nome: '{indice_dicionario["Nome do Cliente"]}' - Total Comprado: {Reset}{Verde}R${Reset}{Negrito}{indice_dicionario["Total de Compras do Cliente"]:.2f}{Reset}")