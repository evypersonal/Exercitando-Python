import add_tarefa as add
import remove_tarefa as rm
import mark_tarefa as mark
import all_tarefas as allt
import pendence_tarefa as pt
import done_tarefa as dt

# MENU
def menu():
    print('\033[33m             🏠  M E N U  🏠\n\033[33m')
    print('\033[33m 1.    ➕    Adicionar Tarefa\n\033[33m')
    print('\033[33m 2.    ➖    Remover Tarefa\n\033[33m')
    print('\033[33m 3.    ✅    Marcar Tarefa Como Concluída\n\033[33m')
    print('\033[33m 4.    📘    Listar Todas As Tarefas\n\033[33m')
    print('\033[33m 5.    📕    Listar Tarefas Pendentes\n\033[33m')
    print('\033[33m 6.    📗    Listar Tarefas Concluídas\n\033[33m')
    print('\033[33m 7.    🚫    Sair\n\033[33m')

# PROGRAMA
menu()
resposta = input('\033[33m Escolha um número como opção: \033[33m')
while resposta != "7":
    if resposta == "1":
        add.add_tarefa()
        menu()
        resposta = input('\033[33m Escolha um número como opção:\033[33m')
    elif resposta == "2":
        rm.remove_tarefa()
        menu()
        resposta = input('\033[33m Escolha um número como opção:\033[33m')
    elif resposta == "3":
        mark.mark_tarefa()
        menu()
        resposta = input('\033[33m Escolha um número como opção:\033[33m')
    elif resposta == "4":
        allt.listar_tarefas()
        menu()
        resposta = input('\033[33m Escolha um número como opção:\033[33m')
    elif resposta == "5":
        pt.listar_tarefas_pendentes()
        menu()
        resposta = input('\033[33m Escolha um número como opção:\033[33m')
    elif resposta == "6":
        dt.listar_tarefas_concluidas()
        menu()
        resposta = input('\033[33m Escolha um número como opção:\033[33m')
    else:
        print('Opção inválida')
        menu()
        resposta = input('\033[33m Escolha um número como opção:\033[33m')