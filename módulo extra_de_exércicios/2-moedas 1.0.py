(f"""
Conversor de Moedas 🪙

- Parte 1: Crie um conversor de moedas que pergunte para o usuário 
qual moeda ele quer converter e para qual moeda destino ele quer converter. 
Caso alguma das moedas não estejam na lista de conversão, 
o usuário deve ser informado que essa conversão não é possível. 
Sendo possível a conversão, o seu conversor de moedas deve em seguida pedir 
o valor da moeda de origem que ele quer converter para a moeda de destino, 
fazer a conversão e exibir para o usuário o valor convertido.
""")
# Parte 1
# taxas fixas (exemplo)
from cores import *
taxa_brl_usd = 0.20
taxa_brl_eur = 0.18
taxa_usd_brl = 5.00
taxa_usd_eur = 0.90
taxa_eur_brl = 5.50
taxa_eur_usd = 1.10

while True:
    opcao = str(input(f"{Negrito}Deseja realizar uma conversão? [S / N]{Reset}")).strip().upper()
    while not (opcao in ["S", "N"]):
        print(f"{Vermelho}Termo Inválido!! ❌ Digite uma opção VÁLIDA acima 👆 [S / N] APENAS!{Reset}")
        opcao = str(input(f"{Negrito}Deseja realizar uma conversão? [S / N]{Reset}")).strip().upper()
    
    if (opcao == "S"):
        moeda_original = str(input(f"{Negrito}Digite a moeda original que quer converter (Real, Dolar, Euro): {Reset}")).strip().capitalize()
        while not (moeda_original.replace(" ", "", 10).isalpha()):
            print(f"{Vermelho}Termo Inválido!! ❌ Digite uma moeda VÁLIDA para ser convertida! {Reset}")
            moeda_original = str(input(f"{Negrito}Digite a moeda original que quer converter: {Reset}")).strip().capitalize()
        
        moeda_destino = str(input(f"{Negrito}Digite a moeda destino (Real, Dolar, Euro): {Reset}")).strip().capitalize()
        while not (moeda_destino.replace(" ", "", 10).isalpha()):
            print(f"{Vermelho}Termo Inválido!! ❌ Digite uma moeda VÁLIDA de destino! {Reset}")
            moeda_destino = str(input(f"{Negrito}Digite a moeda destino: {Reset}")).strip().capitalize()
        
        valor_moeda_original = float(input(f"{Negrito}Digite o valor que deseja converter: {Reset}"))
        
        if (moeda_original == moeda_destino):
            valor_convertido = valor_moeda_original
        
        elif (moeda_original == "Real" and moeda_destino == "Dolar"):
            valor_convertido = valor_moeda_original * taxa_brl_usd
        
        elif (moeda_original == "Real" and moeda_destino == "Euro"):
            valor_convertido = valor_moeda_original * taxa_brl_eur
        
        elif (moeda_original == "Dolar" and moeda_destino == "Real"):
            valor_convertido = valor_moeda_original * taxa_usd_brl
        
        elif (moeda_original == "Dolar" and moeda_destino == "Euro"):
            valor_convertido = valor_moeda_original * taxa_usd_eur
        
        elif (moeda_original == "Euro" and moeda_destino == "Real"):
            valor_convertido = valor_moeda_original * taxa_eur_brl
        
        elif (moeda_original == "Euro" and moeda_destino == "Dolar"):
            valor_convertido = valor_moeda_original * taxa_eur_usd
        
        else:
            print(f"{Vermelho}❌ Conversão não disponível!{Reset}")
            continue
        
        print(f"\n{Negrito}💱 Valor convertido: {valor_convertido:.2f} {moeda_destino}{Reset}\n")
    
    else:
        print(f"{Magenta}Programa encerrado. Até a próxima! 👋{Reset}")
        break