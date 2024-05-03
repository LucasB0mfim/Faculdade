class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome
    
    def set_ender(self, ender):
        self.ender = ender
    
    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender
    
pessoa1 = Pessoa("Maria", "Rua X")
print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')


# Herança 
class Profissional(Pessoa):
    def __init__(self, nome, ender, profissao):
        super().__init__(nome, ender)
        self.profissao = profissao
    
    def imprimir(self):
        print(f'Nome: {self.nome}, Endereço: {self.ender}, Profissão: {self.profissao}')

p = Profissional("Paula", "Rua Y", "Médico(a)")
p.imprimir()