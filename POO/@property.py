class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def info(self):
        return f"{self.nome} tem {self.idade} anos."

# Criando uma instância da classe Pessoa
pessoa = Pessoa("João", 30)

# Acessando o atributo 'info' como se fosse um atributo de instância
print(pessoa.info)  # Saída: João tem 30 anos.