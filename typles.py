
# Typles are immutable
my_typles  = ("Apple",8,True,5.5)

# defferent between list and typles
# list are mutable but typles are immutable

# ordered collection of items
print(my_typles[3])

# in List and Typles can add duplicate items
my_list = [12,10,5,4,1,5]
my_typles_1 = (12,10,5,4,1,5)

print(my_list)
print(my_typles_1)

# if use want to get length of typles
print(len(my_typles))

# if use need to get type of typles
print(type(my_typles))

# if tupe has only one item then it will be consider as int not typles 
my_typles_2 = (8)
print(type(my_typles_2))

# if you have only one item then you need to add comma at the end of item
my_typles_3 = (8,)
print(type(my_typles_3))

# if you want to get last item from typles
print(my_typles[-2])

# if you want to get range of items from typles
print(my_typles[1:3])

# if use want to change typles value then you need to convert it into list
# then change the value and then convert it into typles
my_typles_4 = (1,2,3,4,5)

my_list_1 = list(my_typles_4)
my_list_1[2] = 6
print(my_list_1)

my_typles_5 = tuple(my_list_1)
print(my_typles_5)

my_typle_6 = ( (1,3,5,64) , ("apple","banana") , (True,False) )
print(my_typle_6)

print(my_typle_6[1][1])
print(my_typle_6[2][1])
