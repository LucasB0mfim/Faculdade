from threading import Thread

minha_lista = []

def adiciona(): # Esta função adiciona() simplesmente adiciona o número 1 à lista minha_lista 100 vezes. Ela é utilizada para simular uma operação que pode ser executada em paralelo por várias threads.
    for i in range(100):
        minha_lista.append(1)

def main(): # Esta função main() cria uma lista chamada tarefas e executa 10 vezes. Em cada iteração, ela cria uma nova thread que executa a função adiciona().
    tarefas = []

    for indice in range(10):
        t = Thread(target=adiciona)
        tarefas.append(t)
        t.start()

    print(len(minha_lista))

if __name__ == '__main__':
    main()


    # Thread 1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 2: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 3: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 4: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 5: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 6: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 7: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 8: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 9: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...]  =  100 vezes
    # Thread 10: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1...] =  100 vezes
    # Total = 1.000