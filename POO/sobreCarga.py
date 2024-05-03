#  No Python, a última definição de uma função ou método 
# com um determinado nome prevalece sobre as anteriores, 
# independentemente dos tipos de parâmetros.

def minha_funcao(x):
    return x

def minha_funcao(x, y):
    return x + y

resultado = minha_funcao(3, 4)
print(resultado)