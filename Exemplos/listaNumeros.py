

#Métodos de Listas:

#Crie uma lista com números de 1 a 10.
listaNumeros = list(range(1,11))
print(listaNumeros)

#Ordene a lista em ordem crescente.
listaNumeros.sort()
print(listaNumeros)

#Inverte a ordem da lista.
listaNumeros.reverse()
print(listaNumeros)

#Conte quantas vezes o número 5 aparece na lista.
contagem = listaNumeros.count(1)
print(f"O numero 5 aparece {contagem} na lista")

listaNumeros.sort()


#Encontre o índice do número 8 na lista.
for i, numero in enumerate(listaNumeros):
    if numero == 8:
        print(f"A posição do numero 8 é {i}")