import os

os.system("cls")

from tarefas import adicionar_tarefas, listar_tarefas,concluir_tarefa,carregar_dados,salvar_dados


carregar_dados()


while True:
    print("-- [1]Adicionar --")
    print("-- [2]listar --")
    print("-- [3]conluir tarefas --")
    print("-- [0]sair --")

    try:
        opcao = int(input("escolha uma das opções:"))
    except ValueError:
        print("Digite um número válido!")
        continue


    match opcao:

        case 1:
            descricao = input("escrever o nome da tarefa: ")
            adicionar_tarefas(descricao)
            salvar_dados()

        case 2:
            listar_tarefas()
            
        case 3:

            try:
                indice = int(input("digite o número da tarefa que deseja concluir:"))
                concluir_tarefa(indice)
                salvar_dados()
            except ValueError:
                print("falha, número inválido !!")
            
        case 0:
            print("saindo...")
            break
        
        case _:
            print("opção inválida")