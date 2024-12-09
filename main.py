import random #Подключение библиотеки random 
size = [-15, -4, -2, -7, 0, 3 , 5, 12, 7 ] #Значеия которые будут заполнять массив
height = random.randint(4, 8) #Длина массива то есть длина строки
width = random.randint(4, 8) #Ширина массива то есть длина столбца
array = [[random.choice(size) for x in range(width)] for x in range(height)] #Заполнение массива рандомными элементами из значения size с помощью перебора
for i in array: #Перебор 
    print("|".join(f"{num:>3}" for num in i)) #Вывод массива с условием того что элемент будет занимать 3 символа 
    