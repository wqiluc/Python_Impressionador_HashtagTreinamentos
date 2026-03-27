from cores import (Azul, Magenta, Amarelo, Reset,Negrito,Verde)

faturamento = 1000
custo = 500
lucro = (faturamento - custo)

print(f"""
{Azul}Operações com String 🔍💬{Reset}

{Magenta}Principais operações utilizadas com strings em Python:{Reset}

{Amarelo}str(){Reset} {Magenta}-> transforma números em texto{Reset}
{Amarelo}in{Reset} {Magenta}-> verifica se um texto está contido em outro{Reset}
{Amarelo}+{Reset} {Magenta}-> concatena strings{Reset}
{Amarelo}format() e {{}}{Reset} {Magenta}-> substituição de valores{Reset}
{Amarelo}%s{Reset} {Magenta}-> substitui textos{Reset}
{Amarelo}%d{Reset} {Magenta}-> substitui números inteiros{Reset}
""")

print(f"{Azul}Uso do str() e concatenação com +{Reset}")
print(f'{Negrito}O faturamento da loja foi de:{Reset} {Verde}R${Reset}', str(faturamento))

print(f"\n{Azul}Uso do format(){Reset}")
print('O faturamento foi de: {}'.format(faturamento))

print(f"\n{Azul}Uso do %s e %d{Reset}")
print('O faturamento foi de: %d' % faturamento)
print('O faturamento foi de: %s' % faturamento)

# Não se usa mais hj em dia👆

print(f"\n{Azul}Uso do operador in{Reset}")
print(f"@" in 'lira@gmail.com')
print(f"@" in 'lira.gmail.com')