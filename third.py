# name = "Sophie"
# gender = "female"
# age = 40.5
# print("i am %s and i am %s and am %f years old" %(name,gender,age))

# month = "Jan\n Feb\n March"
# print(month)

# month = "Jan\t Feb\t March"
# print(month)
# a = ["string","int",1,2,10.24]
# print (a[2])

# b = a[:]

# a[1] = "glo"
# print(a[1], a[4])
# print(b)
favour = [1,2,3,4,5,6,7,8,9,10]
Kim = favour[0:7]
cyril = favour[0:3]
Ray = favour[1:6]
Daniel = favour[3:9]
print("the full list is" , favour)
print("kim list is " , Kim)
print("cyril list is ", cyril)
print("Ray list is ", Ray)
print("Dan's list is ", Daniel)
Nuru = favour[2:4]
kings = favour[0:]
print(Nuru)
print(kings)
print(favour[-1])

favour.pop()
print(favour)

favour.append("4")
print(favour)

del favour[1]
print(favour)