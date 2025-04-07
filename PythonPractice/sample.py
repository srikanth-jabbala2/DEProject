# my_list = [1, 2, 2, 3, 4, 4, 5]
# print(set(my_list))'''

# '''my_list = [1, 2, 2, 3, 4, 4, 5]
# my_list2 = []
# print(len(my_list))
# for i in range(len(my_list)):
#     if i!=len(my_list)-1 and my_list[i] == my_list[i+1]:
#         print("Duplicate element is: ", my_list[i])
#     else:
#         my_list2.append(my_list[i])
# print(my_list2)


my_list = [10, 1, 2, 2, 3, 4, 4, 5, 1, 10]
my_list2 = []
for item in my_list:
    if item not in my_list2:
        my_list2.append(item)
print(my_list2)
