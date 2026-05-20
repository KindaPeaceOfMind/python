'''
Программа выводит все возможные уникальные строки,
составленные из символов введённой строки
'''
from itertools import permutations

input_str = input("Enter a string: ")
unique_chars = list(set(input_str))  # уникальные символы

print("\nAll unique permutations:")
results = set()

# Генерируем перестановки разной длины
for length in range(1, len(input_str) + 1):
    for perm in permutations(input_str, length):
        results.add(''.join(perm))

# Выводим отсортированные результаты
for item in sorted(results):
    print(item)

print(f"\nTotal unique strings: {len(results)}")