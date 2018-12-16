#parametrized constructor:
class student:
    def __init__(self,n,r,m):
        self.name=n
        self.rollno=r
        self.marks=m
    def details(self):
        print('name:',self.name)
        print('roll-no:',self.rollno)
        print('marks:',self.marks)
        print('total=',sum(self.marks))
        print('average=',sum(self.marks)/len(self.marks))
n=input('enter name')
r=int(input('enter roll-no'))
m=[int(i)for i in input('enter marks').split(',')]
s=student(n,r,m)
s.details()
        