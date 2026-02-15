(f"""Desenvolva um programa que armazene
quatro notas em uma lista e que apresente: 
a média final, 
a maior nota e 
a menor nota""")

#solução:👇
from cores import *

lista_notas = list()
notas = 4

for indice_nota in range(notas):
    nota = str(input(f"{Negrito}Digite a {indice_nota+1}º nota: {Reset}")).strip()
    while not (nota.replace(".","").replace(",","").isdigit()):
        print(f"{Vermelho}Termo Inválido!! Digite uma NOTA (int/float){Reset}")
        nota = str(input(f"{Negrito}Digite a {indice_nota+1}º nota: {Reset}")).strip()
    nota = float(nota)
    lista_notas.append(nota)

print(lista_notas)
print(f"{Negrito}A MAIOR nota da lista é:{Reset} {Verde}{max(lista_notas)}{Reset}")
print(f"{Negrito}A MENOR nota da lista é:{Reset} {Vermelho}{min(lista_notas)}{Reset}")