""" # problem1
data = input()
output = ""

for char in data:
    if char >= 'a' and char <= 'z':
        output += chr((ord(char) - 97) + 65)
    elif char >= 'A' and char <= 'Z':
        output += chr((ord(char) - 65) + 97)
    else:
        output += char

print(output)
 """

""" # problem2
data = int(input())

for i in range(1, data+1):

    for j in range(1, i + 1):
        print(j, end = " ")
    print("\n") """


""" #  problem3
first = 0
second = 1
third = 0
print(first, end = " ")
print(second, end = " ")
for i in range (10 - 2):
    third = first + second
    print(third, end = " ")
    first = second
    second = third
# print(third) """

""" # problem4

data = "P@#yn26at^&i5ve"
Upercase = 0
Lowercase = 0
Digits = 0
Symbol = 0
for char in data:
    if char >= 'a' and char <= 'z':
        Lowercase += 1
    elif char >= 'A' and char <= 'Z':
        Upercase += 1
    elif char >= '0' and char <= '9':
        Digits += 1
    else:
        Symbol += 1
print(f'Upercase = {Upercase}')
print(f'Lowercase = {Lowercase}')
print(f'Digits = {Digits}')
print(f'Symbol = {Symbol}') """

""" # problem5

s1 = input()
s2 = input()
output = ""

count_s1 = 0
count_s2 = 0

for char in s1:
    count_s1 += 1
for char in s2:
    count_s2 += 1
# print(count_s1, count_s2)
i = 0
count_s1 -= 1
count_s2 -= 1
while count_s1 >= 0 or count_s2 >= 0:
    output += (s1[i] + s2[count_s2])
    i += 1
    count_s1 -= 1
    count_s2 -= 1
print(output) """

""" # problem6

s1 = input()
s2 = input()
count = 0
for char in s1:
    for letter in s2:
        if char == letter:
            count += 1
count_s1 = 0
for i in s1:
    count_s1 += 1;

if count == count_s1:
    print("True")
else:
    print("False") """

""" # problem7

data1 = int(input())
data = data1
revers_data = 0

while data1 > 0:
    mod = data1 % 10
    data1 = data1 // 10
    revers_data = (revers_data * 10) + mod
# print(revers_data)
# print(data)
bull = True
while data != 0:
    a = data % 10
    data = data // 10
    b = revers_data % 10
    revers_data = revers_data // 10
    if a != b:
        bull = False
        break
if bull == True:
    print("True")
else:
    print(False) """

""" # problem8

left = int(input())
right = int(input())

for number in range(left, right):
    is_prime = True
    for i in range(2, int(number/2)):
        if number % i == 0:
            is_prime = False
    if is_prime == True:
        print(number) """

""" # problem9

data = int(input())
revers_data = 0

while data > 0:
    mod = data % 10
    data = data // 10
    revers_data = (revers_data * 10) + mod
print(revers_data) """

# problem10

data = int(input())

