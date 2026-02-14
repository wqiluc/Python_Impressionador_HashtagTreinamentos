(f"""
Analisador de texto💬

Criar função analisar_texto(texto).

Retornar:
- contagem total de palavras;
- frequência de palavras;
- frequência de letras.

Ignorar diferença entre maiúsculas e minúsculas.❌

Não se preocupar com pontuação.""")

# solução (EM ANDAMENTO)👇:
from cores import *

lista_palavras = list()
dicionario_palavras = dict()

while True:
    opcao = str(input(f"{Negrito}Digite uma opção: [1 - Escrever / 2 - Sair]{Reset}")).strip()
    while not (opcao.isdigit()):
        print(f"{Vermelho}Termo Inválido!! Digite uma OPÇÃO (int){Reset}")
        opcao = str(input(f"{Negrito}Digite uma opção: [1 - Escrever / 2 - Sair]{Reset}")).strip()
    opcao = int(opcao)
    if (opcao==2):
        print(f"{Amarelo}Encerrando o loop. {Reset}")
        break
    else:
        palavra = str(input(f"{Negrito}Digite uma PALAVRA (str): {Reset}")).strip()
        while not (palavra.isalpha()):
            print(f"{Vermelho}Termo Inválido!! Digite um PALAVRA (str){Reset}")
            palavra = str(input(f"{Negrito}Digite uma PALAVRA (str): {Reset}")).strip()
        palavra = str(palavra)
        lista_palavras.append(palavra)
        dicionario_palavras["Palavras"] = lista_palavras

print(dicionario_palavras)