#Exercício 1: "Olá, Mundo!"
print("Alo Mundo")


#Exercício 2: Variáveis e Tipos de Dados
from cores import (Negrito, Magenta, Reset)
numero = int(input(f"\n {Negrito}Digite um número inteiro: {Reset} "))
print(f"\n {Magenta}Você digitou o número inteiro: {numero}{Reset}\n")


#Exercício 3: Operações Matemáticas
from cores import (Negrito, Amarelo, Reset)
numero1 = int(input(f"\n {Negrito}Digite o 1º número inteiro: {Reset} "))
numero2 = int(input(f"\n {Negrito}Digite o 2º número inteiro: {Reset} "))
soma = (numero1 + numero2)
print(f"\n {Amarelo}A soma entre {numero1} e {numero2} é igual a: {soma}{Reset}\n")


#Exercício 4: Media Aritmética
from cores import (Negrito, Reset)
nota1 = float(input(f"\n {Negrito}Digite a 1ª nota: {Reset} "))
nota2 = float(input(f"\n {Negrito}Digite a 2ª nota: {Reset} "))
nota3 = float(input(f"\n {Negrito}Digite a 3ª nota: {Reset} "))
nota4 = float(input(f"\n {Negrito}Digite a 4ª nota: {Reset} "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"\n {Negrito}A média das notas é: {media}{Reset}\n")


#Exercício 5: Conversão de distâncias
from cores import (Negrito, Reset)
conversao = float(input(f"\n {Negrito}Digite uma distância em metros: {Reset} "))
conversao_cm = conversao * 100
print(f"\n {Negrito}A distância em centímetros é: {conversao_cm} cm{Reset}\n")


#Exercício 6: Área de uma sala
from cores import (Negrito, Reset, Azul)
largura_sala = float(input(f"\n {Negrito}Digite a largura da sala em metros: {Reset} "))
comprimento_sala = float(input(f"\n {Negrito}Digite o comprimento da sala em metros: {Reset} "))
area_sala = (largura_sala * comprimento_sala)
print(f"\n {Azul}A área da sala é: {area_sala}m² {Reset}\n")


#Exercício 7: Salário do mês
from cores import (Negrito, Reset, Verde)
ganho_por_hora = float(input(f"\n {Negrito}Digite quanto você ganha por hora: {Reset} "))
ganho_dia = ganho_por_hora * 8
ganho_mes = ganho_dia * 22
print(f"\n {Negrito}Seu ganho mensal é de:{Reset} {Verde}R${ganho_mes:.2f}{Reset}\n")


#Exercício 8: Conversão de temperaturas (Fahrenheit para Celsius)
from cores import (Negrito, Reset, Vermelho)
fahrenheit = float(input(f"\n {Negrito}Digite a temperatura em Fahrenheit: {Reset} "))
celsius = (fahrenheit - 32) * 5/9
print(f"\n {Vermelho}A temperatura em Celsius é: {celsius:.2f}°C{Reset}\n")


#Exercício 9: Conversão de temperaturas (Celsius para Fahrenheit)
from cores import (Negrito, Reset, Azul)
celsius = float(input(f"\n {Negrito}Digite a temperatura em Celsius: {Reset} "))
fahrenheit = (celsius * 9/5) + 32
print(f"\n {Azul}A temperatura em Fahrenheit é: {fahrenheit:.2f}°F{Reset}\n")

#Exercício 10: Peso ideal (pessoa)
from cores import (Negrito, Reset, Magenta, Azul)
peso_homem = float(input(f"\n {Negrito}Digite a altura do homem em metros: {Reset} "))
peso_ideal_homem = (72.7 * peso_homem) - 58
print(f"\n {Azul}O peso ideal do homem é: {peso_ideal_homem:.2f} kg{Reset}\n")


#Exercício 11: Peso ideal (homem e mulher)
from cores import (Negrito, Reset, Magenta, Azul)
peso_homem = float(input(f"\n {Negrito}Digite a altura do homem em metros: {Reset} "))
peso_mulher = float(input(f"\n {Negrito}Digite a altura da mulher em metros: {Reset} "))
peso_ideal_homem = (72.7 * peso_homem) - 58
peso_ideal_mulher = (62.1 * peso_mulher) - 44.7
print(f"\n {Azul}O peso ideal do homem é: {peso_ideal_homem:.2f} kg{Reset} \n")
print(f"\n {Azul}O peso ideal da mulher é: {peso_ideal_mulher:.2f} kg{Reset} \n")


#Exercício 12: Salários e impostos
from cores import (Negrito, Reset, Verde)
ganho_hora = float(input(f"\n {Negrito}Digite quanto você ganha por hora: {Reset} "))
horas_trabalhadas = float(input(f"\n {Negrito}Digite quantas horas você trabalha por mês: {Reset} "))
# a) Salário bruto
salario_bruto = ganho_hora * horas_trabalhadas
print(f"\n {Negrito}Seu salário bruto é de: {Reset} {Verde}R${salario_bruto:.2f}{Reset}\n")
# b) Imposto de renda (11%)
imposto_renda = salario_bruto * 0.11
print(f"\n {Negrito}Seu imposto de renda é de: {Reset} {Verde}R${imposto_renda:.2f}{Reset}\n")
# c) INSS (8%)
inss = salario_bruto * 0.08
print(f"\n {Negrito}Seu INSS é de: {Reset} {Verde}R${inss:.2f}{Reset}\n")
# d) Sindicato (5%)
sindicato = salario_bruto * 0.05
print(f"\n {Negrito}Seu sindicato é de: {Reset} {Verde}R${sindicato:.2f}{Reset}\n")
# e) Salário líquido
taxas = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - taxas
print(f"\n {Negrito}Seu salário líquido é de: {Reset} {Verde}R${salario_liquido:.2f}{Reset}\n")


# Exercício 13: Loja de tintas
from cores import (Negrito, Reset, Magenta, Amarelo)
tamanho_area = float(input(f"\n {Negrito}Digite o tamanho da área em m²: {Reset} "))
cobertura_latas = tamanho_area / 3
latas_necessarias = cobertura_latas / 18
cobertura_total = latas_necessarias * 80
print(f"\n {Amarelo}Para pintar uma área de {tamanho_area}m², você precisará de {latas_necessarias:.2f} latas de tinta, totalizando R${cobertura_total:.2f}.{Reset}\n")


# Exercício 14: Download de arquivos
from cores import (Negrito, Reset, Magenta)
tamanho_arquivo = float(input(f"\n {Negrito}Digite o tamanho do arquivo em MB: {Reset} "))
velocidade_internet = float(input(f"\n {Negrito}Digite a velocidade da internet em Mbps: {Reset} "))
tempo_download = (tamanho_arquivo / velocidade_internet) * 8
print(f"\n {Magenta}O tempo estimado para o download do arquivo é de: {tempo_download:.2f} segundos.{Reset}\n")

#Fim do código#