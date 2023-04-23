import struct
import math

def multiply(a, b):
    # перевірка на спеціальні випадки
    if math.isnan(a) or math.isnan(b):
        return float('nan')
    if math.isinf(a) or math.isinf(b):
        return float('inf')
    if a == 0.0 or b == 0.0:
        return 0.0
    
    # перетворення числа в десяткове представлення
    a_bits = struct.unpack('I', struct.pack('f', a))[0]
    b_bits = struct.unpack('I', struct.pack('f', b))[0]
    
    # визначення знаків чисел
    a_sign = (a_bits >> 31) & 1
    b_sign = (b_bits >> 31) & 1
    
    # виділення показника та мантиси з бінарного представлення числа
    a_exp = (a_bits >> 23) & 0xFF
    b_exp = (b_bits >> 23) & 0xFF
    a_mantissa = a_bits & 0x7FFFFF
    b_mantissa = b_bits & 0x7FFFFF
    
    # множення мантиси
    prod_mantissa = a_mantissa * b_mantissa
    
    # нормалізація отриманого результату
    shift_amt = 0
    if prod_mantissa & (1 << 46):
        prod_mantissa >>= 1
        shift_amt = 1
        
    # поєднання знаку, експоненти та мантиси,
    # щоб отримати остаточне двійкове представлення
    result_sign = a_sign ^ b_sign
    result_exp = a_exp + b_exp - 127 + shift_amt
    
    if result_exp >= 255:
        # якщо результат перевищує діапазон показника, повертається нескінченність.
        return struct.unpack('f', struct.pack('I', (result_sign << 31) | 0x7F800000))[0]
    
    elif result_exp <= 0:
        # якщо результат менше діапазону показника, повернути 0
        return struct.unpack('f', struct.pack('I', result_sign << 31))[0]
    
    result_bits = (result_sign << 31) | (result_exp << 23) | (prod_mantissa & 0x7FFFFF)
    
    # перетворення бінарного числа у десятковий формат з плаваючою точкою
    result = struct.unpack('f', struct.pack('I', result_bits))[0]
    return result

a = 1.5
b = 2.0
result = multiply(a, b)
print(f"{a} * {b} = {result}")

a = 0.15
b = 0.25
result = multiply(a, b)
print(f"{a} * {b} = {result}")

a = -1.5
b = 258.25
result = multiply(a, b)
print(f"{a} * {b} = {result}")
