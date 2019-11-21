apple=0
x=0
while (x>=0):
    x=int(input("Give a positive number: "))
    if (x>=0):
        apple=apple+x
    else:
        break
print("That is a negative number!")
print("Here is your sum of the positive numbers: " + str(apple))
