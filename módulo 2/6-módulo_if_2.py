from cores import (Negrito,Reset,Azul, Magenta, AmareloClaro, Verde, Vermelho)

retorno_fundo = int(input(f"\n {Negrito}Digite o retorno de fundo: {Reset}"))

print(f"""{Azul}BLOCOS E IDENTAÇÃO _ – ANÁLISE DE FUNDO DE INVESTIMENTOS 🏦📊{Reset}

{Magenta}
Este programa avalia o retorno anual de um fundo de investimentos
e define se haverá cobrança de taxa com base nas regras do fundo.
{Reset}

{AmareloClaro}Retorno anual do fundo:{Reset} {retorno_fundo}%""")

if (retorno_fundo) >= 5:
    print(f"""{Magenta}Resultado da Análise:{Reset} O fundo atingiu o retorno mínimo exigido.\n""")
    if retorno_fundo > 20:
        taxa = 4
        print(f"""{Verde}Excelente desempenho!{Reset} Taxa cobrada: {taxa}%\n""")
    else:
        taxa = 2
        print(f"""{AmareloClaro}Bom desempenho.{Reset} Taxa cobrada: {taxa}%\n""")
else:
    taxa = 0
    print(f"""{Magenta}Resultado da Análise:{Reset} {Vermelho}Retorno insuficiente.{Reset} Nenhuma taxa será cobrada dos investidores.\n""")