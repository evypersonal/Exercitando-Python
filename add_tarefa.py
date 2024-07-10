import lista_tarefas as lt
# import tarefas
# import datetime #Pesquisar
# import time #Pesquisar

def add_tarefa():
    """Adiciona uma tarefa a lista de tarefas"""
    tarefa = input("Digite a tarefa: ")
    lt.todas_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    print("1. Adicionar nova tarefa")
    print("2. Voltar ao Menu Anterior")
    resposta_adc = input("Escolha um número como opção:")
    if resposta_adc == "1":
        add_tarefa()
    elif resposta_adc == "2":
        tarefas.menu()
    else:
        print("Opção inválida! Tente novamente.")
