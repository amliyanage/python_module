response_code = 203

# Using match statement
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Response Code")

numbers = [1]

# match statement also checking pattern matching
match numbers:
    case [] :
        print("Empty list") 
    case [x]:
        print(f"Only one element: {x}")
    case [x, y]:
        print(f"Two elements: {x} and {y}")
    case [x, y, z]:
        print(f"Three elements: {x}, {y} and {z}")
    case _:
        print("More than three elements")

