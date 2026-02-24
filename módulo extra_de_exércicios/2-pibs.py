### Desafio (esse exercício é mais difícil mesmo)
# Com o PIB de 2022 e de 2021 de cada estado brasileiro, descubra: 
# qual o maior PIB, menor PIB, média do PIB, PIB total em cada ano e
# qual estado mais cresceu o PIB percentualmente e 
# em valores absolutos de um ano pro outro

#resolução👇:

pib_2022 = {
    "Acre": 21374,
    "Alagoas": 76266,
    "Amapá": 20100,
    "Amazonas": 131531,
    "Bahia": 352618,
    "Ceará": 194885,
    "Distrito Federal": 286944,
    "Espírito Santo": 186337,
    "Goiás": 269628,
    "Maranhão": 124981,
    "Mato Grosso": 233390,
    "Mato Grosso do Sul": 142204,
    "Minas Gerais": 857593,
    "Paraná": 549973,
    "Paraíba": 77470,
    "Pará": 262905,
    "Pernambuco": 220814,
    "Piauí": 64028,
    "Rio de Janeiro": 949301,
    "Rio Grande do Norte": 80181,
    "Rio Grande do Sul": 581284,
    "Rondônia": 58170,
    "Roraima": 18203,
    "Santa Catarina": 428571,
    "Sergipe": 51861,
    "São Paulo": 2719751,
    "Tocantins": 51781}


pib_2021 = {
    "Acre": 16476,
    "Alagoas": 63202,
    "Amapá": 18469,
    "Amazonas": 116019,
    "Bahia": 305321,
    "Ceará": 166915,
    "Distrito Federal": 265847,
    "Espírito Santo": 138446,
    "Goiás": 224126,
    "Maranhão": 106916,
    "Mato Grosso": 178650,
    "Mato Grosso do Sul": 122628,
    "Minas Gerais": 682786, 
    "Paraná": 487931,
    "Paraíba": 70292,
    "Pará": 215936,
    "Pernambuco": 193307,
    "Piauí": 56391,
    "Rio de Janeiro": 753824,
    "Rio Grande do Norte": 71577,
    "Rio Grande do Sul": 470942, 
    "Rondônia": 51599,
    "Roraima": 16024,
    "Santa Catarina": 349275,
    "Sergipe": 45410,
    "São Paulo": 2377639,
    "Tocantins": 43650 }


#Passo a Passo do Desafio:
# 1º Passo: Retirar apenas o valor dos PIB's de cada ano (2022 e 2021) de suas listas;
    #1.1 - Pib 22;
    #1.2 - Pib 21.
# 2º Passo: Inserir esses valores em listas separadas (algo como: pibs 22 [] e pib 21 []);
# 3º Passo: Após ter essas novas duas listas apenas com os pibs; fazer um for enumerate para realizar 
# as operações de:
    # 3.1 - o maior PIB, 
    # 3.2 - menor PIB, 
    # 3.3 - média do PIB, 
    # 3.4 - PIB total em cada ano, e 
    # 3.5 - Qual estado mais cresceu o PIB percentualmente e em valores absolutos de um ano pro outro 