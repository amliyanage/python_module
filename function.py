# # function
# def calculate_perimiter(width, height):
#     print (2 * (width + height) )

# calculate_perimiter(10, 20) # call the function

# pie = 22 / 7

# def calculate_area_of_circle(radius):
#     print( pie * radius * radius)

# calculate_area_of_circle(7) 

# #Default arguments
# def greet(name = "Guest"):
#     print("Hello " + name)

# greet()
# greet("John")

# # def add_number(a,b=3,x) :
# #     return a+b+x

# # there is an error in the above function because the default argument should be at the end of the function

# def add_number(a,x,b=3) :
#     return a+b+x

# print(add_number(1,2)) 

# # positional arguments
# def add_number(a,b,c) :
#     return a+b+c

# print(add_number(1,2,3))

# # keyword arguments
# def add_number(a,b,c) :
#     return a+b+c

# print(add_number(a=1,b=2,c=3))

# def calculate_cost(price , qty , discount = 0 , tex = 0) :
#     total = price * qty
#     discount = total * discount / 100
#     tex = total * tex / 100
#     total = total - discount + tex
#     return total

# print(calculate_cost(100, 2, 10, 5))

# ## arbitrary positional arguments
# def add_number(*args) :
#     total = 0
#     for a in args :
#         print(a)
#         total += a
#     return total

# print(add_number(1,2,3,4,5,6,7,8,9,10))

# def add_string(*args) :
#     total = ""
#     for a in args :
#         total += " " + a
#     return total

# print(add_string("Hello", "World", "Python"))
# convert the positional arguments to tuple

# if use dont know how many arguments will be passed to the function then use arbitrary positional arguments

## Q1
# write a python function called summarized_grade that accept student's name as a mandatory argument and
# an arbitrary number of grades scores the function should , 

# 1. print the student's name
# 2 . calculate and print the highest grade , lowest grade and average grade form provided scores
# 3. if no grade are provided you should print "No grades available"

# def summarized_grade(name, *scores) :
#     print("student name : " + name)
#     if len(scores) == 0 :
#         print("No grades available")
#     else :
#         print("Highest grade : ", max(scores))
#         print("Lowest grade : ", min(scores))
#         print("Average grade : ", sum(scores)/len(scores))

# summarized_grade("John", 10, 20, 30, 40, 50 , 70 , 90)
# summarized_grade("Smith")


## arbitrary keyword arguments

def print_student(**kwargs) :
    print("kwargs Type : ", type(kwargs))
    for key, value in kwargs.items() :
        print(key , " : " , value)

print_student(name = "John", age = 25, city = "New York")
# convert the keyword arguments to dictionary