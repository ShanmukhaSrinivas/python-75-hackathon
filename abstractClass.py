#Abstract Class Example
from abc import ABC, abstractmethod
class Operation(ABC):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @abstractmethod
    def execute(self):
        pass

class add(Operation):
    def execute(self):
        print("sum is:",self.a+self.b)


class sub(Operation):
    def execute(self):
        print("sub value is",self.a-self.b)

class mul(Operation):
    def execute(self):
        print("mul value is",self.a*self.b)

class div(Operation):
    def execute(self):
        print("div value is",self.a/self.b)
              


o1=add(10,20)
o1.execute()
o2=sub(20,10)
o2.execute()
o3=mul(1,2)
o3.execute()
o4=div(50,100)
o4.execute()
