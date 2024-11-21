# my_list = [8,9,3,0,12,15]

# # break statement
# # use break statement to exit the loop
# for item in my_list :
#     if item == 0 :
#         break
#     else :
#         print(item)

# # continue statement
# # use continue statement to skip the current iteration
# for item in my_list :
#     if item == 0 :
#         continue
#     else :
#         print(item)


while True :
    user_input = input("Enter number : ")
    if int(user_input) == 0 :
        break
    else :
        print(int(user_input) * int(user_input) )

