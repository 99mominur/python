import math
import time


def timer(func):
    def inner(*args, **kwargs):
        print("Time Start")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'Time end. Total time taken: {end - start}')
    return inner


@timer
def get_factorial(n):
    fact = math.factorial(n)
    print(f'Factorial of {n} is {fact}.')


get_factorial(n=10)
