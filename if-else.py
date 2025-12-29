x = 110
if (x == 10):
    print("x is 10")
elif (x > 100):
    print ("x is too big")
else:
    print("x is not 10")

#Inherited if/else statement
x = 210
if (x == 10):
    print("x is 10")
elif (x > 100):
    if ((x > 100) & (x < 200)):
        print ("Between 100 and 200") #nested if statement
    else:
        print ("Greater than 200")
else:
    print("x is not 10")
