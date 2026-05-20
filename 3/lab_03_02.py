# создание множества
b1 = set()
print("Set b1 = ", b1)
b2 = {"bear", "fox", "squirrel", "woodpecker", "woodpecker", "wolf", "hedgehog"}
print("Set b2 = ", b2)

# создание множества из строки
b3 = set("abcdabcdefg")
print("Set b3 from string: ", set(b3))
print("\n")

# Задание 6: Создание множества из строки
print("=== Задание 6 ===")
s = "Electricity is the set of physical phenomena associated with the presence of electric charge. Lightning is one of the most dramatic effects of electricity"
set1 = set(s)
print("Множество set1 из строки s:", set1)

# Задание 7: Вывод гласных букв
print("\n=== Задание 7 ===")
vowels = "aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ"
print("Гласные буквы из множества set1:")
for char in set1:
    if char in vowels:
        print(char, end=" ")
print()