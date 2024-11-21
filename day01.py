# # a = 2.5E4;
# # print(a);
# # print(type(a));

# # c = 5.0;
# # d = int(c);
# # print(d, type(d));

# # my_list = [20, 30 , 10, 15];
# # print(my_list, type(my_list));
# # print('index3 : ', my_list[4]);

# my_list = [20, 30 , 'cat', 'dog', True]; # python lists are ordered // python list allow duplicate
# print(my_list, type(my_list));
# print('index3 : ', my_list[4]);
# # my_list[1] = 'Kaluwa';
# print(my_list);
# print(len(my_list));
# print(my_list[-1]); # Negative indexing mechanism

# print(my_list[1:4], type(my_list[1:4])); # also return list 
# print(my_list[:3]); # return first 3 values of the list

# print(my_list[2:])

# # my_list[1:3] = ["Carrot", 17.0] 
# # print(my_list)

# my_list.insert(2, "Rat")
# print(len(my_list))
# print(my_list)

# my_list.append("Kaluwa") # Add value at end of the array
# print(len(my_list))
# print(my_list)

# my_list_1 = [1, 2, 3, 4]
# my_list.extend(my_list_1)
# print(len(my_list))
# print(my_list)

# my_list.pop(2)
# print(len(my_list))
# print(my_list)

# del my_list[2]
# print(len(my_list))
# print(my_list)

# # del my_list #destroy the list
# # print(len(my_list))
# # print(my_list)

# my_list.clear() # empty list []
# print(len(my_list))
# print(my_list)

# my_list = ["grapes", "apple", "orange", "banana"]
# my_list.sort() # This function set the list to accending order
# print(my_list) # ['apple', 'banana', 'grapes', 'orange']

# my_list = ["Grapes", "apple", "orange", "banana"]
# my_list.sort() # sort() function is case sensitive..
# print(my_list) # ['Grapes', 'apple', 'banana', 'orange']

# my_list = ["Grapes", "apple", "orange", "banana"]
# my_list.sort(key=str.lower) # remove case sensitivity (case insensitive)
# print(my_list) # ['apple', 'banana', 'grapes', 'orange']

# my_list = [5,3,10,25,8]
# my_list.sort()
# print(my_list)

# my_list = [5,3,10,25,8]
# my_list.sort(reverse=True) # this will reverse the list
# print(my_list) #[25, 10, 8, 5, 3]

# my_list_1 = [12,10,13,4,1,5]
# my_list_2 = [6,1,7,8,10]

# my_list_1.extend(my_list_2)
# print(my_list_1)
# my_list_1.sort()
# print(my_list_1)

# position_of_median = int((len(my_list_1)+1)/2)
# # print(position_of_median)
# median = my_list_1[position_of_median-1]
# print(median)

# position_of_q1 = int((len(my_list_1)+1)/4)
# print(position_of_q1)
# q1 = my_list_1[position_of_q1 - 1]
# print(q1)

# position_of_q3 = int((len(my_list_1)+1)/4)*3
# print(position_of_q3)
# q3 = my_list_1[position_of_q3 - 1]
# print(q3)

my_list_1 = [8, 5, 9, 4, 11,12]
print(my_list_1)
my_list_2 = []
my_list_2 = my_list_1.copy()
print(my_list_2)