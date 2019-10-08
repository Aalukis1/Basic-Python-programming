#program to display linear search and bubble sort

# l1 = [2,3,4,5,6,7,8,9]

# for x in l1:
#     if x == 6:
#         print(l1.index(x))

l2 = [8,1,3,7,3,9,2,23,45,232,546,10]
for x in range(len(l2)-1,0,-1):
        for i in range(x):
                while l2[i] > l2[i + 1]:
                        temp = l2[i]
                        l2[i] = l2[i+1]
                        l2[i+1]= temp
print(l2)

# def bubblesort(l2):
#         for x in range(len(l2)-1,0,-1):
#                 for i in range(x):
#                         if l2[i] > l2[i+1]:
#                                 temp = l2[i]
#                                 l2[i] = l2[i+1]
#                                 l2[i+1] = temp
# 
# bubblesort(l2)
# print(l2)   

