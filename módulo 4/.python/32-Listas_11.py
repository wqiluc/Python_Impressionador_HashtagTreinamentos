from cores import (Azul, Magenta, Amarelo, Reset)

print(f"""
{Azul}# Copiar e "Igualdade" de Listas ✍🏻 {Reset}

{Azul}### Estrutura:{Reset}

{Magenta}- Quando fazemos:{Reset}
{Amarelo}lista2 = lista1{Reset}  
{Magenta}não estamos criando uma lista nova, mas estamos atribuindo outra variável à mesma lista.{Reset}

{Magenta}- Se quisermos copiar lista devemos fazer:{Reset}  
{Amarelo}lista2 = lista1.copy(){Reset}  
{Magenta}ou então{Reset}  
{Amarelo}lista2 = lista1[:]{Reset}

{Magenta}Para entender bem isso, vamos ver na prática:{Reset}""")