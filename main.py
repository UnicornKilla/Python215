# name = "Amir"
# print("Hello, ", name, "!")
# age = 20
# print(age)

# a = 5
# print(a)

# a = 4
# b = 5
# print(a)
# print(id(a))
# a = b
# print(a)
# print(id(a))
# print(id(b))

# a = b = c = 5
# a, b, c = 2, "Hello", 4.5
# print(a, b, c)
# PI = 3.14
# print(PI)
# a = False
# print(type(a))

# print('Документ \"file.py\" находится в \nC:\\python\\file.py')
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ' ' + s2
# print(s3 * 3)


# num1 = "2"
# num2 = 3.5
# res = int(num1) + num2
# print(res)
#
# print(int(3.891))

# a = 3.981
# a = round(a, 2)
# print(a)
# print(type(a))

# num1 = "5.2"
# num2 = 10
# c = int(num1) + num2
# print()

# name = "Victor"
# age = 26
# print("My name is ", name, "I'm", age, "y.o.")
# print("My name is " + name + "I'm" + str(age) + "y.o.")
# print("My name is ", name, "I'm", age, "y.o.", sep=" ", end=" ")
# # print()
# print("I'm learn Python.")

# name = input("Enter your name: ")
# print("your name is", name)


# num = int(input("enter the number: "))
# power = int(input("enter the power: "))
# res = num ** power
# print(res)

# print("Введите 4 числа:")
# num1 =int(input("1:"))
# num2 =int(input("2:"))
# num3 =int(input("3:"))
# num4 =int(input("4:"))
#
# sum1 = num1 + num2
# sum2 = num3 + num4
#
# res = round((sum1 / sum2),2)
# print("результат: ", res)

# b1 = True
# b2 = False
#
# print(b1 + 5)

# print(7 == 7)
# print(2 + 5 == 9 - 2)
# print(7 != 7)

# print(2 < 4 < 9) #True : True = True
# print(3 * 3 <= 7 >= 2) #False : True = False
# print(2 * 5 > 7 >= 4 + 3)
#
# a = 10
# b = 5
# c = a == b
# print(a,b,c)

# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# a = 5
# b = 15
# if a > b:
#     print("a>b")
# elif b>a:
#     print("b>a")
# else:
#     print("a==b")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
# if a == b == c:
#     print("треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("треугольник равнобедренный")
# else:
#     print("треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if(day>=1) and (day<=5):  #if 1 <= day <= 5
#     print("Рабочий день -", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day ==7:
#     print("Выходной -",end=" ")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("такого дня нет")

# month = int(input("Введите номер месяца: "))
# if (month == 1) or (month == 2) or (month == 12):
#     print("Зима")
# if (month == 3) or (month == 4) or (month == 5):
#     print("Весна")
# if (month == 6) or (month == 7) or (month == 8):
#     print("Лето")
# if (month == 9) or (month == 10) or (month == 11):
#     print("Осень")
# else:
#     print("Такого месяца нет")

# crow = int(input("Введите количество ворон: "))
# if 0 <= crow <= 9:
#     print("на ветке ", end=" ")
#     if crow == 1:
#         print(crow, "ворона")
#     if 2 <= crow <= 4:
#         print(crow,"вороны")
#     if 5 <= crow <= 9 or crow == 0:
#         print(crow, "ворон")
# else:
#     print("Ошибка ввода данных")

# i=1
# while i<5:
#     print("внешний цикл i=", i)
#     j=1
#     while j<4:
#         print("\t Внутренний цикл j=", j)
#         j+=1
#     i+=1

# i = 1
# while i < 10:
#         j = 1
#         while j < 10:
#             print(i,"*", j,"=",i*j, end="\t\t")
#             j += 1
#         print()
#         i += 1 #таблица умножения

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end = "")
#         j += 1
#     print()
#     i += 1 #^^^ kvadrat

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end = "")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" "*i,"*")
#     i+=1 # * no диагонали

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1 # * no диагонали

# for элемент in коллекция:
#   тело цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green':
#     print(color)

# for i in range(9):
#     print(i, end=" ")

# a = int(input('Введите целое число: '))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# w = int(input("Vvedite shirinu pryamougolnika: "))
# h = int(input("Vvedite visotu pryamougolnika: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = 16
# h = 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# w = [letter * 2 for letter in "hello"]
# print(w)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки

# nums = [8,3,9,4,1]
# print(nums)
# print(type(nums))

# a =[0 for i in range(5)]
# print(a)

# генератор списков

# n=5
# a=[i**2 for i in range(1, n + 1)]
#
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)

# a = [0] * int(input("Введите кол-во эл-тов списка:"))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('->'))
# print(a)

# a = [input("->") for i in range (int(input("n= ")))]
# print(a)

# a = [9,8,6,4,3]
# for i in range(len(a)):
#     print(i,":",a[i])
# print()

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i]<0:
#         s +=a[i]

# n = list(range(21, 41))
# print(n)
# a =0
# b = 0
# for i in n:
#     if i%2 == 0:
#         a+=1
#     else:
#         b += 1
#
# print(f'Количество четных элементов списка: {a}\nСумма нечетных элементов: {b}')

# a = [int(input("->")) for i in range(int(input("n = ")))]
# print(a)
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         k += 1
#     s += a[i]
# print(s / k)

# a = [6,3,0,8,2]
# a[0], a[1] = a[1], a[0]
# print(a)

# Срезы
# список [start:stop:step]

# a = [6,3,0,8,2,7]
# print(a[1:4])
# print(a[2:])
# print(a[:2])
# print(a[::-1])

# a = [6,3,0,8,2,7]
# print(a[:])
# a[1:3] = [1,1,1,1]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = 50
# print(a)

# b = 0
# del b #удаляет элемент
# print(b)

# Методы списка

# a = [6,3,0,8,2,7]
# print(a)
# a.append(99) # добавляет 1 элемент в конец списка
# print(a)
# a.extend([5,6,7]) # добавляет несколько элементов в конец списка
# print(a)

# a = []
# a.extend([i ** 2 for i in range(1,11)]) #добавляет список элементов в конец списка
# print(a)

# a = [6,3,0,8,2,7]
# print(a)
# a.insert(2,100) #добавляет 1 элемент в определенное место в списке (первый параметр - индекс, второй - значение)
# print(a)
# a.insert(0, 200)
# print(a)
# a.insert(len(a) + 1, 300)
# print(a)

# s = []
# n= int(input("Кол-во эл-тов: "))
# for num in range(n):
#     x= int(input("vedi chislo kratnoe 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x,"ne delitsya na 3 bez ostatka")
# print(s)

# a = [5,9,2,1,4,3]
# b = [4,2,1,3,7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1,2,3,44,55]
# b = [11,22,33]
# c = []
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# a = [5,9,2,1,4,3,2,4]
# a.remove(2) #удаляет элемент из списка по значению(если несколько таких, первый по совпадению)
# print(a)
# last = a.pop() #удаляет последний эт-т из списка (без параметров) и возвращает удаленный элемент в переменную
# print(last)
# second = a.pop(0) #удаляет по индексу эт-т из списка
# print(a)
# print(second)
# a.clear() #очищает список
# print(a)

# a = [int(input("->")) for i in range(int(input("n =")))]
# print(a)
# k = int(input(("Введите индекс\nk = ")))
# a.pop(k)
# print(a)

# a = [5,2,9,2,1,2,4,3,2,4]
# num = a.count(8) #считает кол-во заданных значений в списке
# print(num)
#
# b = 2
# # ind = a.index(9) #возвращает положение первого индекса по заданому значению
# ind = a.index(b,4,-1)
# print(ind)

# c = [1,2,3]
# d = c.copy() # возвращает копию списка
# print("c = ",c)
# print("d = ",d)
# c.append(4)
# d.insert(0, 100)
# print("c = ",c)
# print("d = ",d)

# a = [5,2,9,2,1,2,4,3,2,4]
# a.reverse() #разворачивает список в обратную сторону
# print(a)

# a.sort() #отсортировали список по возрастанию
# print(a)
#
# a.sort(reverse=True) #отсортировали список по убыванию
# print(a)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key = len, reverse=True)
# print(s)

# b = sorted(a)
# print(b)

# Генерация случайных данных
# import random
#
# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(6,15,2))

# import random as r
#
# print(r.randint(0, 5))
# print(r.randrange(6,15,2))

# from random import randint, randrange
#
# print(randint(0, 5))
# print(randrange(6,15,2))

# from random import *
#
# print(randint(0,5))
# print(randrange(6,15,2))
# print (uniform(10.5, 25.5)) #Вещественное число
# print (round(uniform(10.5, 25.5), 2))

# city_list = ['Tokyo','Yokohama','Osaka','Saitama','Kyoto']
# print(choices(city_list, k=3))
#
# s = [55,66,77,88,99]
# print(choice(s))
# print(choices(s, k=3))
# shuffle(s)
# print(s)

# from random import randint
# mas = [randint(0,20) for i in range (5)]
# print(mas)

# Функции агрегирования

# lst = [7,12,20,18,9]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst)) # Работает только с числами
#
# print("hello" > "Hello")

# from random import randint
# mas = [randint(0,100) for i in range (10)]
# print(mas)
# max_1 = max(mas)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)

# from random import randint
# mas = [randint(-20, 20) for i in range (10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# from random import randint
# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# min_1 = min(mas)
# print(min_1)
# ind = mas.index(min_1)
# del mas[:ind]
# print(mas)

# lst = []
# if len(lst) == 0:
#     print("list is empty")
#
# if not lst:
#     print("!!!list is empty")

# print(bool(lst))

# from random import randint
# n1= int(input("Введите размер первого списка: "))
# n2= int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
#
# print("First:", a)
# print("second:", b)
#
# # c = a + b
# # print("Third: ", c)
#
# c = []
# # for i in range(len(a)):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
#
# # print("Без повторов:", c)
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Общие:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# from random import randint
# k = int(input("List size: "))
# s = []
# while len(s) < k:
#     w = randint(0, k-1)
#     if w not in s:
#         s.append(w)
# print(s)

# m = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12]
# ]
# # print(len(m))
# print(m)
# # print(m[1][2])
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x**2, end="\t\t")
#     print()

from random import randint
# matrix = [[0 for x in range(5)]for y in range(3)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# matrix = [[randint(-20, 10) for x in range(3)] for y in range(4)]
# print(matrix)
# s = 0
# for row in matrix:
#     for j in row:
#         print(j, end="\t\t")
#         if j < 0:
#             s +=1
#     print()
# print("Количество отрицательных элементов: ", s)

# n = int(input("n = "))
# m = [[randint(0, 100) for x in range(5)] for y in range(5)]
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
#
# t = m[0][0]
# for k in range(n):
#     if t > m[k][k]:
#         t = m[k][k]
# print(t)

