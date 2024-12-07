#Funções
# são a maneira de criar código que pode ser reutilizável
#2, 3, 4 partes que verificam a idade do usuario => transformar em função

# def <=> function
def saudacao():
    print("Olá, seja vem-vindo!")

# a função precisa ser chamada/invocada

saudacao()

#parametros => de configurar a função
# mandar valores para função, e ela executa de maneira diferente

def saudacao_personalizada(nome):
    print(f"Olá {nome} , seja bem-vindo!")

saudacao_personalizada("Rodrigo")
filha = 'Alice'

# nome da variável na função é um , quando você vai chamar a função passando 
# o parametro pode utilizar outro nome para variável sem problemas
saudacao_personalizada(filha)

# multiplos parametros(sempre separado por virgulas)
def apresentar_pessoa(nome,idade,profissao):
    print(f"Dados da pessoa, nome: {nome}, idade: {idade} anos, profissao: {profissao}")

apresentar_pessoa("Rodrigo",34,"Desenvolvedor Web")

# return => instrução que retorna o valor pro programa

def soma(a,b):
    resultado = a + b
    return resultado

# return => ele volta o valor da função para o escopo global
print(soma(1,99))

#criar função que converte fahrenheit para celsius

# preciso criar a função, aceitar a temperatura em F
# passar pela formula de conversão ( f - 32 ) * 5/9
# retorna o valor para o escopo global 
# imprimir o resultado

def fahrenheit_p_celsius(f):
    return (f-32) * 5/9

temp_f = 102
temp_c = fahrenheit_p_celsius(temp_f)

print (f"Sua temperatura em Fahrenheit de {temp_f} em Graus Celsius é : {temp_c}")
