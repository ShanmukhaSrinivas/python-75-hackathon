#Handling Built-in Exceptions
try:
    a=[int(i) for i in input('Enter a list:').split()]
except Exception as e:
    print(e)
else:
    print(sum(a))
