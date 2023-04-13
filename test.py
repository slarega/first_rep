def sum_two_number(a, b):
    """Сумма переменных"""

    access_type_list = [int, float]
    if type(a) in access_type_list and type(b) in access_type_list:
        return a + b
    else:
        return False

# определение переменных
a = 5
b = 7.5

# расчет
print(sum_two_number(a, b))

