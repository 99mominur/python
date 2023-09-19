def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def add(num1, num2= 0):
    return num1 + num2


print(add(num2= 2, num1= 4))
