""" All about person """


class Human:
    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight


class Police(Human):
    # def __init__(self, gender, height, weight):
    #      super().__init__(gender, height, weight)
    def __init__(self, case, nationality):
        self.case = case
        self.nationality = nationality


polis = Police(3, "Bangladeshi")

print(polis.case)
print(polis.nationality)
