import re
from collections import Counter

# Чтение текста из файла
with open("3/text1.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Очистка текста и получение слов
words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

print("words = ", words)
print("\n")

print("Counter(words) = ", Counter(words))
print("\n")

print("dict(Counter(words)) = ", dict(Counter(words)))

# Подсчёт частоты слов
textDict = dict(Counter(words))

# Запись словаря в файл
with open("textDict.txt", "w", encoding="utf-8") as f:
    for word, count in sorted(textDict.items(), key=lambda x: -x[1]):
        f.write(f"{word}: {count}\n")

print("Словарь частот слов сохранён в textDict.txt")
print(f"Всего уникальных слов: {len(textDict)}")
print(f"Топ-10 наиболее частых слов:")
for word, count in sorted(textDict.items(), key=lambda x: -x[1])[:10]:
    print(f"  {word}: {count}")