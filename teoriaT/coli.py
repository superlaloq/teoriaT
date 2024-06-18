import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de la simulación
num_particles = 20       # Número de partículas desprendidas
collision_point = np.array([0.5, 0.5])  # Punto de colisión (centrado en la figura)
max_velocity = 0.01      # Velocidad máxima de las partículas

# Generar posiciones iniciales (el punto de colisión para todas las partículas)
positions = np.tile(collision_point, (num_particles, 1))

# Generar direcciones y velocidades aleatorias para las partículas
angles = np.random.uniform(0, 2 * np.pi, num_particles)
velocities = np.random.uniform(0, max_velocity, num_particles)
directions = np.column_stack((np.cos(angles), np.sin(angles))) * velocities[:, np.newaxis]

# Figura y eje para la visualización
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
scat = ax.scatter(positions[:, 0], positions[:, 1], c='blue')
ax.set_title("Simulación de Colisión Subatómica")

# Función de actualización para la animación
def update(frame):
    global positions
    # Actualizar posiciones
    positions += directions
    
    # Verificar colisiones con los bordes y reflejar las partículas
    directions[positions[:, 0] < 0] *= [-1, 1]
    directions[positions[:, 0] > 1] *= [-1, 1]
    directions[positions[:, 1] < 0] *= [1, -1]
    directions[positions[:, 1] > 1] *= [1, -1]
    
    # Actualizar la posición de los puntos en el gráfico
    scat.set_offsets(positions)
    return scat,

# Crear animación
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Mostrar la animación
plt.tight_layout()
plt.show()
