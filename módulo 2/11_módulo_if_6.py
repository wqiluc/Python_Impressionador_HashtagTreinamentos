from cores import (Azul, Magenta, AmareloClaro, Reset, Negrito,Vermelho)

print(f"""
{Azul}{Negrito}COMPARAÇÕES CONTRAINTUITIVAS NO PYTHON{Reset}

{Magenta}
Existem algumas comparações no Python que, à primeira vista,
podem parecer estranhas, mas são muito utilizadas no dia a dia
por programadores mais experientes.
{Reset}

{AmareloClaro}
Essas comparações costumam ser usadas para verificar
se um valor "existe" ou não, sem precisar comparar
explicitamente com números ou textos.
{Reset}""")

faturamento = input(f"{Negrito}{Azul}Qual foi o faturamento da loja nesse mês? {Reset}")
if faturamento == " " or faturamento == 0:
    print(f"{Vermelho}Termo Inválido!! ❌{Reset}")
    faturamento = input(f"{Negrito}{Azul}Qual foi o faturamento da loja nesse mês? {Reset}")
custo = input(f"{Negrito}{Azul}Qual foi o custo da loja nesse mês? {Reset}")
if custo == " " or custo == 0:
    print(f"{Vermelho}Termo Inválido!! ❌{Reset}")
    custo = input(f"{Negrito}{Azul}Qual foi o custo da loja nesse mês? {Reset}")

lucro = int(faturamento) - int(custo)

print(f"""{Magenta}Resultado do cálculo: {Reset}O lucro da loja foi de {lucro} reais""")

print(f"""
{Azul}{Negrito}RESUMO{Reset}

{AmareloClaro}
Algumas comparações contraintuitivas muito usadas em Python:
{Reset}

{Magenta}
- if 0:
- if '':

Essas estruturas verificam valores considerados "falsos"
pelo Python (valores vazios ou zero).
{Reset}

{Magenta}
Esse conceito também se aplica a listas vazias,
dicionários vazios e outros objetos.
Esses casos serão retomados em módulos futuros.
{Reset}""")