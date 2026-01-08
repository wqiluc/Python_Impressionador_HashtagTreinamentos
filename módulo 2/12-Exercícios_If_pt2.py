from cores import (Azul, Magenta, AmareloClaro, Reset, Negrito,Vermelho,Verde)

print(f"""
{Azul}{Negrito}EXERCÍCIO – SISTEMA DE CONTROLE DE ESTOQUE 🕹️📦{Reset}

{Magenta}
Neste exercício, você irá criar um mini sistema
para controle de estoque de um centro de distribuição.
{Reset}

{AmareloClaro}Objetivo:{Reset}
- Verificar se a quantidade em estoque de um produto
  está abaixo do mínimo permitido para sua categoria
- Caso esteja abaixo, avisar o time de compras

{AmareloClaro}Categorias e Estoque Mínimo:{Reset}
- alimentos → 50 unidades
- bebidas → 75 unidades
- limpeza → 30 unidades

{Magenta}
O programa deve solicitar ao usuário (inputs):
- Nome do produto ✅
- Categoria do produto ✅
- Quantidade atual em estoque ✅
{Reset}

{Magenta}
Regras importantes:
- Se o estoque estiver abaixo do mínimo da categoria,✅
  exibir uma mensagem solicitando reposição 
- Caso alguma informação não seja preenchida,
  exibir uma mensagem de aviso ✅
- Utilize int() para converter a quantidade informada ✅
{Reset}
""")

print(f"{Azul}{Negrito}SEU CÓDIGO–RESPOSTA AQUI ⬇️{Reset}")

alimento = 50
bebida = 75
limpeza = 35

nome_produto = str(input(f"\n {Negrito}Digite o Nome do Produto: {Reset}")).strip()
while (nome_produto == "" or nome_produto==" "):
    print(f"{Vermelho}Termo: 'Nome do Produto' vazio.❌ Digite novamente {Reset}")
    nome_produto = str(input(f"\n {Negrito}Digite o Nome do Produto: {Reset}")).strip()

categoria_produto = str(input(f"\n {Negrito}Digite a Categoria do Produto: {Reset}")).strip().lower()
while categoria_produto == "" or categoria_produto == " " or categoria_produto not in ["comida", "bebida", "limpeza"]:
    print(f"{Vermelho}Termo: 'Categoria do Produto' vazio ou errado.❌ Digite novamente {Reset}")
    categoria_produto = str(input(f"\n {Negrito}Digite a Categoria do Produto: {Reset}")).strip().lower()

estoque_produto = str(input(f"\n {Negrito}Digite quanto do produto: {categoria_produto} tem em estoque: {Reset}"))
while estoque_produto == "":
    print(f"{Vermelho}Termo: 'Quantidade em Estoque' vazio.❌ Digite novamente {Reset}")
    estoque_produto = str(input(f"\n {Negrito}Digite quanto do produto: {categoria_produto} tem em estoque: {Reset}"))

estoque_produto = int(estoque_produto)

while estoque_produto <= 0:
    print(f"{Vermelho}Estoque Vazio{Reset}")
    estoque_produto = int(input(f"\n {Negrito}Digite quanto do produto: {categoria_produto} tem em estoque: {Reset}"))

if categoria_produto == "comida" or categoria_produto=="alimento":
    if estoque_produto < alimento:
        print(f"{Vermelho}Estoque de {categoria_produto} Insuficiente ❌. É necessário ordenar{Reset} + {alimento-estoque_produto}{Reset}{Vermelho} desse produto {Reset}\n")
    else:
        print(f"{Verde}Estoque de {categoria_produto} Preenchido ✅👍{Reset}\n")

elif categoria_produto == "bebida":
    if estoque_produto < bebida:
        print(f"{Vermelho}Estoque de {categoria_produto} Insuficiente ❌ É necessário ordenar {Reset}+ {bebida-estoque_produto}{Reset}{Vermelho} desse produto {Reset}\n")
    else:
        print(f"{Verde}Estoque de {categoria_produto} Preenchido ✅👍{Reset}")

elif categoria_produto == "limpeza":
    if estoque_produto < limpeza:
        print(f"{Vermelho}Estoque de {categoria_produto} Insuficiente ❌ É neceesário ordenar {Reset}+ {limpeza-estoque_produto}{Reset}{Vermelho} desse produto {Reset}\n")
    else:
        print(f"{Verde}Estoque de {categoria_produto} Preenchido ✅👍{Reset}\n")