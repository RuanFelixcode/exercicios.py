'''5. Lista de Tarefas (To-Do)
Requisitos:
adicionar tarefa
listar tarefas
remover tarefa
Funções:
adicionar_tarefa()
listar_tarefas()
remover_tarefa()'''
tarefas = []
def adicionar_tarefa():
    tarefas_add = input('digite a tarefa:')
    if tarefas_add in tarefas:
        print('tarefa ja esta na lista')
    else:
        tarefas.append(tarefas_add)
        print(f'tarefa {tarefas_add} adicionada na lista')
adicionar_tarefa()

def ver_lista_tarefas ():
    print(tarefas)
ver_lista_tarefas ()

def remover_tarefa():
    rmv = input('digite a tarefa que deseja remover:')
    tarefas.remove(rmv)

remover_tarefa()
