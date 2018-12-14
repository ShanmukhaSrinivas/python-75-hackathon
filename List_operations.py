#list methods
odd=[1,3,5,7]

#adding elements to list
odd.append(7)

#adding more than one element to list
odd.extend([9,11,13])
print(odd+[9,7,5])
print(["re"]*3)

#inserting an element at specific position
odd.insert(1,3)
print(odd)

#slicing list elements
odd[2:2]=[4,7]
print(odd)

#deleting elements
del odd[2]
print(odd)

del odd[1:2]
print(odd)
