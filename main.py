"""
Написать программу, которая:
- Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка [-15, -4, -2, -7, 0, 3, 5, 12, 7]

- Выводит данную матрицу в форматированном виде. Пример:
0 6 7 3
0 3 8 3
3 8 3 7
- Выводит сумму всех нечетных элементов
"""
import random #Подключение библиотеки random 
size = [-15, -4, -2, -7, 0, 3 , 5, 12, 7 ] #Значеия которые будут заполнять массив
height = random.randint(4, 8) #Длина массива то есть длина строки
width = random.randint(4, 8) #Ширина массива то есть длина столбца
array = [[random.choice(size) for x in range(width)] for x in range(height)] #Заполнение массива рандомными элементами из значения size с помощью перебора
for i in array: #Перебор 
    print("|".join(f"{num:>3}" for num in i)) #Вывод массива с условием того что элемент будет занимать 3 символа 
    
