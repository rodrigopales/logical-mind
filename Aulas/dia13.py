# como trabalhar com arquivos em python

# uma forma de ler o arquivo todo
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# ler o arquivo linha por linha
with  open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
        break

# escrever em um arquivo
with open('saida.txt', 'w') as arquivo:
    arquivo.write("Nova linha \n")
    arquivo.write("Nova linha 2 \n")

# quando eu não tenho o arquivo, o write cria ele e depois escreve
# este write dessa maneira , ele vai sobscrever o arquivo

# adicionar o conteudo - append -a
with open('saida.txt', 'a') as arquivo:
    arquivo.write("Nova linha 3\n")
    arquivo.write("Nova linha 4 \n")

# r - read - ler
# w - write - escrever
# a - append - adicionar

# CSV - Comma Separeted Values
import csv

with open("contastos.cv", "w", newline='') as arquivo_csv:
    # cabeçalho (colunas)
    # dados
    # dados
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['Nome', 'Profissão' , 'Idade'])
    escritor.writerow(['Rodrigo', 'Supervisor de Transporte',33])
    escritor.writerow(['Rodrigo', 'Gerente de Transporte',34])
    escritor.writerow(['Rodrigo', 'Analista de Sistemas',35])

# Json - javascript object notation (APIs)
import json

dados = {
    'nome': 'Rodrigo',
    'idade': 33,
    'profissao': 'Programador'
}

with open('dados.json', 'w') as arquivo:
    json.dump(dados,arquivo,indent=4)