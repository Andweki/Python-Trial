#Polymorphism
#Employee work system using polymorphism

class Employee():
    def work(self):
        return "Employee is working"
    
class Programmer[Employee]:
    def work(self):
        return "Writing Code"
    
class Designer[Employee]:
    def work(self):
        return "Designing UI"
    
class Manager[Employee]:
    def work(self):
        return "Managing team"

team = [Employee(), Programmer(), Designer(), Manager()]
#print(Employee(). work())
#print(Programmer(). work())
#print(Designer(). work())
#print(Manager(). work())

for t in team:
    print(t.work())
