import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Dados
datas = ['12/2023', '01/2024', '02/2024', '03/2024', '04/2024']
clientes = [843, 866, 833, 837, 873]

# Converter datas para objeto datetime
datas = pd.to_datetime(datas, format='%m/%Y')

# Criar DataFrame
df = pd.DataFrame({'Data': datas, 'Clientes': clientes})
df.set_index('Data', inplace=True)

# Ajustar o modelo ARIMA
modelo = ARIMA(df['Clientes'], order=(1, 1, 1))
resultado = modelo.fit()

# Prever os próximos 3 meses
previsoes = resultado.predict(start=len(df), end=len(df)+2, typ='levels')

# Criar DataFrame para as previsões
proximos_meses = pd.date_range(start=df.index[-1], periods=3, freq='MS')
previsoes = pd.DataFrame({'Data': proximos_meses, 'Clientes': previsoes.values})
previsoes.set_index('Data', inplace=True)

# Concatenar os DataFrames
previsoes_completas = pd.concat([df, previsoes])

# Imprimir previsões no terminal
for data, clientes in previsoes.iterrows():
    print(f"{data.strftime('%m/%Y')} = {int(clientes)} clientes")

# Plotar os dados e as previsões
plt.figure(figsize=(10, 6))
plt.plot(previsoes_completas, label='Clientes (Previsão)')
plt.scatter(df.index, df['Clientes'], color='red', label='Clientes (Real)')
plt.title('Previsão de Clientes com ARIMA')
plt.xlabel('Data')
plt.ylabel('Número de Clientes')
plt.legend()
plt.grid(True)
plt.show()
