from cores import Azul, Magenta, Amarelo, Verde, Reset, Negrito

vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

joao_ipad = vendas[1][0]
diego_iphone = vendas[2][1]
total_iphone = sum([linha[1] for linha in vendas])


print(f"\n{Azul}=========== LISTAS DE LISTAS — EXEMPLO PRÁTICO 📘 =========== {Reset}\n")


print(f"\n{Azul}{Negrito}📊 RESULTADOS DAS VENDAS 📊{Reset}")
print(f"{Magenta}João vendeu de iPad:{Reset} {Verde}{joao_ipad}{Reset}")
print(f"{Magenta}Diego vendeu de iPhone:{Reset} {Verde}{diego_iphone}{Reset}")
print(f"{Magenta}Total de vendas de iPhone:{Reset} {Verde}{total_iphone}{Reset}\n")

vendas[0][1] = 50

print(f"{Azul}{Negrito}✏️ ALTERAÇÃO DE DADOS (LIRA){Reset}")
print(f"{Magenta}Nova venda de iPhone de Lira:{Reset} {Verde}{vendas[0][1]}{Reset}\n")

produtos.append('mac')
for macOS in range(len(vendas)):
    vendas[macOS].append(0)

print(f"{Azul}{Negrito}🆕 NOVO PRODUTO ADICIONADO ✚ {Reset}")
print(f"{Magenta}Produtos atuais:{Reset} {Amarelo}{produtos}{Reset}")
print(f"{Magenta}Nova tabela de vendas:{Reset} {Amarelo}{vendas}{Reset}\n")
