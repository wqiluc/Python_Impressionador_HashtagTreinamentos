# Vamos criar uma function com parâmetro
#
# Digamos que estamos criando um programa para categorizar os produtos
# de uma revendedora de bebidas.
#
# Cada produto tem um código.
# O tipo de produto é dado pelas 3 primeiras letras do código.
#
# Exemplos:
# Vinho    -> BEB12302
# Cerveja -> BEB12043
# Vodka   -> BEB34501
#
# Guaraná -> BSA11104
# Coca    -> BSA54301
# Sprite  -> BSA34012
# Água    -> BSA09871
#
# Repare que:
# - Bebidas alcoólicas começam com "BEB"
# - Bebidas não alcoólicas começam com "BSA"
#
# Crie um programa que analise uma lista de produtos e envie instruções
# para a equipe de estoque dizendo quais produtos devem ser enviados
# para a área de bebidas alcoólicas

from cores import(Negrito,Reset)

produtos = ['BEB46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

produtos_BEB = list()

for indice_produto, (produto) in (enumerate(produtos)):
    if (produto.startswith("BEB")):
        produtos.remove(produto)
        produtos_BEB.append(produto)
for indice_bebidas_nao_alcoolicas, (bebidas_nao_alcoolicas) in (enumerate(produtos)): 
    print(f"\n {Negrito}{indice_bebidas_nao_alcoolicas+1}º Produto não-alcóolico: {bebidas_nao_alcoolicas[0:]}{Reset}")

for indice_bebidas_alcoolicas, (bebidas_alcoolicas) in (enumerate(produtos_BEB)):
    print(f"\n {Negrito}{indice_bebidas_alcoolicas+1}º Produto alcóolico: {bebidas_alcoolicas[0:]}{Reset}")