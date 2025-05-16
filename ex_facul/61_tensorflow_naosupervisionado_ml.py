import tensorflow as tf
from tensorflow.keras.layers import Input, Dense # type: ignore
from tensorflow.keras.models import Model # type: ignore
import matplotlib.pyplot as plt

# Dados de exemplo
X_unsupervised = tf.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0], [4.0, 5.0]])

# Modelo Autoencoder Simples
input_layer = Input(shape=(2,))
encoded = Dense(units=1)(input_layer)
decoded = Dense(units=2)(encoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento do modelo não supervisionado
autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

# Previsão
prediction_unsupervised = autoencoder.predict(X_unsupervised)
print("Predição Não Supervisionada:", prediction_unsupervised)

# Visualização (opcional)
plt.scatter(X_unsupervised[:, 0], X_unsupervised[:, 1], color='blue', label='Entrada')
plt.scatter(prediction_unsupervised[:, 0], prediction_unsupervised[:, 1], color='red', label='Saída do Autoencoder')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Autoencoder - Entrada vs Saída')
plt.legend()
plt.show()
