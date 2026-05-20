class Person:
    """Базовый класс для представления человека"""

    _id_counter = 0  # Счётчик для уникальных ID

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display(self):
        print(f"Person: {self.firstname} {self.lastname}, Age: {self.age}")


class Student(Person):
    """Класс студента, наследуется от Person"""

    def __init__(self, firstname, lastname, age, recordBook):
        super().__init__(firstname, lastname, age)
        Student._id_counter += 1
        self.studentID = f"STU{Student._id_counter:04d}"  # Уникальный ID
        self.recordBook = recordBook  # Список: [5s, 4s, 3s, 2s]

    def display(self):
        super().display()
        print(f"  Student ID: {self.studentID}")
        print(f"  Record Book: 5s={self.recordBook[0]}, 4s={self.recordBook[1]}, "
              f"3s={self.recordBook[2]}, 2s={self.recordBook[3]}")
        print()


class Professor(Person):
    """Класс преподавателя, наследуется от Person"""

    def __init__(self, firstname, lastname, age, degree):
        super().__init__(firstname, lastname, age)
        Professor._id_counter += 1
        self.professorID = f"PROF{Professor._id_counter:04d}"  # Уникальный ID
        self.degree = degree  # Научная степень

    def display(self):
        super().display()
        print(f"  Professor ID: {self.professorID}")
        print(f"  Degree: {self.degree}")
        print()


# Задачи 13-14: Тестирование
if __name__ == "__main__":
    print("=== Students ===")
    s1 = Student("Anna", "Smirnova", 20, [10, 5, 2, 0])
    s2 = Student("Dmitry", "Kozlov", 22, [8, 7, 3, 1])
    s3 = Student("Elena", "Volkova", 19, [12, 4, 1, 0])

    s1.display()
    s2.display()
    s3.display()

    print("=== Professors ===")
    p1 = Professor("Ivan", "Petrov", 45, "PhD in Computer Science")
    p2 = Professor("Maria", "Sokolova", 52, "Doctor of Technical Sciences")
    p3 = Professor("Sergey", "Novikov", 38, "PhD in Mathematics")

    p1.display()
    p2.display()
    p3.display()