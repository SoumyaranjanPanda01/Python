from Person import person

class student(person):
    # child class
    def __init__(self, name, age, total):
        super().__init__(name, age)
        self.total = total

    def display(self):
        super().display()
        print(self.total)