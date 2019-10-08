
# def person(first_name, lastName):
#     print(first_name, lastName)


# person("peter", "JOhn")

 #example 2


# num1 = [24, 15, 5, 9, 18,56,13]
# num2 = [7, 3, 12, 8,2,45,10,39]

# num3 = []
# num4 = []
# number = []
# def arrange():                          #defines the function
#     for num in num1:
#         if num%2 ==0:
#             number.append(num)          #collects even numbers in num1 into number
#     for num in num2:
#         if num%2 !=0:
#             number.append(num)          #collects old numbers in num2 into number
#     # number.append(num3)
#     # number.append(num4)
#     return number


# print(arrange())                        #prints the 'number' list 

#EXAMPLE 3
# word = input("say anything: ")
# def evens(lower, upper):
#     collect = []
#     for num in range(lower, upper,):
#         if num % 2 == 0 and num % 5 !=0:
#             collect.append(num)
#     return collect


# print(evens(1,20))

#EXAMPLE 4: program to print the even index of a word or sentence inputed by the user

words = input("say anything: ")
def evens(word):
    # collect = []
   
    for x in range(0,len(word),2):
    #     if x %  2 ==0:
    #      collect.append(word[x])
        print(word[x])


print(evens(words))



