
""" clean the data and get a string output "a e i o u" """

data = "aNtEriOur\n\t"

data = data.lower();

output = "";

for char in data:
    # print(char)
    if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u'):
        output += char 
        if char != 'u':
            output += '_'
             

# print(data)
print(output)