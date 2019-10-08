class Bird():
    def __init__(self):
        print("bird")

    def whatIsThis(self):
        print("this bird that cannot swim")

class Animal(Bird):                                         
    def  __init__(self):
        print("this is bird which can swim")
        super(Bird,self).__init__()
        print("animal")

    def whatIsThis(self,a):
        print("this is animal which  cannot swim")

    def next(self):
        print("this is next")

    def __del__(self):
        print("destroy")
#pass

a = Animal()
a.whatIsThis(3)


a.next()
# a.__del__()