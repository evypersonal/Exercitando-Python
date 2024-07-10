import lista_tarefas as lt

def listar_tarefas_concluidas():
    print('\033[31m============================================\033[31m')
    print(lt.tarefas_concluidas)
    print('\033[31m============================================\033[31m')
    print('\033[33m 1. Imprimir novamente as tarefas\033[33m')
    print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
    resposta_imp = input('\033[33m Escolha um número como opção:\033[33m')
    if resposta_imp == "1":
        listar_tarefas_concluidas()
    elif resposta_imp == "2":
        print('\033[31m============================================\033[31m')
        return
    else:
        print('\033[31m============================================\033[31m')
        print('\033[33m Opção inválida! Tente novamente.\033[33m')
