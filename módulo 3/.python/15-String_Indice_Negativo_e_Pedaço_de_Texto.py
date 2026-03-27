from cores import Azul, Magenta, Amarelo, Reset

print(f"""
{Azul}String: Índice Negativo e Pedaço de Texto{Reset}

{Magenta}Este conteúdo demonstra como manipular strings em Python utilizando:{Reset}
{Magenta}- Índices negativos para acessar caracteres de trás para frente{Reset}
{Magenta}- Fatiamento (slicing) de textos com dois pontos (:){Reset}
{Magenta}- A função len() para obter o tamanho de uma string{Reset}

{Amarelo}Índices positivos:{Reset}
{Amarelo}Começam em 0 e seguem da esquerda para a direita{Reset}

{Amarelo}Índices negativos:{Reset}
{Amarelo}Começam em -1 e seguem da direita para a esquerda{Reset}

{Amarelo}Fatiamento de strings:{Reset}
{Amarelo}texto[:indice]   -> do início até o índice{Reset}
{Amarelo}texto[indice:]   -> do índice até o final{Reset}
{Amarelo}texto[inicio:fim] -> intervalo específico do texto{Reset}
""")
