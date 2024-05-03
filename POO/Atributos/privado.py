class Carro:
    def __init__(self):
        self.__modelo = "Corolla"  # Atributo privado

    def get_modelo(self):  # Método para acessar o atributo privado
        return self.__modelo

meu_carro = Carro()
print(meu_carro.get_modelo())  # Acessando um atributo privado por meio de um método público