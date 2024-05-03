from abc import ABC, abstractmethod

class Forma(ABC):  # Classe abstrata Forma
    @abstractmethod
    def area(self):  # Método abstrato
        pass

    @abstractmethod
    def perimetro(self):  # Método abstrato
        pass

class Retangulo(Forma):  # Subclasse Retangulo que herda de Forma
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def area(self):  # Implementação do método area para Retangulo
        return self.comprimento * self.largura

    def perimetro(self):  # Implementação do método perimetro para Retangulo
        return 2 * (self.comprimento + self.largura)

class Circulo(Forma):  # Subclasse Circulo que herda de Forma
    def __init__(self, raio):
        self.raio = raio

    def area(self):  # Implementação do método area para Circulo
        return 3.14 * self.raio ** 2

    def perimetro(self):  # Implementação do método perimetro para Circulo
        return 2 * 3.14 * self.raio

# Não é possível instanciar uma classe abstrata
# forma = Forma()  # Isso causaria um erro

# Podemos instanciar as subclasses
retangulo = Retangulo(5, 4)
circulo = Circulo(3)

print("Área do retângulo:", retangulo.area())
print("Perímetro do retângulo:", retangulo.perimetro())
print("Área do círculo:", circulo.area())
print("Perímetro do círculo:", circulo.perimetro())