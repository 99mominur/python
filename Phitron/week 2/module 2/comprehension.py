numbers = [1, 56, 67, 8, 9, 4, 34]

odd_numbers = []

for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

# print(*odd_numbers)

odd_numbers2 = [num for num in numbers if num % 2 == 0 if num % 4 == 0]

# print(*odd_numbers2)

names = ["mominur", "sakid", "rakid"]
ages = [22, 35, 23]

a_list = [(name, age) for name in names for age in ages if age < 23]

print(a_list)