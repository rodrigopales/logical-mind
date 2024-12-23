# Tratamento de Erros e Exceções
# Criar programas que precisam está a prova de falhas

# try, except, else, finally

# try => tentando fazer algo
# except => tratar um erro
# else => para uma condição positiva
# finally => que roda sempre, independente da situação

# outras linguagens => except = catch

try:
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo 'arquivo.txt' não foi encontrado.")
else:
    print("Arquivo lido com sucesso!")
    print(conteudo)
finally:
    print("Operação de leitura de arquivo finalizada.")
    # Liberar memória
    if 'arquivo' in locals():
        arquivo.close()
        print("Arquivo fechado!")

# Tratamento de erro para o usuário 
try:
    numero = int(input("Digite um numero: "))
    resultado = 100 / numero
except ValueError:
    print("Entrada inválida, tente novamente")
except ZeroDivisionError:
    print("Divisão por 0!")
else:
    print(f"O resultado é:{resultado}")
finally:
    print("Operação finalizada")

# Tratamento de erro para o programador simplificando o código e usando erros do python mesmo para debugar
try:
    numero = int(input("Digite um numero: "))
    resultado = 100 / numero
except (ValueError,ZeroDivisionError) as error:
    print("Erro: ", error)
else:
    print(f"O resultado é:{resultado}")
finally:
    print("Operação finalizada")