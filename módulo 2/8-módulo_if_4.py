from cores import (Azul, Magenta, AmareloClaro, VerdeClaro, Vermelho, Reset, Negrito)

faturamento_loja_1 = int(input(f"\n{Negrito}Digite o faturamento da Loja 1: {Reset}"))
faturamento_loja_2 = int(input(f"\n{Negrito}Digite o faturamento da Loja 2: {Reset}"))

email = "testeifs@gmail.com"

print(f"""\n {Azul}COMPARADORES NO PYTHON 💉 2️⃣ 3️⃣ 4️⃣ ...{Reset}

{Magenta}
Este módulo demonstra o uso dos principais comparadores
utilizados em estruturas condicionais (exemplo educativo).
{Reset}""")

print(f"{Azul}Programa 1 – Comparação de Faturamento{Reset}")
if (faturamento_loja_1 == faturamento_loja_2):
    print(f"{VerdeClaro}Os faturamentos são iguais ✅{Reset}")
else:
    print(f"{AmareloClaro}Os faturamentos são diferentes ⚠️{Reset}")

print(f"\n{Azul}{Negrito}Programa 2 – Validação de Email Fictício{Reset}")
if (email != "testeifs@gmail.com"):
    print(f"{Vermelho}Esse não é o email correto ❌{Reset}")
else:
    print(f"{VerdeClaro}Email correto✅{Reset}")

print(f"\n{Azul}Programa 3 – Verificação de Formato de{Reset} {AmareloClaro}Email{Reset}")

email_usuario = input(f"\n\n{Negrito}Insira seu e-mail: {Reset}")

if (not "@" in email_usuario):
    print(f"{Vermelho}Email inválido ❌{Reset}")
else:
    print(f"{VerdeClaro}Email válido ✅{Reset}")
    pass