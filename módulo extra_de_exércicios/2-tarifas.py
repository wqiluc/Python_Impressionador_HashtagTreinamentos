(f"""
Você está analisando a conta de energia de um pequeno escritório e precisa saber:
 
1. Qual o valor total da conta de energia em cada mês do ano
2. Qual o valor total da conta de energia no ano

Considere as listas dadas como os 12 meses do ano, 
tanto para bandeiras quanto para consumo. 
O valor da conta é dado por: consumo * multiplicador_bandeira * preco_kwh """)

#resolução:
from cores import *

bandeiras_tarifarias = ["vermelha", "vermelha", "amarela", "amarela", "verde", "verde", "verde", "verde", "verde", "amarela", "amarela", "amarela"]
consumo_kwh = [400, 350, 325, 350, 200, 220, 250, 290, 360, 290, 300, 300]
preco_kwh = 1.3
multiplicador = {"vermelha": 2, "amarela": 1.3, "verde": 1}
valores_cheios = list()

for indice_tarifas, (tarifa, valor_consumo) in enumerate(zip(bandeiras_tarifarias, consumo_kwh)):
    
    valor = preco_kwh * valor_consumo
    multiplicador_tarifa = multiplicador[tarifa]
    valor_real = valor * multiplicador_tarifa

    print(f"{Negrito}{indice_tarifas+1}º Tarifa: {tarifa.capitalize()} - Valor da Tarifa: {valor:.2f}{Reset}")
    print(f"{Negrito}Multiplicador Aplicado: {multiplicador_tarifa}x{Reset}")
    print(f"{Negrito}Valor Real a Pagar:{Reset} {Verde}R${Reset}{Negrito}{valor_real:.2f}{Reset}")
    valores_cheios.append(valor_real)

print(f"{Negrito}A soma de todos os valores a serem pagos é de:{Reset} {Verde}R${Reset}{Negrito}{sum(valores_cheios)}{Reset}")