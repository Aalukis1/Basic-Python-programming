score = eval(input("please, input your JAMB score: "))
if(score >=180 and score<250):
    print("admitted into Geograohy")
elif(score>=250 and score<350):
    print("admitted into Pharmacy")
elif(score>=350 and score<400):
    print("admitted into Medicine")
elif(score==400):
    print("admitted into Computer Science")
elif(score>400):
    print("WARNING! YOU ARE A SCAMMER")
else:
    print("SORRY!, try again next year")

# fruit = "orange"
# if (fruit == "orange"):
#     print ("hay")
# else:
#     print("ney")