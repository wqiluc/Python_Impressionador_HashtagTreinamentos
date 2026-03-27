(f"""
 Desenvolva um programa que armazene quatro notas em uma lista 
e que apresente a média final. 
Caso a média seja igual ou superior a 7,
apresentar a mensagem 'APROVADO', caso contrário, 
armazenar a nota da prova final e recalcular a média (nova média = (antiga média + prova final) / 2). 
Caso a nova média seja igual superior a 5, 
apresentar a mensagem 'APROVADO', caso contrário, 
apresentar a mensagem 'REPROVADO' """)

# seu código aqui:
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
maior_nota = (max(lista_notas))
menor_nota = (min(lista_notas))
media = (sum(lista_notas)/len(lista_notas))

print(f"{Negrito}A MAIOR nota da lista é:{Reset} {Verde}{maior_nota}{Reset}")
print(f"{Negrito}A MENOR nota da lista é:{Reset} {Vermelho}{menor_nota}{Reset}")
print(f"{Negrito}A MÉDIA das nota da lista é:{Reset} {Azul}{media:.2f}{Reset}")

if (media>=7):
    print(f"{Negrito}Aluno{Reset} {Verde}APROVADO POR MÉDIA!! ✅{Reset}")
else:
    nova_media = (media + lista_notas[3])/2
    print(f"{Negrito}A nova média é = {media}+{lista_notas[3]}/2.0 = {nova_media}{Reset}")
    if (nova_media>=5):
        print(f"{Negrito}Aluno{Reset} {Verde}APROVADO!✅{Reset}{Amarelo} PELA RECUPERAÇÃO FINAL⚠️{Reset}")
    else:
        print(f"{Negrito}Aluno{Reset} {Vermelho}REPROVADO POR MÉDIA! ❌{Reset}")