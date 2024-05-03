class Pessoa:
    total_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1

    @classmethod
    def total(cls):
        return cls.total_pessoas

print(Pessoa.total())  # Saída: 0

pessoa1 = Pessoa("João")
print(Pessoa.total())  # Saída: 1