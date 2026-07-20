# 📊 Kaggle

<img src="https://img.shields.io/badge/Kaggle-Data%20Science-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white" height="28" alt="Kaggle"/>
<img src="https://img.shields.io/badge/Datasets-p%C3%BAblicos-blue?style=for-the-badge" height="28" alt="Datasets"/>
<img src="https://img.shields.io/badge/Pandas-compat%C3%ADvel-150458?style=for-the-badge&logo=pandas&logoColor=white" height="28" alt="Pandas"/>
<img src="https://img.shields.io/badge/Uso-estudo%2Fexerc%C3%ADcio-lightgrey?style=for-the-badge" height="28" alt="Licença"/>

<p align="center">
<img src="../img/Kaggle.jpeg" width="700" alt="Homepage do Kaggle"/>
<br/>
<sub>Homepage do Kaggle — "The World's AI Proving Ground"</sub>
</p>

## O que é

[Kaggle](https://www.kaggle.com) é uma plataforma (hoje parte do Google) voltada para ciência de dados e machine learning. É conhecida principalmente por quatro coisas:

| Recurso | Descrição |
|---|---|
| 🗂️ **Datasets** | Milhares de bases de dados públicas, de qualquer tema (economia, esportes, saúde, comércio exterior, redes sociais...), enviadas pela comunidade ou por organizações |
| 🏆 **Competitions** | Desafios de machine learning: empresas/pesquisadores publicam um problema + dataset, e a comunidade compete para construir o melhor modelo, geralmente com prêmios em dinheiro |
| 📓 **Notebooks** | Cadernos Jupyter que rodam na nuvem do próprio Kaggle — dá para explorar um dataset e escrever código (Python ou R) sem instalar nada localmente |
| 🎓 **Kaggle Learn** | Cursos curtos e gratuitos (Python, Pandas, SQL, Machine Learning, etc.) |

## Como usar o Kaggle para estudar bases de dados

| Passo | O que fazer |
|---|---|
| 1️⃣ Buscar | Em [kaggle.com/datasets](https://www.kaggle.com/datasets), filtrar por tema, tamanho, tipo de arquivo (CSV, JSON, SQLite...) e popularidade (upvotes) |
| 2️⃣ Ler a documentação | Cada dataset tem a descrição das colunas, a fonte original dos dados e a licença de uso. As abas **Discussion** e **Code** mostram o que outras pessoas já exploraram naquela base |
| 3️⃣ Baixar ou usar na nuvem | Dá para baixar o CSV/Excel e analisar localmente (como neste repositório, com pandas) ou abrir um notebook do próprio Kaggle e rodar tudo de graça na nuvem deles |
| 4️⃣ Praticar limpeza e análise | A maioria dos datasets é "crua" (dados reais, com inconsistências, nulos, colunas mal nomeadas) — ótimo treino de `read_csv`, tratamento de nulos, `groupby`, `merge`, filtros e agregações |
| 5️⃣ Comparar notebooks públicos | Como qualquer pessoa pode publicar sua análise do mesmo dataset, dá pra comparar abordagens diferentes para o mesmo problema |

> No curso Python Impressionador, o Kaggle é usado como fonte de bases de dados **reais** para praticar pandas em exercícios de análise de dados, complementando os datasets didáticos "Contoso" já usados no módulo.

---

## 🇫🇷 A base de dados: exportações do Brasil para a França

**Arquivo:** `spec/Onde pegar exercícios de análise de dados- Kaggle - exportacoes_franca.csv`

<img src="https://img.shields.io/badge/formato-CSV-success?style=for-the-badge" height="28" alt="CSV"/>
<img src="https://img.shields.io/badge/linhas-~142k-orange?style=for-the-badge" height="28" alt="Linhas"/>
<img src="https://img.shields.io/badge/per%C3%ADodo-2016--2020-yellow?style=for-the-badge" height="28" alt="Período"/>
<img src="https://img.shields.io/badge/fonte-Comex%20Stat%20%2F%20MDIC-informational?style=for-the-badge" height="28" alt="Fonte"/>

### Origem

Recorte de um dataset maior de **exportações e importações do Brasil**, construído a partir dos dados públicos do **Comex Stat** (Ministério da Economia/MDIC) e disponibilizado no Kaggle. Este arquivo contém **apenas as exportações do Brasil com destino à França**.

### Estrutura (colunas)

| Coluna | Tipo | Descrição |
|---|---|---|
| `Year` | inteiro | Ano da exportação (2016 a 2020 neste recorte) |
| `Month` | inteiro | Mês da exportação (1 a 12) |
| `Country` | texto | País de destino (sempre `France` neste arquivo) |
| `City` | texto | Cidade brasileira de origem da exportação |
| `SH4 Code` | inteiro | Código do produto no Sistema Harmonizado, nível de 4 dígitos |
| `SH4 Description` | texto | Descrição detalhada do produto (ex.: *"Fish, frozen, excluding fish fillets..."*) |
| `SH2 Code` | inteiro | Código do produto no Sistema Harmonizado, nível de 2 dígitos |
| `SH2 Description` | texto | Categoria mais ampla do produto (ex.: *"Fish and crustaceans, molluscs..."*) |
| `Economic Block` | texto | Bloco econômico do destino (ex.: `Europe`, `European Union (EU)`) |
| `US$ FOB` | numérico | Valor da exportação em dólares, modalidade **FOB** (*Free On Board* — sem frete/seguro internacional) |
| `Net Weight` | numérico | Peso líquido exportado, em quilogramas |

### ⚠️ Pontos de atenção antes de analisar

| Característica | Por que importa |
|---|---|
| **Duplicidade por bloco econômico** | A mesma operação pode aparecer em mais de uma linha (uma vez para `Europe`, outra para `European Union (EU)`) — cuidado ao somar `US$ FOB` para não contar em dobro |
| **~972 cidades brasileiras** | Boa base para praticar `groupby` por cidade/UF (extraindo o estado do nome da cidade) |
| **Hierarquia SH2 → SH4** | Exemplo prático de dados hierárquicos: categoria ampla (SH2) contendo produtos específicos (SH4) |
| **Série temporal** | Colunas `Year` e `Month` permitem estudar evolução mensal/anual e sazonalidade por produto |

### 💡 Exemplos de perguntas para praticar pandas

- Quais produtos (`SH2 Description`) o Brasil mais exportou para a França em valor (`US$ FOB`)?
- Qual foi a evolução mês a mês do valor exportado ao longo de 2016–2020?
- Quais cidades/estados brasileiros mais exportaram para a França?
- Qual o valor médio por quilo (`US$ FOB` / `Net Weight`) por categoria de produto?
- Houve queda nas exportações em 2020 (ano da pandemia) em relação aos anos anteriores?

---

<p align="center">
<img src="https://img.shields.io/badge/M%C3%B3dulo-15%20Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" height="28" alt="Módulo 15 Pandas"/>
</p>
