class Row:
    """Строка таблицы истинности"""

    _id_counter = 0

    def __init__(self, collection, value):
        Row._id_counter += 1
        self.id = Row._id_counter  # Уникальный идентификатор строки
        self.collection = collection  # Список значений переменных
        self.value = value  # Значение функции (0 или 1)

    def __repr__(self):
        return f"Row(id={self.id}, collection={self.collection}, value={self.value})"


class Table:
    """Таблица истинности"""

    def __init__(self, rowsNum):
        self.rows = []  # Список объектов Row
        self.rowsNum = rowsNum  # Ожидаемое количество строк

    def addRow(self, row):
        """Добавление строки. Ошибка, если id уже существует."""
        # Проверка на дублирование id
        for existing in self.rows:
            if existing.id == row.id:
                raise ValueError(f"Строка с id={row.id} уже существует!")
        if len(self.rows) >= self.rowsNum:
            raise ValueError("Достигнуто максимальное количество строк!")
        self.rows.append(row)

    def setRow(self, row):
        """Изменение строки по id. Ошибка, если id не найден."""
        for i, existing in enumerate(self.rows):
            if existing.id == row.id:
                self.rows[i] = row
                return
        raise ValueError(f"Строка с id={row.id} не найдена!")

    def getRow(self, rowId):
        """Получение строки по идентификатору"""
        for row in self.rows:
            if row.id == rowId:
                return row
        raise ValueError(f"Строка с id={rowId} не найдена!")

    def display(self, variables=None):
        """Вывод таблицы в формате: id | x1 x2 ... | f"""
        if not self.rows:
            print("Таблица пуста")
            return

        # Заголовок
        if variables is None:
            variables = [f"x{i+1}" for i in range(len(self.rows[0].collection))]
        header = "id\t" + "\t".join(variables) + "\tf(" + ",".join(variables) + ")"
        print(header)
        print("-" * len(header.expandtabs()))

        # Строки
        for row in self.rows:
            row_str = f"{row.id}\t" + "\t".join(map(str, row.collection)) + f"\t| {row.value}"
            print(row_str)
        print()


class LogicFunction:
    """Логическая функция с таблицей истинности"""

    def __init__(self, variablesNum, table):
        self.variablesNum = variablesNum  # Количество переменных
        self.table = table  # Объект класса Table

    def getExpression(self):
        """
        Вычисление минимальной ДНФ (упрощённо).
        Для полноценной минимизации требуется алгоритм Квайна-Мак-Класки.
        Здесь возвращаем СДНФ по единицам.
        """
        terms = []
        variables = [f"x{i+1}" for i in range(self.variablesNum)]

        for row in self.table.rows:
            if row.value == 1:
                term_parts = []
                for i, val in enumerate(row.collection):
                    if val == 1:
                        term_parts.append(variables[i])
                    else:
                        term_parts.append(f"¬{variables[i]}")
                terms.append(" ∧ ".join(term_parts))

        if not terms:
            return "0"  # Тождественный ноль
        return " ∨ ".join(f"({t})" for t in terms)

    def getTable(self):
        """Получение объекта таблицы"""
        return self.table

    def printTable(self, variables=None):
        """Вывод таблицы истинности"""
        self.table.display(variables)


# Тестирование
if __name__ == "__main__":
    print("=== Logic Function Demo ===\n")

    # Создаём таблицу для функции 2 переменных: f = x1 XOR x2
    table = Table(rowsNum=4)

    # Добавляем строки: [x1, x2] -> f
    table.addRow(Row([0, 0], 0))  # id=1
    table.addRow(Row([0, 1], 1))  # id=2
    table.addRow(Row([1, 0], 1))  # id=3
    table.addRow(Row([1, 1], 0))  # id=4

    # Создаём логическую функцию
    func = LogicFunction(variablesNum=2, table=table)

    # Вывод таблицы
    print("Truth Table for XOR:")
    func.printTable(variables=["x1", "x2"])

    # Получение выражения (СДНФ)
    print("Minimal Expression (SDNF):")
    print(func.getExpression())

    # Демонстрация методов Table
    print("\n=== Table Methods Demo ===")
    row = table.getRow(2)
    print(f"Row with id=2: {row}")

    # Изменение строки
    new_row = Row([0, 1], 0)  # Меняем значение функции для [0,1]
    new_row.id = 2  # Сохраняем тот же id
    table.setRow(new_row)
    print("After updating row id=2:")
    func.printTable(["x1", "x2"])