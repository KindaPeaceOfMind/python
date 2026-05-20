d5 = {"bananas": 3, "apples": 5, "oranges": 2, "bag": "basket"}
d5_copy = d2.copy() if 'd2' in globals() else d5.copy()
print("Dict d5 copying d2 = ", d5_copy)

# получение значения по ключу
print("Get dict value by key d5['bag']: ", d5["bag"])
print("Get dict value by key d5.get('bag'): ", d5.get('bag'))
print("Get dict keys d5.keys(): ", d5.keys())
print("Get dict values d5.values(): ", d5.values())
print("\n")

# Задание 15: Словарь с личной информацией
print("=== Задание 15 ===")
myInfo = {
    "surname": input("Фамилия: "),
    "name": input("Имя: "),
    "middlename": input("Отчество: "),
    "day": int(input("День рождения: ")),
    "month": int(input("Месяц рождения: ")),
    "year": int(input("Год рождения: ")),
    "university": input("Университет: ")
}
print("\nКлючи словаря myInfo:", list(myInfo.keys()))
print("Значения словаря myInfo:", list(myInfo.values()))