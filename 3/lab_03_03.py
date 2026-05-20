b2 = set("bear") 
print("b2 = ", b2)
print("Check 'bear' in b2 = ", "bear" in b2)
b4 = set("123456135")
b5 = set("12367")
print("Set b4: {0}, \nSet b5: {1}".format(b4, b5))
print("b4 - b5: ", b4 - b5)
print("b4 difference b5 (b4-b5): ", b4.difference(b5))
print("b4 | b5: ", b4 | b5)
print("b4 union b5 (b4 | b5): ", b4.union(b5))
print("b4 & b5: ", b4 & b5)
print("b4 intersection b5 (b4&b5): ", b4.intersection(b5))
print("b4 ^ b5: ", b4 ^ b5)
print("b4 and b5 are disjoint: ", b4.isdisjoint(b5))
b4.update(b5)
print("add b5 to b4: ", b4)
b4.add("abc")
print("add 'abc' to b4: ", b4)
b4.remove("5")
print("remove element '5' from b4: ", b4)
b4.clear()
print("clear b4: ", b4)
print("\n")

# Задание 9: Операции с множествами set1 и set2
print("=== Задание 9 ===")
set1 = set("qetuwrt")
set2 = set("asfrewgq")

print("Исходные множества:")
print("set1:", set1)
print("set2:", set2)

print("\n--- До изменения ---")
print("Разность set1 - set2:", set1 - set2)
print("Объединение set1 | set2:", set1 | set2)
print("Пересечение set1 & set2:", set1 & set2)
print("Симметричная разность set1 ^ set2:", set1 ^ set2)

# Изменение множеств
set1.update(set2)
set2.add("t")
set2.add("u")

print("\n--- После изменения ---")
print("set1 после update(set2):", set1)
print("set2 после add('t') и add('u'):", set2)

print("\nРазность set1 - set2:", set1 - set2)
print("Объединение set1 | set2:", set1 | set2)
print("Пересечение set1 & set2:", set1 & set2)
print("Симметричная разность set1 ^ set2:", set1 ^ set2)

# Задание 10: frozenset
print("\n=== Задание 10 ===")
set3 = frozenset(set1)
print("Неизменяемое множество set3:", set3)
try:
    set3.remove("q")  # Вызовет ошибку
except AttributeError as e:
    print(f"Ошибка: {e}")
    print("frozenset не поддерживает методы изменения, "
    "так как является неизменяемым типом данных")
