from cores import *
from re import fullmatch as padrao

print(f"""{Magenta}
 Analisador de URL
- Seu programa deve pedir um link/URL para o usuário, como por exemplo:{Reset} \n
{Amarelo}https://www.hashtagtreinamentos.com/blog{Reset}{Magenta}
- Ele deve analisar essa URL dizendo:
    - Domínio:{Reset} {Amarelo}hashtagtreinamentos.com{Reset}{Magenta};
    - Protocolo:{Reset} {Amarelo}HTTPS (tudo que vem antes de começar o endereço da URL, no caso antes do :){Reset}{Magenta};
    - Caminho:{Reset} {Amarelo}/blog (tudo que vem depois do domínio, a partir da primeira / até antes dos parâmetros de busca){Reset}{Negrito}; e{Reset}
    - {Magenta}Parâmetros de busca:{Reset} {Amarelo}(Tudo que vem depois do ? e são separados entre si por um &. Os links podem ter isso ou não).{Reset}{Negrito}

Exemplos de URL:{Reset}
{Azul}https://www.hashtagtreinamentos.com/blog
https://lp.hashtagtreinamentos.com/inscricao-intensivao-de-python-igfb?origemurl=curso&fonte=portal
https://lp.hashtagtreinamentos.com/inscricao-intensivao-de-python-igfb?origemurl=exercicios{Reset} """)

# seu código aqui:
url_sites = str(input(f"\n{Negrito}Copie aqui a url que você quer analisar: {Reset}")).strip()
while not (padrao(r"^(https?)://([\w.-]+)(/[^?]*)?(\?.*)?$",(f"{url_sites}"))):
    print(f"{Vermelho}URL Inválida!! ❌⚠️ Copie novamente. {Reset}")
    url_sites = str(input(f"{Negrito}Copie aqui a url que você quer analisar: {Reset}")).strip()

print(f"{Negrito}URL do site: {url_sites[0:].lower()}{Reset}")