#Write a program that runs a loop from 1 to 100
    # a) display tic if a number is divisiable by 5
    # b) display tac if a number is divisiable by 3
    # c) display tictac if a number is divisiable by 3 and 5

for x in range(100):
    if (x%5==0) and (x%3==0):
        print("tictac")
    elif (x%5==0):       
        print('Tic')
    elif (x%3==0):       
        print('tac')
    
