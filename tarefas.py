import json



lista_tarefas = []

def salvar_dados():
    with open("dados.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo, indent=4)


def carregar_dados():
    global lista_tarefas
    try:
        with open("dados.json", "r") as arquivo:
            lista_tarefas = json.load(arquivo,)
    except FileNotFoundError:
        print("erro: lista não encontrada!!")
        lista_tarefas = []
        salvar_dados()

    


def adicionar_tarefas(descricao):

    tarefa = {
        "descricao" :descricao,
        "concluida" : False
    }

    lista_tarefas.append(tarefa)


def listar_tarefas():
    for indice, tarefa in enumerate(lista_tarefas):
        status = "✔" if tarefa["concluida"] else "❌"
        print(f"{indice}. {tarefa['descricao']} [{status}]")


def concluir_tarefa(indice):
    try:
        lista_tarefas[indice]["concluida"] = True
    except IndexError:
        print("erro")

     

print(adicionar_tarefas)
print(listar_tarefas)
print(concluir_tarefa)