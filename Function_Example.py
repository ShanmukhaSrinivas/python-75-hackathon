#Defining a function
def function_01(n1, n2):
    a = n1+n2
    b = n1-n2
    c = n1*n2
    d = n1/n2
    return a,b,c,d
tpl = function_01(int(input('Enter a number:')), int(input('Enter another number')))
print(tpl) 
