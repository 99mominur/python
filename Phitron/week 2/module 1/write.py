with open("messege.txt", "a") as file_write:
    file_write.write("Hello, again I am from Python\n")

read_file = open("messege.txt", "r")
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())

read_file.close()