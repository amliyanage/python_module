# ## lambda function
# add = lambda x,y : x + y
# print(add(10,20)) # output = 30

# result = (lambda x,y : x + y)(10,20)   
# print(result) # output = 30

# write a python program that ,
# 1 . take a list of tupeles where each tuple contains a name(string) and age(integer).
# 2 use a lambda function to filter out the tuples where the age is less than 18

my_list = [("Alice", 25), ("John", 17), ("andrew", 25), ("Kate", 15)]
result = filter(lambda x: x[1] >= 18, my_list)
print(list(result))