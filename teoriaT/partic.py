import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para crear una matriz de fluctuaciones del CMB
def create_cmb_matrix(size, mean=2.725, stddev=0.0001):
    # Generar fluctuaciones alrededor de la temperatura promedio del CMB (2.725 K)
    return np.random.normal(mean, stddev, (size, size))

# Función para agregar partículas (esferas de quarks) a la matriz
def add_quark_spheres(matrix, num_spheres, sphere_radius, sphere_temp):
    size = matrix.shape[0]
    for _ in range(num_spheres):
        x, y = np.random.randint(sphere_radius, size-sphere_radius, 2)  # Evitar bordes para colocar la esfera completa
        for i in range(x-sphere_radius, x+sphere_radius+1):
            for j in range(y-sphere_radius, y+sphere_radius+1):
                if (i-x)**2 + (j-y)**2 <= sphere_radius**2:
                    matrix[i, j] = sphere_temp
    return matrix

# Tamaño de la matriz
size = 100

# Figura y eje para la visualización
fig, ax = plt.subplots(figsize=(8, 8))

# Función de inicialización de la animación
def init():
    # Crear matriz inicial de fluctuaciones del CMB (frío)
    cmb_matrix = create_cmb_matrix(size)
    im.set_data(cmb_matrix)
    ax.set_title("Universo Frío")
    return [im]

# Función de actualización para la animación
def update(frame):
    if frame < 10:  # Los primeros 5 segundos (10 cuadros si interval=500 ms)
        # Simulación del enfriamiento inicial (sin creación de partículas ni interacciones)
        new_cmb_matrix = create_cmb_matrix(size)
    elif frame < 20:  # Siguiente período de 5 segundos (20 cuadros si interval=500 ms)
        # Simulación de la inflación y calentamiento (aumento de temperatura)
        new_cmb_matrix = create_cmb_matrix(size, mean=3000, stddev=500)
        new_cmb_matrix[new_cmb_matrix < 3000] = 3000
    else:  # Último período de 5 segundos (30 cuadros si interval=500 ms)
        # Simulación del enfriamiento gradual y aparición de partículas (esferas de quarks)
        new_cmb_matrix = create_cmb_matrix(size, mean=2000, stddev=300)
        new_cmb_matrix[new_cmb_matrix < 2000] = 2000
        new_cmb_matrix = add_quark_spheres(new_cmb_matrix, num_spheres=5, sphere_radius=5, sphere_temp=5000)
        
    # Actualizar la imagen con la nueva matriz de fluctuaciones
    im.set_data(new_cmb_matrix)
    
    # Actualizar el título según el estado del universo
    if frame < 10:
        ax.set_title("Universo Frío")
    elif frame < 20:
        ax.set_title("Inflación y Calentamiento")
    else:
        ax.set_title("Enfriamiento y Aparición de Partículas (Esferas de Quarks)")

    return [im]

# Crear imagen inicial de fluctuaciones del CMB (frío)
cmb_matrix = create_cmb_matrix(size)

# Crear imagen inicial
im = ax.imshow(cmb_matrix, cmap='inferno', interpolation='nearest')

# Crear animación
ani = FuncAnimation(fig, update, frames=30, init_func=init, blit=True, interval=500)

# Mostrar la animación
plt.tight_layout()
plt.show()
