(f"""Crie um programa que converta a temperatura de celsius para Faremheit.
E agora, adapte o programa para ele funcionar 
para uma lista de temperaturas""")

# Parte 2

from cores import *
lista_temperaturas_celcius = list()
lista_temperaturas_faremheit = list()

qtd_temperaturas = str(input(f"{Negrito}Digite quantas temperaturas quer computar: {Reset}")).strip()
while not (qtd_temperaturas.isdigit()):
    print(f"{Vermelho}Digite a QUANTIDADE de temperaturas quer adicionar (int){Reset}")
    qtd_temperaturas = str(input(f"{Negrito}Digite quantas temperaturas quer computar: {Reset}")).strip()
qtd_temperaturas = int(qtd_temperaturas)

for temperaturas in range(qtd_temperaturas):
    tempeatura_celcius = str(input(f"{Negrito}Digite a {temperaturas+1}º temperatura em grau Celsius (°C): {Reset}")).strip()
    while not (tempeatura_celcius.isdigit()):
        print(f"{Vermelho}Termo Inválido!! ❌ Digite uma temperatura em grau Celsius (°C) (int){Reset}")
        tempeatura_celcius = str(input(f"{Negrito}Digite a temperatura em grau Celsius (°C): {Reset}")).strip()
    tempeatura_celcius = int(tempeatura_celcius)
    tempeatura_faremheit = (tempeatura_celcius*(9/5)+32) 
    lista_temperaturas_celcius.append(tempeatura_celcius)
    lista_temperaturas_faremheit.append(tempeatura_faremheit)

print(f"{Negrito}Lista de Temperaturas °C: {lista_temperaturas_celcius}{Reset}")
print(f"{Negrito}Lista de Temperaturas F: {lista_temperaturas_faremheit}{Reset}")