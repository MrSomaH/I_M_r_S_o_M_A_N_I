import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

while True:
    print("1 = F1 = 2X**2 = 4Y**2,\n2 = F2 = X**2 + 2Y**2 - Z\n0 = stop")
    
    task = int(input('Ведіть номер завдання: 1 or 2: '))
    if task == 1:   
     
        print("Задвання а = F1 = 2X**2 = 4Y**2")
        # створення сітки значень x та y
        x = np.linspace(-10, 10, 150)
        y = np.linspace(-10, 10, 150)
        X, Y = np.meshgrid(x, y)

        # обчислення значень функції на сітці
        F1 = 2 * X**2 + 4 * Y**2


        # візуалізація скалярного поля за допомогою функції contourf
        plt.contourf(X, Y, F1, cmap='viridis')
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


        # обчислення градієну . Використаємо функцію 'gradient з пакету NumPy'

        Fx, Fy = np.gradient(F1)

        # зображення векторного поля градієнта

        plt.quiver(X, Y, Fy, color='green')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        

        # зображення ліній рівня за допомогою функції contour
        plt.contour(X, Y, F1, levels=[2, 4, 6, 8, 10], colors='black')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

        # координати точки та вектора напрямку вводяться користувачем
        x0 = float(input('Введіть х - координату: '))
        y0 = float(input('Введіть y - координату: '))
        t1 = float(input('Введіть х - компоненту вектора напрямку: '))
        t2 = float(input('Введіть y - компоненту вектора напрямку: '))

        # обчислення значення градієнту в точці (x0, y0)
        grad_F = np.array([4 * x0, 8 * y0])

        # обчислення значення похідної за напрямом вектора (t1, t2) в точці (x0, y0)
        t = np.array([t1, t2])
        dF_dt = np.dot(grad_F, t)

        # виведення результату
        print('Похідна в напрямку вектора ({}, {}) у точці ({}, {}) дорівнює {}'.format(t1, t2, x0, y0, dF_dt))

    elif task == 2:
        
        print('Завдання b = b=F2 = X**2 + 2Y**2 - Z')
        
        # створення сітки значень x, y та z
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        z = np.linspace(-5, 5, 100)
        X, Y, Z = np.meshgrid(x, y, z)

       # обчислення значень функції на сітці
        F2 = X**2 + 2*Y**2 - Z  

        # візуалізація скалярного поля за допомогою функції slice
        plt.figure(figsize=(6, 6))
        plt.contourf(X[:, :, 50], Y[:, :, 50], F2[:, :, 50], cmap='viridis')
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

        # зображення ліній рівня за допомогою функції contour
        plt.figure(figsize=(6, 6))
        plt.contour(X[:, :, 50], Y[:, :, 50], F2[:, :, 50], levels=[-2, 0, 2, 4, 6, 8], colors='black')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

        # обчислення градієнту. Використаємо функцію 'gradient' з пакету NumPy
        Fx, Fy, Fz = np.gradient(F2)

        # зображення векторного поля градієнта
        plt.figure(figsize=(6, 6))
        plt.quiver(X[:, :, 50], Y[:, :, 50], Fx[:, :, 50], Fy[:, :, 50], color='green')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

        # координати точки та вектора напрямку вводяться користувачем
        x0 = float(input('Введіть х - координату: '))
        y0 = float(input('Введіть y - координату: '))
        z0 = float(input('Введіть z - координату: '))
        t1 = float(input('Введіть х - компоненту вектора напрямку: '))
        t2 = float(input('Введіть y - компоненту вектора напрямку: '))
        t3 = float(input('Введіть z - компоненту вектора напрямку: '))

        # обчислення значення градієнту в точці (x0, y0, z0)
        grad_F = np.array([2*x0, 4*y0, -1])

        # обчислення значення похідної за напрямом вектора (t1, t2, t3) в точці (x0, y0, z0)
        t = np.array([t1, t2, t3])
        dF_dt = np.dot(grad_F, t)

        # виведення результату
        print('Похідна в напрямку вектора ({}, {}, {}) у точці ({}, {}, {}) дорівнює {}'.format(t1, t2, t3, x0, y0, z0, dF_dt))
    
    elif task ==0:
        break