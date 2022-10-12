s = 'Тестовая строка.'
print(s[0])
print(s[5])
print(s[-1])
print(s[-4])

numbers = [5, 3, 10, 4, -1, 7, 11, 6]

print(numbers[2:5])
print(numbers[:3])
print(numbers[4:])
print(numbers[:])
print(numbers[1:5:2])
print(numbers[7:3:-1])
print(numbers[-5:-1])
print(numbers[-1:-4:-1])


test = [False, 4, 'floor']
print(test)

a = [1, 2, 3]
b = [6, 5, 4]

print(a + b)      # Сложение
print(a * 2)      # Умножение на число
print(8 in a)     # Вхождение элемента
print(7 not in b) # Невхождение элемента
print(len(a))     # Количество элементов в списке
print(a > b)      # Сравнение списков
print(min(b))     # Минимальный элемент
print(max(a))     # Максимальный элемент
print(a[:1])      # Срезы
print(b[::-1])    # Срезы с шагом
print(a.index(2)) # Начало вхождения подстроки
print(b.count(4)) # Количество вхождений подстроки

a = [1, 2, 3]
b = [6, 5, 4]

a[1] = 9       # Изменение значения по его индексу
b[0:2] = a     # Замена среза значениями другого списка
print(a, b)    # [1, 9, 3] [1, 9, 3, 4]

del a[0]       # Удаление элемента из списка (работает и со срезами)
a.append(7)    # Добавление элемента в конец списка
b.insert(1, 8) # Вставка по указанному индексу элемента
print(a, b)    # [9, 3, 7] [1, 8, 9, 3, 4]

a += b         # Сложение с присваиванием
b *= 2         # Умножение с присваиванием
print(a, b)    # [9, 3, 7, 1, 8, 9, 3, 4] [1, 8, 9, 3, 4, 1, 8, 9, 3, 4]

a.remove(3)    # Удаление первого элемента с заданным значением
b.pop()        # Удаление последнего элемента и его возврат
print(a, b)    # [9, 7, 1, 8, 9, 3, 4] [1, 8, 9, 3, 4, 1, 8, 9, 3]

a.reverse()    # Переворот списка
b.sort()       # Сортировка списка, принимает аргумент reversed
print(a, b)    # [4, 3, 9, 8, 1, 7, 9] [1, 1, 3, 3, 4, 8, 8, 9, 9]

# Для каждого числа от 0 до 9 поместим в список его квадрат
squares = [x ** 2 for x in range(10)]

# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)

# Можно просто написать if с условием в конце, и тогда
# в список попадут только элементы, удовлетворяющие условию
squares = [x ** 2 for x in range(10) if x % 3 == 0]
# [0, 9, 36, 81]
print(squares)

# А можно написать полноценный тернарный оператор
# в начале генератора, и это сработает
squares_cubes = [x ** 2 if x % 3 == 0 else x ** 3 for x in range(10)]
# [0, 1, 8, 9, 64, 125, 36, 343, 512, 81]
print(squares_cubes)


a = 'Hello World!'
b = 'Hello Universe!'

print(a + b)                # Сложение
print(a * 2)                # Умножение на число
print('Hello' in a)         # Вхождение подстроки
print('world' not in b)     # Невхождение подстроки
print(len(a))               # Длина строки
print(a <= b)               # Сравнение строк
print(min(a))               # Символ с минимальным номером
print(max(b))               # Символ с максимальным номером
print(a[:2])                # Срезы
print(b[::-1])              # Срезы с шагом
print(a.index('World'))     # Начало вхождения подстроки
print(b.count('Universe'))  # Количество вхождений подстроки

a = 'Hello world! My name is NICK.'

# Сделать все буквы строчными, "hello world! my name is nick."
print(a.lower())

# Сделать все буквы заглавными, "HELLO WORLD! MY NAME IS NICK."
print(a.upper())

# Индекс первого вхождения подстроки в срезе [15:30], получим 16
print(a.find('name', 15, 30))

# Если подстроки нет, то возвращается -1
print(a.find('Universe'))

# Замена одной подстроки другой, "Hello Universe! My name is NICK."
print(a.replace('world', 'Universe'))

# Можно указать количество замен, "He__o world! My name is NICK."
print(a.replace('l', '_', 2)

# Разбиваем строку по пробельным символам
# Получим список ['Hello', 'world!', 'My', 'name', 'is', 'NICK.']
print(a.split())

# А можно сделать наоборот и соединить список в строку
words = ['Hello', 'world!', 'My', 'name', 'is', 'NICK.']
separator = '_'
print(separator.join(words))

a = 5
b = 8
print(f"{a} + {b} = {a + b}") # Выведется "5 + 8 = 13"

number = 10003
print('Десятичная СС:        {0:d}'.format(number))
print('Двоичная СС:          {0:b}'.format(number))
print('Восьмеричная СС:      {0:o}'.format(number))
print('Шестнадцатеричная СС: {0:x}'.format(number))
print('Символ по коду:       {0:c}'.format(number))

print()

pi = 3.14159265
print('Экспоненциальная запись: {0:e}'.format(pi))
print('С фиксированной запятой: {0:.3f}'.format(pi))
print('Стандартная запись:      {0:g}'.format(pi))
print('Процент:                 {0:.1%}'.format(pi))

# Слева кортеж и справа кортеж
a, b, c = 4, 5, 6

print(a) # 4
print(b) # 5
print(c) # 6

a = 1, 2, 3
b = 9, 8, 7

print(a + b)        # Сложение и умножение
print(a * 2)        # Умножение на число
print(5 in a)       # Вхождение
print(5 not in b)   # Отрицание вхождения
print(len(a))       # Длина кортежа
print(a > b)        # Сравнение
print(min(a))       # Минимум
print(max(b))       # Максимум
print(a[2], b[-1])  # Индексы
print(a[:2])        # Срезы
print(b[::-1])      # Срезы с шагом
print(a.index(3))   # Индекс элемента
print(b.count(4))   # Количество элементов

a = range(-10, 10, 3)
b = range(-15, 5, 4)
print(tuple(a))
print(tuple(b))

print(-7 in a)      # Вхождение
print(5 not in b)   # Отрицание вхождения
print(len(a))       # Длина диапазона
print(a == b)       # Сравнение
print(min(a))       # Минимум
print(max(b))       # Максимум
print(a[3], b[-2])  # Индексы
print(a[:2])        # Срезы
print(b[::-1])      # Срезы с шагом
print(a.index(-4))  # Индекс элемента
print(b.count(0))   # Количество элементов

s = {5, 3, 9, 2, 7, 3}
print(s)               # {2, 3, 5, 7, 9}

