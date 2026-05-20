class Worker:
    'doc class Worker'
    count = 0  # Общий атрибут класса

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Worker.count += 1  # Увеличиваем счётчик при создании объекта

    def display(self):
        print("Worker:")
        print("{} {}".format(self.name, self.surname))


# Тестирование класса Worker
w1 = Worker("Ivan", "Ivanov")
print("w1.count:", w1.count)

w2 = Worker("Alexei", "Petrov")
print("w2.count:", w2.count)
print("w1.count:", w1.count)
print("Worker.count: {}\n".format(Worker.count))

# Специальные атрибуты класса
print("Worker.__name__:", Worker.__name__)
print("Worker.__dict__:", Worker.__dict__)
print("Worker.__doc__:", Worker.__doc__)
print("Worker.__bases__:", Worker.__bases__)


# Задача 7: Класс Animal
class Animal:
    'Класс для представления животных'
    id = 0  # Общий атрибут — счётчик

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.id += 1  # Увеличиваем ID при создании
        self.instance_id = Animal.id  # Уникальный ID для объекта

    def display(self):
        print("Animal id:", self.instance_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print()


# Задача 8-9: Создание объектов Animal
print("\n--- Animals ---")
a1 = Animal("Barsik", 3)
a2 = Animal("Murka", 5)
a3 = Animal("Rex", 2)

a1.display()
a2.display()
a3.display()

# Пояснение: атрибут id — общий для класса, поэтому при изменении
# Animal.id он меняется для всех объектов. Чтобы у каждого объекта
# был свой уникальный ID, мы сохраняем значение в атрибут экземпляра
# self.instance_id в момент создания.