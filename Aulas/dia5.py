"""""
#Exemplo simples 

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print("Eu gosto de", fruta )

#Podemos usar a função range() para gerar uma sequência de números.
for i in range(5):
 print("Número:", i)

# O loop while repete um bloco de código enquanto uma condição for verdadeira. É como
# dizer: "Enquanto a condição for verdadeira, continue fazendo isso"
contador = 0
while contador < 5:
  print("Contagem:", contador)
  contador += 1 # Equivale a contador = contador + 1

#O comando break é usado para interromper o loop imediatamente, mesmo que a condição do loop ainda seja verdadeira
for numero in range(10):
 if numero == 5:
    break
 print("Número:", numero)

# Ocomando continue é usado para pular a iteração atual e continuar com a próxima iteração do loop
for numero in range(5):
 if numero == 2:
    continue
 print("Número:", numero)

  #Imprimindo numeros de 1 a 10 com for
for numero in range(1,11):
    print(numero)
 

#Calculando a soma dos numeros de 1 a n
n = int(input("Digite um número inteiro positivo: "))
soma = 0
for i in range (1,n+1):
    soma += i #equivale a soma = soma + i

print("A soma dos números de 1 a", n , "é:", soma)



#Calculando a a tabuada do numero digittado
n = int(input("Digite um número inteiro positivo para calcular a tabuada: "))

for i in range (1,11):
   tabuada = n * i
   print(f"{n} x {i} = {tabuada}")

"""""

#contando numeros áres impares de 1 a 20
pares = 0
impares = 0
for numero in range(1,21):
    if numero % 2 == 0:
        pares +=1
    else:
        impares +=1
print("Quantidade de números pares" , pares)
print("Quantidade de numero impares", impares)
    

