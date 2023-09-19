numbers = [1, 3, 5, 6, 7]

# print(sum(numbers))

total = 0

for item in numbers:
    total += item
# print(total)

for i, number in enumerate(numbers):
    print(i, number)

nums = {1, 4, 12, 5, 5, 61}
total = 0
# print(sum(nums))
# for item in nums:
#     total += item
#     print(item)
# print(total)

numbers_tuple = (1, 4, 5, 6, 7, 8, 8)

# print(sum(numbers_tuple))

# for item in numbers_tuple:
#     total += item
#     print(item)

# print(total)

marks = {"phisics": 54,
         "chemistry": 45,
         "biology": 65
         }
marks["math"] = 60
marks["english"] = 65

# for item in marks:
#     value = marks[item]
#     print(item, value)

# for subject, mark in marks.items():
#     print(subject, mark)
