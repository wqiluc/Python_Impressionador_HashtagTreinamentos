from cores import(Negrito,Reset,Amarelo,Azul,Magenta)
print(f"""
{Azul}==================== FATIAMENTO DE STRINGS🔪🧭 ===================={Reset}

{Magenta}Forma Básica:{Reset}
{Amarelo}texto[inicio:fim]{Reset}
Retorna os caracteres da posição inicio até a posição fim (sem incluir o fim).

{Magenta}Exemplo:{Reset}
precos = "Jan: 25, Fev: 27, Mar: 29"
{Amarelo}precos[0:8]{Reset} → "Jan: 25"
{Amarelo}precos[10:18]{Reset} → "Fev: 27"
{Amarelo}precos[20:29]{Reset} → "Mar: 29"

------------------------------------------------------------

{Magenta}Posição Inicial e Final:{Reset}
{Amarelo}texto[inicio:fim]{Reset}
Define exatamente de onde até onde o texto será fatiado.

{Magenta}Exemplo:{Reset}
precos = "Jan: 25, Fev: 27, Mar: 29"
{Amarelo}precos[5:7]{Reset} → "25"
{Amarelo}precos[11:13]{Reset} → "27"
{Amarelo}precos[21:23]{Reset} → "29"

------------------------------------------------------------

{Magenta}Posição Inicial e Final com Step:{Reset}
{Amarelo}texto[inicio:fim:step]{Reset}
O step define de quantos em quantos caracteres o Python irá pular.

{Magenta}Exemplo:{Reset}
codigo = "1.2.3.4,5,1,2.3.4,7.9"

{Amarelo}codigo[0:7]{Reset} → "1.2.3.4"
{Amarelo}codigo[0:7:2]{Reset} → "1234"
{Amarelo}codigo[8:11]{Reset} → "5,1"
{Amarelo}codigo[12:19]{Reset} → "2.3.4"
{Amarelo}codigo[12:19:2]{Reset} → "234"
{Amarelo}codigo[20:23]{Reset} → "7.9"

------------------------------------------------------------

{Magenta}Observações importantes:{Reset}
{Amarelo}[:]{Reset} → pega a string inteira  
{Amarelo}[::]{Reset} → string inteira  
{Amarelo}[::-1]{Reset} → inverte a string  
{Amarelo}[::2]{Reset} → pula de 2 em 2
""")
