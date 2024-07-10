import add_tarefa as add
import remove_tarefa as rm
import mark_tarefa as mark

# MENU
def menu():
    print("Menu:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Marcar Tarefa Como Concluída")
    print("4. Listar Todas As Tarefas")
    print("5. Listar Tarefas Pendentes")
    print("6. Listar Tarefas Concluídas")
    print("7. Sair")

# PROGRAMA
menu()
resposta = input("Escolha um número como opção:")
while resposta != "7":
    if resposta == "1":
        add.add_tarefa()
    elif resposta == "2":
        rm.remove_tarefa()
    elif resposta == "3":
        mark.mark_tarefa()
    elif resposta == "4":
        add.listar_tarefas()
    elif resposta == "5":
        add.listar_tarefas_pendentes()
    elif resposta == "6":
        add.listar_tarefas_concluidas()
    else:
        print("Opção inválida")
        menu()








