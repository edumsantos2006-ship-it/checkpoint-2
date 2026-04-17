from tarefas import adicionar_tarefas, listar_tarefas


while True:
    print("-- [1]Adicionar --")
    print("-- [2]listar --")
    print("-- [0]sair --")

    opcao = int(input("escolha uma das opções:"))


    match opcao:
        case 1:
            descricao = input("escrever o nome da tarefa: ")
            adicionar_tarefas(descricao)
        case 2:
            listar_tarefas()
        case 0:
            break
        case _:
            print("opção inválida")