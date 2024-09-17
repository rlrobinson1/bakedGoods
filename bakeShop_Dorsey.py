import sys

#calculate total balance
def calTotal (spent, sum):
    #sum is the money the user entered
    #spent is deducted from sum
    print("********************************************************************")
    print("\nMoney available: ", sum)
    print("Money spent: ",spent)
    boxing = 10.00
    total = (spent + boxing) 
    total += (total * 0.07)
    print("Total purchase: ", total)
    #print
    if total > sum:
        print("Insufficient Funds! You do not have enough to complete this purchase!!")
        print("Money available:  ",sum)
        sys.exit()
    sum -= total
    print("You have {} remaining.".format(sum), "\n")
    print("********************************************************************")
    
    

#driver code

print("********************")
print("Tastie Treat Bake Shop")
print("********************")

print("Hi!  Welcome to Tastie Treat Bake Shop!\n")
spend = float(input("Please enter the amount you intend to spend:  "))
balance = 0 
print("Please be advised there will be a $10 charge added to each balance in addition to 7% sales tax.")
print("\nPlease select from the following category:  ")
while True:
    balance < spend
    menu = "1 - Layer Cakes\n2 - Pound Cakes\n3 - Cheesecakes\n4 - Cupcakes\n5 - Other Treats\n6 - Nothing"
    print(menu)
    choice = int(input("Please select an item from the above menu:  "))

    if choice == 1:
        print("You have chosen layered cakes.")
        submenu1 = "1 - Strawberry Crunch: $75\n2 - Coconut Cream: $55\n3 - Lemon Custard: $65"
        print(submenu1)
        choice2 = int(input("Please select a type of cake:  "))
        if choice2 == 1:
            lc = 75
            print("Your cake costs: ",lc)
            balance += lc
            print("Your balance is: ",balance)
            #calTotal(balance, spend)
            
        elif choice2 == 2:
            lc = 55
            print("Your cake costs: ",lc)
            balance += lc
            print("Your balance is: ",balance)
            #calTotal(balance, spend)
        elif choice2 == 3:
            lc = 65
            print("Your cake costs: ",lc)
            balance += lc
            print("Your balance is: ",balance)
            #calTotal(balance, spend)
        else:
            print("You have chosen an invalid response.  Please try again!")
            
    
    elif choice == 2:
        print("You have chosen pound cakes.")
        submenu2 = "1 - Cream Cheese - $55\n2 - Pineapple - $60\n3 - 7UP - $55"
        print(submenu2)
        choice3 = int(input("Please select the type of cake:  "))
        if choice3 == 1:
            pc = 55
            print("Your cake costs: ",pc)
            balance += pc
            print("Your balance is: ",balance)
            #calTotal(balance, spend)
        elif choice3 == 2:
            pc = 60
            print("Your cake costs: ",pc)
            balance += pc
            print("Your balance is: ",balance)
            #calTotal(balance, spend)
        elif choice3 == 3:
            pc = 55
            print("Your cake costs: ",pc)
            balance += pc
            print("Your balance is: ",balance)
            #calTotal(balance, spend)
        else:
            print("You have chosen an invalid response.  Please try again!")
        
    elif choice == 3:
        print("You have chosen cheesecakes.")
        submenu3 = "1 - Banana Pudding: $55\n2 - Plain with fruit topping: $45\n3 - Vanilla Bean: $50"
        print(submenu3)
        choice4 = int(input("Please select the type of cake:  "))
        if choice4 == 1:
            cc = 55
            print("Your cake costs: ",cc)
            balance += cc
            print("Your balance is: ",balance)
            
        elif choice4 == 2:
            cc = 45
            print("Your cake costs: ",cc)
            balance += cc
            print("Your balance is: ",balance)
            
        elif choice4 == 3:
            cc = 50
            print("Your cake costs: ",cc)
            balance += cc
            print("Your balance is: ",balance)
            
        else:
            print("You have chosen an invalid response.  Please try again!")
        
    elif choice == 4:
        print("You have chosen cupcakes.")
        submenu4 = "1 - Dozen Twix: $45\n2 - Dozen Tutti Celebration: $25\n3 - Dozen Peach Cobbler: $45"
        print(submenu4)
        choice5 = int(input("Please select the type of cupcake:  "))
        if choice5 == 1:
            cup = 45
            print("Your cake costs: ",cup)
            balance += cup
            print("Your balance is: ",balance)
            
        elif choice5 == 2:
            cup = 25
            print("Your cake costs: ",cup)
            balance += cup
            print("Your balance is: ",balance)
            
        elif choice5 == 3:
            cup = 45
            print("Your cake costs: ",cup)
            balance += cup
            print("Your balance is: ",balance)
            
        else:
            print("You have chosen an invalid response.  Please try again!")
    elif choice == 5:
        print("You have chosen the Sweet Tooth option.")
        submenu5 = "1 - Dozen Chocolate Covered Strawberries: $40\n2 - Dozen Salted Caramel Turtles: $25\n3 - Half-pound Almond Chocolate Bark: $15"
        print(submenu5)
        choice6 = int(input("Please select your chocolate option:  "))
        if choice6 == 1:
            st = 40
            print("Your cake costs: ",st)
            balance += st
            print("Your balance is: ",balance)
            
        elif choice6 == 2:
            st = 25
            print("Your cake costs: ",st)
            balance += st
            print("Your balance is: ",balance)
            #calTotal(balance, spend)
        elif choice6 == 3:
            st = 15
            print("Your cake costs: ",st)
            balance += st
            print("Your balance is: ",balance)
            
        else:
            print("You have chosen an invalid response.  Please try again!")
    else:
        print("You have selected an invalid response!  Please try again.")
    if  choice == 6:
        print("You have chosen not to purchase anything.")  
        calTotal(balance, spend)
        break 