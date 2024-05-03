class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

# Chamando o método estático diretamente da classe
resultado = Calculadora.somar(5, 3)
print(resultado)  # Saída: 8