from cores import (Reset,Amarelo,Azul,Magenta)

print(f"""
{Azul}==================== LISTAS EM PYTHON ✅📋 ===================={Reset}

{Magenta}Estrutura de uma Lista:{Reset}
{Amarelo}lista = [valor, valor, valor, valor, ...]{Reset}

{Magenta}O que é uma lista?{Reset}
Lista é um dos objetos mais importantes do Python.  
Ela serve para armazenar vários valores dentro de uma única variável.

Quando importamos uma base de dados para o Python, normalmente os dados
são carregados como uma {Amarelo}lista{Reset} ou alguma variação de lista.

Listas foram feitas para serem {Amarelo}homogêneas{Reset}, mas aceitam
valores de tipos diferentes (heterogêneas).

------------------------------------------------------------

{Magenta}Exemplo — Lista de produtos de uma loja:{Reset}

{Amarelo}produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']{Reset}

Cada item da lista ocupa uma posição (índice):
{Amarelo}produtos[0]{Reset} → 'tv'  
{Amarelo}produtos[1]{Reset} → 'celular'  
{Amarelo}produtos[2]{Reset} → 'mouse'  
{Amarelo}produtos[3]{Reset} → 'teclado'  
{Amarelo}produtos[4]{Reset} → 'tablet'

------------------------------------------------------------

{Magenta}Exemplo — Quantidade vendida de cada produto:{Reset}

{Amarelo}vendas = [1000, 1500, 350, 270, 900]{Reset}

A posição do número corresponde à posição do produto:
{Amarelo}produtos[0]{Reset} → 'tv'      → {Amarelo}vendas[0]{Reset} → 1000  
{Amarelo}produtos[1]{Reset} → 'celular' → {Amarelo}vendas[1]{Reset} → 1500  
{Amarelo}produtos[2]{Reset} → 'mouse'   → {Amarelo}vendas[2]{Reset} → 350  
{Amarelo}produtos[3]{Reset} → 'teclado' → {Amarelo}vendas[3]{Reset} → 270  
{Amarelo}produtos[4]{Reset} → 'tablet'  → {Amarelo}vendas[4]{Reset} → 900

------------------------------------------------------------

{Magenta}Importante:{Reset}
O índice de listas em Python sempre começa em {Amarelo}0{Reset}.
O último elemento é sempre {Amarelo}len(lista) - 1{Reset}.
""")
