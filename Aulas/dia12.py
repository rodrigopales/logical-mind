# Tratamento de Erros e Exceções
# Criar programas que precisam está a prova de falhas

# try, except, else, finally

# try => tentando fazer algo
# except => tratar um erro
# else => para uma condição positiva
# finally => que roda sempre, independente da situação

try:
    arquivo = open("arquivso.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo 'arquivo.txt' não foi encontrado.")
else:
    print("Arquivo lido com sucesso!")
    print(conteudo)
finally:
    print("Operação de leitura de arquivo finalizada.")