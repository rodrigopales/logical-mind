#Criar um analisador de viagem(utilizando função) baseados nos dados digitados pelo usuário
#Usuário ira digita a Rota que foi km de saída , km de chegada , tipo veículo , litros abastecidos
#Mostrar resumo da viagem para usuário , km total rodado , média por litros , valor total gasto 
#baseado no tipo de veículo para decidir qual combustível , deixar valores para cada tipo de combustível baseado na vida real

def analisaViagem(kmSaida,kmChegada):
    kmTotal = kmChegada - kmSaida
    return kmTotal
    


kmSaida = int(input("Digite o km de saída: "))
kmChegada = int(input("Digite o km de chegada: "))
listrosAbastecidos = int(input("Digite a quantidade de listros abatescidos: "))


print(f"Km total rodado foi {analisaViagem(kmSaida,kmChegada)} ")
