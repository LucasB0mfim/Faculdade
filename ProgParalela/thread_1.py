import threading
import time

def funcao():
    for i in range(10):
        print(i, "Executando a thread!")
        time.sleep(1)

print("Iniciando o programa!")
threading.Thread(target=funcao).start()
print("Finalizando o programa!")
