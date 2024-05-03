import threading
import time

def funcao(mensagem):
    for i in range(10):
        print(i, mensagem)
        time.sleep(1)

print("Iniciando o programa!")
x = threading.Thread(target=funcao, args=("Executado!",))
x.start()
print("Finalizando o programa!")
