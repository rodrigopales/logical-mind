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