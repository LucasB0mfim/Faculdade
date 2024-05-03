while True:
    try:
        x = int(input("digite um número: "))
        break
    except ValueError:
        print("Digite um número válido!")