import math
print("Welcome to the Internt Banking Apllication. ")
print("This is not a real banking app but a Demo Banking app.")
print("Everything is developed uing Python code feel free to play around.")
def signin():
    global name # username
    global pin #Password
    global cb # current balance
    name =str(input("Please create your username: "))
    pin = str("Please create your 6 digits pin: ")
    if len(pin) ==6:
        pin = pin
    else:
        print("The pin has to be 6 digit: ")
        newpin = str(input("Please Create your 6 digits pin: "))
        if len(newpin) !=6:
           print("The pin has to be in 6 digits: ")
           signin()
        else:
            pin = newpin 
            
    print("Thanks for creating your bank account")
    
def forgotpin():
    recoverpin = str(input("please create your new 6 digits pin: "))
    if len(recoverpin) != 6:
        print("The pin has to be in 6 digits")
        forgotpin()
    else:
        print("The new has been stored, please log in")
        pin = recoverpin
    
def depositinterest(p,r,t):
    # A = Pe^(rt) which is the formula for calculating the compound interest
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r*t
    e = math.exp(rt)
    # Calculation
    a = p * e # Future value of your investment
    return a

def  login():
    #make1 represent username
    #pin1 represent user's pin
    name1 = str(input("Please enter your username: "))
    pin1 = str(input("Please enter your pin: "))
    #Check if the name and pin matched
    if name1 == name and pin1 == pin:
        print("Welcome to the Online banking application" + " " + name)
        print("Please choose the Menu down here")
        listmenu = ["1-Deposit", "2-Withdraw", "3-Transfer", "4-Check Balance", "5-Deposit Interest Rate", "6-Calculate compound interest"]
        for b in listmenu:
            print(b)
        choose = int(input("Please enter the number of your choice: "))
        d = 0 # d representation deposit
        w = 0 # w represent withdraw
        cb = 0 #cb represent current balance
        if choose ==1:
            d =int(input("Enter the amount of your deposit: "))
            cb = cb + d
            print("Your curent balance is" +" "+ str(cb))
        elif choose == 2:
            w = int(input("Enter the amount of money that you want to withdraw: "))
            if w > cb:
                print("Your current balance is not sufficient for this transaction")
                login()
            else:
                cb = d-w
                print(str(w +" "+ "has been withdrawn from your account" +" "+ "and your current balance is" +" "+ str(cb)))
        elif choose ==3:
            dest = str(input("Please enter the account number of your destination: "))
            if len(dest) ==8:
                amount =int(input("Please enter the amount of money that you want to transfer: "))
                if amount > cb:
                    print("Your current balance is not sufficient for this transaction")
                    login()
                else: 
                    cb = d-amount
                    print("The trabsaction of" +" "+ str(amount) +" "+ "has been transferred to" +" "+ str(dest) +" "+ "your current balance is" +str(cb))
            else:
                print("The transaction has been rejected since the transaction account is invalid")
                login()
                
        elif choose == 4:
            print("Your current balance is" +" "+ str(cb))
        elif choose == 5:
            if d > 5000:
                rate = 3
            elif d >30000:
                rate =2
            else:
                rate = 1.5
            print("Your current deposit interest rate is" +" "+ str(rate) +"%")
        elif choose == 6:
            listoption = ["1-calculate your deposit compound interest base on your current balance", "calculate your deposit compound interest base on your input"]
            for n in listoption:
                print(n)
            choose = int(input("Please enter your choice from the options above: "))
            if choose  ==1:
                timing = str(input("How many years you want to invest your moneny: "))
                if d > 50000:
                    ratex =0.03
                elif d > 30000:
                    ratex = 0.02
                else:
                    ratex = 0.015(
                print("Your current balance in:" +" "+ str(timing) + " "+ "years will be:"))
                print(depositinterest(cb,ratex,timing))
            elif choose == 2:
                timing = str(input("How many years you want to invest your moneny: "))
                money = str(input("Please enter the amount of money to deposit: "))
                money = int(money)
                if money > 50000:
                    ratex = 0.03
                elif money > 30000:
                    ratex = 0.02
                else:
                    ratex = 0.015(
                print("Your current balance in:" +" "+ str(timing) + " "+ "years will be: "))
                print(depositinterest(money,ratex,timing))
            else:
                print("Option is not available, back to main menu")
                login()
        else:
            print("Option is not available, back to main menu")
            login()
                
        
    else:
        print("Either of your username or pin is wrong, did you create your account?")
        list1 = ["1-Yes", "2-No"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice below: "))
        if inp == 1:
            list2 = ["1-do you want to attempt to log in again?", "2-you forgot your pin"]
            for e in list2:
                print(e)
            theanswer = str(input("Please enter your choice: "))
            theanswer = int(theanswer)
            if theanswer == 1:
                login()
            elif theanswer == 2:
                forgotpin()
            else:
                print("Option is not available")
                login()
        elif inp ==2:
            print("Please create your account:")
            signin()
            
        else:
            print("Option is not available")
            login()
    exit()
    
def mainmenu():
    optionone = int(input("Choose 1 to sign in and choose 2 to log in: "))
    if optionone ==1:
        signin()
    elif optionone == 2:
        login()
    else:
        print("option not available")
        mainmenu()
    exit()
        
def exit():
    answer = str(input("Do you still want to conduct transaction? Yes or No: "))
    if answer =="Yes":
        login()
    elif answer =="No":
        print("Thank you for using this app")
    else:
        print("Option is not available")
        mainmenu()
        
mainmenu()       
            
            
        
                            