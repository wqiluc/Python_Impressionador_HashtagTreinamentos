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

#11 = Salários e reajustes💰:
from cores import (Negrito,Reset,Verde)

bonus = 0

salario = float(input(f"\n {Negrito}Digite o salário do funcionário:{Reset} {Verde}R${Reset}"))

if (salario <280):
    bonus = salario + (0.20*salario)
    print(f"{Verde}Parábens!!✅💰 seu salário teve um aumento de 20%, ou seja: R${bonus-salario:.2f} a mais!. Agora ele passa a ser de: {bonus:.2f}{Reset}")
elif (salario>=280 and salario <700):
    bonus = salario + (0.15*salario)
    print(f"{Verde}Parábens!!✅💰 seu salário teve um aumento de 15%, ou seja: R${bonus-salario:.2f} a mais!. Agora ele passa a ser de: {bonus:.2f}{Reset}")
elif (salario>=700 and salario<1500):
    bonus = salario + (0.10*salario)
    print(f"{Verde}Parábens!!✅💰 seu salário teve um aumento de 10%, ou seja: R${bonus-salario:.2f} a mais!. Agora ele passa a ser de: {bonus:.2f}{Reset}")
else:
    bonus = salario + (0.05*salario)
    print(f"{Verde}Parábens!!✅💰 seu salário teve um aumento de 05%, ou seja: R${bonus-salario:.2f} a mais!. Agora ele passa a ser de: {bonus:.2f}{Reset}")

#12 = Folha de Pagamento 💸📃:
from cores import (Negrito, Reset, Verde)

salario = float(input(f"{Negrito}Digite o salário do funcionário:{Reset} {Verde}R${Reset}"))

inss = 0.10 * salario
fgts = 0.11 * salario

if (salario < 900):
    ir = 0
elif (salario < 1500):
    ir = 0.05 * salario
elif (salario < 2500):
    ir = 0.10 * salario
else:
    ir = 0.20 * salario

salario_liquido = salario - (ir + inss + fgts)

print(f"{Negrito}O seu salário BRUTO é de:{Reset} {Verde}R${salario:.2f}{Reset}, "
    f"{Negrito}no entanto, com o desconto do INSS de:{Reset} {Verde}R${inss:.2f}{Reset}, "
    f"o FGTS de:{Reset} {Verde}R${fgts:.2f}{Reset}, "
    f"{Negrito}e o Imposto de Renda de:{Reset} {Verde}R${ir:.2f}{Reset}."
    f"\n{Negrito}Teu salário LÍQUIDO será de:{Reset} {Verde}R${salario_liquido:.2f}{Reset}")

#13 = Dias da Semana 🗓️:
from cores import (Negrito,Reset,Vermelho)
contador = 0

numero_diadasemana = int(input(f"\n {Negrito}Digite um número: {Reset}"))
contador+=numero_diadasemana

if (numero_diadasemana==1):
    print(f"{Negrito}1 - Domingo{Reset}")
elif (numero_diadasemana==2):
    print(f"{Negrito}2 - Segunda-feira{Reset}")
elif (numero_diadasemana==3):
    print(f"{Negrito}3 - Terça-feira{Reset}")
elif (numero_diadasemana==4):
    print(f"{Negrito}4 - Quarta-feira{Reset}")
elif (numero_diadasemana==5):
    print(f"{Negrito}5 - Quinta-feira{Reset}")
elif (numero_diadasemana==6):
    print(f"{Negrito}6 - Sexta-feira{Reset}")
elif (numero_diadasemana==7):
    print(f"{Negrito}7 - Sábado{Reset}")
else:
    print(f"{Vermelho}Dia da semana inválido!! ❌ Digite um número de 1-7{Reset}")

#14 = Conceito de Média Aritmética Americano 🇺🇸:
from cores import (Negrito, Reset, Verde, Vermelho, AmareloClaro)

nota1 = float(input(f"{Negrito}Digite a 1ª nota do aluno: {Reset} "))
nota2 = float(input(f"{Negrito}Digite a 2ª nota do aluno: {Reset} "))

media = (nota1 + nota2) / 2

if media < 0 or media > 10:
    print(f"{Vermelho}{Negrito}Média inválida!{Reset}")
elif media >= 9:
    print(f"{Verde}{Negrito}Média: {media:.2f} → Conceito A 🌟{Reset}")
elif media >= 8:
    print(f"{Verde}{Negrito}Média: {media:.2f} → Conceito B 👍{Reset}")
elif media >= 7:
    print(f"{AmareloClaro}{Negrito}Média: {media:.2f} → Conceito C ⚠️{Reset}")
elif media >= 6:
    print(f"{AmareloClaro}{Negrito}Média: {media:.2f} → Conceito D ❌{Reset}")
else:
    print(f"{Vermelho}{Negrito}Média: {media:.2f} → Conceito F 🚫{Reset}")

#15 = Anos Bissextos🧭:
from cores import (Negrito,Reset,Verde,Vermelho)

ano_analisado = int(input(f"\n {Negrito}Digite um ano p computar no sistema: {Reset}"))

if (ano_analisado % 4 == 0 and ano_analisado % 100 !=0) or (ano_analisado %400 == 0):
    print(f"{Verde}O ano {ano_analisado} É BISSEXTO. ✅{Reset}")
else:
    print(f"{Vermelho}O ano {ano_analisado} NÃO É bissexto. ❌{Reset}")

#16 = Média Aritmética Brasileira 🇧🇷:
from cores import (Negrito, Reset, Verde, Vermelho, AmareloClaro)

nota1 = float(input(f"\n {Negrito}Digite a 1ª nota: {Reset} "))
nota2 = float(input(f"\n {Negrito}Digite a 2ª nota: {Reset} "))
nota3 = float(input(f"\n {Negrito}Digite a 3ª nota: {Reset} "))

media = (nota1 + nota2 + nota3) / 3

if media < 0 or media > 10:
    print(f"{Vermelho}{Negrito}Média inválida!{Reset}")
elif media >= 7:
    print(f"{Verde}{Negrito}Média: {media:.2f} → APROVADO ✅{Reset}")
elif media >= 5:
    print(f"{AmareloClaro}{Negrito}Média: {media:.2f} → RECUPERAÇÃO ⚠️{Reset}")
else:
    print(f"{Vermelho}{Negrito}Média: {media:.2f} → REPROVADO ❌{Reset}")

#17 = Pesca 🎣:
from cores import (Negrito,Reset,Verde)
RS_excedente = 0

quilo_peixe = int(input(f"\n {Negrito}Digite o peso puro do peixe (em Kg): {Reset}"))
valor_excedente = quilo_peixe-50
RS_excedente = 4 * valor_excedente

print(f"{Negrito}Como João pescou um peixe de: {quilo_peixe}Kg, e houve um excesso de: {valor_excedente} Kg no peso do animal (50 Kg máximo); \no valor cobrado pelo excesso será de:{Reset}\n{Verde} R${RS_excedente:.2f}{Reset}")

#18 = Caixa Eletrônico 🏧💰:
from cores import (Negrito, Reset, Verde, Vermelho)

valor = int(input(f"{Negrito}Digite o valor a ser sacado (R$):{Reset} "))

if valor > 0:
    if valor >= 100:
        notas_100 = valor // 100
        valor = valor % 100
        print(f"{Verde}R$100 x {notas_100}{Reset}")
    else:
        notas_100 = 0

    if valor >= 50:
        notas_50 = valor // 50
        valor = valor % 50
        print(f"{Verde}R$50 x {notas_50}{Reset}")
    else:
        notas_50 = 0

    if valor >= 10:
        notas_10 = valor // 10
        valor = valor % 10
        print(f"{Verde}R$10 x {notas_10}{Reset}")
    else:
        notas_10 = 0

    if valor >= 5:
        notas_5 = valor // 5
        valor = valor % 5
        print(f"{Verde}R$5 x {notas_5}{Reset}")
    else:
        notas_5 = 0

    if valor >= 1:
        notas_1 = valor
        print(f"{Verde}R$1 x {notas_1}{Reset}")
else:
    print(f"{Vermelho}{Negrito}Valor inválido! ❌{Reset}")

#19 = Perguntas de um Crime 🔪🩸:
from cores import (Negrito, Reset, Verde, AmareloClaro, Vermelho)

contador_sus = 0

p1 = input(f"\n {Negrito}Telefonou para a vítima? (s/n):{Reset} ").strip().upper()
if (p1 == "S"):
    contador_sus += 1

p2 = input(f"\n {Negrito}Esteve no local do crime? (s/n):{Reset} ").strip().upper()
if (p2 == "S"):
    contador_sus += 1

p3 = input(f"\n {Negrito}Mora perto da vítima? (s/n):{Reset} ").strip().upper()
if (p3 == "S"):
    contador_sus += 1

p4 = input(f"\n {Negrito}Devia para a vítima? (s/n):{Reset} ").strip().upper()
if (p4 == "S"):
    contador_sus += 1

p5 = input(f"\n {Negrito}Já trabalhou com a vítima? (s/n):{Reset} ").strip().upper()
if (p5 == "S"):
    contador_sus += 1

if contador_sus == 2:
    print(f"\n{AmareloClaro}{Amarelo}Classificação: SUSPEITA{Reset}")
elif contador_sus == 3 or contador_sus == 4:
    print(f"\n{Vermelho}{Vermelho}Classificação: CÚMPLICE{Reset}")
elif contador_sus == 5:
    print(f"\n{Vermelho}{Vermelho}Classificação: ASSASSINO{Reset}")
else:
    print(f"\n{Verde}{Negrito}Classificação: INOCENTE{Reset}")

#20 = Posto de Gasolina ⛽️🏎️:
from cores import (Negrito, Reset,Verde)

tipo = str(input("""
    Digite seu tipo de combustível: 
    A - Álcool; ou
    G - Gasolina.
""")).strip().upper()

litros = int(input(f"{Negrito}Quantos L de {tipo} são necessários? {Reset}"))

if (tipo == "A"):
    total = litros * 1.90
    if litros <= 20:
        total = total * 0.97
    else:
        total = total * 0.95
else:
    total = litros * 2.50
    if litros <= 20:
        total = total * 0.96
    else:
        total = total * 0.94

print(f"{Negrito}Valor a pagar:{Reset} {Verde}R${total:.2f}{Reset}")

#21 = Fruteira 🍓🍎:
from cores import(Negrito,Reset)
quilos_total = 0
rs_total = 0

quilo_maca = int(input(f"\n {Negrito}Digite o peso da Maçã (em Kg): {Reset}"))
quilo_morango = int(input(f"\n {Negrito}Digite o peso do Morango (em Kg): {Reset}"))

if(quilo_morango<=5):
    rsquilo_morango = 2.50*quilo_morango
else:
    rsquilo_morango = 2.20*quilo_morango

if(quilo_maca<=5):
    rsquilo_maca = 1.80*quilo_maca
else:
    rsquilo_maca = 1.50*quilo_maca

rs_total = rsquilo_maca+rsquilo_morango
quilos_total = quilo_maca+quilo_morango

if(quilos_total>8 or rs_total>25):
    desconto_rstotal = rs_total - (0.10*rs_total)
    print(f"{Negrito}Valor a pagar com desconto:{Reset} {Verde}R${desconto_rstotal:.2f}{Reset}")
else:
    print(f"{Negrito}Valor a pagar:{Reset} {Verde}R${rs_total:.2f}{Reset}")


# 22 = Açogue 🥩:
from cores import (Negrito, Reset)

print(f"""
{Negrito}Escolha o tipo de carne:{Reset}
1 - Filé Duplo
2 - Alcatra
3 - Picanha""")

opcao = int(input(f"{Negrito}Digite a opção desejada: {Reset}"))

if (opcao == 1):
    quilo = float(input(f"\n {Negrito}Digite o peso do Filé Duplo (em Kg): {Reset}"))
    if (quilo <= 5):
        total = 4.90 * quilo
    else:
        total = 5.80 * quilo

elif (opcao == 2):
    quilo = float(input(f"\n {Negrito}Digite o peso da Alcatra (em Kg): {Reset}"))
    if (quilo <= 5):
        total = 5.90 * quilo
    else:
        total = 6.80 * quilo

elif (opcao == 3):
    quilo = float(input(f"\n {Negrito}Digite o peso da Picanha (em Kg): {Reset}"))
    if (quilo <= 5):
        total = 6.90 * quilo
    else:
        total = 7.80 * quilo

pagamento = int(input(f"""
💳 {Negrito}Escolha o método de pagamento:{Reset}

1️⃣ Dinheiro 💵
2️⃣ Cartão 💳

👉 Digite a opção desejada: """))

if (pagamento) == 2: # Cartão 💳
    total = total - (0.05 * total)
    print(f"\n✅💳 {Negrito}Pagamento no cartão{Reset}")
    print(f"💸 Valor final com desconto: {Negrito}R$ {total:.2f}{Reset}")
else:
    print(f"\n✅💵 {Negrito}Pagamento em dinheiro{Reset}")
    print(f"💸 Valor final: {Negrito}R$ {total:.2f}{Reset}")