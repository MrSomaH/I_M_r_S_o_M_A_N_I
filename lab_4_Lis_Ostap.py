import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


print("==================================================")
print("1-завдання")
print("==================================================")
print("Додавання векторів:  ")
# Вектори
v1 = np.array([1, 2, 1])
v2 = np.array([1, -1, 1])

# Додавання векторів
v3 = v1 + v2

# Візуалізація
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Відображення векторів
ax.quiver(2, 4, 6, v1[0], v1[1], v1[2], color='r')
ax.quiver(3, 5, 7, v2[0], v2[1], v2[2], color='b')
ax.quiver(1, 3, 5, v3[0], v3[1], v3[2], color='g')

# Відображення осей координат
ax.axis([0, 15, 0, 15])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

print("Віднімання векторів: ")

# Вектори
v1 = np.array([1, 2, 1])
v2 = np.array([1, -1, 1])

# Віднімання векторів
v3 = v1 - v2

# Візуалізація
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Відображення векторів
ax.quiver(1, 3, 2, v1[0], v1[1], v1[2], color='r')
ax.quiver(2, 2, 1, v2[0], v2[1], v2[2], color='b')
ax.quiver(3, 1, 3, v3[0], v3[1], v3[2], color='g')

# Відображення осей координат
ax.axis([0, 15, 0, 15])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

print("Множення вектора на скаляр:  ")

# Вектор
v1 = np.array([3, 2, 0])

# Множення вектора на скаляр
s = 3
v2 = s * v1

# Візуалізація
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Відображення векторів
ax.quiver(2, 3, 5, v1[0], v1[1], v1[2], color='r')
ax.quiver(1, 4, 6, v2[0], v2[1], v2[2], color='b')

# Відображення осей координат
ax.axis([0, 15, 0, 15])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

print("Векторний добуток двох векторів: ")
# Вектори
v1 = np.array([-1, 2, 0])
v2 = np.array([-1, 3, 1])

# Векторний добуток
v3 = np.cross(v1, v2)

# Візуалізація
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Відображення векторів
ax.quiver(1, 2, 4, v1[0], v1[1], v1[2], color='r')
ax.quiver(1, 3, 9, v2[0], v2[1], v2[2], color='b')
ax.plot([0, v3[0]],[0, v3[1]], [0, v3[2]], color='g')

# Відображення осей координат
ax.axis([-5, 5, -5, 5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

print("==================================================")
print("2-завдання")
print("==================================================")
def rotate_vector(vector, angle):
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    return np.dot(rotation_matrix, vector)

def translate_vector(vector, displacement):
    return vector + displacement

def invert_coordinates(vector):
    return -vector

def visualize_transformation(vector, transformed_vector, transformation_name):
    plt.figure()
    plt.quiver(*vector, angles='xy', scale_units='xy', scale=1, color='b')
    plt.quiver(*transformed_vector, angles='xy', scale_units='xy', scale=1, color='r')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'{transformation_name} Перетворення')
    plt.grid()
    plt.legend(['Звичайний вектор', 'Змінений вектор'])
    plt.show()

# Вхідні дані
vector = np.array([2, 3])  # Координати вектора у старій системі координат
angle = np.pi/4  # Кут повороту в радіанах
displacement = np.array([1, -2])  # Вектор зміщення

# Поворот вектора
rotated_vector = rotate_vector(vector, angle)
visualize_transformation(vector, rotated_vector, 'Обертальне')

# Паралельне перенесення вектора
translated_vector = translate_vector(vector, displacement)
visualize_transformation(vector, translated_vector, 'Паралельне')

# Інверсія системи координат
inverted_vector = invert_coordinates(vector)
visualize_transformation(vector, inverted_vector, 'Інверсійне')    

print("==================================================")
print("3-завдання")
print("==================================================")

def plot_2d_vector_function():
    t = np.linspace(0, 2*np.pi, 100)  # Задаємо діапазон значень аргументу t
    x = 5*t - 5*np.sin(t)  # Обчислюємо x-координату вектор-функції r(t)
    y = 5 - np.cos(t)  # Обчислюємо y-координату вектор-функції r(t)

    plt.plot(x, y)  # Побудова годографу
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Годограф r(t) = (5t - 5sin(t), 5 - cos(t))')
    plt.grid(True)
    plt.axis('equal')  # Задаємо однаковий масштаб для осей x і y
    plt.show()

plot_2d_vector_function()

def plot_3d_vector_function():
    t = np.linspace(-10, 10, 100)  # Задаємо діапазон значень аргументу t
    x = 3 * np.cos(t)  # Обчислюємо x-координату вектор-функції r(t)
    y = 3 * np.sin(t)  # Обчислюємо y-координату вектор-функції r(t)
    z = t  # Обчислюємо z-координату вектор-функції r(t)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)  # Побудова годографу
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('Годограф r(t) = (3cos(t), 3sin(t), t)')
    plt.show()

plot_3d_vector_function()