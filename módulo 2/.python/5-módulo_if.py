from cores import (Negrito,Reset,Azul, Magenta, AmareloClaro,Vermelho, Verde)

meta_iphone = int(input(f"\n {Negrito}Digite a meta de iPhones da impresa: {Reset}"))
vendas_iphone_empresa = int(input(f"\n{Negrito}Digite quantos iPhones foram vendidos: {Reset}"))

print(f"""{Azul}CONDICIONAL IF – ANÁLISE DE VENDAS 💰{Reset}

{Magenta}
Digamos que você trabalha na Amazon e precisa analisar
o desempenho de vendas de um produto no mês.
Neste exemplo, estamos avaliando as vendas de um iPhone.
{Reset}

{AmareloClaro}Meta de vendas:{Reset} {meta_iphone} unidades
{AmareloClaro}Quantidade vendida no mês:{Reset} {vendas_iphone_empresa} unidades""")

if vendas_iphone_empresa >= meta_iphone:
    print(f"""
{Magenta}Resultado:{Reset}
{Verde}Batemos a meta de vendas do iPhone!{Reset}
Vendemos: {vendas_iphone_empresa} unidades 🎉
""")
else:
    print(f"""{Magenta}Resultado:{Reset}{Vermelho}Infelizmente não batemos a meta.{Reset}\n 
          Vendemos: {vendas_iphone_empresa} unidades.
A meta era de {meta_iphone} unidades.""")