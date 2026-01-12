from cores import (Negrito, Reset, Azul, Magenta, Amarelo)

print(f"""
{Azul}📘 FORMAT — AULA DE CONSULTA{Reset}

{Magenta}O método format permite criar formatações avançadas para números e textos,
controlando alinhamento, sinais, separadores, casas decimais, porcentagens e moedas.{Reset}


{Azul}🔹 CÓDIGOS DE FORMATAÇÃO 🔹{Reset}

{Amarelo}:<{Reset}  {Magenta}Alinha o texto à esquerda{Reset}  
{Amarelo}:>{Reset}  {Magenta}Alinha o texto à direita{Reset}  
{Amarelo}:^{Reset}  {Magenta}Centraliza o texto{Reset}  
{Amarelo}:+{Reset}  {Magenta}Mostra sempre o sinal do número{Reset}  
{Amarelo}:,{Reset}  {Magenta}Usa vírgula como separador de milhar{Reset}  
{Amarelo}:_{Reset}  {Magenta}Usa _ como separador de milhar{Reset}  
{Amarelo}:e{Reset}  {Magenta}Notação científica{Reset}  
{Amarelo}:f{Reset}  {Magenta}Número com casas decimais fixas{Reset}  
{Amarelo}:x{Reset}  {Magenta}Hexadecimal minúsculo{Reset}  
{Amarelo}:X{Reset}  {Magenta}Hexadecimal maiúsculo{Reset}  
{Amarelo}:%{Reset}  {Magenta}Formato percentual{Reset}


{Azul}🔹 EXEMPLOS DE USO 🔹{Reset}

{Amarelo} → {Magenta}Alinhamento à esquerda{Reset}  
{Amarelo} → {Magenta}Exibição de sinal{Reset}  
{Amarelo} → {Magenta}Moeda com milhar e 2 casas decimais{Reset}  
{Amarelo} → {Magenta}Percentual{Reset}  


{Magenta}A função round() pode ser usada para arredondar valores quando necessário.{Reset}
""")