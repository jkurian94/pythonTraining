total=0

for day in range (7):
    nbugs=int(float(input(" How many bugs did you collected today ? : ")))
    print("you have collected for today "+ str(nbugs))
    total = total + nbugs

print("The total bugs collected during the week is " +str(total))
