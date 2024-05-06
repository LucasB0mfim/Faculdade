import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA

# Dados de entrada
datas = ['01/2023', '02/2023', '03/2023', '04/2023', '05/2023', '06/2023', '07/2023', '08/2023', '09/2023', '10/2023', '11/2023', '12/2023', '01/2024', '02/2024', '03/2024', '04/2024']
clientes = [1038, 1003, 1043, 1011, 1014, 973, 1010, 1060, 1008, 972, 882, 843, 866, 833, 837, 873]

# Converter datas para valores numéricos (número de meses desde a primeira data)
datas_datetime = [datetime.strptime(data, '%m/%Y') for data in datas]
meses_desde_inicio = [(data - datas_datetime[0]).days / 30 for data in datas_datetime]

# Ajustar modelo ARIMA
modelo = ARIMA(clientes, order=(5, 1, 0))  # Ordem (p, d, q) - Aqui, deixamos que o modelo determine o valor ótimo para p e q
resultado = modelo.fit()

# Fazer previsões
proximos_meses = np.arange(len(clientes), len(clientes) + 4)  # Prever os próximos 4 meses
previsao_novos_clientes = resultado.predict(start=len(clientes), end=len(clientes) + 3, typ='levels')

# Exibir as previsões
for mes, previsao in zip(proximos_meses, previsao_novos_clientes):
    print(f"Previsão para o mês {mes+1}/2024: {round(previsao)} clientes")

# Plotar os resultados
plt.figure(figsize=(10, 6))
plt.plot(datas, clientes, label='Dados Históricos', marker='o')

# Adicionar datas dos próximos meses
proximas_datas = [datas_datetime[-1] + timedelta(days=30*(i+1)) for i in range(4)]

# Plotar valores de previsão nos próximos meses
plt.plot([data.strftime('%m/%Y') for data in proximas_datas], previsao_novos_clientes, linestyle='--', color='red', label='Previsão')

plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('Número de Clientes')
plt.title('Previsão de Clientes com Modelo ARIMA')
plt.legend()
plt.grid(True)
plt.show()
