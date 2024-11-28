# abs() function
print(abs(-10))
print(abs(10))

# map() function

def cal(x) :
    return (x * x)

my_list = [1,4,3,5,3,5]

result = map(cal,my_list)
print(result) # output =  <map object at 0x00000230A59B83A0>
print("Type : ",type(result)) # output Type :  <class 'map'>

# convert map to list
print(list(result)) # output = [1, 16, 9, 25, 9, 25]
# use can pass any iterable number to map but only one function can pass to map function