speed = int(input("What is the speed of the vehicle in mph? :" ))
time = int(input("How many hours has it traveled? :"))


for hour in range(1,time+1):
    distace=speed*hour
    print("Hour: " + str(hour)+ "  distace: " + str(distace))

