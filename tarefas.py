lista_tarefas = []


def adicionar_tarefas(descricao):

    tarefa = {
        "descrição" :descricao,
        "concluída" : False
    }

    lista_tarefas.append(tarefa)


def listar_tarefas():
    for descricao in lista_tarefas:
        print(descricao)
        

def concluir_tarefa(indice)


print(adicionar_tarefas)
print(listar_tarefas)