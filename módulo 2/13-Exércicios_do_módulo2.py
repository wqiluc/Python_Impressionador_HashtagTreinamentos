#EXÉRCICIOS NO .PY - módulo 2

#1 = compara o maior de 2 números:
from cores import (Negrito,Reset,Amarelo)

numero1 = int(input(f"\n {Negrito}Digite o 1º número: {Reset}"))
numero2 = int(input(f"\n {Negrito}Digite o 2º número: {Reset}"))

if (numero1>numero2):
    print(f"{Amarelo}O maior número é o número1 = {numero1}{Reset}")
else:
    print(f"{Amarelo}O maior número é o número2 = {numero2}{Reset}")

#2 = Valor + ou - :
from cores import(Negrito,Reset, Vermelho,Verde,Amarelo)

numero = int(input(f"\n {Negrito}Digite um número: {Reset}"))
if (numero>0):
    print(f"{Verde}O número: +{numero} é positivo!✅{Reset}")
elif (numero<0):
    print(f"\n {Vermelho}O número: -{numero1} é negativo!❌{Reset}")
else:
    print(f"\n {Amarelo}O número é = {numero}, ou seja, neutro!{Reset}")

#3 = Analisador de Estado Cívil 💍❌😥:
estado_civil = str(input(f"""
{Negrito}Digite o seu estado civil:{Reset}
C = Casado(a) 💍
S = Solteiro(a) 🙅🏻‍♂️🙅🏻‍♀️
V = Viúvo(a) 😥
O = Outro(os)""")).strip().upper()

if estado_civil == "C":
    print(f"{Negrito}Você é casado(a)! 💍{Reset}")
elif estado_civil == "S":
    print(f"{Negrito}Você é solteiro(a)! 😎{Reset}")
elif estado_civil == "V":
    print(f"{Negrito}Você é viúvo(a)! 😥{Reset}")
elif estado_civil == "O":
    print(f"{Negrito}Você escolheu outro estado civil{Reset}")
else:
    print(f"{Negrito}Opção inválida ❌{Reset}")

#4 = Válida E-mails spam ❌:
from cores import(Negrito,Reset,Vermelho)
emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"

email_usuario = str(input(f"\n {Negrito}Digite seu E-mail: {Reset}")).strip().lower()

if email_usuario in ["fulano@gmail.com", "eltrano@gmail.com", "ciclano@gmail.com"]:
    print(f"{Vermelho}E-mail: {email_usuario} é SPAM❌{Reset}")
else:
    print(f"{Verde}E-mail: {email_usuario} é Válido!! ✅{Reset}")
    pass

#5 = Situação Acadêmica📚:
from cores import(Negrito,Reset, Vermelho,Amarelo,Verde)

nota1 = float(input(f"\n {Negrito}Digite a nota da 1º unidade do aluno: {Reset}"))
nota2 = float(input(f"\n {Negrito}Digite a nota da 2º unidade do aluno: {Reset}"))

media = (nota1+nota2) / 2

if media < 7:
    print(f"{Vermelho}Reprovado ❌ | Média: {media:.2f}{Reset}")
elif media == 10:
    print(f"{Amarelo}Aprovado com distinção ✅🏆 | Média: {media:.2f}{Reset}")
else:
    print(f"{Verde}Aprovado ✅ | Média: {media:.2f}{Reset}")

#6 = Maior orçamento entre 3 empresas 🏦:
from cores import (Negrito,Reset, Azul,Verde,Amarelo)

empresa1 = float(input(f"{Negrito}Digite o orçamento da empresa 1:{Reset} {Verde}R$:{Reset}"))
empresa2 = float(input(f"{Negrito}Digite o orçamento da empresa 2:{Reset} {Verde}R$:{Reset}"))
empresa3 = float(input(f"{Negrito}Digite o orçamento da empresa 3:{Reset} {Verde}R$:{Reset}"))

if (empresa1 > empresa2 and empresa1 > empresa3):
    print(f"{Azul}🏆 Empresa 1 possui o maior orçamento:{Reset} {Verde}R$ {empresa1:.2f}{Reset}")
elif (empresa2 > empresa1 and empresa2 > empresa3):
    print(f"{Azul}🏆 Empresa 2 possui o maior orçamento:{Reset} {Verde}R$ {empresa2:.2f}{Reset}")
elif (empresa3 > empresa1 and empresa3 > empresa2):
    print(f"{Azul}🏆 Empresa 3 possui o maior orçamento:{Reset} {Verde}R$ {empresa3:.2f}{Reset}")
else:
    print(f"{Amarelo}🤝 Há empate entre os orçamentos das empresas!{Reset}")

#7 = Menor orçamento entre 3 empresas 🏦:
from cores import (Negrito, Reset, Azul, Verde)

empresa1 = float(input(f"{Negrito}Digite o orçamento da empresa 1:{Reset} {Verde}R$:{Reset}"))
empresa2 = float(input(f"{Negrito}Digite o orçamento da empresa 2:{Reset} {Verde}R$:{Reset}"))
empresa3 = float(input(f"{Negrito}Digite o orçamento da empresa 3:{Reset} {Verde}R$:{Reset}"))

if empresa1 < empresa2 and empresa1 < empresa3:
    print(f"{Azul}📉 Empresa 1 possui o menor orçamento:{Reset} {Verde}R$ {empresa1:.2f}{Reset}")
elif empresa2 < empresa1 and empresa2 < empresa3:
    print(f"{Azul}📉 Empresa 2 possui o menor orçamento:{Reset} {Verde}R$ {empresa2:.2f}{Reset}")
elif empresa3 < empresa1 and empresa3 < empresa2:
    print(f"{Azul}📉 Empresa 3 possui o menor orçamento:{Reset} {Verde}R$ {empresa3:.2f}{Reset}")
else:
    print(f"{Verde}🤝 Há empate entre os menores orçamentos!{Reset}")

#8 = Produto mais Barato💰📦:
from cores import (Negrito, Reset, Azul, Verde)

produto1 = float(input(f"{Negrito}Digite o preço do produto 1:{Reset} {Verde}R$:{Reset}"))
produto2 = float(input(f"{Negrito}Digite o preço do produto 2:{Reset} {Verde}R$:{Reset}"))
produto3 = float(input(f"{Negrito}Digite o preço do produto 3:{Reset} {Verde}R$:{Reset}"))

if produto1 < produto2 and produto1 < produto3:
    print(f"{Azul}🛒 O produto 1 compensa mais comprar! 💸 Preço:{Reset} {Verde}R$ {produto1:.2f}{Reset}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"{Azul}🛒 O produto 2 compensa mais comprar! 💸 Preço:{Reset} {Verde}R$ {produto2:.2f}{Reset}")
elif produto3 < produto1 and produto3 < produto2:
    print(f"{Azul}🛒 O produto 3 compensa mais comprar! 💸 Preço:{Reset} {Verde}R$ {produto3:.2f}{Reset}")
else:
    print(f"{Verde}🤝 Os três produtos têm o mesmo preço! Vale a pena comprar qualquer um 😄{Reset}")

#9 = 3 números em ordem descrescente (maior > menor ....) :
from cores import (Negrito, Reset)

numero1 = int(input(f"\n {Negrito}Digite o 1º número: {Reset}"))
numero2 = int(input(f"\n {Negrito}Digite o 2º número: {Reset}"))
numero3 = int(input(f"\n {Negrito}Digite o 3º número: {Reset}"))

if (numero1 >= numero2 and numero2 >= numero3):
    print(f"{Negrito}{numero1} > {numero2} > {numero3}{Reset}")
elif (numero1 >= numero3 and numero3 >= numero2):
    print(f"{Negrito}{numero1} > {numero3} > {numero2}{Reset}")
elif (numero2 >= numero1 and numero1 >= numero3):
    print(f"{Negrito}{numero2} > {numero1} > {numero3}{Reset}")
elif (numero2 >= numero3 and numero3 >= numero1):
    print(f"{Negrito}{numero2} > {numero3} > {numero1}{Reset}")
elif (numero3 >= numero1 and numero1 >= numero2):
    print(f"{Negrito}{numero3} > {numero1} > {numero2}{Reset}")
else:
    print(f"{Negrito}{numero3} > {numero2} > {numero1}{Reset}")

#10 = Turno Escolar ☀️🌤️🌙🏫: 
from cores import(Negrito,Reset,Vermelho)

turno = str(input("""
    Digite o seu turno:
    M = Matutino☀️
    V = Vespertino🌤️
    N = Noturno 🌙
""")).strip().upper()

if (turno=="M"):
    print(f"{Negrito}Você estuda no turno Matutino!☀️ Bom DIA:){Reset}")
elif (turno=="V"):
     print(f"{Negrito}Você estuda no turno Vespertino!🌤️ Boa TARDE:){Reset}")
elif (turno == "N"):
      print(f"{Negrito}Você estuda no turno Noturno!🌙 Boa NOITE:){Reset}")
else:
     print(f"{Vermelho}Turno Inválido!! ❌{Reset}")