#Interface

from abc import *

class MyInter(ABC):
    @abstractmethod
    def area(self, x, y):
        pass

class Square(MyInter):
    def area(self,x , y):
        print("The area of a square is", x*x)

class Rectangle(MyInter):
    def area(self,x, y):
        print("The area of the rectangle is ", x*y)

obj1 = Square()
x = int(input('Enter the value of side'))
y = int(input('Enter the breadth of the rectangle'))
obj1.area(x, y)

obj2= Rectangle()
obj2.area(x, y)