# for item in sequence:
#     code block

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

for fruit in fruits:
    print(fruit)

numbers = [7,5,8,4,9,12]
square = []

for number in numbers :
    square.append(number*number)

print(square)

input_num = input("Enter a number: ")

for number in range(1 , int(input_num)+1):  
    square.append(number*number)

print(square)

# Using list comprehension
result = [ number * number for number in numbers]
print(result)

numbers = [8 , 12, -1, 5, 4, 0, -3]

square = [ number * number for number in numbers if number > 0]
print(square)

# while loop
# while condition

user_input = input("Enter number : ")

x = 1

while x <= int(user_input) :
    result = x * x
    if( result < int(user_input) ) :
        print(x*x) 
    x = x+1

while x * x <= int(user_input) :
    print(x*x)
    x = x+1