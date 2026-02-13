("""
Segunda versão do relatório de vendas

Validar vendas usando try/except.

Armazenar:
{'Nome': {'total_vendas': X, 'quantidade_vendas': Y}}

Atualizar valores a cada nova venda.

Ao final mostrar total e média por vendedor.""")

# solução:👇
from cores import *

dicionario_funcionario = { }
dicionario_info = { }

while True:
    opcao = str(input(f"{Negrito}Deseja adicionar um vendedor? [S / N]{Reset}")).strip().upper()
    while opcao not in ["S", "N"]:
        print(f"{Vermelho}Termo: '{opcao}' FORA da lista de S/N{Reset}")
        opcao = str(input(f"{Negrito}Deseja adicionar um vendedor? [S / N]{Reset}")).strip().upper()
    opcao = str(opcao)
    if (opcao=="N"):
            break

    vendedor_nome = str(input(f"{Negrito}Digite o nome do Vendedor: {Reset}")).strip().capitalize()
    while not vendedor_nome.isalpha():
        print(f"{Vermelho}Termo Inválido!! Digite um NOME de um vendedor(a){Reset}")
        vendedor_nome = str(input(f"{Negrito}Digite o nome do Vendedor: {Reset}")).strip().capitalize()
    vendedor_nome = str(vendedor_nome)

    vendedor_vendas = str(input(f"{Negrito}Digite a O valor de vendas que o vendedor(a) fez{Reset}"))
    while not vendedor_vendas.isdigit():
        print(f"{Vermelho}Termo Inválido!! Digite O valor de vendas que o vendedor(a) fez{Reset}")
        vendedor_vendas = str(input(f"{Negrito}Digite O valor de vendas que o vendedor(a) fez{Reset}"))
    vendedor_vendas = int(vendedor_vendas)
    vendedor_qtd = str(input(f"{Negrito}Digite a QTD de produtos que o vendedor(a) vendeu{Reset}"))
while not vendedor_qtd.isdigit():
    print(f"{Vermelho}Termo Inválido!! Digite a QTD de produtos que o vendedor(a) vendeu{Reset}")
    vendedor_qtd = str(input(f"{Negrito}Digite a QTD de produtos que o vendedor(a) vendeu{Reset}"))
vendedor_qtd = int(vendedor_qtd)

dicionario_info["Vendas"] = vendedor_vendas
dicionario_info["QTD. Vendas"] = vendedor_qtd
dicionario_funcionario[vendedor_nome] = dicionario_info

print(dicionario_funcionario)