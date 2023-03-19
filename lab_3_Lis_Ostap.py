import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

while True:
    print("1 = F1 = 2X**2 = 4Y**2,\n2 = F2 = X**2 + 2Y**2 - Z")
    
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

        # візуалізація скалярного поля за допомогою функції contourf
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.contourf(X, Y, F2, cmap='viridis')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()

        # зображення ліній рівня за допомогою функції contour
        levels = [-12, -9, -6, -3, 0, 3, 6, 9, 12]
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.contour(X, Y, F2, levels=levels, colors='purple')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()

        # обчислення градієнту
        Fx, Fy, Fz = np.gradient(F2)

        # зображення векторного поля градієнта
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.quiver(X, Y, Z, Fx, Fy, Fz, length=0.3, color='green', normalize=True)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        plt.show()

        # координати точки та вектора напрямку вводяться користувачем
        x0 = float(input('Введіть x-координату точки: '))
        y0 = float(input('Введіть y-координату точки: '))
        z0 = float(input('Введіть z-координату точки: '))
        t1 = float(input('Введіть x-компоненту вектора напрямку: '))
        t2 = float(input('Введіть y-компоненту вектора напрямку: '))
        t3 = float(input('Введіть z-компоненту вектора напрямку: '))


        # обчислення значення градієнту в точці (x0, y0, z0)
        grad_F = np.array([2 * x0, 4 * y0, -1])

        # обчислення значення похідної за напрямом вектора (t1, t2, t3) в точці (x0, y0, z0)
        t = np.array([t1, t2, t3])
        dF_dt = np.dot(grad_F, t)

        # виведення результату
        print('Похідна в напрямку вектора ({}, {}, {}) у точці ({}, {}, {}) дорівнює {}'.format(t1, t2, t3, x0, y0, z0, dF_dt))









