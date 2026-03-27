(f"""### Sua empresa resolveu pagar uma bonificação 
de R$1.000 para todos os funcionários 
com mais de 20 anos de casa. 
Quanto vai custar a ação de bonificação para a sua empresa?
""")

from cores import *

anos_casa_funcionarios = [10, 15, 20, 25, 30, 47, 2, 5, 5, 6, 18, 32, 10, 1, 1, 2, 3, 3, 2, 1, 10, 40, 21, 10, 1, 2, 5, 7, 7, 6, 9, 19]
valor_funcionarios_20_anos = [ ]

# seu código aqui👇:
for indice_ano, (ano) in enumerate(anos_casa_funcionarios):
    valor = 1000
    if ano>20:
        print(f"{Negrito}{indice_ano+1}º Funcionário: {ano} anos na empresa! Receberá uma bonificação de:{Reset} {Verde}R${Reset}{Negrito}{valor:.2f}{Reset}")
        valor_funcionarios_20_anos.append(valor)

print(f"\n{Negrito}O valor TOTAL que a empresa terá que pagar será de:{Reset} {Verde}R${Reset}{Negrito}{sum(valor_funcionarios_20_anos)}")