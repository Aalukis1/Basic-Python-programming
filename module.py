import this
import time
import sys

#print(time.asctime())                                          #prints the current time of the day

def message():                                                  #function
    print("enter your name")
    name = sys.stdin.readline()                                 #calling library
    print("enter your age")
    age = int(sys.stdin.readline())                             #calling library
    print("thank you %s you are %d years old" %(name,age))
message()                                                       #calling function

