# Crie uma Agenda , onde o usuário possa CRIAR um novo contato (Nome,Telefone) , BUSCAR e DELETAR esse contato.

# Criando dicionário
agenda = {}

# Função cria menu de opções
def menu():
    print("----- Agenda Telefônica -----")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Remover Contato")
    print("4. Sair")
    print("-------------------------")

# Função adiciona contato

def addContato(agenda):
    nome = input("Nome contato: ")
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
   

# Função busca contato
def buscaContato():
    nome = input("Qual nome deseja buscar? ")
    if nome in agenda:
        print(f"O telefone de {nome} buscado é {agenda[nome]}")
    else:
        print(f"{nome} não encontrado!")
   


# Função deleta contato
def delContato():
    nome = input("Digite o nome da pessao que deseja excluir da agenda: ")
    if nome in agenda:
        del agenda[nome]
        print(f"{nome} deletado com sucesso!")
    else:
        print(f"{nome} não encontrado na agenda!")


# Principal do programa

while True:
    menu()
    opcao =  int(input("Escolha as opções acima da Agenda:"))
    
    if opcao == 1:
        addContato(agenda)
    elif opcao ==2:
        buscaContato()
    elif opcao == 3:
        delContato()
    else: 
        break

print(agenda)
