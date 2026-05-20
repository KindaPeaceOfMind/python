'''
Программа преобразует введённое двенадцатеричное число
в систему счисления с основанием 14
'''

def from_decimal(num, base):
    """Преобразует десятичное число в строку в системе с основанием base"""
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEF"
    result = ""
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return result

# Ввод числа в 12-ричной системе
input_base12 = input("Enter a base-12 number (digits 0-9, A, B): ").strip().upper()

try:
    # Преобразуем в десятичную систему
    decimal_value = int(input_base12, 12)
    print(f"\nBase-12: {input_base12}")
    print(f"Decimal: {decimal_value}")
    
    # Преобразуем в 14-ричную систему
    result_base14 = from_decimal(decimal_value, 14)
    print(f"Base-14: {result_base14}")
    
except ValueError as e:
    print(f"Error: Invalid base-12 number! {e}")