def dictUpdate(a):
    a.update([("x", 5)])
    print("dict in function: ", a)
    return

def dictNoUpdate(a):
    a = a.copy()
    a.update([("y", 3)])
    print("dict in function: ", a)
    return

def returnFunc(a):
    def f1(a):
        print("returned f1(a): ", a)
    return f1

d = {"v": 7}
dictUpdate(d)
print("dict out of function: ", d)
dictNoUpdate(d)
print("dict out of function: ", d)
f = returnFunc(d)
print("f: ", f)
f(2)
print("\n")

# Задание 17: Функция, возвращающая функцию для вычисления остатка
print("=== Задание 17 ===")
def returnMod():
    def mod15(x):
        result = x % 15
        print(f"Остаток от деления {x} на 15: {result}")
        return result
    return mod15

mod15 = returnMod()
num = int(input("Введите число для вычисления остатка от деления на 15: "))
mod15(num)