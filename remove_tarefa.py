import lista_tarefas as lt

def remove_tarefa():
    """Remove a tarefa da lista de tarefas"""
    print('\033[31m============================================\033[31m')
    print(lt.todas_tarefas)
    tarefa = input('\033[33m Digite a tarefa que deseja remover: \033[33m')
    
    if tarefa != '':
        lt.todas_tarefas.discard(tarefa)
        print('\033[31m============================================\033[31m')
        print('\033[33m Tarefa removida com sucesso!✅\033[33m')
        print(lt.todas_tarefas)
        print('\033[31m============================================\033[31m')
        print('\033[33m 1. remover nova tarefa\033[33m')
        print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
        resposta_rmv = input('\033[33m Escolha um número como opção:\033[33m')
        if resposta_rmv == "1":
            remove_tarefa()
        elif resposta_rmv == "2":
            print('\033[31m============================================\033[31m')
            return
        else:
            print('\033[31m============================================\033[31m')
            print('\033[33m Opção inválida! Tente novamente.\033[33m')
            print('\033[31m============================================\033[31m')
            print('\033[33m 1. Remover nova tarefa\033[33m')
            print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
            resposta_rmv2 = input('\033[33m Escolha um número como opção:\033[33m')
            if resposta_rmv2 == "1":
                remove_tarefa()
            elif resposta_rmv2 == "2":
                print('\033[31m============================================\033[31m')
                return
    else:
        print('\033[31m============================================\033[31m')
        print('\033[33m Digite uma tarefa válida\033[33m')
        remove_tarefa()