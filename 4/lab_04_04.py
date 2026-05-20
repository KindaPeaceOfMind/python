import heapq
from collections import defaultdict, Counter


class Encoder:
    """Базовый класс для кодировщиков"""

    def encode(self, text):
        """Кодирование строки (переопределяется в наследниках)"""
        raise NotImplementedError("Метод encode() должен быть переопределён")

    def decode(self, encoded):
        """Декодирование строки (переопределается в наследниках)"""
        raise NotImplementedError("Метод decode() должен быть переопределён")


class HuffmanEncoder(Encoder):
    """Кодирование по методу Хаффмана"""

    def __init__(self, compression_coef=0.0):
        self.__compression_coef = compression_coef
        self.codes = {}
        self.reverse_codes = {}

    def __setCompressionCoef(self, original_len, encoded_len):
        """Приватный метод расчёта коэффициента сжатия"""
        if original_len > 0:
            self.__compression_coef = (1 - encoded_len / original_len) * 100
        return self.__compression_coef

    def getCompressionCoef(self):
        """Публичный метод получения коэффициента"""
        return self.__compression_coef

    def _build_tree(self, text):
        """Построение дерева Хаффмана"""
        freq = Counter(text)
        heap = [[weight, [char, ""]] for char, weight in freq.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    def encode(self, text):
        """Кодирование строки методом Хаффмана"""
        if not text:
            return ""
        tree = self._build_tree(text)
        self.codes = {char: code for char, code in tree}
        self.reverse_codes = {code: char for char, code in self.codes.items()}

        encoded = ''.join(self.codes[char] for char in text)
        self.__setCompressionCoef(len(text) * 8, len(encoded))  # 8 бит на символ
        return encoded

    def decode(self, encoded):
        """Декодирование строки Хаффмана"""
        decoded = ""
        current_code = ""
        for bit in encoded:
            current_code += bit
            if current_code in self.reverse_codes:
                decoded += self.reverse_codes[current_code]
                current_code = ""
        return decoded


class LZEncoder(Encoder):
    """Упрощённое кодирование по методу Лемпеля-Зива (LZ78)"""

    def __init__(self, compression_coef=0.0):
        self.__compression_coef = compression_coef
        self.dictionary = {}

    def __setCompressionCoef(self, original_len, encoded_len):
        """Приватный метод расчёта коэффициента сжатия"""
        if original_len > 0:
            self.__compression_coef = (1 - encoded_len / original_len) * 100
        return self.__compression_coef

    def getCompressionCoef(self):
        """Публичный метод получения коэффициента"""
        return self.__compression_coef

    def encode(self, text):
        """Кодирование строки методом LZ78"""
        if not text:
            return ""
        self.dictionary = {}
        dict_size = 256  # Начальный размер словаря (ASCII)
        result = []
        w = ""

        for c in text:
            wc = w + c
            if wc in self.dictionary:
                w = wc
            else:
                result.append(self.dictionary.get(w, len(self.dictionary) + 255))
                self.dictionary[wc] = len(self.dictionary) + 256
                w = c

        if w:
            result.append(self.dictionary.get(w, len(self.dictionary) + 255))

        # Для простоты возвращаем строку из кодов, разделённых пробелами
        encoded = ' '.join(map(str, result))
        self.__setCompressionCoef(len(text), len(result) * 4)  # ~4 байта на код
        return encoded

    def decode(self, encoded):
        """Декодирование строки LZ78 (упрощённо)"""
        # Для полноценной реализации требуется сохранение словаря
        # Здесь возвращаем заглушку
        return "[Decoding requires dictionary state - not implemented in demo]"


# Тестирование (Задача 12)
if __name__ == "__main__":
    test_string = "Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991."

    print("--- Huffman Encoder ---")
    huff = HuffmanEncoder()
    encoded_huff = huff.encode(test_string)
    decoded_huff = huff.decode(encoded_huff)
    print(f"Original: {test_string[:50]}...")
    print(f"Encoded (first 100 chars): {encoded_huff[:100]}...")
    print(f"Decoded matches: {decoded_huff == test_string}")
    print(f"Compression: {huff.getCompressionCoef():.2f}%\n")

    print("--- LZ Encoder ---")
    lz = LZEncoder()
    encoded_lz = lz.encode(test_string)
    print(f"Encoded LZ (first 100 chars): {encoded_lz[:100]}...")
    print(f"Compression: {lz.getCompressionCoef():.2f}%")