my_list = [12,10,13]

x , y , z = my_list

print(x)
print(y)
print(z)

# Output:
# 12
# 10
# 13

# typle packing
my_tuple = (12,10,13)

# typle unpacking
x , y , z = my_tuple

print(x)
print(y)
print(z)

# Output:
# 12
# 10
# 13


# Dictionary unpacking
person = {
    'name' : 'John Doe',
    'age' : 30,
    'city' : 'New York',
}

for key , value in person.items():
    print(key , value)

for key in person.keys() :
    print(key)

for value in person.values() :
    print(value)

# Output:
# name John Doe
# age 30
# city New York