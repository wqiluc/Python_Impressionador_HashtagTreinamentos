(f"""
Conversor de Moedas 🪙
 
- Parte 2: Adapte o seu código (crie uma cópia para manter os 2 códigos prontos) 
para o usuário não precisar dizer qual 
a moeda original, mas que permita inserir um valor 
para fazer a conversão com o indicativo da moeda, 
ex: R$50, US$20 
e o sistema fazer a conversão automaticamente. """)

# Parte 2
# taxas fixas (exemplo)
from cores import *
taxa_usd = 0.20
taxa_eur = 0.18
taxa_gbp = 0.16

while True:
    opcao = str(input(f"{Negrito}Deseja converter um valor em R$? [S / N]{Reset}")).strip().upper()
    while not (opcao in ["S", "N"]):
        print(f"{Vermelho}Termo Inválido!! ❌ Digite apenas [S / N]{Reset}")
        opcao = str(input(f"{Negrito}Deseja converter um valor em R$? [S / N]{Reset}")).strip().upper()
    
    if (opcao == "S"):
        valor_real = float(input(f"{Negrito}Digite o valor em R$: {Reset}"))
        
        valor_usd = valor_real * taxa_usd
        valor_eur = valor_real * taxa_eur
        valor_gbp = valor_real * taxa_gbp
        
        print(f"\n{Negrito}🪙 Conversões disponíveis:{Reset}")
        print(f"USD🇺🇸: {valor_usd:.2f}")
        print(f"EUR🇪🇺: {valor_eur:.2f}")
        print(f"GBP🇬🇧: {valor_gbp:.2f}\n")
    
    else:
        print(f"{Negrito}Programa encerrado. Até a próxima! 👋{Reset}")
        break
