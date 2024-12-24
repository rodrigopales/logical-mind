# Contador de palavras em um Arquivo

nome_arquivo = input("Digite o nome do arquivo: ")
try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
else:
    palavras = conteudo.lower().split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.strip('.,!?";:-()')
        if palavra in contagem:
            contagem[palavra] += 1
        else:
         contagem[palavra] = 1
    for palavra, quantidade in contagem.items():
        print(f"{palavra}: {quantidade}")