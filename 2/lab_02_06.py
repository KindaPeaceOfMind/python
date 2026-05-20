'''
Программа выводит дополнительный код (two's complement)
введённого шестнадцатеричного числа на 8 разрядов
'''
hex_input = input("Enter a hexadecimal number: ").strip()

# Преобразуем hex в десятичное число
try:
    num = int(hex_input, 16)
except ValueError:
    print("Invalid hexadecimal number!")
    exit()

# Ограничиваем 8 битами (0-255)
num = num & 0xFF  # маска для 8 бит

# Вычисляем дополнительный код (для отрицательных чисел)
# Для 8-бит: two's complement = (256 - num) % 256
if num > 127:  # если старший бит = 1, это отрицательное число
    twos_complement = num  # уже в формате two's complement
    decimal_value = num - 256  # истинное значение
    print(f"\nHex: {hex_input}")
    print(f"Unsigned decimal: {num}")
    print(f"Signed decimal (two's complement): {decimal_value}")
    print(f"Binary (8-bit): {bin(num)[2:].zfill(8)}")
else:
    print(f"\nHex: {hex_input}")
    print(f"Decimal: {num}")
    print(f"Binary (8-bit): {bin(num)[2:].zfill(8)}")
    print(f"Two's complement (same for positive): {bin(num)[2:].zfill(8)}")