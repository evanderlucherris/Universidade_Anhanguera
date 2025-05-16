import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential # type: ignore
from keras.layers import Dense, Input # type: ignore
import matplotlib.pyplot as plt

# Dados de exemplo
X_train = tf.constant([[1.0], [2.0], [3.0], [4.0]])
y_train = tf.constant([[2.0], [4.0], [6.0], [8.0]])

# Modelo de Regressão Linear Simples
model = Sequential()
model.add(Input(shape=(1,)))  # Usando Input como a primeira camada
model.add(Dense(units=1))
model.compile(optimizer='sgd', loss='mean_squared_error')

# Treinamento do modelo
model.fit(X_train, y_train, epochs=1000, verbose=0)

# Previsão
X_new = tf.constant([[5.0]])
prediction = model.predict(X_new)

print("Predição:", prediction[0][0])

# Visualização
plt.scatter(X_train, y_train, color='blue', label='Dados de treino')
plt.scatter(X_new, prediction, color='red', label='Previsão')
plt.xlabel('Entradas')
plt.ylabel('Saídas')
plt.legend()
plt.title('Regressão Linear Simples')
plt.show()
