(f"""
ChatBot de Recomendações de Viagens🤖✈️
 
- Você trabalha em uma agência de viagens e precisa criar um chatbot para os seus clientes. Esse chatbot deve pedir para o usuario escolher um mês de viagem. Em seguida, seu chatbot deve perguntar para qual lugar o usuário deseja viajar. Caso o local escolhido pelo usuário esteja na lista de bons lugares para viajar naquele mês, o seu chatbot deve dizer que é um ótimo lugar para viajar nesse mês. Caso o local não esteja na lista de bons locais daquele mês, seu chatbot deve:
 
    1. Dizer para ele quais lugares são bons para viajar nesse mês
    2. Verificar no resto dos meses se o local que o usuário quer viajar está em algum outro mês. Se tiver, seu programa deve dizer para ele qual o melhor mês para viajar para o local desejado pelo cliente. """)

from cores import *

meses = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"]
viagens_mensais = {
    "jan": ["Tailandia", "Brasil", "Antartica", "AfricaDoSul", "Argentina"],
    "fev": ["Tailandia", "Brasil", "Argentina", "Uruguai", "AfricaDoSul"],
    "mar": ["Brasil", "Marrocos", "Eua", "Egito", "Dubai"],
    "abr": ["Brasil", "Marrocos", "Egito", "Dubai", "Equador"],
    "mai": ["Brasil", "Eua", "Italia", "Franca", "Inglaterra"],
    "jun": ["Brasil", "Italia", "Franca", "Grecia", "Turquia"],
    "jul": ["Brasil", "Italia", "Franca", "Grecia", "Turquia"],
    "ago": ["Brasil", "Italia", "Franca", "Grecia", "Turquia"],
    "set": ["Brasil", "Croacia", "Grecia", "Mexico", "Alemanha"],
    "out": ["Brasil", "Alemanha", "Japao", "Chile", "Indonesia"],
    "nov": ["Brasil", "Mexico", "CostaRica", "Barbados", "Colombia"],
    "dez": ["Tailandia", "Mexico", "CostaRica", "Barbados", "Colombia"]
}

#resolução:
mes_viagem = str(input(f"\n{Negrito}Digite o mês que deseja viajar: (ex: jan,fev,mar..){Reset}")).strip().lower()
while (mes_viagem not in meses[0:]):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite um mês de jan-dez (nesse modelo){Reset}")
    mes_viagem = str(input(f"{Negrito}Digite o mês que deseja viajar: (ex: jan,fev,mar..){Reset}")).strip().lower()
mes_viagem = str(mes_viagem)

local_viagem = str(input(f"{Negrito}Digite o seu local de destino: {Reset}")).strip().capitalize()
while not (local_viagem.replace(" ", "", 10).isalpha()):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite um país de destino (str){Reset}")
    local_viagem = str(input(f"{Negrito}Digite o seu local de destino: {Reset}")).strip().capitalize()
local_viagem = str(local_viagem)

print(f"\n {Negrito}Melhores meses pra viajar pro(pra):{Reset} {Amarelo}'{local_viagem.capitalize()}': {Reset}")
for indice_viagem, (mes,países) in enumerate(viagens_mensais.items()):
    if (local_viagem.capitalize() in países):
        print(f"{Negrito}{indice_viagem+1}º mês: '{mes.capitalize()}' - país: {local_viagem}{Reset}")
    else:
        pass