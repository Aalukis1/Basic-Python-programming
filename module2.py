# users = ["z","e","r","p","b","z"]
# if users[0] == users[-1]:
#     print ("TRUE")
# else:
#     print("FALSE")


def hobbies1():
    hobbies_list = input("enter your hobbies seperated by space::: ")
    new_hobbies = hobbies_list.split()
    print(new_hobbies)
    length=[]
    for hobby in range(0, len(new_hobbies)):

        length.append(len(new_hobbies[hobby]))
    print(length)
    for hobby in range(0, len(new_hobbies)):
        if len(new_hobbies[hobby]) == max(length):
            print("the longest character hobby is ..." + new_hobbies[hobby])
#         if len(hobby) > len(new_hobbies[:]):
# #     int(hobby)
#             print(hobby)

hobbies1()