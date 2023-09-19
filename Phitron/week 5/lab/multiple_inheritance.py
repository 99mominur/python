class School:
    def __init__(self, name) -> None:
        self.SchoolName = name

    def __repr__(self) -> str:
        return f"School({self.SchoolName})"


class Teacher:
    def __init__(self, name) -> None:
        self.teacherName = name

    def __repr__(self) -> str:
        return f"Teacher({self.teacherName})"


class Student(Teacher, School):
    def __init__(self, name, teacherName, schoolName) -> None:
        self.studentname = name
        Teacher.__init__(self, teacherName)
        School.__init__(self, schoolName)

    def __repr__(self) -> str:
        return f"Student({self.studentname})"


student = Student("Rakib", "Alamgir Hossein", "prime Univercity")
print(student.teacherName)
