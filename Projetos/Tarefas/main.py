# Importando módulos que vamos usar no projeto Gerenciador de Tarefas

import json
import os
from datetime import datetime


# Função para carregar as tarefas do arquivo
def carregar_tarefas():
    if os.path.exists('Projetos/Tarefas/tarefas.json'):
        with open('Projetos/Tarefas/tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    else:
        return []

# Função para salvar as tarefas no arquivo
def salvar_tarefas(tarefas):
    with open('Projetos/Tarefas/tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função de gerador de id automático
def gerar_id(tarefas):
    if tarefas:
        ultimo_id = tarefas[-1]['id']
        return ultimo_id + 1
    else:
        return 1

# Função para adicionar tarefa 
def adicionar_tarefa(tarefas):
    print("\nAdicionar Nova Tarefa")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_input = input("Data de conclusão (dd/mm/aaaa): ")
    try:
        data_obj = datetime.strptime(data_input, '%d/%m/%Y')
        data = data_obj.strftime('%d/%m/%Y')
        if data_obj.date() < datetime.now().date():
            print("Data de conclusão não pode ser no passado.")
            return
    except ValueError:
        print("Data em formato inválido. Utilize dd/mm/aaaa.")
        return

    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'data': data,
        'concluida': False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

# Função para listar tarefas
def listar_tarefas(tarefas):
    print("\nTarefas Pendentes:")
    tarefas_pendentes = [t for t in tarefas if not t['concluida']]
    tarefas_pendentes = sorted(tarefas_pendentes, key=lambda x:datetime.strptime(x['data'], '%d/%m/%Y'))
    
    for tarefa in tarefas_pendentes:
        print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Data:{tarefa['data']}")
    print("\nTarefas Concluídas:")
    tarefas_concluidas = [t for t in tarefas if t['concluida']]
    tarefas_concluidas = sorted(tarefas_concluidas, key=lambda x:datetime.strptime(x['data'], '%d/%m/%Y'))
    
    for tarefa in tarefas_concluidas:
        print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Data:{tarefa['data']}")

# Função para marcar tarefa como conluida
def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser concluída:"))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['concluida']:
                    print("A tarefa já está concluída.")
                else:
                    tarefa['concluida'] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída com sucesso!")
        return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido.")

# Função para remover tarefa


def menu():
    print("\n==== Gerenciador de Tarefas Avançado ====")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Pesquisar Tarefas")
    print("6. Ordenar Tarefas por Data")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            pesquisar_tarefas(tarefas)
        elif opcao == '6':
            ordenar_tarefas(tarefas)
        elif opcao == '7':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opçãoválida.")

if __name__ == '__main__':
    main()