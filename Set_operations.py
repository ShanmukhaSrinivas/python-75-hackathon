#set operations

data_set=set()
data_set.update(["DATA SCIENCE","BIG DATA"])
print(data_set)

#pop operation
num_set=set([0,1,2,3,4,5])
num_set.pop()
print(num_set)
#num_set.pop()
#print(num_set)

#remove operation:
num_set.remove(2)
print(num_set)

#discard operation
num_set.discard(3)
print(num_set)