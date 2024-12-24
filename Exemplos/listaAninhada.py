#importando biblioteca e colocando um apelido para ficar mais fácil o uso
import numpy as np

#Listas Aninhadas:

#Crie uma lista de numeros inteiros listas para representar uma matriz 3x3.
listaMatriz = [
                [1,2,3],
                [4,5,6],
                [7,8,9]    
              ]
#Acesse o elemento na segunda linha e terceira coluna.
elemento = listaMatriz[1][2]
print(elemento)

#Calcule a soma de todos os elementos da matriz.

#Exemplo de forma aninhada
soma_total = 0
for linha in listaMatriz:
    for elemento in linha:
        soma_total += elemento

print("A soma de todos os elementos usando aninhamento é:", soma_total)

#Exemplo usando List Comprehension e a função sum()
soma_total = sum(elemento for linha in listaMatriz for elemento in linha)
print("A soma de todos os elementos usando List Comprehension e a função sum() é:", soma_total)

#Exemplo usando a biblioteca NumPy (para matrizes maiores)
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

soma_total = np.sum(matriz)
print("A soma de todos os elementos usando a biblioteca Numpy é:", soma_total)

