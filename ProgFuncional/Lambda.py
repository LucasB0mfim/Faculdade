lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numerosPares = lambda x: x % 2 == 0

pares = list(filter(numerosPares, lista))

print(f"Os números pares da lista são: {pares}")