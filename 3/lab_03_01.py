# создание кортежа
a1 = tuple()
a2 = 1, 2, 3, "abc"
a3 = (1, 2, 3, "abc")
print("Tuple a1 = ", a1)
print("Tuple a2 = ", a2)
print("Tuple a3 = ", a3)

# создание кортежа из других структур данных
l = [1, 2, 3, "abc"]  # из списка
a4 = tuple(l)
print("Tuple a4 from list l = ", a4)
a5 = tuple("Hello, World!")  # из строки
print("Tuple a5 from string = ", a5)

# вложенность кортежей
a6 = a2, a3
print("Tuple a6 formed by a2 and a3 = ", a6)

# объединение кортежей
a7 = a2 + a3
print("Tuple a7 by combining a2 and a3 = ", a7)

# доступ к элементам кортежей
print("a6[0]: ", a6[0])
print("a6[0][3]: ", a6[0][3])

# Задание 2: Раскомментированная строка вызовет ошибку,
# так как кортежи неизменяемы
a6[0][3] = "cba"  # TypeError: 'tuple' object does not support item assignment

print("\n")

# Задание 3: Кортеж с датой рождения и ФИО
print("=== Задание 3 ===")
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения: "))
year = int(input("Введите год рождения: "))
k1 = (day, month, year)

surname = input("Введите фамилию: ")
name = input("Введите имя: ")
patronymic = input("Введите отчество: ")
k2 = (surname, name, patronymic)

k3 = k1 + k2
print("Объединённый кортеж k3:", k3)

# Задание 4: Вложенные кортежи
print("\n=== Задание 4 ===")
k4 = (k1, k2)
print("Вложенный кортеж k4:", k4)
print("Второй элемент второго вложенного кортежа:", k4[1][1])