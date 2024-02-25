import random
arr = [[0,-1,1],[1,0,-1],[-1,1,0]]
print("Enter 0 for Stone.\nEnter 1 for paper.\nEnter 2 for ciser.\n")
while True:
    plyr = int(input("Enter your choice : "))
    if(plyr >2):
        print("\nWrong choice!!!\n")
        break
    comp = random.randrange(0, 3)
    if(comp==0):
        print("\nComputer has choosen = STONE\n")
    elif(comp==1):
        print("\nComputer has choosen = PAPER\n")
    elif(comp==2):
        print("\nComputer has choosen = CISER\n")

    if(arr[plyr][comp]==1):
        print("You Won!!!\n")
    elif(arr[plyr][comp]==0):
        print("Match Draw!!!\n")
    elif(arr[plyr][comp]== -1):
        print("You Lost!!!\n")