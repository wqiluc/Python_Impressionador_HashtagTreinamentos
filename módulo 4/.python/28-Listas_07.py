from cores import (Reset, Amarelo, Azul, Magenta)

print(f"""
{Azul}==================== LISTAS EM PYTHON — PARTE 07 🖨️📋 ===================={Reset}

{Magenta}Print de listas:{Reset}

Existem duas formas principais de imprimir listas:

------------------------------------------------------------

{Magenta}Opção 1 — Print normal:{Reset}

{Amarelo}print(lista){Reset}

Exibe a lista inteira, com colchetes e vírgulas.

Exemplo:
['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']

------------------------------------------------------------

{Magenta}Opção 2 — Método join:{Reset}

{Amarelo}texto.join(lista){Reset}

Transforma a lista em um texto único, usando um separador.

Exemplo:
{Amarelo}', '.join(produtos){Reset}

Resultado:
apple tv, mac, iphone x, iphone 11, ipad, apple watch, mac book, airpods

------------------------------------------------------------

{Magenta}Exemplo de lista:{Reset}

produtos = ['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']

------------------------------------------------------------

{Magenta}Lembrando o método split de strings:{Reset}

{Amarelo}lista = texto.split(separador){Reset}

Exemplo:
texto = 'apple tv, mac, iphone x, iphone 11, ipad, apple watch, mac book, airpods'

{Amarelo}texto.split(', '){Reset}

Resultado:
['apple tv', 'mac', 'iphone x', 'iphone 11', 'ipad', 'apple watch', 'mac book', 'airpods']

------------------------------------------------------------

{Magenta}Resumo:{Reset}

{Amarelo}join(){Reset} {Azul}→{Reset} lista para texto  
{Amarelo}split(){Reset} {Azul}→{Reset} texto para lista
""")
