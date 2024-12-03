#Lista de (array) e tuplas
#Interligados com os loops - estrutura de repetição

marcaCaminhoes = ['Volvo','Mercedes Benz','Iveco','Man']

#Os indices começam a contar de 0
print(marcaCaminhoes[0])
print(marcaCaminhoes[1])
print(marcaCaminhoes[2])
print(marcaCaminhoes[3])


#Lista de convidados.Crie uma lista de convidados e exiba uma mensagem personalisada para cada um.

lista = ['Marcelo' , 'Davi' , 'Veronica']

for convidado in lista:
    print(f"Bem vindo {convidado} você é um convidado especial")


# Solicita ao usuário que digite uma sequência de números separados por espaço
entrada = input("Digite números separados por espaço: ")

# Converte a entrada do usuário em uma lista de números float
numeros = [float(num) for num in entrada.split()]

# Encontra o maior número na lista
maior_numero = max(numeros)

# Encontra o menor número na lista
menor_numero = min(numeros)

# Calcula a soma de todos os números na lista
soma_numeros = sum(numeros)

# Calcula a média dos números dividindo a soma pela quantidade de números
media_numeros = soma_numeros / len(numeros)

# Imprime os resultados na tela
print("Maior número:", maior_numero)
print("Menor número:", menor_numero)
print("Soma dos números:", soma_numeros)
print("Média dos números:", media_numeros)


# Solicita ao usuário que digite uma frase e converte para letras minúsculas
frase = input("Digite uma frase: ").lower()

# Cria um dicionário vazio para armazenar a contagem de cada letra
letras = {}

# Itera sobre cada caractere da frase
for caractere in frase:
    # Verifica se o caractere é uma letra (alfabeto)
    if caractere.isalpha():
        # Se a letra já existe no dicionário, incrementa a contagem
        if caractere in letras:
            letras[caractere] += 1
        # Caso contrário, adiciona a letra ao dicionário com contagem 1
        else:
            letras[caractere] = 1

# Itera sobre os itens do dicionário (letra e contagem) e imprime o resultado
for letra, contagem in letras.items():
    print(f"A letra '{letra}' aparece {contagem} vez(es).")
