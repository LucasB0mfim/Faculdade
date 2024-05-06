import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Dados de entrada
datas = ['01/2023', '02/2023', '03/2023', '04/2023', '05/2023', '06/2023', '07/2023', '08/2023', '09/2023', '10/2023', '11/2023', '12/2023', '01/2024', '02/2024', '03/2024', '04/2024']
clientes = [1038, 1003, 1043, 1011, 1014, 973, 1010, 1060, 1008, 972, 882, 843, 866, 833, 837, 873]

# Converter datas para valores numéricos (número de meses desde a primeira data)
datas_datetime = [datetime.strptime(data, '%m/%Y') for data in datas]
meses_desde_inicio = [(data - datas_datetime[0]).days / 30 for data in datas_datetime]

# Converter para arrays NumPy
X = np.array(meses_desde_inicio).reshape(-1, 1)
y = np.array(clientes)

# Aplicar regressão polinomial de grau 2
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_poly, y)

# Fazer previsões para os próximos meses
proximos_meses = np.arange(max(meses_desde_inicio) + 1, max(meses_desde_inicio) + 5).reshape(-1, 1)
proximos_meses_poly = poly_features.transform(proximos_meses)
previsao_novos_clientes = model.predict(proximos_meses_poly)

# Exibir as previsões
for mes, previsao in zip(proximos_meses, previsao_novos_clientes):
    print(f"Previsão para o mês {int(mes)}: {round(previsao)} clientes")

# Plotar os resultados
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dados Históricos')
plt.plot(np.concatenate((X, proximos_meses)), np.concatenate((y, previsao_novos_clientes)), color='red', label='Previsão')
plt.xlabel('Meses desde o Início')
plt.ylabel('Número de Clientes')
plt.title('Previsão de Clientes com Regressão Polinomial')
plt.legend()
plt.grid(True)
plt.show()
