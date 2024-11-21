input_mark = input("Enter a number: ")
mark = int(input_mark)
print(mark)
if mark > 100 :
    print("Invalid mark")
elif mark >= 85 :
    print("A")
elif mark >= 75 :
    print("B")
elif mark >= 65 :
    print("C")
elif mark >= 50 :
    print("D")
else :
    print("F")