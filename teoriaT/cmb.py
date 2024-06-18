import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
    # Crear una nueva matriz de fluctuaciones del CMB
    new_cmb_matrix = create_cmb_matrix(size)
    
    # Actualizar la imagen con la nueva matriz de fluctuaciones
    im.set_data(new_cmb_matrix)
    
    return [im]

# Crear animación
ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=500)

# Mostrar la animación
plt.tight_layout()
plt.show()
