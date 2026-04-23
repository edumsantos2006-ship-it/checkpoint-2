from tarefas import adicionar_tarefas, listar_tarefas,concluir_tarefa


while True:
    print("-- [1]Adicionar --")
    print("-- [2]listar --")
    print("-- [3]conluir tarefas --")
    print("-- [0]sair --")

    opcao = int(input("escolha uma das opções:"))


    match opcao:
        case 1:
            descricao = input("escrever o nome da tarefa: ")
            adicionar_tarefas(descricao)
        case 2:
            listar_tarefas()
            
        case 3:
            try:
                indice = int(input("digite o número da tarefa que deseja concluir:"))
                concluir_tarefa(indice)

            except ValueError:
                print("falha, tente um número válido !!")
            
        case 0:
            print("saindo...")
            break
        case _:
            print("opção inválida")