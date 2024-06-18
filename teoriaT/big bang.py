import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors

# Función para crear una matriz de fluctuaciones del CMB
def create_cmb_matrix(size, mean=2.725, stddev=0.0001):
    # Generar fluctuaciones alrededor de la temperatura promedio del CMB (2.725 K)
    return np.random.normal(mean, stddev, (size, size))

# Tamaño de la matriz
size = 100

# Crear matriz inicial de fluctuaciones del CMB
cmb_matrix = create_cmb_matrix(size)

# Figura y eje para la visualización
fig, ax = plt.subplots(figsize=(8, 8))

# Crear imagen inicial
im = ax.imshow(cmb_matrix, cmap='inferno', interpolation='nearest')
ax.set_title("Fluctuaciones Cuánticas del Fondo Cósmico de Microondas")

# Función de inicialización de la animación
def init():
    im.set_data(cmb_matrix)
    return [im]

# Función de actualización para la animación
def update(frame):
    if frame < 10:  # Los primeros 5 segundos (10 cuadros si interval=500 ms)
        # Crear una nueva matriz de fluctuaciones del CMB
        new_cmb_matrix = create_cmb_matrix(size)
    else:
        # Simular calentamiento y creación de partículas
        new_cmb_matrix = create_cmb_matrix(size, mean=3000, stddev=500)  # Aumentar la temperatura
        new_cmb_matrix[new_cmb_matrix < 3000] = 3000  # Evitar valores muy bajos
        
    # Actualizar la imagen con la nueva matriz de fluctuaciones
    im.set_data(new_cmb_matrix)
    
    if frame == 10:  # Cambiar colormap después de 5 segundos
        im.set_cmap('viridis')  # Cambiar el mapa de colores a viridis (verde-azul)
        ax.set_title("Universo Caliente y Creación de Partículas")

    return [im]

# Crear animación
ani = FuncAnimation(fig, update, frames=40, init_func=init, blit=True, interval=500)

# Mostrar la animación
plt.tight_layout()
plt.show()
