import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Mapeo de combinaciones de gluones a colores RGB
color_map = {
    'gg': (0, 255, 0),    # verde-verde
    'rb': (255, 0, 0),    # rojo-azul
    'gr': (0, 255, 0),    # verde-rojo
    'rr': (255, 0, 0),    # rojo-rojo
    'bb': (0, 0, 255),    # azul-azul
    'gb': (0, 255, 0),    # verde-azul
    'rg': (255, 0, 0),    # rojo-verde
    'bg': (0, 0, 255),    # azul-verde
    'br': (0, 0, 255)     # azul-rojo
}

# Función para crear una matriz de configuraciones de gluones
def create_gluon_matrix(size):
    keys = list(color_map.keys())
    return np.random.choice(keys, size=(size, size))

# Tamaño de la matriz
size = 10

# Crear matriz inicial de gluones
gluon_matrix = create_gluon_matrix(size)

# Función para convertir la matriz de gluones a una matriz de colores RGB
def gluon_matrix_to_rgb(gluon_matrix):
    rgb_matrix = np.zeros((gluon_matrix.shape[0], gluon_matrix.shape[1], 3), dtype=int)
    for i in range(gluon_matrix.shape[0]):
        for j in range(gluon_matrix.shape[1]):
            rgb_matrix[i, j] = color_map[gluon_matrix[i, j]]
    return rgb_matrix

# Convertir la matriz de gluones a una matriz de colores RGB
rgb_matrix = gluon_matrix_to_rgb(gluon_matrix)

# Figura y eje para la visualización
fig, ax = plt.subplots(figsize=(8, 8))

# Crear imagen inicial
im = ax.imshow(rgb_matrix, interpolation='nearest')
ax.set_title("Nube de Gluones - Colores Cromodinámicos")

# Función de inicialización de la animación
def init():
    im.set_data(rgb_matrix)
    return [im]

# Función de actualización para la animación
def update(frame):
    # Crear una nueva matriz de gluones
    new_gluon_matrix = create_gluon_matrix(size)
    
    # Convertir la nueva matriz de gluones a una matriz de colores RGB
    new_rgb_matrix = gluon_matrix_to_rgb(new_gluon_matrix)
    
    # Actualizar la imagen con la nueva matriz de colores RGB
    im.set_data(new_rgb_matrix)
    
    return [im]

# Crear animación
ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=500)

# Mostrar la animación
plt.tight_layout()
plt.show()
