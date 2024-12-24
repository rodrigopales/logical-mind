# Crie uma Agenda , onde o usuário possa CRIAR um novo contato (Nome,Telefone) , BUSCAR e DELETAR esse contato.

# Criando dicionário
agenda = {}

# Função cria menu de opções
def menu():
    print("----- Agenda Telefônica -----")
    print("1. Adicionar Contato")
    print("2. Atualizar Contato")
    print("3. Buscar Contato")
    print("4. Remover Contato")
    print("5. Listar Contatos")
    print("6. Sair")
    print("-------------------------")

# Função adiciona contato

def addContato(agenda):
    nome = input("Nome contato: ").upper()
    telefone = input("Telefone Contato:")
    
    # Validação básica: verificar se o nome digitado é vazio
    if not nome:
        print("O nome do contato não pode ser vazio.")
        return False
    
    # Vereificando se o nome já tem cadastro
    if nome in agenda:
        print(f"{nome} já cadastrado na agenda!")
        return False

    agenda[nome] = telefone
    print(f"{nome} adicionado com sucesso!")
    return True


# Funcao para atualizar contato
def atualizaContato(agenda):
    nome = input("Digite o nome para atualizar o telefone:")
    if nome in agenda:
        telefone = input(f"Digite novo numero para {nome} : ")
        agenda[nome] = telefone
    else:
        print("Nome não encontrado para atualização!")


# Função busca contato
def buscaContato(agenda):
    nome = input("Qual nome deseja buscar? ")
    if nome in agenda:
        print(f"O telefone de {nome} buscado é {agenda[nome]}")
    else:
        print(f"{nome} não encontrado!")
   


# Função deleta contato
def delContato(agenda):
    nome = input("Digite o nome da pessao que deseja excluir da agenda: ")
    if nome in agenda:
        del agenda[nome]
        print(f"{nome} deletado com sucesso!")
    else:
        print(f"{nome} não encontrado na agenda!")

# Função para listar agenda completa por ondem alfabética
def listarAgenda(agenda):
    if not agenda:
       print("Agenda vazia!")  
    for nome in sorted(agenda):
            print(f"{nome}: {agenda[nome]}") 
    
            


# Principal do programa

while True:
    menu()
    opcao =  int(input("Escolha as opções acima da Agenda:"))
        
    if opcao == 1:
        addContato(agenda)
    elif opcao ==2:
        atualizaContato(agenda)
    elif opcao == 3:
        buscaContato(agenda)
    elif opcao == 4:
        delContato(agenda)
    elif opcao == 5:
        listarAgenda(agenda)
    elif opcao == 6:
        break
    else: 
        print("Opção não encontrada tente novamente!")

print(agenda)
