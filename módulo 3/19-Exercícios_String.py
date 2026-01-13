from cores import (Negrito, Reset, Azul, Magenta, Amarelo)

print(f"\n {Azul}📘 EXERCÍCIOS — STRINGS{Reset}\n")


print(f"{Azul}🔹 EXERCÍCIO 1 — CADASTRO DE CPF{Reset}")
"""
{Magenta}Receba um CPF digitado apenas com números.
O CPF deve conter exatamente {Amarelo}11 dígitos{Reset}{Magenta}.
Qualquer letra, símbolo ou tamanho inválido deve gerar erro.{Reset}
"""
print(f"\n {Negrito}Sua Resposta aqui 👇{Reset} \n")

from cores import Negrito, Reset, Vermelho, Verde,Amarelo

cpf = input(f"\n{Negrito}Digite seu CPF (ex: 999.999.999-99): {Reset}")

cpf_formatado = cpf.replace(".", "").replace("-", "").replace(" ", "")

while not (cpf_formatado.isdigit() and len(cpf_formatado) == 11):
    print(f"{Vermelho}CPF inválido! Digite 11 números válidos.{Reset}")
    cpf = input(f"\n{Negrito}Digite seu CPF (ex: 999.999.999-99): {Reset}")
    cpf_formatado = cpf.replace(".", "").replace("-", "").replace(" ", "")

cpf_formatado = f"{Amarelo}{cpf_formatado[:3]}.{cpf_formatado[3:6]}.{cpf_formatado[6:9]}-{cpf_formatado[9:]}{Reset}"
print(f"{Verde}CPF válido: {cpf_formatado}{Reset}")


print(f"\n{Azul}{Negrito}🔹 EXERCÍCIO 2 — TRATAMENTO DE CPF{Reset}")
"""
{Magenta}O usuário pode digitar pontos, traços e espaços.
O sistema deve remover {Amarelo}., - e espaços{Reset}{Magenta}.
Após o tratamento, o CPF deve conter apenas números e {Amarelo}11 dígitos{Reset}{Magenta}.{Reset}
"""
print(f"{Negrito}Sua Resposta aqui 👇{Reset}")


from cores import Negrito, Reset, Vermelho, Verde,Amarelo

cpf = str(input(f"\n{Negrito}Digite seu CPF (ex: 999.999.999-99): {Reset}")).strip()
cpf_formatado = cpf.replace(".", "").replace("-", "").replace(" ", "")

while not (cpf_formatado.isdigit() and len(cpf_formatado) == 11):
    print(f"{Vermelho}CPF inválido! Digite 11 números válidos.{Reset}")
    cpf = str(input(f"\n{Negrito}Digite seu CPF (ex: 999.999.999-99): {Reset}").strip())
    cpf_formatado = cpf.replace(".", "").replace("-", "").replace(" ", "")

cpf_formatado = f"{Amarelo}{cpf_formatado[:3]}{cpf_formatado[3:6]}{cpf_formatado[6:9]}{cpf_formatado[9:]}{Reset}"
print(f"{Verde}CPF válido: {cpf_formatado}{Reset}")


print(f"\n{Azul}{Negrito}🔹 EXERCÍCIO 3 — CADASTRO DE E-MAIL{Reset}")
"""
{Magenta}Peça nome e e-mail.
Ambos devem ser preenchidos.
O e-mail é válido somente se tiver {Amarelo}@{Reset}{Magenta} e um {Amarelo}.{Reset}{Magenta} após o @.{Reset}
"""
print(f"{Negrito}Sua Resposta aqui 👇{Reset}")

from cores import Negrito, Reset, Vermelho, Verde

email = input(f"{Negrito}Digite o seu E-mail (gmail): {Reset}").lower().strip()

email_limpo = email.replace("@gmail.com", "").replace(".", "").replace("com", "")

while "@gmail.com" not in email or not email_limpo.isalpha():
    print(f"{Vermelho}E-mail inválido! Use um Gmail válido ❌{Reset}")
    email = input(f"{Negrito}Digite o seu E-mail (gmail): {Reset}").lower().strip()
    email_limpo = email.replace("@gmail.com", "").replace(".", "").replace("_", "")

print(f"{Verde}{Negrito}Meu E-mail = {email}{Reset}")