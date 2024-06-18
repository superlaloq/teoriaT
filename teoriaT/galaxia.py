import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Función para generar las posiciones iniciales en un disco
def generate_initial_positions(num_particles):
    theta = np.random.rand(num_particles) * 2 * np.pi
    r = np.random.rand(num_particles)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros(num_particles)
    return x, y, z

# Función para actualizar las posiciones de las partículas en cada frame de la animación
def update(frame, x, y, z):
    # Movimiento espiral alrededor del eje z
    omega = 0.1  # Velocidad angular de rotación
    spiral_density = 6.0  # Densidad de los brazos espirales
    theta = np.linspace(0, spiral_density * 2 * np.pi, num_particles)
    x_new = np.cos(theta) * x - np.sin(theta) * y
    y_new = np.sin(theta) * x + np.cos(theta) * y
    return x_new, y_new, z

# Generar posiciones iniciales para las estrellas de la galaxia
num_particles = 1000  # Número de estrellas (partículas)
x, y, z = generate_initial_positions(num_particles)

# Tamaño de la matriz para el CMB
cmb_size = 100
# Crear matriz de fluctuaciones del CMB
mean_cmb = 2.725
stddev_cmb = 0.0001
cmb_matrix = np.random.normal(mean_cmb, stddev_cmb, (cmb_size, cmb_size))

# Configuración de la figura y el gráfico 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-0.5, 0.5)

# Mostrar imagen del CMB como fondo
extent = [-2, 2, -2, 2]
ax.imshow(cmb_matrix, cmap='inferno', extent=extent, aspect='auto', alpha=0.6)

# Crear puntos de la galaxia espiral
sc = ax.scatter(x, y, z, s=1, c=z, cmap='plasma', alpha=0.8)

# Función de animación
def animate(frame):
    global x, y, z
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-0.5, 0.5)
    ax.imshow(cmb_matrix, cmap='inferno', extent=extent, aspect='auto', alpha=0.6)
    x, y, z = update(frame, x, y, z)
    sc = ax.scatter(x, y, z, s=1, c=z, cmap='plasma', alpha=0.8)
    ax.set_title(f'Frame {frame}', color='white')  # Título blanco
    ax.grid(False)  # Sin cuadrícula
    return sc,

# Crear la animación
ani = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

# Mostrar la animación
plt.show()
