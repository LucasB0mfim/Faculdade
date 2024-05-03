x = 10
if x > 5:
    raise Exception("x não pode ser maior que 5. O valor de x é: {}".format(x))

# Outra forma:

# Se quiser ver o resultado no console, crie um novo arquivo e cole esse código nele.
class ExcecaoCustomizada(Exception):
    pass

def throws():
    raise ExcecaoCustomizada("Esta é uma mensagem de exceção customizada.")

try:
    throws()
except ExcecaoCustomizada as ex:
    print("Exceção lançada:", ex)

