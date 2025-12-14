# Importar bibliotecas necessárias
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# Carregar dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Construir modelo de rede neural
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
history = model.fit(X_train, y_train, epochs=50, batch_size=8,
                    validation_split=0.2, verbose=1)

# Avaliar o modelo
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Acurácia do modelo nos dados de teste: {accuracy*100:.2f}%")

# Fazer previsões
predictions = model.predict(X_test[:5])

print("Previsões (probabilidades):", predictions)
print("Classes previstas:", np.argmax(predictions, axis=1))
print("Classes reais:", y_test[:5])
