import tensorflow as tf
import numpy as np  # Importado para verificação opcional

# Carregando o conjunto de dados MNIST
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizando os dados
x_train, x_test = x_train / 255.0, x_test / 255.0

# Verificando a forma dos dados (opcional)
print(f"x_train shape: {x_train.shape}, y_train shape: {y_train.shape}")
print(f"x_test shape: {x_test.shape}, y_test shape: {y_test.shape}")

# Definindo o modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # Camada de entrada
    tf.keras.layers.Dense(128, activation='relu'),   # Camada oculta
    tf.keras.layers.Dropout(0.2),                    # Camada de Dropout
    tf.keras.layers.Dense(10, activation='softmax')   # Camada de saída
])

# Compilando o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinando o modelo
model.fit(x_train, y_train, epochs=5)

# Avaliando o modelo
test_loss, test_accuracy = model.evaluate(x_test, y_test)

# Exibindo a precisão do teste
print(f'Test accuracy: {test_accuracy:.4f}')
