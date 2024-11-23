"""""


#Variables in python not typed
idade = 34
nome = "Rodrigo"
altura = 1.68

#Data type
#int, float, textos = strings, bool = true ou false
cidade = 'Anápolis'
esta_logado = True
nome = 2
print(nome)

#Check data type
print(type(nome))
print(type(cidade))
print(type(esta_logado))
print(type(altura))

#Operators
print(5 + 1.2 )
print( 10 * 2)
print(50 / 5 )
print(50 - 25)
print( 15.2 % 5)
print( 2 ** 2)
print(-3 + 12)
#Concatenation
nomeUsuario = " Mister Chap"
frase = "Olá" + nomeUsuario + " tudo bem?"
print(frase)

#Comparisons
maior = 15 > 2
print(maior)

menor = 15 < 12
print(menor)

print(5 == 5)

#Python compares lowercase and uppercase
print( "teste" == "teste")
print( "Rodrigo" == "rodrigo")

print ( 15!= 2)

"""

"""
#Day 2 Training 

nome = "Rodrigo Pales"
idade = 34
altura = 1.73
estudante = False

print("Nome:",nome)
print("Idade:",idade)
print("Altura",altura)



if estudante == True:
    print("Você é estudante.")
else: print("Você não é estudante.")

#Concatenation and transform String
frase = "Olá "+nome+" sua idade é:"+str(idade)+" sua altura é "+str(altura)+" e você é estudante? "+str(estudante)
print(frase)

#Concatenation modern
frase2 = f"Olá {nome} sua idade é: {idade} sua altura é {altura} e vocé estudante? {estudante}" 
print(frase2)

#Simple Calculator
print("Digite dois numeros para o programa realizar operações simples da matemática: Soma , Subtração, Multiplicação e Divisão")
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))


soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print("Soma",soma)
print("Subtração",sub)
print("Multiplicação",mult)
print("Divisão",div)

"""

#Fahrenheite converter to celsius
print("Escolha como quer converter a sua temperatura:")

while True:
    opcao = int(input("Escolha uma opção:\n1. Fahrenheit para Celsius\n2. Celsius para Fahrenheit\n3. Sair\n"))

    if opcao == 1:
        temp = float(input("Digite sua temperatura em Fahrenheit: "))
        resultado = (temp - 32) * 5/9
        print(f"Sua temperatura em Celsius é: {resultado:.2f}°C")
    elif opcao == 2:
        temp = float(input("Digite sua temperatura em Celsius: "))
        resultado = (temp * 9/5) + 32
        print(f"Sua temperatura em Fahrenheit é: {resultado:.2f}°F")
    elif opcao == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")
        
#Calc to area Circle
raio = float(input("Digite o raio do cirulo:"))
pi = 3.14159
area = pi * raio ** 2
print("A área do círculo é:",area)







