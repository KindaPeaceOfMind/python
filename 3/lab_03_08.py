lfunc = lambda x, y, z=1: x + y + z
print("lfunc(1,2,3): ", lfunc(1,2,3))
print("lfunc(1,2): ", lfunc(1,2))
print("lfunc(x=1,y=3): ", lfunc(x=1,y=3))
print("lambda result: ", \
    (lambda a,b,sep=", ": sep.join((a,b)))("Hello","World!"))
print("\n")

# Задание 21: Lambda для проверки делимости на 3
print("=== Задание 21 ===")
lam = lambda x: print(f"{x} делится на 3" if x % 3 == 0 else None) if x % 3 == 0 else None

num = int(input("Введите число для проверки делимости на 3: "))
lam(num)