from cores import (Negrito,Reset,Amarelo,Azul,Magenta,Vermelho,Verde)

print(f"""
{Azul} ==================== LISTAS EM PYTHON — PARTE 04 ✅📋 ===================={Reset}

{Magenta}Adicionar e remover itens de uma lista:{Reset}

{Magenta}Adicionar:{Reset}
{Amarelo}lista.append(item){Reset}  
Adiciona um novo item no final da lista.

{Magenta}Remover:{Reset}
{Amarelo}item_removido = lista.pop(indice){Reset}  
{Vermelho}Remove{Reset} {Negrito}o item da posição indicada e retorna o valor removido.{Reset}

{Amarelo}lista.remove(item){Reset}  
{Vermelho}Remove{Reset} {Negrito}o item pelo valor informado.{Reset}

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

Existem duas formas de evitar {Vermelho}erros{Reset}:

{Verde}1) Verificar antes ✅{Reset}:
{Amarelo}if item in lista:{Reset}
    {Amarelo}lista.remove(item){Reset}

{Verde}2) Usar tratamento de erro ✅{Reset}:
{Amarelo}try:{Reset}
    {Amarelo}lista.remove(item){Reset}
{Amarelo}except:{Reset}
    {Vermelho}Mostrar mensagem de erro{Reset}

------------------------------------------------------------

{Magenta}Quando usar cada um:{Reset}

Use {Amarelo}if in{Reset} quando você quer evitar o erro.  
Use {Amarelo}try / except{Reset} quando o erro pode acontecer e precisa ser tratado.
""")
