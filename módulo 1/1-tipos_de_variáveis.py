from cores import (Azul, AmareloClaro, Magenta, Reset)

print(f"""
{Azul}Tipos de Variáveis em Python{Reset}

{Magenta}Uma variável é um objeto, afinal tudo é um objeto em Python{Reset}

{AmareloClaro}int{Reset} {Magenta}-> inteiro{Reset}
{AmareloClaro}str{Reset} {Magenta}-> texto{Reset}
{AmareloClaro}float{Reset} {Magenta}-> números com casas decimais (ponto flutuante){Reset}
{AmareloClaro}bool{Reset} {Magenta}-> True ou False{Reset}

{Magenta}Obs: Variáveis em Python não são declaradas explicitamente{Reset}
{Magenta}Obs2: Cuidado com nomes reservados{Reset}\n """)

faturamento = 1000
type(faturamento)

faturamento = 1000.00
type(faturamento)

faturamento = '1.000'
type(faturamento)

ganha_bonus = True
type(ganha_bonus)