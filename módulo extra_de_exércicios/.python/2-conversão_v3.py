(f"""Crie um programa que converta a temperatura de celsius para Faremheit.
E agora, adapte o programa para o usuário dizer qual temperatura
deseja converter e mostre o resultado""")

# Parte 3
from cores import *

while True:
    opcao = str(input(f"{Negrito}Digite uma opção: [1 - Realizar Conversão / 2 - Sair] {Reset}")).strip()
    while not (opcao.isdigit()):
        print(f"{Vermelho}Termo Inválido!! ❌ Digite UMA OPÇÃO [1 - Realizar Conversão / 2 - Sair] (int) {Reset}")
        opcao = str(input(f"{Negrito}Digite uma opção: [1 - Realizar Conversão / 2 - Sair] {Reset}")).strip()
    opcao = int(opcao)
    if (opcao==2):
        break
    else:
        opcao_temperatura_escolha = str(input(f"{Negrito}Digite uma temperatura para converter (°C / F){Reset}")).strip().lower()
        while not (opcao_temperatura_escolha in ["c","f"] and opcao_temperatura_escolha.isalpha()):
            print(f"{Vermelho}Termo Inválido!! Digite uma temperatura (°C / F){Reset}")
            opcao_temperatura_escolha = str(input(f"{Negrito}Digite uma temperatura para converter (°C / F){Reset}")).strip().lower()
        opcao_temperatura_escolha = str(opcao_temperatura_escolha)

        temperatura = str(input(f"{Negrito}Digite o valor da temperatura:{Reset}")).strip()
        while not (temperatura.replace(".", "", 1).isdigit()):
            print(f"{Vermelho}Termo Inválido!!❌ Digite um valor numérico válido (int){Reset}")
            temperatura = str(input(f"{Negrito}Digite o valor da temperatura:{Reset}")).strip()
        temperatura = float(temperatura)

        if (opcao_temperatura_escolha) == "c":
            conversao = (temperatura * 9/5) + 32
            print(f"{Negrito}{temperatura}°C equivalem a {conversao:.2f}°F{Reset}")
        else:
            conversao = (temperatura - 32) * 5/9
            print(f"{Negrito}{temperatura}°F equivalem a {conversao:.2f}°C{Reset}")
