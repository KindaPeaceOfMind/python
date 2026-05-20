import time

class Ticket:
    def __init__(self, date, name, deadline):
        self.createDate = date
        self.owner = name
        self.deadline = deadline

    def __del__(self):
        print("Delete ticket:", time.asctime(self.createDate))

    def display(self):
        print("Ticket:")
        print("  createDate:", time.asctime(self.createDate))
        print("  owner:", self.owner)
        print("  deadline:", time.asctime(self.deadline))


# Создание объекта класса Ticket
ticket1 = Ticket(
    time.localtime(),
    "Ivan Ivanov",
    time.strptime("17.12.2017", "%d.%m.%Y")
)

# Вызов метода
ticket1.display()

# Получение значения атрибута
print("Owner:", ticket1.owner)
print("Owner(getattr):", getattr(ticket1, "owner"))

# Проверка наличия атрибута
print("hasattr:", hasattr(ticket1, "owner"))

# Установка значения атрибута
setattr(ticket1, "owner", "Alexei Petrov")
print("Owner(setattr):", ticket1.owner)

# Удаление атрибута с защитой от ошибки
delattr(ticket1, "owner")
# Безопасная проверка: если атрибут удалён, не вызываем ошибку
if hasattr(ticket1, "owner"):
    print("delattr:", ticket1.owner)
else:
    print("delattr: атрибут 'owner' был удалён")

# Удаление объекта (раскомментировано по заданию)
# del ticket1
print("# print(ticket1)  # Вызовет ошибку, так как объект уже удалён")

# Задача 4: Вывод текущего времени в формате "9 Mar 2017 14:53:55"
current_time = time.localtime()
print("\nCurrent time:", time.strftime("%d %b %Y %H:%M:%S", current_time))
print("\n")
# Задача 5: Создание объекта времени из строки
time_str = "17.07.2017 10:53:00"
parsed_time = time.strptime(time_str, "%d.%m.%Y %H:%M:%S")
print("Parsed time tuple: ", parsed_time)
print("\n")
print("Parsed time as string: ", time.asctime(parsed_time))
