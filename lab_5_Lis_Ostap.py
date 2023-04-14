import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Задання вектор-функції
def vector_function(t):
    x = np.sin(t)
    y = np.cos(t)
    z = t
    return np.array([x, y, z])

# Створення інтервалу аргументу
t = np.arange(0, 10, .1)

# Створення тривимірної фігури
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Побудова годографа
for i in range(len(t)):
    vector = vector_function(t[i])
    ax.plot([0, vector[0]], [0, vector[1]], [0, vector[2]], color='b')
    ax.scatter(vector[0], vector[1], vector[2], color='r')
    plt.pause(0.1)

plt.show()


# Задання скалярного поля
def scalar_field(x, y, t):
    return np.sin(x + t) + np.cos(y)

# Створення масивів значень x та y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

# Створення сітки з масивів x та y
X, Y = np.meshgrid(x, y)

# Створення фігури та підготовка пустого графіка
fig = plt.figure()
ax = fig.add_subplot(111)

# Функція, яка викликається на кожному кроці анімації
def update_plot(t):
    ax.clear()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    
    # Знаходження значення скалярного поля для кожної точки на сітці
    Z = scalar_field(X, Y, t)
    
    # Створення ліній рівня та їх побудова на графіку
    levels = np.linspace(-2, 2, 10)
    CS = ax.contour(X, Y, Z, levels=levels, cmap='rainbow')
    
    # Додавання підписів до ліній рівня
    ax.clabel(CS, inline=1, fontsize=10)

# Створення анімації
ani = FuncAnimation(fig, update_plot, frames=np.linspace(0, 2*np.pi, 50), interval=100)

# Показ анімації
plt.show()
