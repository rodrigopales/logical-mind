# Dicionário e Conjuntos

# Imagine um dicionário que armazena as notas de alunos

notas = {
"Alice": 8.5,
"Bruno": 7.0,
"Carla": 9.0
}

# Imagine que você tem uma lista de frutas, mas algumas estão repetidas:
frutas = ["maçã", "banana", "laranja", "maçã", "banana"]

# Transformando essa lista ácima em conjunto
# Ao transformar essa lista em um conjunto, você elimina as duplicatas:

frutas_unicas = set(frutas)
print(frutas_unicas) # Saída: {'maçã', 'banana', 'laranja'}

# Criando um Dicionário
aluno = {
"nome": "Daniel",
"idade": 20,
"curso": "Engenharia"
}

# Acessando Dicionário
print(aluno["nome"])

# Adicionando um novo par chave-valor
aluno["nota"] = 9.5

# Atualizando um valor existente
aluno["idade"] = 21

# Usando del Removendo um item
del aluno["curso"]

print(aluno)

# Exemplo Prático: Análise de Texto
# Imagine que você quer analisar um texto e contar a frequência de cada palavra. Com um dicionário, 
# você pode criar um contador para cada palavra:
texto = "Este é um exemplo de texto. Texto é muito legal."
palavras = texto.split()  # Divide o texto em uma lista de palavras
print(palavras)

contador_palavras = {}
for palavra in palavras:
    if palavra in contador_palavras:
        contador_palavras[palavra] += 1
    else:
        contador_palavras[palavra] = 1
print(contador_palavras)

# Criando um Conjunto
numeros = {1, 2, 3, 4, 5}


# Ou transformando uma lista em conjunto:
lista = [1, 2, 2, 3, 4, 4, 5]
numeros_unicos = set(lista)
print(numeros_unicos) # Saída: {1, 2, 3, 4, 5}

# Adicionando e Removendo Elemento

# Adicionando
numeros_unicos.add(6)
# Removendo
numeros_unicos.remove(2)
print(numeros_unicos)

# Operações entre Conjuntos
# União: Combina elementos de ambos os conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
uniao = conjunto_a.union(conjunto_b)
print(uniao) # Saída: {1, 2, 3, 4, 5}

# Interseção: Elementos comuns aos dois conjuntos.
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao) # Saída: {3}

# Diferença: Elementos presentes em um conjunto e não no outro.
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca) # Saída: {1, 2}

# Usando Conjuntos para Encontrar Valores Únicos
# Se você tem uma lista de emails e quer saber quantos emails únicos existem (eliminando
# duplicatas), os conjuntos são ideais.
emails = ["a@exemplo.com", "b@exemplo.com", "a@exemplo.com","c@exemplo.com"]
emails_unicos = set(emails)
print(emails_unicos)