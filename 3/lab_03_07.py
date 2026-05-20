def sum(x, y, z=1):
    return x + y + z

print("sum(1,2,3): ", sum(1,2,3))
print("sum(1,2): ", sum(1,2))
print("sum(x=1,y=3): ", sum(x=1,y=3))

# переменное количество аргументов
def printArgs(*args):
    print("args of printArgs(): ", args)
    return

# переменное количество аргументов и аргументов-ключевых слов
def printArgsnKwargs(m, *args, **kwargs):
    print("main argument of printArgsnKwargs(): ", m)
    print("args of printArgsnKwargs(): ", args)
    print("kwargs of printArgsnKwargs(): ", kwargs)
    return

printArgs("Hello World!", 1, 3, 5)
printArgsnKwargs("Earth", 7.125, radius=6371, pos=3)
print("\n")

# Задание 19: Функция checkArgs с проверкой количества аргументов
print("=== Задание 19 ===")
def checkArgs(*args, **kwargs):
    if len(args) <= 3 and len(kwargs) < 3:
        print("Позиционные аргументы:", args)
        print("Именованные аргументы:", kwargs)
    else:
        print("⚠️  Предупреждение: превышено количество передаваемых аргументов!")
        print(f"  Позиционных: {len(args)} (макс. 3), Именованных: {len(kwargs)} (макс. 2)")

# Тесты
print("Тест 1 (должно вывести аргументы):")
checkArgs(1, 2, a=10)

print("\nТест 2 (должно вывести предупреждение — много позиционных):")
checkArgs(1, 2, 3, 4, a=10)

print("\nТест 3 (должно вывести предупреждение — много именованных):")
checkArgs(1, a=10, b=20, c=30) 