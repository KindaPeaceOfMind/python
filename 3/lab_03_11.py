import heapq
from collections import Counter, defaultdict
import pickle

# ========== Хаффман ==========
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None
    freq = Counter(text)
    heap = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)
    return heap[0]

def build_huffman_codes(node, prefix="", codes={}):
    if node is None:
        return codes
    if node.char is not None:
        codes[node.char] = prefix or "0"
    build_huffman_codes(node.left, prefix + "0", codes)
    build_huffman_codes(node.right, prefix + "1", codes)
    return codes

def encode_huffman(text):
    if not text:
        return "", {}
    root = build_huffman_tree(text)
    codes = build_huffman_codes(root)
    encoded = ''.join(codes[char] for char in text)
    return encoded, codes

def decode_huffman(encoded, codes):
    if not encoded:
        return ""
    reverse_codes = {v: k for k, v in codes.items()}
    decoded, current = [], ""
    for bit in encoded:
        current += bit
        if current in reverse_codes:
            decoded.append(reverse_codes[current])
            current = ""
    return ''.join(decoded)

def encodeHuffman(fileIn, fileOut):
    try:
        with open(fileIn, 'r', encoding='utf-8') as f:
            text = f.read()
        encoded, codes = encode_huffman(text)
        with open(fileOut, 'wb') as f:
            pickle.dump({'encoded': encoded, 'codes': codes, 'original_len': len(text)}, f)
        return True
    except Exception as e:
        print(f"Ошибка кодирования Хаффмана: {e}")
        return False

def decodeHuffman(fileIn, fileOut):
    try:
        with open(fileIn, 'rb') as f:
            data = pickle.load(f)
        decoded = decode_huffman(data['encoded'], data['codes'])
        with open(fileOut, 'w', encoding='utf-8') as f:
            f.write(decoded)
        return True
    except Exception as e:
        print(f"Ошибка декодирования Хаффмана: {e}")
        return False

# ========== Лемпель-Зив (LZ77 упрощённый) ==========
def encode_lz(text, window_size=20, lookahead=10):
    if not text:
        return [], {}
    encoded, pos = [], 0
    while pos < len(text):
        best_match = (0, 0, text[pos] if pos < len(text) else '')
        for length in range(1, min(lookahead + 1, len(text) - pos + 1)):
            substring = text[pos:pos + length]
            search_start = max(0, pos - window_size)
            found = text[search_start:pos].rfind(substring)
            if found != -1:
                offset = pos - found
                if length > best_match[1]:
                    best_match = (offset, length, text[pos + length] if pos + length < len(text) else '')
        if best_match[1] > 0:
            encoded.append((best_match[0], best_match[1], best_match[2]))
            pos += best_match[1] + (1 if best_match[2] else 0)
        else:
            encoded.append((0, 0, text[pos]))
            pos += 1
    return encoded, {'window_size': window_size, 'lookahead': lookahead}

def decode_lz(encoded, params):
    if not encoded:
        return ""
    window_size = params.get('window_size', 20)
    decoded = []
    for offset, length, next_char in encoded:
        if length > 0:
            start = len(decoded) - offset
            for i in range(length):
                decoded.append(decoded[start + i])
        if next_char:
            decoded.append(next_char)
    return ''.join(decoded)

def encodeLZ(fileIn, fileOut):
    try:
        with open(fileIn, 'r', encoding='utf-8') as f:
            text = f.read()
        encoded, params = encode_lz(text)
        with open(fileOut, 'wb') as f:
            pickle.dump({'encoded': encoded, 'params': params, 'original_len': len(text)}, f)
        return True
    except Exception as e:
        print(f"Ошибка кодирования LZ: {e}")
        return False

def decodeLZ(fileIn, fileOut):
    try:
        with open(fileIn, 'rb') as f:
            data = pickle.load(f)
        decoded = decode_lz(data['encoded'], data['params'])
        with open(fileOut, 'w', encoding='utf-8') as f:
            f.write(decoded)
        return True
    except Exception as e:
        print(f"Ошибка декодирования LZ: {e}")
        return False

# ========== Тестирование и сравнение ==========
def calculate_compression_ratio(original_file, compressed_file):
    import os
    original_size = os.path.getsize(original_file)
    compressed_size = os.path.getsize(compressed_file)
    return original_size / compressed_size if compressed_size > 0 else float('inf')

if __name__ == "__main__":
    # Создание тестовых файлов
    text_huffman = "aaaaabbbcccdde"  # Много повторений символов — хорошо для Хаффмана
    text_lz = "abababababababab" * 10  # Повторяющиеся паттерны — хорошо для LZ
    
    with open("test_huffman.txt", "w", encoding="utf-8") as f:
        f.write(text_huffman * 100)
    with open("test_lz.txt", "w", encoding="utf-8") as f:
        f.write(text_lz)
    
    print("=== Тестирование Хаффмана ===")
    if encodeHuffman("test_huffman.txt", "test_huffman_enc.bin"):
        if decodeHuffman("test_huffman_enc.bin", "test_huffman_dec.txt"):
            with open("test_huffman.txt", "r", encoding="utf-8") as f1:
                with open("test_huffman_dec.txt", "r", encoding="utf-8") as f2:
                    print("✓ Декодирование Хаффмана:", "УСПЕШНО" if f1.read() == f2.read() else "ОШИБКА")
            ratio = calculate_compression_ratio("test_huffman.txt", "test_huffman_enc.bin")
            print(f"Коэффициент сжатия (Хаффман): {ratio:.2f}")
    
    print("\n=== Тестирование Лемпеля-Зива ===")
    if encodeLZ("test_lz.txt", "test_lz_enc.bin"):
        if decodeLZ("test_lz_enc.bin", "test_lz_dec.txt"):
            with open("test_lz.txt", "r", encoding="utf-8") as f1:
                with open("test_lz_dec.txt", "r", encoding="utf-8") as f2:
                    print("✓ Декодирование LZ:", "УСПЕШНО" if f1.read() == f2.read() else "ОШИБКА")
            ratio = calculate_compression_ratio("test_lz.txt", "test_lz_enc.bin")
            print(f"Коэффициент сжатия (Лемпель-Зив): {ratio:.2f}")
    
    print("\n=== Сравнение методов ===")
    # Тест на тексте, подходящем для Хаффмана
    ratio_huff_on_huff = calculate_compression_ratio("test_huffman.txt", "test_huffman_enc.bin")
    encodeLZ("test_huffman.txt", "test_huffman_lz.bin")
    ratio_lz_on_huff = calculate_compression_ratio("test_huffman.txt", "test_huffman_lz.bin")
    
    # Тест на тексте, подходящем для LZ
    ratio_lz_on_lz = calculate_compression_ratio("test_lz.txt", "test_lz_enc.bin")
    encodeHuffman("test_lz.txt", "test_lz_huff.bin")
    ratio_huff_on_lz = calculate_compression_ratio("test_lz.txt", "test_lz_huff.bin")
    
    print(f"Текст с повторами символов (для Хаффмана):")
    print(f"  Хаффман: {ratio_huff_on_huff:.2f}, LZ: {ratio_lz_on_huff:.2f}")
    print(f"Текст с повторяющимися паттернами (для LZ):")
    print(f"  LZ: {ratio_lz_on_lz:.2f}, Хаффман: {ratio_huff_on_lz:.2f}")
    
    print("\n📌 Вывод:")
    print("  • Метод Хаффмана эффективнее для текстов с неравномерным распределением символов")
    print("  • Метод Лемпеля-Зива эффективнее для текстов с повторяющимися подстроками")