import threading
import time

ls = []

def contador_1(n):
    for i in range(1, n + 1):
        print(i)
        ls.append(i)
        time.sleep(0.4)

def contador_2(n):
    for i in range(6, n + 1):
        print(i)
        ls.append(i)
        time.sleep(0.5)

x = threading.Thread(target=contador_1, args=(5,))
x.start()

y = threading.Thread(target=contador_2, args=(10,))
y.start()


x.join() # Printar a lista
y.join() # Printar a lista
print(ls)