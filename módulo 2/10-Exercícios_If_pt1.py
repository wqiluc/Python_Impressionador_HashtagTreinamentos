from cores import (Azul, Magenta, AmareloClaro, Reset, Negrito,Verde,Vermelho)

print(f"""
{Azul}{Negrito}EXERCÍCIOS COM IF – CÁLCULO DE BÔNUS{Reset}

{Magenta}
Exercício 1 – Cálculo de Bônus
{Reset}

{AmareloClaro}Regras:{Reset}
- A meta é 1000 vendas
- Se o valor de vendas for maior ou igual à meta,
  o bônus do funcionário é de 10% do valor de vendas
- Caso contrário, o bônus é 0
- Deve ser exibido o bônus de 3 funcionários

{Magenta}
Variáveis disponíveis:
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700
{Reset}
""")

print(f"{Negrito}SEU CÓDIGO–RESPOSTA AQUI ⬇️{Reset}")

bonus = 0
meta = 1000 # Meta de vendas
vendas_funcionario1 = 1000 #funcionário 1
vendas_funcionario2 = 770 #funcionário 2
vendas_funcionario3 = 2700 #funcionário 3

if vendas_funcionario1 >= meta:
    bonus = 0.10 * vendas_funcionario1
    print(f"\n{Verde}Parabéns!!✅ o seu bônus é de: {bonus:,.2f}{Reset}")
else:
    bonus = 0
    print(f"\n{Vermelho}Bônus Zerado ❌{Reset}")

if vendas_funcionario2 >= meta:
    bonus = 0.10 * vendas_funcionario2
    print(f"\n{Verde}Parabéns!!✅ o seu bônus é de: {bonus:,.2f}{Reset}")
else:
    bonus = 0
    print(f"\n{Vermelho}Bônus Zerado ❌{Reset}")

if vendas_funcionario3 >= meta:
    bonus = 0.10 * vendas_funcionario3
    print(f"\n{Verde}Parabéns!!✅ o seu bônus é de: {bonus:,.2f}{Reset}")
else:
    bonus = 0
    print(f"\n{Vermelho}Bônus Zerado ❌{Reset}")


print(f"""
{Azul}{Negrito}EXERCÍCIO 2 – NOVA REGRA DE BÔNUS{Reset}

{Magenta}
Agora o cálculo de bônus segue uma nova lógica,
considerando diferentes níveis de desempenho.
{Reset}

{AmareloClaro}Regras:{Reset}
- A meta continua sendo 1000 vendas
- Se o funcionário vender 2000 ou mais, o bônus é de 15%
- Se vender entre 1000 e 1999, o bônus é de 10%
- Se vender menos de 1000, o bônus é 0

{Magenta}
Use as mesmas variáveis do exercício anterior.
Você pode resolver usando if dentro de if
ou usando if, elif e else.
{Reset}""")

print(f"{Negrito}SEU CÓDIGO–RESPOSTA AQUI ⬇️{Reset}")

bonus = 0 # inicializar o bônus como sendo 0
meta = 1000 # vendas

vendas_funcionario = int(input(f"\n {Negrito}Digite as vendas do funcionário: {Reset}"))

if (vendas_funcionario < 1000):
    bonus = 0
    print(f"\n {AmareloClaro}O seu bônus é de:{Reset} {Vermelho}R${bonus:.2f}{Reset}")
else:
    if (vendas_funcionario >= 1000 and vendas_funcionario<=1999):
        bonus = vendas_funcionario * 0.10
        print(f"\n {Azul}Parábens!!👊 {Reset} {Negrito} O seu bônus é de:{Reset} {Verde}R${bonus:.2f}{Reset}")
    else:
        if vendas_funcionario >= 2000:
            bonus = vendas_funcionario*0.15
            print(f"{Verde}MEUS PARÁBENS!! ✅{Reset} {Negrito} O seu bônus foi de:{Reset} {Verde}R${bonus:.2f}{Reset}")