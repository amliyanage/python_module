my_dic = {
    "name" : "John",
    "age" : 25,
    "is_student" : False,
    "price" : 10.22,
    "price" : 17
}

# print type of dictionary
print(type(my_dic))

# print value of key
print(my_dic["name"])

print(my_dic)

# update value of key
my_dic["name"] = "Smith"
print(my_dic)

# get value of key
print(my_dic.get("age"))

print(my_dic.get("address"))

my_dic.get("address","Not Found")

print(my_dic.get("address","Not Found"))

# update single value
my_dic.update({"name":"John","age":25,"is_Not_a_student":False,"price":10.122})
print(my_dic)

# add new key value
my_dic["color"] = "Red"
print(my_dic)

# remove values
my_dic.pop("color")
print(my_dic) 

# remove item
del my_dic["price"]
print(my_dic)

# use copy method
my_dic_1 = my_dic.copy()
print("dewani eka",my_dic_1)

# use clear method
my_dic.clear()
print(my_dic)

# print(len(my_dic))
# del my_dic
# print(my_dic)

my_dic_1 = my_dic.copy()
print(my_dic_1)
