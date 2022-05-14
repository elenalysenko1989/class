class Employee:
    vacation_days = 20

class Tester(Employee):

    def __init__(self, name, title) -> None:
        self.name = name
        self.title = title

    def  get_emloyee_details(self):
        return f'My name is {self.name} and I am {self.title}'
    
Hanna = Tester('Hanna', 'Accountant')
George = Tester('George', 'Manager')
Arnold = Tester('Arnold', 'Operator')

print(Hanna.name)
print(George.title)
print(Arnold.get_emloyee_details())
print(Hanna.vacation_days)