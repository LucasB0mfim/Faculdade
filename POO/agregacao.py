class SalarioAnual:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus
    
    def salario_anual(self):
        return (self.base * 12) + self.bonus
    

class Empregado:
    def __init__(self, nome, ender, profissao, salario):
        self.nome = nome
        self.ender = ender
        self.profissao = profissao
        self.salario = salario # Agregação
    
    def salario_total(self):
        return self.salario.salario_anual()
    
salario = SalarioAnual(10000, 700)
emp = Empregado('Pedro', "Rua Z", "Advogado", salario)
print(f"Nome: {emp.nome}, Endereço: {emp.ender}, Profissão: {emp.profissao}, Salário Anual: {emp.salario_total()}")