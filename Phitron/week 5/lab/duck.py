class Teacher:
    def __init__(self, name) -> None:
        self.teacherName = name
        self.students = []

    def entry_student(self, studentObj):
        self.students.append(studentObj)


class Student:
    def __init__(self, name) -> None:
        self.studentName = name

    def enter_in_a_teacher(self, teacherObj):
        teacherObj.students.append(self)

    def __repr__(self) -> str:
        return f"Student({self.studentName})"


Alamgir = Teacher("Alamgir Hossein")
R_Rahman = Teacher("Rimon Rahman")
Imam = Teacher("Imam Hossen")
student = Student("Rahim")
student.enter_in_a_teacher(Alamgir)
student.enter_in_a_teacher(Imam)
print(Alamgir.students)
print(Imam.students)
print(R_Rahman.students)
