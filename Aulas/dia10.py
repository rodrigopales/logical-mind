
# Uso de Módulos permite que você use funcionalidades já existentes sem ter que reiventá-las
# Isso torna seu código mais eficiente, organizado e fácil de manter.
from datetime import datetime
import random
import sys 
import os 

# Importando modulo criado
import conversoes

# Importando um módulo dentro do python e colocando uma apelido nele
import math as m

# Jeito de importar funções espeficicas
# Lembrando que dessa maneira a importacao que vai valer é essa última 
from math import sqrt, pi


print(f"Cosseno de 0 é {m.cos(0)}")


# Calculo usando módulo math e função sqrt
numero = 16
raiz_quadrada = m.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada}")


# Usando funcao especifica
print(f"O valor de pi é {pi}")
print(f"A raiz quadrada de 25 é {sqrt(25)}")

# Simulando o lançamento de um dado
dado = random.randint(1, 6)
print(f"O resultado do dado é: {dado}")

# Usando o Módulo Datetime do python
agora = datetime.now()
print(f"Data e hora atuais: {agora}")

# Usando Módulo Os para interagir com sistema operacional
# Listando arquivos no diretório atual
arquivos = os.listdir('.')
print("Arquivos no diretório atual",arquivos)


# Quer saber mais sobre o sistema onde seu programa está rodando? O sys tem as respostas
print("Versão do Python:", sys.version)

# Usando módulo criado na aula
temperatura_c = float(input("Digite a temperatura em Celsius: "))
temperatura_f = conversoes.celsius_para_fahrenheit(temperatura_c)
temperatura_k = conversoes.celsius_para_kelvin(temperatura_c)
print(f"{temperatura_c}°C equivalem a {temperatura_f}°F e {temperatura_k}K")


# Escrever um programa que cria uma pasta, cria um arquivo dentro dela e lista os arquivos no diretório.
def manipular_arquivos():
    # Criando uma pasta
    os.mkdir('nova_pasta')
    print("Pasta 'nova_pasta' criada.")
    
    # Mudando para o novo diretório
    os.chdir('nova_pasta')
   
    # Criando um arquivo
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.write("Este é um arquivo dentro da nova pasta.")
    print("Arquivo 'arquivo.txt' criado dentro de 'nova_pasta'.")
    
    # Listando arquivos
    arquivos = os.listdir('.')
    print("Arquivos no diretório atual:", arquivos)
    
manipular_arquivos()
