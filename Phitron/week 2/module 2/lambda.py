# def square(x):
#     return x * x

def square(x): return x*x
# print(square(6))


def add(a, b): return a + b


# print(add(4, 5))

numbers = [1, 4, 6, 7, 8, 9]


def double_it(x): return x * 2


# print(list(map(double_it, numbers)))
print(*numbers)
print(*list(filter(lambda x: x % 2 == 0, numbers)))
