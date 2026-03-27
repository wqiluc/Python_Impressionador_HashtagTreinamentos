from cores import (Reset, Azul, Amarelo, Magenta, Verde)

print(f"""
{Azul}Exercícios — Estruturas Básicas em Python 🐍{Reset}

{Magenta}────────────────────────────────────────{Reset}
{Amarelo}Exercício 1 — Cadastro de Produtos{Reset}
{Magenta}────────────────────────────────────────{Reset}

{Magenta}Objetivo:{Reset}
Criar um sistema simples de cadastro de produtos em uma lista.

{Magenta}Requisitos:{Reset}
• Solicitar ao usuário, via input, o nome do produto a ser cadastrado; 
• Garantir que letras maiúsculas e minúsculas não gerem produtos duplicados; 
• Caso o produto já exista, exibir a mensagem: 
  {Amarelo}"Produto já existente, tente novamente"{Reset}; 
• Caso o produto não exista, adicioná-lo à lista; 
• Exibir a mensagem:
  {Amarelo}"Produto X cadastrado com sucesso"{Reset}; 
• Imprimir a lista completa de produtos ao final.

{Magenta}────────────────────────────────────────{Reset}
{Amarelo}Exercício 2 — Consulta de Preços{Reset}
{Magenta}────────────────────────────────────────{Reset}

{Magenta}Objetivo:{Reset}
Criar um sistema de consulta de preços de produtos cadastrados.

{Magenta}Requisitos:{Reset}
• Solicitar ao usuário o nome de um produto; 
• Caso o produto exista, exibir o preço correspondente; 
• Exemplo:
  O produto celular custa {Verde}R$1500{Reset}; 
• Caso o produto não exista, solicitar que o usuário tente novamente.

{Magenta}────────────────────────────────────────{Reset}
{Amarelo}Exercício 3 — Cálculo de Bônus de Funcionários{Reset}
{Magenta}────────────────────────────────────────{Reset}

{Magenta}Objetivo:{Reset}
Calcular o bônus de um funcionário com base na quantidade de vendas realizadas.

{Magenta}Regras de Bônus:{Reset}
• Mais de 1000 unidades vendidas:
  bônus de {Verde}R$2{Reset} por unidade; 
• Mais de 5000 unidades vendidas:
  bônus de {Verde}R$2{Reset} por unidade + {Verde}R$1000{Reset} fixos; 
• Menos de 1000 unidades vendidas:
  não há bônus.

{Magenta}Ao final, o sistema deve imprimir o valor total do bônus.{Reset}

{Magenta}────────────────────────────────────────{Reset}
{Amarelo}Exercício 4 — Análise de Vendas{Reset}
{Magenta}────────────────────────────────────────{Reset}

{Magenta}Objetivo:{Reset}
Identificar qual vendedor obteve o maior volume de vendas.

{Magenta}Contexto:{Reset}
• Cada vendedor possui uma lista com suas vendas; 
• O programa deve somar as vendas de cada vendedor; 
• Comparar os totais e indicar quem vendeu mais.""")


# 1:
from cores import(Negrito,Reset,Vermelho,Verde)

produtos = ["celular", "camera", "fone de ouvido", "monitor"]

cadastro_produto = str(input(f"\n {Negrito}Digite o nome do produto que quer cadastrar: {Reset}")).strip().lower()
while (cadastro_produto in produtos):
    print(f"\n {Vermelho}O produto: '{cadastro_produto}', já está cadastrado na lista! ❌ tente novamente{Reset}")
    cadastro_produto = str(input(f"\n {Negrito}Digite o nome do produto que quer cadastrar: {Reset}")).strip().lower()
else:
    produtos.append(cadastro_produto)
    print(f"\n {Negrito}Produto: '{cadastro_produto}' {Reset} {Verde}cadastrado com sucesso ✅🖋️{Reset}")

print(produtos)


#2:
from cores import(Negrito,Reset,Vermelho,Verde)

produtos = ["celular", "camera", "fone de ouvido", "monitor"]
precos = [1500, 1000, 800, 2000]
produtos_preços = {
        "celular": 1500,
        "camera":1000,
        "fone de ouvido":800,
        "monitor":2000}

encontrar_produto = str(input(f"\n {Negrito}Digite o nome do produto que quer encontrar: {Reset}"))
if (encontrar_produto in produtos_preços):
        print(f"\n {Negrito}Produto:{Reset} '{encontrar_produto}'{Reset} {Verde}encontrado ✅ 🖋️{Reset}")
        print(f"\n {Negrito}Seu preço é:{Reset} {Verde}{produtos_preços.items()}{Reset}")
else:
    print(f"\n {Vermelho}Produto: '{encontrar_produto}' não foi encontrado ❌{Reset}")
    pass


#3:
from cores import (Negrito,Reset,Verde,Vermelho)

vendas_funcionario = int(input(f"\n {Negrito}Digite a quantidade de vendas realizadas por esse funcionário: {Reset}"))
if vendas_funcionario > 1000:
    bonus_funcionário = vendas_funcionario*2
elif vendas_funcionario > 5000:
    bonus_funcionário = (vendas_funcionario*2) + 1000
elif vendas_funcionario<1000:
    print(f"\n {Negrito}O funcionário{Reset} {Vermelho}Não{Reset} {Negrito}obteve pelo menos 1000 vendas! ❌{Reset}")
    bonus_funcionário = 0

print(f"\n {Negrito}O Bônus do funcionário foi de:{Reset} {Verde}R${Reset}{bonus_funcionário}{Reset}")


#4:
from cores import(Negrito,Reset,Verde)
vendas = [
    [10, 20, 100, 80, 90, 100, 20, 30, 44, 55, 33, 34, 100, 90, 80, 39, 87, 45, 50, 50, 50, 50, 40, 30, 3, 93, 39, 49, 88],    
    [100, 1, 1, 4, 5, 90, 100, 20, 4, 5, 100, 100, 100, 100, 100, 93, 20, 15, 40, 90, 90, 90, 90, 90, 90, 33, 22, 44, 43, 34]
    ]

print(f"\n {Negrito}A soma das vendas do 1º vendedor foi de:{Reset} {Verde}R${Reset}{sum(vendas[0])}")
print(f"\n {Negrito}A soma das vendas do 2º vendedor foi de:{Reset} {Verde}R${Reset}{sum(vendas[1])}")

if (sum(vendas[0]) > sum(vendas[1])):
    print(f"\n {Negrito}O 1º vendedor vendeu mais! {Reset}")
else:
    print(f"\n {Negrito}O 2º vendedor vendeu mais! {Reset}")