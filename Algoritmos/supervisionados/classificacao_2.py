# Importa as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

# Carrega o conjunto de dados de dígitos manuscritos
digitos = load_digits()

# Imprime as dimensões dos dados de imagens e dos dados rotulados
print('Shape dos dados de imagens: {}'.format(digitos.data.shape))
print('Shape dos dados rotulados: {}'.format(digitos.target.shape))

# Cria uma nova figura com tamanho específico (28 polegadas de largura por 8 polegadas de altura)
plt.figure(figsize=(28, 8))  


# Plota as primeiras 5 imagens com seus respectivos rótulos
                            # A função enumerate() é usada para iterar sobre os pares de dados, atribuindo a cada par um índice (index)
for index, (imagem, rotulo) in enumerate(zip(digitos.data[0:5], digitos.target[0:5])):
                                        # A função zip() combina os dados de imagem e rótulo em pares

    # Cria uma célula para cada imagem, em uma linha e cinco colunas
    plt.subplot(1, 5, index + 1)  
                    # O índice "+ 1" é adicionado porque os índices de subplot começam em 1, não em 0

    # Plota a imagem como uma matriz 8x8 usando a função imshow() do matplotlib
    plt.imshow(np.reshape(imagem, (8, 8)), cmap=plt.cm.gray)
                # np.reshape(imagem, (8, 8)) reconfigura a imagem em uma matriz 8x8 (cada imagem é originalmente um vetor de 64 elementos)

    # Adiciona o rótulo como título da imagem
    plt.title('Treinamento: {}/n'.format(rotulo, fontsize=15))

    plt.show()  # Exibe a imagem