from cores import (Reset, Amarelo, Azul, Magenta,CyanClaro)

print(f"""
{Azul}==================== LISTAS EM PYTHON — CARTILHA DE MÉTODOS 📚 ===================={Reset}

{Magenta}append(){Reset}
{Amarelo}list.append(valor){Reset}
Adiciona um valor ao final da lista.

{CyanClaro}Exemplo{Reset}:
vendas = [150, 320]  
vendas.append(110)  
Resultado: [150, 320, 110]

------------------------------------------------------------

{Magenta}extend(){Reset}
{Amarelo}list.extend(lista2){Reset}
Adiciona todos os valores de outra lista.

{CyanClaro}Exemplo{Reset}:
vendas = [150, 320, 110]  
vendas_2semestre = [440, 470, 900]  
vendas.extend(vendas_2semestre)

------------------------------------------------------------

{Magenta}insert(){Reset}
{Amarelo}list.insert(posicao, valor){Reset}
Insere um valor em uma posição específica.

{CyanClaro}Exemplo{Reset}:
vendas = [150, 320]  
vendas.insert(1, 110)  
Resultado: [150, 110, 320]

------------------------------------------------------------

{Magenta}remove(){Reset}
{Amarelo}list.remove(valor){Reset}
Remove a primeira ocorrência do valor.

{CyanClaro}Exemplo{Reset}:
vendedores = ['João', 'Julia', 'Maria']  
vendedores.remove('Maria')

------------------------------------------------------------

{Magenta}pop(){Reset}
{Amarelo}list.pop(posicao){Reset}
Remove o item pelo índice e retorna o valor removido.

{CyanClaro}Exemplo{Reset}:
vendedores = ['João', 'Julia', 'Maria']  
vendedores.pop(2)

------------------------------------------------------------

{Magenta}clear(){Reset}
{Amarelo}list.clear(){Reset}
Remove todos os itens da lista.

{CyanClaro}Exemplo{Reset}:
vendedores.clear()  
Resultado: []

------------------------------------------------------------

{Magenta}index(){Reset}
{Amarelo}list.index(valor){Reset}
Retorna o índice do valor na lista.

{CyanClaro}Exemplo{Reset}:
vendedores.index('João') {Azul}→{Reset} 0

------------------------------------------------------------

{Magenta}count(){Reset}
{Amarelo}list.count(valor){Reset}
Conta quantas vezes o valor aparece.

{CyanClaro}Exemplo{Reset}:
['João', 'Ana', 'João'].count('João') {Azul}→{Reset} 2

------------------------------------------------------------

{Magenta}sort(){Reset}
{Amarelo}list.sort(reverse=False){Reset}
Ordena a lista (crescente ou decrescente).

{CyanClaro}Exemplo{Reset}:
vendas.sort(reverse=True)

------------------------------------------------------------

{Magenta}reverse(){Reset}
{Amarelo}list.reverse(){Reset}
Inverte a ordem da lista.

------------------------------------------------------------

{Magenta}copy(){Reset}
{Amarelo}list.copy(){Reset}
Cria uma cópia da lista.

{Amarelo}Alternativa{Reset}:
{Amarelo}lista2 = lista1[:]{Reset}

------------------------------------------------------------

{Magenta}Resumo rápido:{Reset}

append / extend {Azul}→{Reset} adicionar  
remove / pop   {Azul}→{Reset} remover  
index / count  {Azul}→{Reset} buscar  
sort / reverse {Azul}→{Reset} ordenar  
copy {Azul}→{Reset} copiar""")
