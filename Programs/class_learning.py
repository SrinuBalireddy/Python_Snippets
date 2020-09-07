class employee:

    raise_amount = 1.05

    def __init__(self, first, last, sal):
        self.first = first
        self.last = last
        self.sal = sal
        self.email = self.first+self.last+'@.com'

    def fullname(self):
        return f'{self.first} {self.last}'

    def raise_sal(self):
        self.sal = int(self.sal * self.raise_amount)


    @classmethod
    def from_string(cls, str ):
        first, last, pay = str.split('-')
        return cls(first, last, int(pay))


class developer(employee):
    raise_amount = 2

    def __init__(self, first, last, pay, skill):
        super().__init__(first, last, pay)
        #employee.__init__(self, first, last, pay)
        self.skill = skill


class manager(employee):

    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())


"""

dev1 = developer('sow','b',40000,'Java')
dev2 = developer('srinu','b',30000,'python')

mgr1 = manager('dave', 'patrick', 40000 , [dev1])
mgr1.add_emp(dev2)
print(mgr1.email)

mgr1.remove_emp(dev1)
mgr1.print_emp()

"""



"""
dev1 = developer('sow','b',40000,'Java')
dev2 = developer('srinu','b',30000,'python')
print(dev1.first)
dev1.raise_sal()
print(dev1.__dict__)
print(dev2.__dict__)
"""

"""
emp1 = employee('srinu','b',40000)
emp2 = employee('sow', 'y', 40000)

emp1.raise_amount = 1.04
employee.raise_amount = 10.03
#emp2.raise_amount = 1.08

print(emp1.__dict__)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(employee.raise_amount)
"""



import os
print(os.__file__)
