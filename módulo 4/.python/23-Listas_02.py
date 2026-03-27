from cores import (Reset,Amarelo,Azul,Magenta)

print(f"""
{Azul}==================== LISTAS EM PYTHON — PARTE 02 ✅📋 ===================={Reset}

{Magenta}Estrutura de uma Lista:{Reset}
{Amarelo}lista = [valor, valor, valor, valor, ...]{Reset}

{Magenta}Acessando valores:{Reset}
{Amarelo}lista[i]{Reset} {Azul}→{Reset} retorna o valor do índice {Amarelo}i{Reset}

No Python, o índice sempre começa em {Amarelo}0{Reset}, então:
{Amarelo}lista[0]{Reset} {Azul}→{Reset} primeiro elemento  
{Amarelo}lista[1]{Reset} {Azul}→{Reset} segundo elemento  
{Amarelo}lista[2]{Reset} {Azul}→{Reset} terceiro elemento  

------------------------------------------------------------

{Magenta}Alterando valores de uma lista:{Reset}
Para substituir um valor use:
{Amarelo}lista[i] = novo_valor{Reset}

{Magenta}Exemplo:{Reset}
produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

{Amarelo}produtos[1] = 'smartphone'{Reset}

Agora a lista fica:
['tv', 'smartphone', 'mouse', 'teclado', 'tablet']

------------------------------------------------------------

{Magenta}Relação entre listas:{Reset}

produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
              0 ,      1   ,    2   ,     3    ,     4

vendas    = [ 1000,    1500  ,   350  ,    270   ,    900 ]

A posição de cada produto corresponde à mesma posição nas vendas.

{Amarelo}produtos[0]{Reset} {Azul}→{Reset} 'tv'   {Azul}→{Reset} {Amarelo}vendas[0]{Reset} {Azul}→{Reset} 1000  
{Amarelo}produtos[1]{Reset} {Azul}→{Reset} 'celular'  {Azul}→{Reset} {Amarelo}vendas[1]{Reset} {Azul}→{Reset} 1500  
{Amarelo}produtos[2]{Reset} {Azul}→{Reset} 'mouse'  {Azul}→{Reset} {Amarelo}vendas[2]{Reset} {Azul}→{Reset} 350  

------------------------------------------------------------

{Magenta}Exemplo com texto:{Reset}

texto = 'lira@gmail.com'

{Amarelo}texto[0]{Reset} → 'l'  
{Amarelo}texto[4]{Reset} → '@'  
{Amarelo}texto[-1]{Reset} → 'm'  

Strings também funcionam como listas de caracteres.""")