class Person:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"이름 : {self.name}\t좋아하는 색:{self.color}"