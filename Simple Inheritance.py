class student:
    def __init__(self, roll_no, name, total):
        self.roll_no = roll_no
        self.name = name
        self.total = total

    def display(self):
        print(self.roll_no, self.name, self.total)

    def result(self):
        if self.total >= 120:
            print('pass')
        else:
            print('fail')

# __init__, display, result these all are methodes for class student.


s0 = student(0, 'somu', 160)
s0.display()
s0.result()
s1 = student(1, 'amit', 99)
s1.display()
s1.result()