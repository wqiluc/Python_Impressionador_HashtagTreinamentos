(f"""
Você recebeu uma lista de alunos da Arroba Treinamentos 
e precisa descobrir quantos alunos e quais aluno 
estão devendo ainda algum pagamento do curso. 
O curso custa 2.000 reais e os pagamentos dos alunos 
são representados por uma lista de valores 
já pagos no dicionário de alunos """)

#resolução:
from cores import *

pagamentos_alunos = {
    "André": [2000],
    "Fulano": [1000, 1000],
    "Ciclano": [500, 500],
    "Beltrano": [100], 
    "João": [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    "Amanda": [200, 300, 250, 250, 500, 400, 100],
    "Lira": [1000],
    "Alon": [10]
}

for indice_pagamentos, indice_dicionario in enumerate(pagamentos_alunos.items()):
    if (sum(indice_dicionario[1])<2000):
        print(f"\n{Negrito}{indice_pagamentos+1}º Aluno - Nome:{Reset} {Amarelo}'{indice_dicionario[0].capitalize()}'{Reset}{Negrito} - Valor Pago:{Reset} {Verde}R${Reset}{Negrito}{sum(indice_dicionario[1]):.2f}{Reset}")

print(f"\n{Negrito}Esses alunos devem ser informados que o pagamento total ainda não foi realizado, \ne cobrar o respectivo valor (R$💵){Reset}\n\n")