days=int(input("How many days did you work? :"))
total=0
pay=.01
print("Your pay for Day 1 is : $0.01")
for work in range(2,days+1):
    pay=(pay*2)
    print ("Your pay for Day " + str(work) + " is : $" +str(pay))
    total+=pay
print("Your total pay for "+ str(work) +" days is $" + str(round((total+.01),3)))