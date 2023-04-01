import numpy as np
'''

#задаємо розмір масиву та k-тий стовбець

N, M, k = 3, 3, 2

#1-task
#A
arr = np.random.randint(-10, 10, size=(N, M))
print("Масив сортування:")
print(arr)


#сортуємо по k-товому стовбцю
idx = np.argsort(arr[:, k])
arr = arr[idx]

print("Масив після сортування по k-товому стовбц:")
print(arr)


#перевірка чи є нульові стовбці чи рядки
#Б
zero_c = np.where((arr == 0).all(axis=0))[0]
zero_r = np.where((arr ==0).all(axis=1))[0]

if len(zero_c) > 0:
    print(f"Масив має нульові стовбці з індексами {zero_c}")
else:
    print("Масив не має нульових стовців")

if len(zero_r) > 0:
    print(f"Масив має нульові рядки з індексами {zero_r}")
else:
    print("Масив не має нульових рядків")  

#C
#Знаходимо середнє значання кожного рядка
arr_average = arr.mean(axis=1, keepdims=True)
print(arr_average)

#віднімаємо сер. знач. кожного рядка від кожного рядка
arr1 = arr-arr_average
print(arr1)

#Д
#Додаємо до кожного числа по 2 нулі
arr = np.zeros((N, M * 3), dtype=int)
arr[:, ::3] = np.random.randint(-10, 10, size=(N,M))
print(arr)

#2-task
#Створеня матриці(10,2) з випадковими числами

cord = np.random.rand(10, 2)

#Перетворення в полярні координати

r = np.sqrt(cord[:, 0]**2 + cord[:, 1]**2)
theta = np.arctan2(cord[:, 1], cord[:, 0])

print("Координати точок:")
print(cord)
print("\nПолярні координати:")
print(np.column_stack((r, theta)))
'''
#3-task
#Створеня масиву з 15 елементів 

arr = np.random.randint(-10, 10, 15)
print('Масив до заміни знака:')
print(arr)

#заміна знака на протиежний з 3 до 8
arr [(arr >= 3) & (arr <= 8)] *= -1
print('Масив із заміною знака від 3 до 8')
print(arr)