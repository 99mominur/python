import pandas

data = pandas.read_csv("hr.csv")
# print(data)
# missing data
# print(data.isnull().values.any())
# check data type
# print(data.dtypes)

print(data.salary)
