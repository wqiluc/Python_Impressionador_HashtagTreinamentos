from cores import (Reset, Amarelo, Azul, Magenta,Vermelho,Verde)

print(f"""
{Azul}==================== LISTAS EM PYTHON — PARTE 06 🔗📊 ===================={Reset}

{Magenta}Juntar listas: (🔁){Reset}

Duas formas de juntar {Amarelo}listas{Reset}:

{Amarelo}lista1.extend(lista2){Reset}  
Adiciona todos os itens da segunda lista dentro da primeira.

{Amarelo}lista_nova = lista1 + lista2{Reset}  
Cria uma nova lista unindo as duas.

{Azul}Obs:{Reset}  
{Amarelo}.append(){Reset} {Vermelho}não junta{Reset} {Amarelo}listas{Reset}, ele adiciona a lista inteira como um único elemento.

------------------------------------------------------------

{Magenta}Exemplo: {Reset}

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']  
novos_produtos = ['iphone 12', 'ioculos']

{Amarelo}produtos.extend(novos_produtos){Reset}  
Ou  
{Amarelo}todos = produtos + novos_produtos{Reset}

------------------------------------------------------------

{Magenta}❌ Cuidado com tipos de dados: {Reset}

{Amarelo}[1] + [2]{Reset} {Azul}→{Reset} [1, 2]  
{Amarelo}1 + 2{Reset} {Azul}→{Reset} 3  

{Verde}Sempre{Reset} verifique se você está trabalhando com listas ou com números.✅

------------------------------------------------------------

{Magenta}Exemplo com vendas: {Reset}

vendas = [1000, 1500, 15000, 20000, 270, 900, 100, 1200]  
vendas_iphonex = [15000]  
vendas_iphone11 = [20000]

{Amarelo}vendas_iphonex + vendas_iphone11{Reset} {Azul}→{Reset} [15000, 20000]

------------------------------------------------------------

{Magenta}Ordenar listas:{Reset}

{Amarelo}lista.sort(){Reset}  
Organiza a lista em ordem crescente.

Exemplo:
{Amarelo}vendas.sort(){Reset}

{Vermelho}Antes{Reset}: [1000, 1500, 15000, 20000, 270, 900, 100, 1200]
{Verde}Depois{Reset}: [100, 270, 900, 1000, 1200, 15000, 20000]""")