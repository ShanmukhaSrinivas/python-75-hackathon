# making the local variable as global using global keywords
# global scope
m = 15

def local_function(n):
    global m
    m=n

print('Local',m)
local_function(52.5)
print('Global', m)