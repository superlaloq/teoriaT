import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Función para crear matrices aleatorias de configuraciones de quarks
def create_random_configuration(size):
    return np.random.choice([0, 1], size=(size, size))

# Tamaño de las matrices
size = 3

# Crear matrices iniciales aleatorias para protón y neutrón
particles = {
    'Protón': {'matriz': create_random_configuration(size), 'cmap': 'Blues', 'title': 'Protón'},
    'Neutrón': {'matriz': create_random_configuration(size), 'cmap': 'Reds', 'title': 'Neutrón'}
}

# Figura y ejes para la visualización
fig, axs = plt.subplots(2, 1, figsize=(5, 10))

# Lista para almacenar los artistas de las imágenes
images = []
texts = []

# Crear imágenes iniciales para los subplots
for idx, (particle_name, particle_info) in enumerate(particles.items()):
    ax = axs[idx]
    im = ax.imshow(particle_info['matriz'], cmap=particle_info['cmap'], interpolation='nearest')
    ax.set_title(particle_info['title'])
    images.append(im)
    
    # Mostrar los valores de la matriz como texto dentro de cada celda
    particle_texts = []
    for i in range(size):
        for j in range(size):
            text = ax.text(j, i, str(particle_info['matriz'][i, j]), color='black', ha='center', va='center')
            particle_texts.append(text)
    texts.append(particle_texts)

# Función de inicialización de la animación
def init():
    return images + [text for sublist in texts for text in sublist]

# Función de actualización para la animación
def update(frame):
    # Crear nuevas configuraciones aleatorias
    particles['Protón']['matriz'] = create_random_configuration(size)
    particles['Neutrón']['matriz'] = create_random_configuration(size)

    # Actualizar las imágenes y textos en los subplots
    for idx, (particle_name, particle_info) in enumerate(particles.items()):
        images[idx].set_array(particle_info['matriz'])
        
        # Actualizar los valores de la matriz como texto dentro de cada celda
        for i in range(size):
            for j in range(size):
                texts[idx][i * size + j].set_text(str(particle_info['matriz'][i, j]))

    return images + [text for sublist in texts for text in sublist]

# Crear animación
ani = FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=500)

# Mostrar la animación
plt.tight_layout()
plt.show()
