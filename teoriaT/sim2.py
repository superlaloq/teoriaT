import numpy as np
import matplotlib.pyplot as plt

# Función para crear matrices aleatorias de configuraciones de quarks
def create_random_configuration(size):
    return np.random.choice([0, 1], size=(size, size))

# Matrices iniciales para el protón y el neutrón
size = 3  # Tamaño de las matrices
Lambda_p = create_random_configuration(size)
Lambda_n = create_random_configuration(size)

# Función para aplicar transformadas (simulación conceptual)
def apply_transform(matrix):
    transformed_matrix = np.zeros_like(matrix)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] == 1:
                # Ejemplo conceptual de transformación
                transformed_matrix[i, j] = np.random.choice([0, 1])  # Simulación de fluctuaciones
            else:
                transformed_matrix[i, j] = matrix[i, j]
    return transformed_matrix

# Aplicar transformadas a las matrices iniciales
Lambda_p_prime = apply_transform(Lambda_p)
Lambda_n_prime = apply_transform(Lambda_n)

# Visualización de las matrices originales y transformadas
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].imshow(Lambda_p, cmap='Blues', interpolation='nearest')
axs[0, 0].set_title('Protón Original')

axs[0, 1].imshow(Lambda_p_prime, cmap='Reds', interpolation='nearest')
axs[0, 1].set_title('Protón Transformado')

axs[1, 0].imshow(Lambda_n, cmap='Blues', interpolation='nearest')
axs[1, 0].set_title('Neutrón Original')

axs[1, 1].imshow(Lambda_n_prime, cmap='Reds', interpolation='nearest')
axs[1, 1].set_title('Neutrón Transformado')

# Añadir el "fondo de microondas" como una capa de ruido aleatorio
for ax in axs.flat:
    ax.imshow(np.random.rand(size, size), cmap='Greys', alpha=0.3)

plt.tight_layout()
plt.show()
