(f"Crie um programa que converta a temperatura de celsius para Faremheit")

from cores import *
# Parte 1
tempeatura_celcius = str(input(f"{Negrito}Digite a temperatura em grau Celsius (°C): {Reset}")).strip()
while not (tempeatura_celcius.isdigit()):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite uma temperatura em grau Celsius (°C) (int){Reset}")
    tempeatura_celcius = str(input(f"{Negrito}Digite a temperatura em grau Celsius (°C): {Reset}")).strip()
tempeatura_celcius = int(tempeatura_celcius)

tempeatura_faremheit = (tempeatura_celcius*(9/5)+32)

print(f"{Negrito}A temperatura em Celsius (°C) é de: {tempeatura_celcius}°C {Reset}")
print(f"{Negrito}A temperatura em Faremheit (F) é de: {tempeatura_faremheit}°C {Reset}")