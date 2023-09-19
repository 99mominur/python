class Student:
    def __init__(self, name, id, marks) -> None:
        self._name = name
        self.__id = id
        self.marks = marks

    @property
    def Student_id(self):
        return self.__id

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        del self._name


chowdhury = Student("choto", 14, 85)

# print(chowdhury.Student_id)
# chowdhury.Student_id = 77
print(chowdhury.name)
del chowdhury.name
# print(chowdhury.name)

print(dir(chowdhury))
