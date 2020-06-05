class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Robert', 'Johnson', 41000)
emp2 = Employee('Tempest', 'Davis', 40000)

print(emp1.first)
print(emp2.pay)

