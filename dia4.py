"""""

#Verifica desconto

valorCompra = 2000

if valorCompra >= 1000:
    descPor = 0.10 #desconto de 10% 
    desconto = valorCompra * descPor
    print(f"Você recebeu um desconto de {descPor * 100:.0f} %  no valor de R$ {desconto:.2f} ")

elif valorCompra >=500:
    descPor = 0.05 #desconto de 5% 
    desconto = valorCompra * descPor
    print(f"Você recebeu um desconto de {descPor * 100:.0f} %  no valor de R$ {desconto:.2f} ")

else:
    desconto = 0
    ("Não há desconto disponivel>")

valorCompraFinal = valorCompra - desconto
print(f"Valor final da compra com desconto é: R$ {valorCompraFinal:.2f}") 

#Fim verifica desconto


#Planejanto um passeio

diaSemana = "Sabado"
chovendo = True

if(diaSemana == "Sabado" or diaSemana == "Domingo") and not chovendo:
    print("Ótimo dia para ir ao parque!")
else:
    print("Vamos ficar em casa e assistir a um filme.")

#Fim planejamento passeio

#Calculadora
num1 = float(input("Digite o primeiro numero:"))
num2 = float(input("Digite o segundo numero:"))
operacao = input("Digite a operação desejada (+, - , * , /):")

if operacao == "+":
    resultado = num1 + num2
    print(f"resultado  é: {resultado:.0f}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"resultado  é: {resultado:.0f}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"resultado  é: {resultado:.0f}")

elif operacao == "/":
    if num2 !=0:
        resultado = num1 / num2
        print(f"resultado  é: {resultado:.0f}")

    else: print("Erro: Divisão por zero")

else:
    print("Operação inválida")

#Fim Calculadora


#Classificacao idade
# Criança: 0 a 12 anos
# Adolescente: 13 a 17 anos
# Adulto: 18 a 59 anos
# Idoso: 60 anos ou mais

idade = int(input("Digite sua idade:"))

if (idade >=0 and idade <= 12):
    print(f"Voce é uma Criança pois tem {idade:.0f} anos.")
elif (idade >=13 and idade <= 17):
    print(f"Voce é uma Adolescente pois tem {idade:.0f} anos.")
elif (idade >=18 and idade <= 59):
    print(f"Voce é uma Adulto pois tem {idade:.0f} anos.")
elif (idade >=60):
    print(f"Voce é uma Idoso pois tem {idade:.0f} anos.")
else:
    print("Idade digitada é negativa nao vale")

#Fim classificao idade

"""""

#Ano bissexto sim ou não?
ano = int(input("Digite um ano para saber se é bissexto: "))
if(ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print(ano, "é um ano bissexto.")
else:
    print(ano, " não é um ano bissexto.")

sabe = input("Sabe o que é um ano bissexto ? S ou N : ")
print(type(sabe))

if (sabe == "s"):
    print("Parabéns você é muito inteligente")
else:
    print("Um ano bissexto é aquele que possui 366 dias, ao invés dos 365 dias que temos nos anos normais. Isso significa que o mês de fevereiro, que normalmente tem 28 dias, nos anos bissextos ganha um dia a mais, ficando com 29 dias.")


#Fim ano bissexto