lista_tarefas = []


def adicionar_tarefas(descricao):

    tarefa = {
        "descricao" :descricao,
        "concluida" : False
    }

    lista_tarefas.append(tarefa)


def listar_tarefas():
    for indice, tarefa in enumerate(lista_tarefas):
        status = '[x]' if tarefa['concluido'] else '[]'
        print(f"{indice}. {tarefa['descricao']} [{status}]")


def concluir_tarefa(indice):
    try:
        lista_tarefas[indice]["concluida"] = True

    except IndexError:
        print("erro")

     

print(adicionar_tarefas)
print(listar_tarefas)
print(concluir_tarefa)