import lista_tarefas as lt


def mark_tarefa():
    """Marcar as tarefas concluidas"""
    print('\033[31m============================================\033[31m')
    print (lt.todas_tarefas.symmetric_difference(lt.tarefas_concluidas))
    resposta_mark = input('\033[33m Digite a tarefa que deseja marcar:\033[33m')
    lt.tarefas_concluidas.add(resposta_mark)
    print('\033[31m============================================\033[31m')
    print('\033[33m Tarefa marcada com sucesso!✅\033[33m')
    print (lt.tarefas_concluidas)
    print('\033[31m============================================\033[31m')
    print('\033[33m 1. Marcar nova tarefa\033[33m')
    print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
    resposta_mrk = input('\033[33m Escolha um número como opção:\033[33m')
    if resposta_mrk == "1":
        mark_tarefa()
    elif resposta_mrk == "2":
        print('\033[31m============================================\033[31m')
        return
    else:
        print('\033[31m============================================\033[31m')
        print('\033[33m Opção inválida! Tente novamente.\033[33m')
        print('\033[31m============================================\033[31m')
        print('\033[33m 1. Adicionar nova tarefa\033[33m')
        print('\033[33m 2. Voltar ao Menu Anterior\033[33m')
        resposta_mark2 = input('\033[33m Escolha um número como opção:\033[33m')
        if resposta_mark2 == "1":
            mark_tarefa()
        elif resposta_mark2 == "2":
            print('\033[31m============================================\033[31m')
            return


