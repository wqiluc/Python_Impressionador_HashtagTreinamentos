from cores import Negrito, Reset, Azul, Magenta, Amarelo, Verde

print(f"""
{Azul}📘 MÓDULO STRING — FÓRMULAS DE TEXTO{Reset}

{Magenta}Métodos de string permitem manipular, analisar e transformar textos.
Usamos sempre o formato:
texto.método(argumentos)

Eles são essenciais para tratar, validar e formatar dados em Python.{Reset}


{Azul}🔹 PRINCIPAIS MÉTODOS 🔹{Reset}

{Amarelo}capitalize() → Primeira letra maiúscula{Reset}  
{Amarelo}casefold() → Tudo em minúsculo{Reset}  
{Amarelo}count() → Conta ocorrências{Reset}  
{Amarelo}endswith() → Verifica o final do texto{Reset}  
{Amarelo}find() → Localiza um trecho{Reset}  
{Amarelo}format() → Formata valores na string{Reset}  
{Amarelo}isalnum() → Letras e números{Reset}  
{Amarelo}isalpha() → Apenas letras{Reset}  
{Amarelo}isnumeric() → Apenas números{Reset}  
{Amarelo}replace() → Substitui texto{Reset}  
{Amarelo}split() → Divide a string{Reset}  
{Amarelo}splitlines() → Divide por linhas{Reset}  
{Amarelo}startswith() → Verifica o início{Reset}  
{Amarelo}strip() → Remove espaços extras{Reset}  
{Amarelo}title() → Iniciais maiúsculas{Reset}  
{Amarelo}upper() → Texto em maiúsculo{Reset}  


{Magenta}Esses métodos são usados para:{Reset} {Amarelo}limpar, validar e formatar{Reset} {Magenta}dados de forma profissional.{Reset}
""")

texto = f'''Olá, bom dia
Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
Faturamento = {Verde}R$2.500,00{Reset}
'''
print(texto)