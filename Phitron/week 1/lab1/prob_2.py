""" Encript and Decript """

data = "az"

shift = 1
encript = ""
for char in data:
    encript += chr((((ord(char)+shift)-97) % 26) + 97)

print(f"{encript} \n")

decript = ""

for char in encript:
    decript += chr((((ord(char)-shift) - 97) % 26) + 97)

print(decript)
