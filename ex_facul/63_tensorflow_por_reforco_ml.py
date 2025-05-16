import tensorflow as tf
import gym
import numpy as np

# Ambiente CartPole do Gym
env = gym.make('CartPole-v1')

# Modelo Simples para Aprendizado por Reforço
model_reinforcement = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation='relu', input_shape=(env.observation_space.shape[0],)),
    tf.keras.layers.Dense(env.action_space.n, activation='linear')
])

model_reinforcement.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mse')

# Treinamento por Reforço
max_episodes = 1000  # Defina o número máximo de episódios
for episode in range(max_episodes):
    state = env.reset()
    done = False
    total_reward = 0  # Armazenar a recompensa total do episódio

    while not done:
        action = env.action_space.sample()

        # Captura todos os valores retornados
        step_result = env.step(action)

        # Inicializa as variáveis
        next_state, reward, done, info = None, 0, False, {}  # Valores padrão

        # Desempacotando os valores de forma segura
        if len(step_result) == 4:
            next_state, reward, done, info = step_result
        elif len(step_result) == 3:
            next_state, reward, done = step_result
            info = {}  # Caso não haja informação extra

        # Se next_state for None, encerra o episódio
        if next_state is None:
            print("O estado retornado é None. Encerrando o episódio.")
            break

        # Atualizando a recompensa total
        total_reward += reward

        # Reshape do estado
        target = reward + 0.95 * tf.reduce_max(model_reinforcement.predict(next_state.reshape(1, -1)))

        # Predição do valor atual
        target_f = model_reinforcement.predict(state.reshape(1, -1))
        target_f[0][action] = target

        # Treinamento do modelo
        model_reinforcement.fit(state.reshape(1, -1), target_f, epochs=1, verbose=0)

        # Atualiza o estado
        state = next_state

    # Condição de parada
    if episode % 10 == 0:
        print(f'Episode {episode}, Total Reward: {total_reward}')

        # Adicionando uma condição de parada
        if total_reward >= 195:  # CartPole é considerado resolvido em média 195 pontos
            print(f'Solved after {episode} episodes!')
            break
