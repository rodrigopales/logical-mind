# Manipulação de Strings

# Concatenação = juntar uma ou mais strings usando o operador +

nome = "Alice"
sobrenome = "Pales"
print(nome + " " + sobrenome)

# Repetição = multiplicar uma string por um número para repetir seus caracteres

asteriscos = "*" * 10
print(asteriscos) 

# Indexação = acessar caracteres individuais de uma string utilizando colchetes. O primeiro caractere tem o índice 0

palavra = "Python"
primeiraLetra = palavra[0]
print(primeiraLetra)

# Fatiamento = extrair partes de uma string utilizando colchetes com dois índices separados por dois pontos

frase = "Olá,mundo!"
subfrase = frase[4:9]
print(subfrase)

# Comprimento da String , descobrir quantos caracteres tem sua String

texto = "Aprendendo Pyhton"
tamanho = len(texto)

# Formatação usando format() não é muito utilizada
print("O texto tem {} caracteres.".format(tamanho))

# Formatação usando f-strings uma versão mais simples do que o format() e mais elagante também
print(f"O texto tem {tamanho} caracteres.")


# Métodos comuns de Strings

# upper() Transforma todos os caracteres em maiúsculas
texto = "      Bom dia!          "
print(texto.upper())

# lower() Transforma todos os caracteres em minusculas
print(texto.lower())

# title() Coloca a primeira letra de cada palavra maiúscula
print(texto.title())

# strip() Remove espaços em branco no ício e no fim da string
print(texto.strip())

# replace() Substitui uma parte da string por outra
novaFrase = texto.replace("dia!","te ver!")
print(novaFrase.strip())

# find() Encontra a posição de uma substring dentro da string
posicao = texto.find("dia!")
print (f"dia! está na posição {posicao}")

# split() Divide a string em uma lista, usando um separador
dados = "maçã,banana,laranja"
listaFrutas = dados.split()
print(listaFrutas)

# join() Junta elementos de uma lista em uma string
listaPalavras = ["Python", "é" , "legal"]
frase = " ".join(listaPalavras)
print(frase)


# contador de vogais , usuário digita uma frase e o contador conta as vogais que existe na frase

frase = input("Digite uma frase para descobrir a quantidade de vogais: ")
vogais = "aeiou"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1
    
print(f"A quandidade de vogais na frase {frase} é {contador} vogais!")