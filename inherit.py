class A(object):
    def method(self):
        print("A class method")
        super().method()

class B(object):
    def method(self):
        print("B class method")
        super().method()

class C(object):
    def method(self):
        print('class method')

class X(A,B):
        def method(self):
            print("X class method")
            super().method()
class Y(B,C):
    def method(self):
        print("y class method")
        super().method()

class P(X,Y,C):
    def method(self):
        print("p class method")
        super().method()

p1=P()
p1.method()
print(P.mro())