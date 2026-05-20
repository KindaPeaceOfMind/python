import math

class Geometric:
    def calculateArea(self):
        print("Calculating area")


class Square(Geometric):
    def __init__(self, a):
        self.side = a

    def _perimeter(self):  # "Приватный" метод (по соглашению)
        print("Perimeter of Square {}: {}\n".format(self.side, self.side * 4))

    def calculateArea(self):  # Переопределение метода
        print("Area of Square {}: {}\n".format(self.side, pow(self.side, 2)))


# Задача 11: Класс Circle с приватным атрибутом
class Circle(Geometric):
    def __init__(self, radius):
        self.__radius = radius  # Приватный атрибут (двойное подчёркивание)

    def calculateArea(self):  # Переопределение
        area = math.pi * pow(self.__radius, 2)
        print("Area of Circle with radius {}: {:.2f}\n".format(self.__radius, area))

    # Геттер для доступа к приватному атрибуту
    def get_radius(self):
        return self.__radius


# Тестирование
print("--- Geometric & Square ---")
geom = Geometric()
geom.calculateArea()

sq = Square(5)
sq.calculateArea()
sq._perimeter()

print("--- Circle ---")
circle = Circle(3)
circle.calculateArea()

# Проверка наследования
print("Check subclass:", issubclass(Square, Geometric))
print("Check instance sq->Square:", isinstance(sq, Square))
print("Check instance sq->Geometric:", isinstance(sq, Geometric))
print("Check instance sq->dict:", isinstance(sq, dict))

print("Geometric.__bases__:", Geometric.__bases__)
print("Square.__bases__:", Square.__bases__)
print("Circle.__bases__:", Circle.__bases__)

# Доступ к приватному атрибуту (только через имя класса!)
# print(circle.__radius)  # Ошибка!
print("Circle radius via getter:", circle.get_radius())
# Или через "имя-с-подчёркиванием":
# print(circle._Circle__radius)  # Не рекомендуется, но возможно