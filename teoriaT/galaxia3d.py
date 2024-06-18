import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros de la galaxia espiral
num_particles = 1000  # Número de estrellas (partículas)
num_frames = 200  # Número de frames de la animación
omega = 0.1  # Velocidad angular de rotación (simulando la rotación de la galaxia)

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
    # Actualización de las posiciones rotando alrededor del eje z
    theta = np.linspace(0, 2 * np.pi, num_particles)
    x = x * np.cos(omega) - y * np.sin(omega)
    y = x * np.sin(omega) + y * np.cos(omega)
    return x, y, z

# Generar posiciones iniciales
x, y, z = generate_initial_positions(num_particles)

# Configuración de la figura y el gráfico 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-0.5, 0.5)

# Función de animación
def animate(frame):
    global x, y, z
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-0.5, 0.5)
    x, y, z = update(frame, x, y, z)
    ax.scatter(x, y, z, s=1)
    ax.set_title(f'Frame {frame}')

# Crear la animación
ani = FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Mostrar la animación
plt.show()
