# def sum(a,b):
#     c=3
#     d=4
#     print(c+d)
# sumlist("e","f")

# print(len ("geek"))
# print(len([1,2,3,7,9,1,0]))
# username = input("enter the username ") 

# if len (username) > 10:
#     print("incorrect!")

# def add(x,y,z=0):
#     return (x+y+z)


# print(add(2,3))
# print(add(2,3,4))

# class Employee:
#     def __init__(self):
#         print("employee created")

#     # def __del__(self):
#     #     print("destroyer called ")
    
#     def come(self):
#         print("yes")

#     def come(self,a):
#         print("i know")

#     def come(self,b,c):
#         print("she doesnt know o")

#     def come(self,d,e,f):
#         print("how come?")

# # a = Employee
# # del a
# # a.come
# bet = Employee()
# bet.come(1,2,3)
# bet.come(7)
# bet.come(5,0)
# bet.come()

#EXAMPLE

class Computer():

    def __init__(self,computer,ram,ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

class Laptop(Computer):

    def __init__(self,computer,ram,ssd,model):
        super(Laptop,self).__init__(computer,ram,ssd)
        self.model = model


lenovo = Computer ("lenovo", 2, 512)

print("this computer is ", lenovo.computer)
print("this computer has ram of ", lenovo.ram)
print("this computer has ssd of ", lenovo.ssd)
# print("the model of the computer is ", lenovo.model)

# Hp = Laptop ("HP", 4, 1024, "HP 650")

# print("this computer brand is ", Hp.computer)
# print("it's RAM is ", Hp.ram)
# print("the HDD is ", Hp.ssd)
# print("the model of this computer is ", Hp.model)

