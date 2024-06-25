class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def __repr__(self):
        return self._name + " has a salary of " + "{:.2f}".format(self._salary)

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return self._name + " has a salary of  " + "{:.2f}".format(self._salary) + " and manages the " + self._department + " department"

class Executive(Manager):

    def __init__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__ (self):
        return self._name + " has a salary of " + "{:.2f}".format(self._salary) + " and the executive for the " + self._department + " department"
