import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Parámetros de la simulación
num_particles = 50       # Número de partículas desprendidas
collision_point = np.array([0.5, 0.5, 0.5])  # Punto de colisión (centrado en la figura)
max_velocity = 0.02      # Velocidad máxima de las partículas

# Generar posiciones iniciales (el punto de colisión para todas las partículas)
positions = np.tile(collision_point, (num_particles, 1))
initial_positions = positions.copy()

# Generar direcciones y velocidades aleatorias para las partículas
angles = np.random.uniform(0, 2 * np.pi, (num_particles, 2))
velocities = np.random.uniform(0, max_velocity, num_particles)
directions = np.column_stack((np.cos(angles[:, 0]) * np.sin(angles[:, 1]),
                              np.sin(angles[:, 0]) * np.sin(angles[:, 1]),
                              np.cos(angles[:, 1]))) * velocities[:, np.newaxis]

# Asignar tipos de partículas aleatoriamente
particle_types = np.random.choice(['quark', 'gluon', 'electron', 'proton'], num_particles)

# Colores asociados a cada tipo de partícula
colors = {'quark': 'red', 'gluon': 'blue', 'electron': 'green', 'proton': 'purple'}
particle_colors = [colors[ptype] for ptype in particle_types]

# Figura y eje para la visualización
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

# Inicializar scatter plot y líneas de traza
scat = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c=particle_colors)
trails = [ax.plot([], [], [], c=particle_colors[i], alpha=0.6)[0] for i in range(num_particles)]

# Función de actualización para la animación
def update(frame):
    global positions
    # Actualizar posiciones
    positions += directions
    
    # Verificar colisiones con los bordes y reflejar las partículas
    for i in range(3):
        directions[positions[:, i] < 0, i] *= -1
        directions[positions[:, i] > 1, i] *= -1
    
    # Actualizar la posición de los puntos en el gráfico
    scat._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])
    
    # Actualizar las trazas
    for i in range(num_particles):
        trail_x = [initial_positions[i, 0], positions[i, 0]]
        trail_y = [initial_positions[i, 1], positions[i, 1]]
        trail_z = [initial_positions[i, 2], positions[i, 2]]
        trails[i].set_data(trail_x, trail_y)
        trails[i].set_3d_properties(trail_z)
    
    return scat, *trails

# Crear animación
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Mostrar la animación
plt.tight_layout()
plt.show()
