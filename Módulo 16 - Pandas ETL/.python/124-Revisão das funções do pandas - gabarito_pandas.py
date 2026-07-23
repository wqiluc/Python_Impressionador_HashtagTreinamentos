# 5 Funções ESSENCIAIS do Pandas que Todo Programador PRECISA Saber

import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo'],
    'Idade': [25, 30, 35, 40, 45],
    'Salário': [3000, None, 7000, None, 11000]
}
tabela = pd.DataFrame(dados)

# describe
print(tabela.describe())

# apply
tabela["Salario Ajustado"] = tabela["Salário"].apply(lambda x: x * 1.1)
print(tabela)

# groupby
# medias_area = tabela.groupby("Área").mean(numeric_only=True)
# print(medias_area)

# fillna
media_salarial = tabela["Salário"].mean()
tabela["Salário"] = tabela["Salário"].fillna(media_salarial)
tabela["Salario Ajustado"] = tabela["Salario Ajustado"].fillna(tabela["Salario Ajustado"].mean())
print(tabela)

# merge

tabela_areas = pd.DataFrame(
{
    "Nome Funcionario": ['Ana', 'Bruno', 'Carlos', 'Eduardo'],
    'Área': ["Administrativo", "Financeiro", "Vendas", "Financeiro"]
}
)
print(tabela_areas)

tabela = tabela.merge(tabela_areas, how="left", left_on="Nome", right_on="Nome Funcionario")
tabela = tabela.drop(columns="Nome Funcionario")
print(tabela)