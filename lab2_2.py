def binary_division(dividend, divisor):
    # перевірка на випадок ділення на 0
    if divisor == 0:
        raise ZeroDivisionError("Ділення на 0 неможливе")
    
    # конвертуємо числа у бінарний формат
    dividend_bin = bin(dividend)[2:]
    divisor_bin = bin(divisor)[2:]
    
    # ініціалізуємо змінні для зберігання результату та остачі
    quotient = ""
    remainder = 0
    
    # проходимо по кожному біту ділення
    for i in range(len(dividend_bin)):
        # додаємо поточний біт ділення до остачі
        remainder = (remainder << 1) + int(dividend_bin[i])
        
        # перевіряємо, чи можемо виконати ділення
        if remainder >= int(divisor_bin, 2):
            # віднімаємо дільник від остачі
            remainder -= int(divisor_bin, 2)
            # додаємо біт до результату
            quotient += "1"
        else:
            # додаємо "0" до результату
            quotient += "0"
    
    # конвертуємо результат з бінарного у десятковий формат
    quotient = int(quotient, 2)
    remainder = int(bin(remainder)[2:], 2)
    
    return quotient, remainder

print(binary_division(839, 112))