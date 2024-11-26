#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

quantoGanhaHora = float(input("Qual o valor que você ganha por hora: "))
quantasHoras = int(input("Qual o numero de horas que trabalha por mês: "))

quantoGanha = quantoGanhaHora * quantasHoras

print(f"Você ganha um total de R$ {quantoGanha:.2f} por mês!")