from functools import reduce

numeros = [1, 2, 3, 4, 5]

f_soma = lambda x, y: x + y

resultado = reduce(f_soma, numeros)
print(resultado)