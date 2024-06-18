import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la transformación
theta = np.pi / 4  # ángulo de 45 grados
cos_theta = np.cos(theta)
sin_theta = np.sin(theta)
cosh_phi = 1 / cos_theta
sinh_phi = sin_theta / cos_theta

# Matriz de transformación de Lorentz
Lambda = np.array([
    [cosh_phi, -sinh_phi, 0, 0],
    [-sinh_phi, cosh_phi, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Redondear los valores de la matriz de Lorentz
Lambda = np.round(Lambda, decimals=2)

# Matriz de Lalo inicial
Lambda_Lalo_inicial = np.array([
    ['u', 'd', 'd'],
    ['d', 'u', 'd'],
    ['d', 'd', 'u']
])

# Representación gráfica de las matrices
def plot_matrix(matrix, title):
    fig, ax = plt.subplots()
    ax.matshow(np.ones_like(matrix), cmap='Greys')
    for (i, j), val in np.ndenumerate(matrix):
        ax.text(j, i, val, ha='center', va='center')
    plt.title(title)
    plt.show()

# Graficar matriz de transformación de Lorentz
plot_matrix(Lambda, 'Matriz de Transformación de Lorentz')

# Graficar matriz de Lalo inicial
plot_matrix(Lambda_Lalo_inicial, 'Matriz de Lalo Inicial')

# Supongamos una fluctuación cuántica que cambia la matriz de Lalo
Lambda_Lalo_final = np.array([
    ['d', 'u', 'd'],
    ['u', 'd', 'd'],
    ['d', 'd', 'u']
])

# Graficar matriz de Lalo final
plot_matrix(Lambda_Lalo_final, 'Matriz de Lalo Final')
