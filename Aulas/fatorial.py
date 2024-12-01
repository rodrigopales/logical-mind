#Peça o usuário para digitar um numero inteiro positivo e calcule o fatorial dele

def fatorial(n):
  """Calcula o fatorial de um número natural.

  Args:
    n: Um número natural.

  Returns:
    O fatorial de n.
  """

  if n == 0:
    return 1
  else:
    return n * fatorial(n-1)
resultado = fatorial(5)
print(resultado)  # Imprime 120


def fatorial_for(n):
  """Calcula o fatorial usando um loop for."""
  fatorial = 1
  for i in range(1, n+1):
    fatorial *= i
  return fatorial

import math

def fatorial_math(n):
  """Calcula o fatorial usando a função factorial da biblioteca math."""
  return math.factorial(n)

N = int(input("Digite um número inteiro positivo: "))
fatorial = 1
if N < 0:
  print("Não existe fatorial de número negativo.")
elif N == 0 or N == 1:
 print(f"O fatorial de {N} é 1.")
else:
 for i in range(1, N+1):
  fatorial *= i
 print(f"O fatorial de {N} é {fatorial}.")