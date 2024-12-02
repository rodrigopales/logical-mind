#Crie um jogo da forca simples em que o usuário deve adivinhar uma palavra letra por letra.
palavra_secreta = "python"
letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0 and "_" in letras_descobertas:
    print("Palavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for idx, letra_secreta in enumerate(palavra_secreta):
            if letra == letra_secreta:
                letras_descobertas[idx] = letra
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print(f"Errou! Você tem {tentativas} tentativas restantes.")

if "_" not in letras_descobertas:
    print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)