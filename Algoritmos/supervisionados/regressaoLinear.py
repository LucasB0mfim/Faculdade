# Importa a biblioteca numpy, que fornece suporte para arrays e funções matemáticas
import numpy as np

# Importa a biblioteca matplotlib.pyplot para criar gráficos
import matplotlib.pyplot as plt

# Importa a classe LinearRegression do módulo sklearn.linear_model
from sklearn.linear_model import LinearRegression

# Define os valores de entrada (x) e saída (y) como arrays numpy
x = np.array([5, 10, 15, 20, 25, 30]).reshape((-1, 1))  # reshape para criar um vetor coluna
y = np.array([6, 12, 14, 23, 27, 32])

# Cria uma instância do modelo de regressão linear
model = LinearRegression().fit(x, y)

# Faz a predição dos valores de saída com base nos valores de entrada
y_predict = model.predict(x)

# Imprime os dados reais e os dados previstos para comparação
print('Dados do teste: ', y, sep='\n')
print('Dados da predição: ', y_predict, sep='\n')

# Plota um gráfico de dispersão dos dados reais e uma linha para os dados previstos
plt.scatter(x, y, c='blue')  # Gráfico de dispersão dos dados reais
plt.plot(x, y_predict, c='red')  # Linha para os dados previstos
plt.legend(['Predição', 'Real'])  # Adiciona uma legenda ao gráfico
plt.show()  # Exibe o gráfico