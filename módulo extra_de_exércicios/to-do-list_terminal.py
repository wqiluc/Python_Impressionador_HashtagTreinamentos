(f"""To-Do List no Terminal:
 
Crie um programa para criar uma lista de tarefas para o usuário (mais futuramente no curso, aprenderemos a armazenar essas informações em um banco de dados para essa lista poder ser editada e armazenada)

Seu programa deve pedir as tarefas que o usuário tem que fazer em um dia e, a cada inserção de uma nova tarefa, dizer que a tarefa foi adicionada a lista de tarefas. Quando o usuário digitar apenas enter no seu input (sem inserir nenhuma tarefa, seu programa deve printar a quantidade de tarefas para o dia e a lista de tarefas completa)""")

#resolução👇:
from cores import *
lista_tarefas_concluidas = [ ]
lista_tarefas_pendentes = [ ]

def numero_de_tarefas():
    qtd_tarefas = str(input(f"\n{Negrito}Digite o n.º de tarefas que quer computar: {Reset}")).strip()
    while not (qtd_tarefas.isdigit()):
        print(f"{Vermelho}Termo Inválido!! ❌ Digite UMA QTD de Tarefas (int){Reset}")
        qtd_tarefas = str(input(f"{Negrito}Digite o n.º de tarefas que quer computar: {Reset}")).strip()
    return int(qtd_tarefas)

tarefas = numero_de_tarefas()

for indice_tarefa in range(tarefas):

    tarefa_nova = str(input(f"{Negrito}Digite a {indice_tarefa+1}º Tarefa: {Reset}")).strip()
    while not (tarefa_nova.replace(" ", "", 20).isalpha()):
        print(f"{Vermelho}Termo Inválido!! ❌ Digite uma TAREFA (atividade/str){Reset}")
        tarefa_nova = str(input(f"{Negrito}Digite a {indice_tarefa+1}º Tarefa: {Reset}")).strip().format_map(tarefa_nova)

    status_tarefa = str(input(f"{Negrito}Deseja confirmar a Tarefa: '{tarefa_nova}' como{Reset}{Verde} Concluída?✅{Reset}{Negrito} [S / N]{Reset}")).strip().upper()
    while not (status_tarefa in ["s".upper(),"n".upper()] and status_tarefa.isalpha()):
        print(f"{Vermelho}Termo Inválido!! ❌ Digite uma opção VÁLIDA [S / N]{Reset}")
        status_tarefa = str(input(f"{Negrito}Deseja confirmar a Tarefa: '{tarefa_nova}' como{Reset}{Verde} Concluída?✅{Reset}{Negrito} [S / N]{Reset}")).strip().upper()
    status_tarefa = str(status_tarefa)

    if (status_tarefa=="S"):
        lista_tarefas_concluidas.append(tarefa_nova)
    else:
        lista_tarefas_pendentes.append(tarefa_nova)

print(f"{Negrito}Tarefas{Reset} {Verde}Concluídas✅ 🖋️:{Reset} {Negrito}{lista_tarefas_concluidas}{Reset}")
print(f"{Negrito}Tarefas{Reset} {Vermelho}Pendentes❌ 🖋️:{Reset} {Negrito}{lista_tarefas_pendentes}{Reset}")