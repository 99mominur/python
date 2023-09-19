class School:
    def __init__(self, name, address, principal="") -> None:
        self.name = name
        self.address = address
        self.principal = principal
        self.grades = []

    def add_grade(self, name, teacher):
        new_grade = Grade(name, teacher)
        self.grades.append(new_grade)


class Grade:
    def __init__(self, name, teacher) -> None:
        self.student = []
        self.name = name
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'{self.name} with the teacher {self.teacher}'


Oxford = School("Oxford school", "Mirpur", "Shihabul Islam")

Oxford.add_grade('class 3', "Alamgir")

print(Oxford.grades)
