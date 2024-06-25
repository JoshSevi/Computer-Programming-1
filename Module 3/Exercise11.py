class Employee:

    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def __repr__(self):
        return self._name + " has a salary of " + self._salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return self._name + " has a salary of " + self._salary + " and manages the " + self._department


class Executive(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return self._name + " has a salary of " + self._salary + " and is the executive for the " + self._department


Emp = Employee("John Smith", "45000.00")
Mgr = Manager("Jane Doe", "60000.00", "Widgets Department")
Exec = Executive("Weird Guy", "90000.00", "Thingies Department")

print(Emp)
print(Mgr)
print(Exec)