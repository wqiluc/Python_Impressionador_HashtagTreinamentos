from cores import (Azul, Magenta, Amarelo, Reset)

print(f"""
{Azul}Índice e Tamanho de String{Reset}

{Magenta}Em Python, strings são sequências de caracteres indexadas a partir do zero.{Reset}
{Magenta}Cada caractere ocupa uma posição específica dentro do texto.{Reset}


{Amarelo} 0 1 2 3 4 5 6 7 8 9 10 11 12 13 \n
         e m a i - l . c o m{Reset}

{Amarelo}• Pegar um item de uma string:{Reset}
{Amarelo}texto[indice]{Reset}

{Amarelo}• Pegar o tamanho de uma string:{Reset}
{Amarelo}len(texto){Reset}""")