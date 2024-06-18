import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros de la galaxia espiral
num_particles = 1000  # Número de estrellas (partículas)
num_frames = 300  # Número de frames de la animación
rot_speed = 0.03  # Velocidad angular de rotación (simulando la rotación de la galaxia)
spiral_density = 6.0  # Densidad de los brazos espirales

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
    global rot_speed
    # Ajuste de la velocidad de rotación gradualmente hacia cero
    if rot_speed > 0:
        rot_speed -= 0.0001
    # Movimiento espiral alrededor del eje z
    theta = np.linspace(0, spiral_density * 2 * np.pi, num_particles)
    x_new = np.cos(theta) * x - np.sin(theta) * y
    y_new = np.sin(theta) * x + np.cos(theta) * y
    return x_new, y_new, z

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
    
    # Gradualmente estabilizar la rotación
    x, y, z = update(frame, x, y, z)
    
    # Mostrar las partículas como una espiral
    ax.scatter(x, y, z, s=1, c=z, cmap='plasma', alpha=0.8)
    
    ax.set_title(f'Frame {frame}')
    ax.grid(False)

# Crear la animación
ani = FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Mostrar la animación
plt.show()
