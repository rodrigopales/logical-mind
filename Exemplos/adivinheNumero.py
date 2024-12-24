import random
#Crie um jogo em que o programa escolhe um número aleatório entre 1 e 100 , e o usuário tente adivinhar.
#O programa deve dar dicas se o número é maior ou menor do que o palpite.O jogo continua até o usuário acertar.

# Gera um número aleatório entre 1 e 50 e armazena em numeroSecreto
numeroSecreto = random.randint(1,50)

# Inicializa um contador para registrar o número de tentativas
tentativas = 0

# Imprime as regras do jogo
print("Jogo de adivinhação , ganha quem acerta com um menor numeros de tentativas ")

# Loop principal do jogo, continua até o jogador acertar
while True:
    # Solicita ao usuário que digite um número e converte para inteiro
    numeroUsuario = int(input("Digite o numero: "))

    # Incrementa o contador de tentativas
    tentativas += 1

    # Verifica se o número digitado é igual ao número secreto
    if numeroUsuario == numeroSecreto:
        # Se acertou, imprime a mensagem de vitória e finaliza o loop
        print(f"Você acertou com {tentativas} tentativas!")
        break

    # Se o número digitado for menor que o número secreto
    elif numeroUsuario < numeroSecreto:
        print("Numero digitado é menor que o numero secreto!")

    # Se o número digitado for maior que o número secreto
    else:
        print("Numero digitado é maior que o numero secreto")