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