result = 0

try:
    result = 10/0
    print(result)
except ZeroDivisionError as err:
    print(err)
finally:
    print("tast done")


print(result)
