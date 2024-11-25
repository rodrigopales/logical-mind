"""""

#operadores aritméticos
a = 5
b = 2

print(a + b)#soma de dois valores(Soma)
print(a * b)#multiplicacao de dois valores(Multiplicacao)
print(a / b)#divisao de dois valores(Divisao)
print(a % b)#resto da divisao(Módulo)
print(a // b)#divisao inteira(sem resto)
print(a ** b)#exponenciação(Potência (elevado a))


#operadores de comparacao
x = 10 
y = 5

print(x > 5)
print(x < y)
print(x >= y)
print(x <= y)

#operadores lógicos
#AND, OR e NOT

idade = 20
possui_carteira = True

pode_dirigir = (idade >=18) and possui_carteira
print(pode_dirigir)

#AND só é verdadeiro quando ambas operacoes resultam em true
#OR é verdadeiro quando PELO MENOS uma operacao é true

eh_estudante = False
idade = 60

#1 = é atribuicao
#2 == é comparacao
meia_entrada = eh_estudante == True or idade >= 60
print(meia_entrada)

#NOT = inverter um booleano

chovendo = True
nao_chovendo = not chovendo

print("Chovendo",chovendo)
print("Não Chovendo",nao_chovendo)

#if -> chovendo == False, not chovendo


#senha iguais
#criando um registro de usuario

senha = "102030"
confirmacao_senha = "102030"

validador =  (senha != confirmacao_senha)
print(validador)

#mesa de bar
# 123.85
# quanto cada pessoa vai pagar? 3 

conta = 123.85
qte_pessoas = 3

conta_rateada = conta / qte_pessoas

print(f"Cada pessoa tem que pagar R$ {conta_rateada:.2f}")

#desafio crie um programa que verifica se uma pessoa pode assitir a um filme classificado como "maiores de 16 anos"
idade = int(input("Digite a sua idade"))

pode_assistir = idade>=16
print("Pode assistir o filme?",pode_assistir)

#calculo imc

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = (peso / (altura ** 2))

peso_ideal = (imc >= 18.5) and (imc <= 24.9)
peso_acima = imc > 24.9
peso_abaixo = imc < 18.5

print(f"Seu IMC é {imc:.2f}")
print("Vocé está no peso ideal?",peso_ideal)
print("Vocé está acima do peso?",peso_acima)
print("Vocé está abaixo do peso?",peso_abaixo)


#Para ser aprovado em um exame, um estudante precisa ter uma nota média maior ou igual
#a 7.0 e uma frequência maior ou igual a 75%.
nota = 8.5
frequencia = 80
resultado = (nota >=7.0) and ( frequencia >= 75)
print("Você passou de ano? ",resultado)

"""

#Uma loja oferece um desconto se o cliente comprar mais de 10 itens ou se o valor total da
#compra for superior a R$100.

