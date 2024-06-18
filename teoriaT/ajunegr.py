import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros de la simulación
num_particles = 1000  # Número de estrellas (partículas)
num_frames = 300  # Número de frames de la animación
galaxy_size = 10.0  # Tamaño de la galaxia (radio)
black_hole_mass = 0.5  # Masa del agujero negro (en unidades arbitrarias)
orbital_speed = 0.05  # Velocidad orbital de las estrellas
horizon_radius = 1.0  # Radio del horizonte de sucesos (afectado por la radiación de Hawking)

# Función para generar las posiciones iniciales en un disco para la galaxia
def generate_initial_positions(num_particles, size):
    theta = np.random.rand(num_particles) * 2 * np.pi
    phi = np.random.rand(num_particles) * np.pi
    r = np.random.rand(num_particles) * size
    x = r * np.cos(theta) * np.sin(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(phi)
    return x, y, z

# Función para actualizar las posiciones de las partículas (estrellas) en cada frame
def update(frame, x, y, z):
    global black_hole_mass, orbital_speed, horizon_radius
    
    # Atracción gravitacional del agujero negro
    dist_sq = x**2 + y**2 + z**2
    accel_x = -black_hole_mass * x / (dist_sq + 1e-6)**1.5
    accel_y = -black_hole_mass * y / (dist_sq + 1e-6)**1.5
    accel_z = -black_hole_mass * z / (dist_sq + 1e-6)**1.5
    
    # Movimiento orbital alrededor del agujero negro
    x += orbital_speed * y
    y += -orbital_speed * x
    
    # Aplicar el efecto del horizonte de sucesos
    mask = dist_sq < horizon_radius**2
    x[mask] = np.random.uniform(-galaxy_size, galaxy_size, np.sum(mask))
    y[mask] = np.random.uniform(-galaxy_size, galaxy_size, np.sum(mask))
    z[mask] = np.random.uniform(-galaxy_size, galaxy_size, np.sum(mask))
    
    return x, y, z

# Generar posiciones iniciales para las estrellas de la galaxia
x, y, z = generate_initial_positions(num_particles, galaxy_size)

# Configuración de la figura y el gráfico 3D
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-galaxy_size, galaxy_size)
ax.set_ylim(-galaxy_size, galaxy_size)
ax.set_zlim(-galaxy_size, galaxy_size)

sc = ax.scatter(x, y, z, s=1)

# Función de animación
def animate(frame):
    global x, y, z
    ax.clear()
    ax.set_xlim(-galaxy_size, galaxy_size)
    ax.set_ylim(-galaxy_size, galaxy_size)
    ax.set_zlim(-galaxy_size, galaxy_size)
    
    # Actualizar posiciones de las estrellas
    x, y, z = update(frame, x, y, z)
    
    # Mostrar las estrellas de la galaxia
    sc = ax.scatter(x, y, z, s=1)
    
    # Mostrar el agujero negro en el centro
    ax.scatter(0, 0, 0, color='black', marker='o', s=100)
    
    ax.set_title(f'Frame {frame}')
    ax.grid(False)

# Crear la animación
ani = FuncAnimation(fig, animate, frames=num_frames, interval=50)

# Mostrar la animación
plt.show()
