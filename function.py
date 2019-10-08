# def test():
#     print("hello")


# def test(a,b):
    
#     print(a,b)

# test("hello","world")

# def myfunc(myname):
#     print("hello %s " %myname)
# myfunc("Aliyu")

# def myfunc1(myname, Surname):
#     print("hello %s %s" %(myname, Surname))
# myfunc1("Lukman","Aliyu")

#VARIABLE SCOPE

# def test(a):
#     return a
# b = test(3)
# print(b)

# a = int(input("enter value of a: "))
# def come(a):
#     if (a<10):
#         return a
#     elif (a>10):
#         print("good")
# come(a)

def test():
    print("am i a yahoo boy?")
    return

    print("this is google")
test()

def test1(*a):                          #function for list
    print("the list is: ", a)
    return
test1(1,2,3,4,"we")                     #call the list function

def test2(**a):                         #function for maps/dict
    print("the list is: ", a)
    return
test2(f=1,s=2,t=3)                      #call map function