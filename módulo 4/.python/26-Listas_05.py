from cores import (Reset, Amarelo, Azul, Magenta,Verde,Vermelho)

print(f"""
{Azul}==================== LISTAS EM PYTHON — PARTE 04 ➕➖ ======================= {Reset}

{Magenta}Adicionar e remover itens de uma lista:{Reset} {Verde}(+){Reset}

{Magenta}Adicionar:{Reset}
{Amarelo}lista.append(item){Reset}  
{Verde}Adiciona{Reset} um novo item no final da lista.

{Magenta}Remover:{Reset}
{Amarelo}item_removido = lista.pop(indice){Reset}  
{Vermelho}Remove{Reset} o item pela posição e retorna o valor removido.

{Amarelo}lista.remove(item){Reset}  
{Vermelho}Remove{Reset} o item pelo nome do item.

------------------------------------------------------------

{Magenta}Exemplo — Controle de produtos da Apple:{Reset}

produtos = ['apple tv', 'mac', 'iphone x', 'ipad', 'apple watch', 'mac book', 'airpods']

A Apple lançou o {Amarelo}iphone 11{Reset}  
E irá remover o {Amarelo}iphone x{Reset}

{Amarelo}produtos.append('iphone 11'){Reset}  
{Amarelo}produtos.remove('iphone x'){Reset}

Agora a lista fica:
['apple tv', 'mac', 'ipad', 'apple watch', 'mac book', 'airpods', 'iphone 11']

------------------------------------------------------------

{Magenta}Tratando erros ao remover itens:{Reset}

Existem duas formas de tratar erros:

{Verde}1) Evitar o erro ✅{Reset}:
{Amarelo}if item in lista:{Reset}  
{Azul}→{Reset} {Amarelo}lista.remove(item){Reset}

{Verde}2) Tratar o erro ✅{Reset}:
{Amarelo}try:{Reset}  
    {Amarelo}lista.remove(item){Reset}  
{Amarelo}except:{Reset}  
    {Vermelho}Mostrar mensagem de erro ❌{Reset}

------------------------------------------------------------

{Magenta}Quando usar cada um{Reset} {Amarelo}?{Reset}

{Verde}Use{Reset}: {Amarelo}if{Reset} {Azul}in{Reset} quando quiser evitar o {Vermelho}erro{Reset}.  
{Verde}Use{Reset}: {Amarelo}try{Reset} / {Vermelho}except{Reset} quando o {Vermelho}erro{Reset} {Amarelo}pode{Reset} acontecer.""")