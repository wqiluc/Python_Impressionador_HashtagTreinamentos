mensagem_boas_vindas = (f"""
╔══════════════════════════════════════════════════════════════╗
║                    🔐 PASSWORD MANAGER 🔐                    ║
╠══════════════════════════════════════════════════════════════╣
║ Banco de dados simulado com DICIONÁRIO em Python 🐍🎲        ║
║                                                              ║
║ ✅ Cadastrar novas senhas;                                   ║
║ ✅ Consultar senhas existentes; e                            ║
║ ✅ Proteção com Senha Mestre                                  ║
║                                                              ║
║ Senha Mestre necessária para qualquer operação 🔐:           ║
║ ➜ "uh&g7fnsd8"                                                ║
║                                                              ║
║ FUNCIONALIDADES:                                             ║
║ • Adicionar novo sistema (nome, login e senha);              ║
║ • Consultar sistemas cadastrados;                            ║
║ • Executar em loop até o usuário decidir sair.               ║
╠══════════════════════════════════════════════════════════════╣
║ ESTRUTURA DO PROGRAMA 🧠                                     ║
║                                                              ║
║ ➜ Início                                                     ║
║ ➜ Solicita senha mestre                                      ║
║ ➜ Exibe menu de opções                                       ║
║ ➜ 1 - Cadastrar senha                                        ║
║ ➜ 2 - Consultar senha                                        ║
║ ➜ 3 - Sair                                                   ║
║ ➜ Executa ação escolhida                                     ║
║ ➜ Retorna ao menu (loop infinito)                            ║
║ ➜ Finaliza quando usuário escolher sair                      ║
║                                                              ║
║ Digite a opção desejada e gerencie suas senhas com segurança ║
╚══════════════════════════════════════════════════════════════╝ """)

print(mensagem_boas_vindas)


from cores import *
gerenciador_senhas = {
    "Gmail": ("lira@emailfalso.com", "minhasenha123"),
    "Github": ("pythonimpressionador", "senhadoida"),
    "Cartão de Crédito": ("NumeroFalsodoCartao", "123456"),
    "Portal Hashtag": ("usuario@gmail.com", "123456")
}
senha_mestre_salva = ["uh&g7fnsd"] 
#já criptografado🔐 se QUALQUER OUTRO USUÁRIO TENTAR fora do computador 
# do dono do github, não funcionará! ❌

#resolução:
gerenciador_senhas = {
    "Gmail": ("lira@emailfalso.com", "minhasenha123"),
    "Github": ("pythonimpressionador", "senhadoida"),
    "Cartão de Crédito": ("NumeroFalsodoCartao", "123456"),
    "Portal Hashtag": ("usuario@gmail.com", "123456")
}
senha_mestre_salva = ["uh&g7fnsd"]

senha_mestre = str(input(f"\n{Negrito}Digite a senha mestre para acessar o banco de dados: {Reset}"))
while not (
    any(senha.isalpha() for senha in senha_mestre) and
    any(senha.isdigit() for senha in senha_mestre) and
    any(senha.islower() for senha in senha_mestre) and
    senha_mestre in senha_mestre_salva):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite a senha mestre correta!! 🔐{Reset}")
    senha_mestre = str(input(f"{Negrito}Digite a senha mestre para acessar o banco de dados: {Reset}"))

print(f"{Negrito}Senha Mestre🔑:{Reset} {Amarelo}'{senha_mestre}'{Reset}{Verde} Inserida com sucesso!! ✅{Reset}\n")

for indice_github, (dados_github) in enumerate(gerenciador_senhas.items()):
    print(f"{Negrito}{indice_github+1}º dado:{Reset} {CyanClaro}'{dados_github[0]}' = {dados_github[1][0]}{Reset}{Negrito} - Senha desse dado:{Reset} {Amarelo}'{dados_github[1][1]}'{Reset}")

opcao_alterar_senha = str(input(f"{Negrito}Deseja Alterar alguma senha? [S / N] {Reset}")).strip().upper()

while not (opcao_alterar_senha in ["S","N"]):
    print(f"{Vermelho}Termo Inválido!! ❌ Digite APENAS [S / N]{Reset}")
    opcao_alterar_senha = str(input(f"{Negrito}Deseja Alterar alguma senha? [S / N] {Reset}")).strip().upper()

if (opcao_alterar_senha == "N"):
    exit()
else:
    while True:
        dado_escolhido = str(input(f"{Negrito}Qual dado deseja alterar? {Reset}")).strip()
        while (dado_escolhido not in gerenciador_senhas):
            print(f"{Vermelho}Dado não encontrado!! ❌ Digite exatamente como aparece acima.{Reset}")
            dado_escolhido = str(input(f"{Negrito}Qual dado deseja alterar? {Reset}")).strip()

        novo_usuario = str(input(f"{Negrito}Digite o novo usuário/login: {Reset}")).strip()
        nova_senha = str(input(f"{Negrito}Digite a nova senha: {Reset}")).strip()

        gerenciador_senhas[dado_escolhido] = (novo_usuario, nova_senha)

        print(f"\n{Verde}Senha do '{dado_escolhido}' alterada e salva com sucesso!! ✅{Reset}\n")

        for indice_github, (dados_github) in enumerate(gerenciador_senhas.items()):
            print(f"{Negrito}{indice_github+1}º dado:{Reset} {CyanClaro}'{dados_github[0]}' = {dados_github[1][0]}{Reset}{Negrito} - Senha desse dado:{Reset} {Amarelo}'{dados_github[1][1]}'{Reset}")

        senha_mestre = str(input(f"\n{Negrito}Digite novamente a senha mestre para continuar: {Reset}"))

        if (senha_mestre not in senha_mestre_salva):
            print(f"{Vermelho}Senha Mestre incorreta!! 🔒❌ Tente novamente.{Reset}")
            continue

        continuar = str(input(f"{Negrito}Deseja alterar outra senha? [S / N] {Reset}")).strip().upper()

        while continuar not in ["S","N"]:
            print(f"{Vermelho}Termo Inválido!! ❌ Digite APENAS [S / N]{Reset}")
            continuar = str(input(f"{Negrito}Deseja alterar outra senha? [S / N] {Reset}")).strip().upper()

        if (continuar == "N"):
            print(f"{Verde}Encerrando gerenciador com segurança... 🔐{Reset}")
            break