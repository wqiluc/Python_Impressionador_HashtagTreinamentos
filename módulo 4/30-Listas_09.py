from cores import (Reset, Amarelo, Azul, Magenta)

print(f"""
{Azul}==================== LISTAS EM PYTHON — PARTE 08 🔄 ===================={Reset}

{Magenta}Alterações de variáveis:{Reset}

Existem duas formas principais de alterar valores:

{Amarelo}variavel = variavel + outro_valor{Reset}  
ou  
{Amarelo}variavel += outro_valor{Reset}

------------------------------------------------------------

{Magenta}Exemplo:{Reset}

lista = ['mac', 'iphone']  
vendas = [100, 200]

Vamos adicionar o produto {Amarelo}ipad{Reset} com {Amarelo}500{Reset} vendas.

{Amarelo}lista.append('ipad'){Reset}  
{Amarelo}vendas.append(500){Reset}

------------------------------------------------------------

{Magenta}Alterando soma de vendas:{Reset}

soma_vendas = 300  

{Amarelo}soma_vendas += 500{Reset}

Agora o total é {Amarelo}800{Reset} vendas.

------------------------------------------------------------

{Magenta}Alterando texto (string):{Reset}

email = 'Esse mês vendemos um total de {{}} produtos, sendo:\\n{{}} unidades de {{}}\\n{{}} unidades de {{}}'.format(
    soma_vendas, vendas[0], lista[0], vendas[1], lista[1])

Para adicionar o iPad ao texto, basta concatenar:

{Amarelo}email += '\\n{...} unidades de {...}'.format(vendas[2], lista[2]){Reset}

------------------------------------------------------------

{Magenta}Resultado final:{Reset}

Esse mês vendemos um total de 800 produtos, sendo:
100 unidades de mac
200 unidades de iphone
500 unidades de ipad""")
