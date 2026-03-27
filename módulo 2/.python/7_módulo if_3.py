from cores import (Azul, Magenta, AmareloClaro, VerdeClaro, Vermelho, Reset, Negrito)

meta_vendas = 20000
vendas = 45000

print(f"""{Azul}{Negrito}ELIF – ANÁLISE DE BÔNUS DE FUNCIONÁRIOS{Reset}

{Magenta}
Este programa analisa o valor de vendas de um funcionário
e calcula o bônus recebido com base nas regras da empresa.
{Reset}

{AmareloClaro}Meta de vendas:{Reset} R$ {meta_vendas:,.2f}
{AmareloClaro}Valor vendido:{Reset} R$ {vendas:,.2f}""")

if vendas <= meta_vendas:
    bonus = 0
    print(f"""{Vermelho}Resultado:{Reset}O funcionário não bateu a meta. Bônus: R$ {bonus:,.2f} ❌""")
elif vendas <= meta_vendas * 2:
    bonus = vendas * 0.03
    print(f"""{VerdeClaro}Resultado:{Reset}O funcionário bateu a meta.Bônus de 3% aplicado. Bônus: R$ {bonus:.2f} ✅""")
else:
    bonus = vendas * 0.07
    print(f"""{AmareloClaro}Resultado:{Reset}O funcionário superou o dobro da meta! Bônus de 7% aplicado. Bônus: R$ {bonus:,.2f} 🚀""")