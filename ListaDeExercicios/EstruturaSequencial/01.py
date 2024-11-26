#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

comprimento = float(input("Digite o comprimento de um dos lados do quadrado para descobrir a área: "))
areaQuadrado = comprimento ** 2
dobroArea = areaQuadrado * 2
print(f"Área do seu quadrado é {areaQuadrado:.2f} cm² e o dobro da sua área é {dobroArea:.2f} cm²")