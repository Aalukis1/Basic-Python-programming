lists = [3,4,5,6,7,8,9,2]

print("the list is: ", lists)

master_list = [lists[:len(lists)//2], lists[len(lists)//2:]]                    #splits the lists into 2 equal halves and creates a nested list

master_list_sum = [sum(lists[:len(lists)//2]), sum(lists[len(lists)//2:])]      #sum of the nested lists

# print("list1 is: ", list1)
# print("list2 is: ", list2)

# master_list = [list1,list2]

# master_list.append(list1)
# master_list.append(list2)

print("master list is: ", master_list)
print("sum of the master list is: ", master_list_sum)

# print("the sum of elements in list1 is ", sum(list1))

# print("the sum of elements in list2 is ", sum(list2))

# finishers = []                              #list
# first_two = finisShers[:2]                   #list of 1st 2 elements