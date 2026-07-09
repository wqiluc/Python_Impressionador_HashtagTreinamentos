# Python Impressionador — Hashtag Treinamentos

Repositório de estudos do curso **Python Impressionador** (Hashtag Treinamentos). Contém as aulas e exercícios de cada módulo do curso, em Jupyter Notebook e em script Python puro.

## Estrutura do repositório

Cada módulo é uma pasta própria na raiz (`módulo 1`, `módulo 2`, ..., `Módulo 15 - pandas`, `módulo extra_de_exércicios`), sempre com o mesmo padrão interno:

- `.ipynb/` (ou `ipynb/` nos módulos 13 e 14) — os notebooks das aulas, numerados sequencialmente pelo número global da aula (ex.: `47-While 01.ipynb`).
- `.python/` (ou `python/` nos módulos 13 e 14) — o mesmo conteúdo das aulas em `.py` puro, quando existe uma versão em script.
- `cores.py` — helper com códigos ANSI de cores para saída no terminal (`Preto`, `Vermelho`, `Verde`, ...), reaproveitado em quase todos os módulos.
- `__pycache__/` — bytecode compilado, não versionar mudanças aqui.

Exceções e conteúdo extra por módulo:
- `módulo 13/ipynb/` também tem `database.py` (dados mockados) e `tabela_funcionarios.xlsx`.
- `módulo 12/.python/` e `módulo 14/.python/` têm `__init__.py` (pasta tratada como pacote).
- `Módulo 15 - pandas/spec/` guarda os CSVs de apoio (dataset "Contoso") usados nos exercícios de pandas.
- `módulo extra_de_exércicios/` reúne exercícios avulsos e não segue a numeração de aula — os arquivos têm nomes descritivos (`2-validar_senha.py`, `to-do-list_terminal.py`, etc.) e várias versões (`v1`, `v2`, `v3`) do mesmo exercício conforme evolui a solução.

Ver detalhes de cada módulo em [SKILLS.md](SKILLS.md).

## Convenções observadas

- Numeração de arquivo = número global da aula no curso, não reinicia a cada módulo.
- Nomes de arquivos e pastas em português, com acentos — preservar ao criar/mover arquivos.
- Cada módulo é independente: `cores.py` é duplicado em cada pasta em vez de compartilhado.
- Ambiente: `.venv/` local (Python 3.14), não versionado.

## Ao trabalhar neste repositório

- Este é um repositório de estudo/aprendizado, não uma aplicação em produção — priorize clareza didática sobre abstrações genéricas.
- Ao adicionar uma nova aula/exercício, siga o padrão existente do módulo (mesma dupla notebook + script, mesmo estilo de nome de arquivo).
- Não é necessário rodar testes automatizados; para validar um script ou notebook, execute-o diretamente com Python/Jupyter.
