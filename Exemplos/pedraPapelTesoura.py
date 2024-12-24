
import random

# Crieum programa que simulao jogo"Pedra,PapelouTesoura"entre o usuário e o computador
# Lista com as opções possíveis do jogo
opcoes = ["pedra", "papel", "tesoura"]

# Solicita ao usuário que escolha uma opção e converte para letras minúsculas
usuario = input("Escolha pedra, papel ou tesoura: ").lower()

# O computador escolhe aleatoriamente uma opção da lista
computador = random.choice(opcoes)

# Imprime as escolhas do usuário e do computador
print(f"Você escolheu: {usuario}")
print(f"O computador escolheu: {computador}")

# Verifica se houve empate
if usuario == computador:
    print("Empate")
# Verifica todas as combinações de vitória do usuário
elif (usuario == "pedra" and computador == "tesoura") or \
     (usuario == "papel" and computador == "pedra") or \
     (usuario == "tesoura" and computador == "papel"):
    print("Você venceu!")
# Se o usuário escolheu uma opção válida, mas não ganhou, ele perdeu
elif usuario in opcoes:
    print("Você perdeu!")
# Se a escolha do usuário não está na lista de opções, é inválida
else:
    print("Escolha inválida")