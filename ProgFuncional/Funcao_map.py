# O primeiro parâmetro da função map é o nome da função (sem parênteses), 
# que será executada para cada item do iterável. O segundo parâmetro é o iterável. 

lista = [1, 2, 3, 4, 5]

def triplica(item):
    return item * 3

def main():
    nova_lista = map(triplica, lista)
    print(list(nova_lista))

if __name__ == "__main__":
    main()