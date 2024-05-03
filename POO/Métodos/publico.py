class Carro:
    def __init__(self, marca):
        self.marca = marca

    def ligar(self):
        print(f"{self.marca} ligando o motor.")  # Método público

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota")

# Chamando o método público
meu_carro.ligar()