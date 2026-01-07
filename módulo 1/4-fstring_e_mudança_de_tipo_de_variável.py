from cores import (Verde,Azul, AmareloClaro, Magenta, Reset, Negrito)

print(f"""
{Azul}Entrada de Dados e Conversão de Tipos{Reset}

{Magenta}Neste exemplo veremos:{Reset}
{AmareloClaro}- Uso do método .format(){Reset}
{AmareloClaro}- Uso de f-string{Reset}
{AmareloClaro}- Entrada de dados com input(){Reset}
{AmareloClaro}- Conversão de tipos (str, int, float){Reset}

{Magenta}Obs: input() sempre retorna texto (string){Reset}""")

faturamento = 1000
custo = 400

lucro = (faturamento - custo)

print(f"{Magenta}Com .format →{Reset} "
    "O faturamento foi de: R${} e o lucro de R${}".format(faturamento, lucro))

print(f"{Magenta}Com f-string →{Reset} "
    f"O faturamento foi de:{Reset} {Verde}R${faturamento}{Reset}{Negrito} e o lucro de:{Reset} {Verde}R${lucro}{Reset}")

faturamento = int(input(f"\n\n{Negrito}Insira o faturamento: R${Reset} "))
custo = int(input(f"\n\n{Negrito}Insira o custo: R${Reset} "))

lucro = (faturamento - custo)

print(f"\n{Magenta}Lucro calculado:{Reset} {Verde}R${lucro}{Reset}\n\n")