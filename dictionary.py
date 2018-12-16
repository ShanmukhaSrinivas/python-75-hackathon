#with col keys

color={"col1":"blue","col2":"green","col3":"white","col4":"red"}
print(type(color))

#adding keys and values to dict
dic=dict()
dic['exp']=14
dic['course']="python"
print(dic)
dic['exp']=15
print(dic)

#retriving data
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age')