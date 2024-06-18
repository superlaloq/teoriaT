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

# Generar direcciones y velocidades aleatorias para las partículas
angles = np.random.uniform(0, 2 * np.pi, (num_particles, 2))
velocities = np.random.uniform(0, max_velocity, num_particles)
directions = np.column_stack((np.cos(angles[:, 0]) * np.sin(angles[:, 1]),
                              np.sin(angles[:, 0]) * np.sin(angles[:, 1]),
                              np.cos(angles[:, 1]))) * velocities[:, np.newaxis]

# Figura y eje para la visualización
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)
scat = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], c='blue')
ax.set_title("Simulación de Colisión Subatómica en 3D")

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
    return scat,

# Crear animación
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)

# Mostrar la animación
plt.tight_layout()
plt.show()
