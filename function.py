# function
def calculate_perimiter(width, height):
    print (2 * (width + height) )

calculate_perimiter(10, 20) # call the function

pie = 22 / 7

def calculate_area_of_circle(radius):
    print( pie * radius * radius)

calculate_area_of_circle(7) 

#Default arguments
def greet(name = "Guest"):
    print("Hello " + name)

greet()
greet("John")

# def add_number(a,b=3,x) :
#     return a+b+x

# there is an error in the above function because the default argument should be at the end of the function

def add_number(a,x,b=3) :
    return a+b+x

print(add_number(1,2)) 

# positional arguments
def add_number(a,b,c) :
    return a+b+c

print(add_number(1,2,3))

# keyword arguments
def add_number(a,b,c) :
    return a+b+c

print(add_number(a=1,b=2,c=3))

def calculate_cost(price , qty , discount = 0 , tex = 0) :
    total = price * qty
    discount = total * discount / 100
    tex = total * tex / 100
    total = total - discount + tex
    return total

print(calculate_cost(100, 2, 10, 5))
    


