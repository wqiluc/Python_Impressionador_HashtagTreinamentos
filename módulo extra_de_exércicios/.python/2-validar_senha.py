(f"""
Password Checker🔐
- Pessa para o usuário um input com a senha e um input com a confirmação de senha 
(aprenderemos no módulo de criação de telas com Python a fazer isso em um sistema bonito, mas para esse exercício faremos com inputs isso)
- Para validar a senha, verifique que:
    - A senha e confirmação são iguais✅;
    - A senha possua mais de 8 caracteres✅; e
    - A senha tenha letras e números✅""")

#resolução:
from cores import *
banco_senha = list()

senha_usuario = str(input(f"{Negrito}Digite a sua senha de usuário: {Reset}"))
while not (
    len(senha_usuario)<=8 and
    any(senha.isdigit() for senha in (senha_usuario)) and
    any(senha.isalpha() for senha in (senha_usuario)) and
    any(senha.isupper() for senha in (senha_usuario))
    ):
    print(f"""{Vermelho}Termo Inválido!! ❌ A senha precisa:
        1 - Ter, ao menos; um NÚMERO (int);
        2 - Ter, ao menos; um CARACTERE (str);
        3 - Ter, ao menos; um CARACTERE MAIÚSCULO (STR);
        4 - Ter, no mínimo; 8 caracteres.{Reset}""")
    senha_usuario = str(input(f"{Negrito}Digite a sua senha de usuário: {Reset}"))

print(f"{Verde}Senha Catalogada!! ✅{Reset}")

confirmacao_senha = str(input(f"{Negrito}Confirme a sua senha de usuário: {Reset}"))
while not (confirmacao_senha == senha_usuario):
    print(f"{Vermelho}Termo Inválido!! ❌ A sua senha não condiz com a senha previamente inserida!{Reset}")
    confirmacao_senha = str(input(f"{Negrito}Confirme a sua senha de usuário: {Reset}"))
banco_senha.append(confirmacao_senha)

print(f"{Negrito}A senha do usuário é:{Reset} {Amarelo}{banco_senha[0].format_map(banco_senha[0])}{Reset}")