import lista_tarefas as tf

def listar_tarefas():

    print('============================================')
    print('\033[33m Tarefas:\033[33m')
    for tarefa in tf.todas_tarefas:
        print(tarefa)
    print('============================================')
    print('\033[33m 1. Listar Novamente as Tarefas\033[33m')
    print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
    resposta_ltf = input('\033[33m Escolha um número como opção:\033[33m')
    if resposta_ltf == "1":
        listar_tarefas()
    elif resposta_ltf == "2":
        print('============================================')
        return
    else:
        print('============================================')
        print('\033[33m Opção inválida! Tente novamente.\033[33m')

