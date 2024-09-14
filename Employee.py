from Person import person

class employee(person):
    # child class
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        # methode overriding
        print(self.name, self.age, self.salary)