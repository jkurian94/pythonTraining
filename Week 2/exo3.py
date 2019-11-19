#declare all funtions first
def sum(tax,interest,amount):
    total= amount*tax + amount
    total= total*interest + total
    return total

def Hello():
    print("Hello everyone")

if __name__== "__main__":
    Hello()
    a=float(input ("give bowrroe"))
    b=0.2
    c=float(input("give interest"))

    d=sum(b,c,a)
    print ("total to pay: " + str(d))