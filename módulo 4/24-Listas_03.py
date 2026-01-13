from cores import (Reset,Amarelo,Azul,Magenta)

print(f"""
{Azul}==================== LISTAS EM PYTHON — PARTE 03 ✅📋 ===================={Reset}

{Magenta}Como descobrir o índice de um item em uma lista:{Reset}
{Amarelo}i = lista.index('item'){Reset}

Retorna o índice (posição) onde o item está dentro da lista.

------------------------------------------------------------

{Magenta}Exemplo de base de dados:{Reset}

produtos = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque  = [100 ,   150    ,   100   ,   120  ,    70     ,    180      ,   80  ]

Cada produto ocupa a mesma posição que seu valor de estoque.

------------------------------------------------------------

{Magenta}Como descobrir o estoque de um produto:{Reset}

{Amarelo}i = produtos.index('geladeira'){Reset}  
{Amarelo}estoque[i]{Reset} {Azul}→{Reset} 180

Ou seja:
{Amarelo}produtos[5]{Reset} {Azul}→{Reset} 'geladeira'  
{Amarelo}estoque[5]{Reset} {Azul}→{Reset} 180

------------------------------------------------------------

{Magenta}Consulta de estoque (lógica):{Reset}

1) O usuário informa o nome do produto  
2) O programa verifica se o produto existe na lista  
3) Se não existir, mostra uma mensagem de erro  
4) Se existir, usa {Amarelo}index(){Reset} para encontrar o índice  
5) Mostra o valor correspondente na lista de {Amarelo}estoque{Reset}

------------------------------------------------------------

{Magenta}Fluxo do programa:{Reset}

produto = input("Digite o produto: ").lower()

Se {Amarelo}produto not in produtos{Reset}  
{Azul}→{Reset} "Produto não encontrado"

Se existir:
{Amarelo}i = produtos.index(produto){Reset}  
{Amarelo}quantidade = estoque[i]{Reset}

Exibir:
"O produto X possui Y unidades em estoque" """)
