from cores import (Azul, Magenta, AmareloClaro, VerdeClaro, Vermelho, Reset, Negrito)
from time import sleep

meta_funcionario = 20000
meta_loja = 100000

vendas_funcionario = float(input(f"{Negrito}{Azul}Digite o valor de vendas do funcionário: {Reset}"))
vendas_loja = float(input(f"{Negrito}{Azul}Digite o valor de vendas da loja: {Reset}"))
nota_avaliacao = int(input(f"{Negrito}{Azul}Digite a nota da avaliação (0 a 10): {Reset}"))

bonus = 0

print(f"""{Magenta} Análisando as condições para cálculo de bônus...{Reset}""")
sleep(1)

print(f"""{AmareloClaro}Meta do funcionário:{Reset} R$ {meta_funcionario:,.2f}
{AmareloClaro}Meta da loja:{Reset} R$ {meta_loja:,.2f}""")

if (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja) or (nota_avaliacao >= 9):
    bonus = vendas_funcionario * 0.03
    print(f"{VerdeClaro}BÔNUS APROVADO ✅{Reset}Bônus de 3% aplicadoValor do bônus: R$ {bonus:,.2f}")
else:
    bonus = 0
    print(f"{Vermelho}BÔNUS NÃO APROVADO ❌{Reset}Nenhum bônus será pago neste mês.")