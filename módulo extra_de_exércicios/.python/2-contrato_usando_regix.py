(f"""
 Desenvolva um programa que pergunte para o usuário: 
o nome completo, 
cpf, 
endereço, e 
duração do contrato. 
Personalize todo o texto do contrato de acordo com as informações dadas. """)

#solução:👇
from cores import *
from re import fullmatch as padrao

lista_dados_cliente = [ ]

nome_cliente = str(input(f"{Negrito}Digite seu nome completo: {Reset}")).strip().capitalize()
while not (nome_cliente.replace(" ", "", 10).isalpha()):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite seu NOME Completo (str){Reset}")
    nome_cliente = str(input(f"{Negrito}Digite seu nome completo: {Reset}")).strip().capitalize()
nome_cliente = str(nome_cliente)
lista_dados_cliente.append(nome_cliente)

cpf_cliente = str(input(f"{Negrito}Digite o CPF do cliente. Ex: (XXX.XXX.XXX-XX): {Reset}").strip())
while not (padrao(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf_cliente)):
    print(f"{Vermelho}CPF inválido! Use o formato XXX.XXX.XXX-XX{Reset}")
    cpf_cliente = str(input(f"{Negrito}Digite o CPF (XXX.XXX.XXX-XX): {Reset}").strip())
lista_dados_cliente.append(cpf_cliente)

duracao_contrato = str(input(f"{Negrito}Digite a data que o contrato terminará (DD/MM/AAAA): {Reset}").strip())
while not (padrao(r"\d{2}/\d{2}/\d{4}", duracao_contrato)):
    print(f"{Vermelho}Data inválida! Digite no formato DD/MM/AAAA{Reset}")
    duracao_contrato = str(input(f"{Negrito}Digite a data que o contrato terminará: {Reset}").strip())
lista_dados_cliente.append(duracao_contrato)

print(lista_dados_cliente)

print("\n" + "=" * 80)
print(f"{'CARTILHA CONTRATUAL':^80}")
print("=" * 80)

print(f"\n{Negrito}Contratante: {nome_cliente}{Reset}")
print(f"{Negrito}CPF: {cpf_cliente}{Reset}")
print(f"{Negrito}Data de término do contrato: {duracao_contrato}{Reset}")

print("\n" + "-" * 80)
print(f"{Negrito}CLÁUSULA 1ª – DO OBJETO{Reset}")
print(f"O presente contrato tem como finalidade formalizar o acordo firmado entre as partes.")

print(f"\n{Negrito}CLÁUSULA 2ª – DA VIGÊNCIA{Reset}")
print(f"{Negrito}O presente contrato terá validade até {duracao_contrato}.{Reset}")

print(f"\n{Negrito}CLÁUSULA 3ª – DAS RESPONSABILIDADES{Reset}")
print(f"{Negrito}As partes comprometem-se a cumprir integralmente as condições estabelecidas neste instrumento.{Reset}")

print("\n" + "-" * 80)
print(f"\n{Negrito}Assinam o presente instrumento:{Reset}\n")

print(" " * 5 + "_" * 35 + " " * 15 + "_" * 35)
print(" " * 8 + f"Contratante - {nome_cliente}" + " " * 13 + "Contratado(a)")

print("\n" + "=" * 80)