def sum_of_digit(number):
    number = str(number)
    if number == "":
        return 0
    return sum_of_digit(number[:-1]) + int(number[-1])

'''
def sum_of_digit(number):
    quot = number // 10
    remainder = number % 10
    if quot == 0:
        return remainder
    return sum_of_digit(quot) + remainder
'''

print(sum_of_digit(3904)) # 16
