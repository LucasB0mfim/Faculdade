import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def plotar_previsao(meses, novos_clientes, proximos_meses, previsao_novos_clientes):
    plt.figure(figsize=(10, 6))
    plt.scatter(meses, novos_clientes, color='blue', label='Dados Históricos')
    plt.plot(np.concatenate((meses, proximos_meses)), np.concatenate((novos_clientes, previsao_novos_clientes)), color='red', linestyle='--', label='Previsão')
    plt.scatter(proximos_meses, previsao_novos_clientes, color='black', marker='o', label='Previsão')
    plt.xlabel('Mês')
    plt.ylabel('Número de Novos Clientes')
    plt.title('Previsão de Novos Clientes')
    plt.xticks(np.arange(1, max(meses.max(), proximos_meses.max()) + 1, 1))
    plt.legend()
    plt.grid(True)
    plt.show()

# Dados históricos dos últimos 4 meses
meses = np.array([1, 2, 3, 4]).reshape(-1, 1)  # Janeiro, Fevereiro, Março, Abril
novos_clientes = np.array([50, 80, 60, 100])

# Criar e treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(meses, novos_clientes)

# Prever para os próximos meses (próximos 3 meses, por exemplo)
proximos_meses = np.array([5, 6, 7]).reshape(-1, 1)  # Maio, Junho, Julho
previsao_novos_clientes = modelo.predict(proximos_meses)

# Exibir as previsões
for mes, previsao in zip(proximos_meses, previsao_novos_clientes):
    print(f"Previsão para o mês {int(mes)}: {round(previsao)} novos clientes")

# Plotar gráfico
plotar_previsao(meses, novos_clientes, proximos_meses, previsao_novos_clientes)
