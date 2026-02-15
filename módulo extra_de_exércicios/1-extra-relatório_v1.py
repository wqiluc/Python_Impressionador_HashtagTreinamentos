("""
Primeira versão do relatório de vendas

Criar programa que calcula total e média de vendas por vendedor.

1. Dicionário vazio.
2. Loop infinito solicitando nome e vendas.
3. Se digitar 'sair', encerrar.
4. Calcular total e média.
5. Ao final imprimir resultados.

Dica:
usar sum() e len().""")

# solução:👇
from cores import *

lista_funcionarios_nome = list()
lista_funcionarios_valor = list()

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
    lista_funcionarios_nome.append(vendedor_nome)

    vendedor_vendas = str(input(f"{Negrito}Digite a QTD de vendas que o vendedor(a) fez{Reset}"))
    while not vendedor_vendas.isdigit():
        print(f"{Vermelho}Termo Inválido!! Digite a QTD de vendas que o vendedor(a) fez{Reset}")
        vendedor_vendas = str(input(f"{Negrito}Digite a QTD de vendas que o vendedor(a) fez{Reset}"))
    vendedor_vendas = int(vendedor_vendas)
    lista_funcionarios_valor.append(vendedor_vendas)

soma_vendas = (sum(lista_funcionarios_valor))
media_vendas = (sum(lista_funcionarios_valor)/len(lista_funcionarios_valor))

print(f"{Negrito}O total arrecadado pelos vendedores foi de:{Reset} {Verde}R${Reset}{Negrito}{soma_vendas}{Reset}")
print(f"{Negrito}A média total arrecadada pelos vendedores foi de:{Reset} {Verde}R${Reset}{Negrito}{media_vendas}/Vendedor{Reset}")

for indice_vendedor, (vendedor, valorvenda) in enumerate(zip(lista_funcionarios_nome,lista_funcionarios_valor)):
     print(f"{Negrito}{indice_vendedor+1}º Vendedor - Nome:{Reset} {Amarelo}'{vendedor}'{Reset}{Negrito} - QTD. Vendas:{Reset} {Magenta}{valorvenda}{Reset}")