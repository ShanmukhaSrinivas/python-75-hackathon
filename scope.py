#Scope
b=8
def func():
    a=7
    print(a)
    print(b)
func()


def red():
    a = 1
    def blue():
        b = 2
        print(a)
        print(b)

    blue()
    print(a)

red()