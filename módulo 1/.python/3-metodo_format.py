from cores import (Verde,Azul, AmareloClaro, Magenta, Reset)

print(f"""
{Azul}Métodos Format{Reset} {AmareloClaro}(f ou .format(parâmetros)){Reset}

{Magenta}Forma que fizemos na última aula ({AmareloClaro}concatenação de textos{Reset}{Magenta}){Reset}
""")

faturamento = 2000
custo = 500
lucro = faturamento - custo
from cores import Azul, AmareloClaro, Magenta, Reset

print(
    f"{Magenta}O faturamento da loja foi:{Reset} {Verde}R${faturamento}{Reset} "
    f"{Magenta}O custo da loja foi: {Verde}R${custo}{Reset}. "
    f"{Magenta}Assim, o lucro da loja foi:{Reset} {Verde}R${lucro}{Reset}")

print(f"\n{Azul}Método .format(parâmetros){Reset}\n")

print(f"{Magenta}O faturamento da loja foi: {Verde}R${faturamento}{Reset} "
    f"{Magenta}O custo da loja foi: {Verde}R${custo}{Reset}. "
    f"{Magenta}Assim, o lucro da loja foi: {Verde}R${lucro}{Reset} \n\n")