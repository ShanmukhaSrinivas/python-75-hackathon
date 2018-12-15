#taking values through keyboard

a,b=[int(i) for i in input('enter two numbers:').split(',')]
if(a>b):
    print(a,'is big')
elif(a<b):
    print(b,'is big')
else:
    print('both are equal')

#taking values directly

a=5
b=3
if(a>b):
    print(a,'is big')
elif(b>a):
    print(b,'is big')
else:
    print('both are equal')