import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Задана вектор-функція
def vector_function(t):
    x = np.sin(t)
    y = np.cos(t)
    z = t
    return x, y, z

# Заданий інтервал аргументу
t_min = 0
t_max = 10
num_points = 100

# Генерація значень аргументу
t_values = np.linspace(t_min, t_max, num_points)

# Генерація векторів у кожному моменті часу
x_values, y_values, z_values = vector_function(t_values)

# Побудова годографу
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values, 'b-', label='Годограф')

# Додавання векторів у конкретні моменти часу
arrow_length = (t_max - t_min) / num_points
for i in range(num_points):
    ax.quiver(x_values[i], y_values[i], z_values[i], x_values[i], y_values[i], z_values[i],
              length=arrow_length, normalize=True, color='r')

# Налаштування відображення графіка
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Годограф вектор-функції')
ax.legend()

# Відображення графіка
plt.show()

# Задане скалярне поле
def scalar_field(x, y):
    return np.sin(x) + np.cos(y)

# Задані межі координат
x_min, x_max = -5, 5
y_min, y_max = -5, 5

# Задані значення константи рівня
num_levels = 10
level_values = np.linspace(-2, 2, num_levels)

# Генерація координатної сітки
num_points = 100
x_values = np.linspace(x_min, x_max, num_points)
y_values = np.linspace(y_min, y_max, num_points)
X, Y = np.meshgrid(x_values, y_values)

# Побудова анімації ліній рівня
fig, ax = plt.subplots()

def update_plot(frame):
    ax.cla()
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_title(f'Лінії рівня для C = {level_values[frame]:.2f}')
    ax.contour(X, Y, scalar_field(X, Y), levels=[level_values[frame]], colors='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

animation = FuncAnimation(fig, update_plot, frames=num_levels, interval=500, repeat=True)

# Відображення анімації
plt.show()
# Задане двовимірне векторне поле сил
def force_field(x, y):
    return np.array([-y, x])  # Приклад поля сил: F = (-y, x)

# Початкові значення
initial_position = np.array([1.0, 0.0])  # Початкова позиція (x, y)
initial_velocity = np.array([0.0, 1.0])  # Початкова швидкість (Vx, Vy)
mass = 1.0  # Маса тіла

# Крок інтегрування
dt = 0.01

# Кількість кадрів анімації
num_frames = 1000

# Розрахунок траекторії руху тіла
trajectory = np.zeros((num_frames, 2))
position = initial_position
velocity = initial_velocity

for i in range(num_frames):
    # Розрахунок прискорення за другим законом Ньютона: F = ma
    acceleration = force_field(position[0], position[1]) / mass
    
    # Оновлення позиції тіла
    position += velocity * dt
    
    # Оновлення швидкості тіла
    velocity += acceleration * dt
    
    # Збереження позиції у траекторію
    trajectory[i] = position

# Побудова анімації руху тіла
fig, ax = plt.subplots()
ax.set_xlim(np.min(trajectory[:, 0]) - 1, np.max(trajectory[:, 0]) + 1)
ax.set_ylim(np.min(trajectory[:, 1]) - 1, np.max(trajectory[:, 1]) + 1)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')

line, = ax.plot([], [], 'b-', lw=2)

def update_plot(frame):
    line.set_data(trajectory[:frame+1, 0], trajectory[:frame+1, 1])
    return line,

animation = FuncAnimation(fig, update_plot, frames=num_frames, interval=10, blit=True)

# Відображення анімації
plt.show()