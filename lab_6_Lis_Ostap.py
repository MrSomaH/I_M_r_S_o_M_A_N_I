import numpy as np


#задаємо розмір масиву та k-тий стовбець
print("==================================================")
print("Перше завдання ")
print("==================================================")
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

print("==================================================")
print("2-задвання")
print("==================================================")
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

print("==================================================")
print("3-задвання")
print("==================================================")
#3-task
#Створеня масиву з 15 елементів 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
print('Масив до заміни знака:')
print(arr)

#заміна знака на протиежний з 3 до 8
minus = (arr >= 3) & (arr <= 8)

arr[minus] *= -1

print('Масив із заміною знака від 3 до 8')
print(arr)

print("==================================================")
print("4-задвання")
print("==================================================")

#4-task
#створеня двовимерного масиву з нулями

arr = np.zeros((10,10))

#встановленя 1 на границяї

arr[0, :] = 1
arr[-1, :] = 1
arr[:, 0] = 1
arr[:, -1] = 1
print("Масив з 1 по контуру і 0 всередині")
print(arr)

print("==================================================")
print("5-задвання")
print("==================================================")
#5-task
# задаємо точки P0, P1 та P
P0 = np.array([[0, 0], [1, 1], [2, 2]])
P1 = np.array([[1, 0], [0, 1], [1, 2]])
P = np.array([[0, 1], [1, 0], [1, 1]])

# обчислюємо відстань між кожною точкою P та кожною лінією P0, P1
def distance_to_line(x, P0, P1):
    numerator = np.abs((P1[:,1] - P0[:,1]) * x[0] - (P1[:,0] - P0[:,0]) * x[1] +
                       P1[:,0] * P0[:,1] - P1[:,1] * P0[:,0])
    denominator = np.sqrt((P1[:,1] - P0[:,1]) ** 2 + (P1[:,0] - P0[:,0]) ** 2)
    distance = numerator / denominator
    return distance

distances = np.apply_along_axis(distance_to_line, 1, P, P0, P1)
print("Відстань кожної точки до кожної лінії")
print(distances)


print("==================================================")
print("6-задвання")
print("==================================================")
#6-task
Z = np.array([1, 2, 3, 4, 5, 6])
print("Початковий масив")
print("Z =",Z)
# Визначаємо розміри та кроки масиву
shape = (len(Z)-2, 3)
strides = (Z.itemsize, Z.itemsize)

# Використовуємо as_strided(), щоб створити двовимірний масив з відповідними розмірами та кроками
result = np.lib.stride_tricks.as_strided(Z[:shape[0]*shape[1]], shape=shape, strides=strides)
print("Масив з відповідним розміром і кроками")
print(result)

print("==================================================")
print("7-задвання")
print("==================================================")
#7-task


X = np.array([1, 2, 3])
Y = np.array([4, 5, 6])
n = len(X)
m = len(Y)
C = np.zeros((n,m))
for i in range(n):
    for j in range(m):
        C[i][j] = 1 / (X[i] - Y[j])
print("Матриця коші")
print(C)


print("==================================================")
print("8-задвання")
print("==================================================")
#task- 8

# Сформувати матрицю з координатами точок
arr = np.random.rand(5, 3)

distans = np.zeros((5,5))
for i in range(5):
    for j in range(5):
        distans[i][j] = np.sqrt(np.sum((arr[i] - arr[j])**2))

print(distans)


print("==================================================")
print("9-задвання")
print("==================================================")
#task - 9 

A = np.random.randint(-10, 10, size=(8,3))
B = np.random.randint(-10, 10, size=(2,2))

#перевірка чи є елементи Б в рядках А

el = np.all(np.isin(A, B), axis=1)

print (np.nonzero(el)[0])


print("==================================================")
print("10-задвання")
print("==================================================")
#task -10
# Вектор цілих додатних чисел
v = np.array([0, 1, 8], dtype=np.uint8)
print("Вектор цілих додатних чисел")
print("v =",v)
# Перетворення у матричне двійкове представлення
bin_matrix = np.unpackbits(v[:, np.newaxis], axis=1)
print("Матриця з двійковим перетворенням")
print(bin_matrix)
print("==================================================")