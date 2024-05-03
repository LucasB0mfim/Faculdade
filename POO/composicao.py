class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def ligar(self):
        print("Motor ligado.")

    def desligar(self):
        print("Motor desligado.")

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor("V8")  # Composição: o carro tem um motor

    def ligar(self):
        print(f"{self.marca} {self.modelo} ligando o motor.")
        self.motor.ligar()

    def desligar(self):
        print(f"{self.marca} {self.modelo} desligando o motor.")
        self.motor.desligar()

# Criando um carro
meu_carro = Carro("Toyota", "Corolla")

# Ligando o carro
meu_carro.ligar()

# Desligando o carro
meu_carro.desligar()