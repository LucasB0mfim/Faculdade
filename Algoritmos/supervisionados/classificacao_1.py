# Importa a classe DecisionTreeClassifier do módulo sklearn.tree
from sklearn.tree import DecisionTreeClassifier

# Define os valores para representar se a fruta está lisa ou irregular
lisa = 1
irregular = 0

# Define os valores para representar se a fruta é uma pera ou uma laranja
pera = 1
laranja = 0

# Define os dados do pomar, onde cada sublista contém [peso, textura] da fruta
pomar = [[120, lisa], [140, lisa], [180, irregular], [200, irregular]]

# Define os resultados esperados para cada fruta no pomar (1 para pera, 0 para laranja)
resultadoEsperado = [pera, pera, laranja, laranja]

# Cria uma instância do classificador de árvore de decisão
clf = DecisionTreeClassifier()

# Treina o classificador usando os dados do pomar e os resultados esperados
clf = clf.fit(pomar, resultadoEsperado)

# Define os valores para um novo usuário (peso e textura) a serem classificados
peso = 220
superficie = 0

# Faz a previsão da fruta com base nos valores do novo usuário
resultadoUsu = clf.predict([[peso, superficie]])

# Verifica se a fruta prevista é uma pera (1) ou uma laranja (0) e imprime o resultado
if resultadoUsu == 1:
    print('Pera')
else:
    print('Laranja')