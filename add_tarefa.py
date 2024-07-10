import lista_tarefas as lt
# import tarefas
# import datetime #Pesquisar
# import time #Pesquisar

def add_tarefa():
    """Adiciona uma tarefa a lista de tarefas"""
    print('\033[31m============================================\033[31m')
    tarefa = input('\033[33m Digite a tarefa: \033[33m')
    if tarefa != '':
        lt.todas_tarefas.add(tarefa)
        print('\033[31m============================================\033[31m')
        print('\033[33m Tarefa adicionada com sucesso! ✅\033[33m')
        print(lt.todas_tarefas)
        print('\033[31m============================================\033[31m')
        print('\033[33m 1. Adicionar nova tarefa\033[33m')
        print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
        resposta_adc = input('\033[33m Escolha um número como opção:\033[33m')
        if resposta_adc == "1":
            add_tarefa()
        elif resposta_adc == "2":
            print('\033[31m============================================\033[31m')
            return
        else:
            print('\033[31m============================================\033[31m')
            print('\033[33m Opção inválida! Tente novamente.\033[33m')
            print('\033[31m============================================\033[31m')
            print('\033[33m 1. Adicionar nova tarefa\033[33m')
            print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
            resposta_adc2 = input('\033[33m Escolha um número como opção:\033[33m')
            if resposta_adc2 == "1":
                add_tarefa()
            elif resposta_adc2 == "2":
                print('\033[31m============================================\033[31m')
                return
    else:
        print('\033[33m Digite uma tarefa válida\033[33m')
        add_tarefa()

