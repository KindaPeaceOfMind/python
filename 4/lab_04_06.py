class HammingEncoder:
    """Кодирование и декодирование с использованием кода Хэмминга (7,4)"""

    # Позиции контрольных битов: 1, 2, 4 (индексы 0, 1, 3)
    # Позиции данных: 3, 5, 6, 7 (индексы 2, 4, 5, 6)

    def __init__(self, dataBits=4):
        """
        Инициализация энкодера.
        Для кода (7,4): dataBits=4, controlBits=3
        """
        self.dataBits = dataBits
        # Для простоты поддерживаем только код (7,4)
        if dataBits == 4:
            self.controlBits = 3
            self.codeLength = 7
        else:
            # Упрощённый расчёт для других значений
            self.controlBits = self._calculateControlBits(dataBits)
            self.codeLength = dataBits + self.controlBits

    def _calculateControlBits(self, dataBits):
        """Расчёт количества контрольных битов: 2^r >= m + r + 1"""
        r = 0
        while (2 ** r) < (dataBits + r + 1):
            r += 1
        return r

    def encode(self, str_bits):
        """
        Кодирование строки двоичных символов (например, '1011')
        с использованием кода Хэмминга.
        Возвращает закодированную строку.
        """
        if len(str_bits) != self.dataBits:
            raise ValueError(f"Ожидается {self.dataBits} бит данных, получено {len(str_bits)}")

        # Создаём массив для кода (индексы 1..n, индекс 0 не используем для удобства)
        code = [0] * (self.codeLength + 1)

        # Размещаем данные на позициях 3,5,6,7 (для (7,4))
        data_positions = [p for p in range(1, self.codeLength + 1)
                         if p & (p - 1) != 0]  # Не степени двойки

        for i, pos in enumerate(data_positions[:self.dataBits]):
            code[pos] = int(str_bits[i])

        # Вычисляем контрольные биты (позиции 1,2,4)
        for parity_pos in [1, 2, 4]:
            if parity_pos > self.codeLength:
                break
            xor_sum = 0
            for i in range(1, self.codeLength + 1):
                if i & parity_pos:  # Если бит позиции участвует в проверке
                    xor_sum ^= code[i]
            code[parity_pos] = xor_sum

        # Возвращаем строку без нулевого элемента
        return ''.join(str(code[i]) for i in range(1, self.codeLength + 1))

    def decode(self, str_bits):
        """
        Декодирование: определение и исправление одиночной ошибки.
        Возвращает кортеж: (исправленные_данные, позиция_ошибки_или_0)
        """
        if len(str_bits) != self.codeLength:
            raise ValueError(f"Ожидается {self.codeLength} бит, получено {len(str_bits)}")

        code = [0] + [int(b) for b in str_bits]  # Индексация с 1

        # Синдром ошибки
        error_pos = 0
        for parity_pos in [1, 2, 4]:
            if parity_pos > self.codeLength:
                break
            xor_sum = 0
            for i in range(1, self.codeLength + 1):
                if i & parity_pos:
                    xor_sum ^= code[i]
            if xor_sum:
                error_pos += parity_pos

        # Исправление ошибки, если найдена
        if error_pos != 0 and error_pos <= self.codeLength:
            code[error_pos] ^= 1  # Инвертируем бит

        # Извлекаем данные
        data_positions = [p for p in range(1, self.codeLength + 1)
                         if p & (p - 1) != 0]
        data = ''.join(str(code[p]) for p in data_positions[:self.dataBits])

        return data, error_pos


# Тестирование
if __name__ == "__main__":
    encoder = HammingEncoder(dataBits=4)

    original = "1011"
    print(f"Original data: {original}")

    encoded = encoder.encode(original)
    print(f"Encoded (Hamming 7,4): {encoded}")

    # Декодирование без ошибки
    decoded, err = encoder.decode(encoded)
    print(f"Decoded: {decoded}, Error position: {err}")

    # Имитация ошибки в бите 3
    corrupted = list(encoded)
    corrupted[2] = '1' if corrupted[2] == '0' else '0'  # Инвертируем 3-й бит
    corrupted = ''.join(corrupted)
    print(f"\nCorrupted: {corrupted}")

    decoded_fixed, err_pos = encoder.decode(corrupted)
    print(f"Decoded (fixed): {decoded_fixed}, Detected error at position: {err_pos}")