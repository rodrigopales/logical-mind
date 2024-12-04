#Crie uma lista com os seguintes elementos: "maçã", "banana", "laranja".
#Acesse o segundo elemento da lista.
#Modifique o primeiro elemento para "pera".
#Adicione "uva" ao final da lista.
#Remova o último elemento da lista.

frutas = ['maçã','banana','laranja']

print(frutas[1])
frutas[0] = 'pera'
print(frutas[0])
frutas.append('uva')
print(frutas[3])
frutas.pop()

for fruta in frutas:
    print(f"Lista atualizada é: {fruta}")




