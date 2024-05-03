import threading
import urllib3
import time

start = time.time()
urls = ["https://www.google.com","https://www.apple.com","https://www.microsoft.com","https://www.instagram.com"]

def chama_url(url):
    http = urllib3.PoolManager()  # Cria um PoolManager
    response = http.request('GET', url)  # Faz a solicitação GET
    the_page = response.data  # Obtém os dados da resposta
    print ("'%s\' carregado em %ss" % (url, (time.time() - start))) #(time.time() - start)) => tempo que levou para carregar

threads = [threading.Thread(target=chama_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print (("Elapse Time: %s" % (time.time() - start))) #(time.time() - start)) => tempo que levou para carregar