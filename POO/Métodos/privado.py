class Carro:
    def __init__(self, marca):
        self.marca = marca

    def __verificar_gasolina(self):
        print("Verificando o nível de gasolina.")  # Método privado

    def ligar(self):
        self.__verificar_gasolina()  # Chamando o método privado dentro da classe
        print(f"{self.marca} ligando o motor.")

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota")

# Chamando o método público
meu_carro.ligar()

# Tentando chamar o método privado diretamente (gerará um erro)
# meu_carro.__verificar_gasolina()