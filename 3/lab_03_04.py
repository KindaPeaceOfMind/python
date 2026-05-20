d1 = {
    "day": 18,
    "month": 6,
    "year": 1983
}
d2 = dict(bananas=3, apples=5, oranges=2, bag="basket")
d3 = dict([("street", "Kronverksky pr."), ("house", 49)])
d4 = dict.fromkeys(["1", "2"], 3)
print("Dict d1 = ", d1)
print("Dict d2 by dict()= ", d2)
print("Dict d3 by dict([])= ", d3)
print("Dict d4 by fromkeys = ", d4)
print("\n")

# Задание 12: Три способа создания словаря startDict
print("=== Задание 12 ===")
# Способ 1: Фигурные скобки
startDict1 = {"ready": 3, "set": 2, "go": 1}
print("startDict1 (фигурные скобки):", startDict1)

# Способ 2: Функция dict() с именованными аргументами
startDict2 = dict(ready=3, set=2, go=1)
print("startDict2 (dict() с аргументами):", startDict2)

# Способ 3: dict() со списком кортежей
startDict3 = dict([("ready", 3), ("set", 2), ("go", 1)])
print("startDict3 (dict() со списком кортежей):", startDict3)

# Задание 13: Словарь с одинаковыми значениями
print("\n=== Задание 13 ===")
value = input("Введите значение для ключей key1 и key2: ")
dict1 = dict.fromkeys(["key1", "key2"], value)
# Альтернативные способы:
# dict1 = {"key1": value, "key2": value}
# dict1 = dict(key1=value, key2=value)
print("Словарь dict1:", dict1)