marks = {"phisics": 54,
         "chemistry": 45,
         "biology": 65
         }

marks["math"] = 60
marks["english"] = 65
del marks["math"]

marks_value = marks.values()
marks_key = marks.keys()
# marks.clear()
# print(marks)

# print(marks_value)
# print(marks_key)

for item in marks.items():
    print(item)