years=int(input("How Many years?: "))

# avg=0
total_rainfall=0
for one_year in range(1,years+1):
    print(" ")
    print ("Year " + str(one_year))
    for twelve_months in range(1,13):
        print(" ")
        rainfall= int(input("How much rain this month?: "))
        total_rainfall+=rainfall
        avg=total_rainfall/12
        print(" ")
        print("Month " + str(twelve_months))
        print("Total rainfall for the year: " + str(total_rainfall) + " Inches")
        print("Avg Rain for the year: " + str(avg) + " Inches")
