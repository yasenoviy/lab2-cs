def binary_array_sum(array):
    
    # визначаємо найбільшу довжину значень в масиві
    max_len = max(len(x) for x in array)
    
    # робимо всі значення однакової довжини, додаючи на початку нулі
    array = [x.zfill(max_len) for x in array]
    
    # створюємо список заповнений нулями
    result = [0] * (max_len + 1)
    
    # виконуємо операцію додавання бінарних чисел
    for i in range(max_len - 1, -1, -1):
        column_sum = sum(int(x[i]) for x in array) + result[i + 1]
        result[i + 1] = column_sum % 2
        result[i] += column_sum // 2

    # перетворення результату в масив 
    string_result = []
    for i in result:
        string_result.append(str(i))
    string_result.pop(0)
    return string_result

# віднімання двох бінарних чисел.
def binary_subtraction(x, y):
    x_int = int(x, 2)
    y_int = int(y, 2)
    result_int = x_int - y_int
    result_str = numb_to_bin(result_int,16)
    max_len = max(len(x), len(y), len(result_str))
    result_str = result_str.zfill(max_len)
    return result_str

# перетворюємо число в двійковий формат
def numb_to_bin(numb, bits_show):

    s = bin(numb & int("1"*bits_show, 2))[2:]
    return ("{0:0>%s}" % bits_show).format(s)


# перетворюємо бінарне число в десяткове
def bin_to_dec(binary):
    binary = int(binary)
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

# перетворюємо бінарне число в десяткове зі знаком мінус
def neg_bin_to_dec(binary):
    binary = binary.replace("0","x")
    binary = binary.replace("1", "0")
    binary = binary.replace("x", "1")
    binary = int(binary) + 1
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal



def booth_algorithm(input_x, input_y):
    print(f"\n\n\n======================({input_x},{input_y})======================\n")
    x_minus = False
    y_minus = False
    if input_x < 0:
        x_minus = True
    if input_y < 0:
        y_minus = True
    if x_minus and y_minus or not x_minus and not  y_minus:
        status = "not negative"
    if x_minus and not y_minus or not x_minus and y_minus:
        status = "negative"

    set_bin_len = 8

    
    if x_minus or y_minus:
        neg_min = min(input_x, input_y)
        x = bin(neg_min)[2:]
        # print(f"x:{x}")
        if 'b' in x:
            set_bin_len = (len(x) - 1) * 2
        else:
            set_bin_len = len(x) * 2



    # перетворюємо числа в бінарний формат та форматуємо їх для множення
    x_bin = numb_to_bin(input_x, set_bin_len)
    y_bin = numb_to_bin(input_y, set_bin_len)

    max_len = max(len(x_bin), len(y_bin))
    total_length = max_len * 2 + 1
    
    # 
    x_bin_minus = numb_to_bin(-input_x, set_bin_len)
    A = x_bin.ljust(total_length, '0')
    S = x_bin_minus.ljust(total_length, '0')
    Product = y_bin.zfill(total_length - 1)
    Product += '0'

    print(f"A:{A}")
    print(f"S:{S}")
    print(f"P:{Product}")
    
    temp = list(Product)
    print("second input array:", temp)
    print(f"max_len:{max_len}")
    for i in range(max_len):
        pre_last = temp[len(temp) - 2] 
        took_last = temp[len(temp) - 1] 
        if pre_last+took_last == "00":
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0,'0')
            else:
                temp.insert(0,'1')
            continue
        elif pre_last+took_last == "01":
            if_10 = "".join(str(x) for x in temp)
            temp = binary_array_sum([if_10, A])
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')
            else:
                temp.insert(0, '1')
            continue
        elif pre_last+took_last == "10":
            if_10 = "".join(str(x) for x in temp)
            temp = binary_array_sum([if_10, S])
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')
            else:
                temp.insert(0, '1')
            continue
        elif took_last + pre_last == "11":
            temp.pop(len(temp) - 1)
            if temp[0] == '0':
                temp.insert(0, '0')
            else:
                temp.insert(0, '1')

    temp.pop(len(temp) - 1)
    result = ''
    for j in temp:
        result += str(j)
    pretty_res = result
    if 4 < max_len < 8:
        pretty_res = result[len(result)-8:len(result)]
    else:
        pretty_res = result[len(result) - max_len:len(result)]
    print(f"result: {pretty_res} and its {status}")
    status_symbol = ''
    if not "not" in status:
        status_symbol = '-'
    if status_symbol == '-':
        print(f"decimal: {status_symbol}{neg_bin_to_dec(result)}")
    else:
        print(f"decimal: {status_symbol}{bin_to_dec(result)}")
    return result


booth_algorithm(5, -20)