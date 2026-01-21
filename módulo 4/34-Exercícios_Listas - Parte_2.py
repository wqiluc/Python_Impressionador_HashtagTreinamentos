from cores import (Reset, Azul, Magenta, Amarelo,Verde)

print(f"""
{Azul}Exercícios — Listas | Mudança de Carga Tributária 🏛️ 🔨 {Reset}

{Magenta}Contexto: {Reset}
{Magenta}Reformas e mudanças de cargas tributárias são comuns no{Reset} {Verde}Brasil 🇧🇷{Reset}. 
{Magenta}Neste exercício, considera-se um cenário de ecommerce onde livros passam a ter 
um novo imposto de 10%, exigindo o reajuste do preço final e a apuração do impacto financeiro.{Reset}

{Magenta}Objetivo: {Reset}
{Magenta}Recalcular o preço de livros presentes na lista de produtos, repassando 
integralmente o imposto ao consumidor final e calculando o custo adicional gerado 
pela nova tributação para a empresa.{Reset}

{Magenta}Regras: {Reset}
{Magenta}• O imposto incide apenas sobre livros; 
• O reajuste é de 10% sobre o preço original; 
• O código deve funcionar mesmo que não existam livros na lista de produtos.{Reset}

{Magenta}Estrutura dos Dados: {Reset}
{Magenta}A lista de produtos contém os nomes dos itens. 
A lista produtos_ecommerce contém sublistas no formato:{Reset}
{Magenta}[quantidade_vendida_no_mês, preço_unitário]{Reset}

{Magenta}Funções Esperadas: {Reset}
{Amarelo}reajustar_preco_livros(){Reset}
{Magenta}Atualiza o preço dos livros aplicando a nova carga tributária.{Reset}

{Amarelo}calcular_impacto_imposto(){Reset}
{Magenta}Calcula o impacto financeiro total do imposto para a empresa.{Reset}""")

#Resolução:
from cores import(Negrito,Reset,VerdeClaro)
produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]]

if "livro" in produtos:
    for (quantidade, preco) in produtos_ecommerce:
        preco_novo = preco + (0.10 * preco)
        diferenca = preco_novo - preco

        print(f"\n{Negrito}Preços antigo:{Reset} {VerdeClaro}R${Reset}{Negrito}{preco}{Reset}")
        print(f"{Negrito}Preços Novo:{Reset} {VerdeClaro}R${Reset}{Negrito}{preco_novo}{Reset}")

        print(f"\n{Negrito}A diferença de{Reset}: {VerdeClaro}R${Reset}{Negrito}{diferenca:.0f}{Reset}")

        print(f"\n{Negrito}O total de imposto, após o reajuste; será de:{Reset} "
            f"{VerdeClaro}R${Reset}{Negrito}{preco_novo * quantidade:.2f}{Reset}")
else:
    pass