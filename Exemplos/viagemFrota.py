#Criar um analisador de viagem(utilizando função) baseados nos dados digitados pelo usuário
#Usuário ira digita a Rota que foi km de saída , km de chegada , tipo veículo , litros abastecidos
#Mostrar resumo da viagem para usuário , km total rodado , média por litros , valor total gasto 
#Considerar que o veículo é um caminhão e utiliza Diesel-10 , deixar valores para cada tipo de combustível baseado na vida real
import requests
from bs4 import BeautifulSoup

#Função para pegar o valor do Diesel
def get_diesel_price(url):
    """Extrai o preço do Diesel S-10 de uma página web.

    Args:
        url (str): URL da página web.

    Returns:
        float: Preço do Diesel S-10, ou None se não encontrado.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Substitua 'preco-diesel' pelo seletor correto da sua página
    price_element = soup.find('p', class_='h1 real-value', id='telafinal-precofinal')

    if price_element:
        price_text = price_element.text.strip()
        price = float(price_text.replace('R$', '').replace(',', '.'))
        return price
    else:
        return None

# Exemplo de uso:
url = "https://precos.petrobras.com.br/sele%C3%A7%C3%A3o-de-estados-diesel"  # Substitua pela URL correta
precoDiesel = get_diesel_price(url)

print(f"Preço atual DIESEL-S10 R$ {precoDiesel:.2f}")


#Função para analisar a viagem
def analisaViagem(kmSaida,kmChegada,litrosAbastecidos,precoDiesel):
    kmTotal = kmChegada - kmSaida
    media = kmTotal / litrosAbastecidos
    valorGasto = litrosAbastecidos * precoDiesel
    return print(f"Km rodados {kmTotal} com média de {media} valor atual do Diesel s-10 R$ {precoDiesel:.2f} com gasto total de R$ {valorGasto:.2f} ")    
    

    
#Coleta de valores com usuario
kmSaida = int(input("Digite o km de saída: "))
kmChegada = int(input("Digite o km de chegada: "))
litros = int(input("Digite a quantidade de listros abatescidos: "))


#Chamando função para analisar viagem
analisaViagem(kmSaida,kmChegada,litros,precoDiesel)
