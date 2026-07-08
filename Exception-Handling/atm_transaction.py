print("All amounts are in dollars.")
while True :
    try :
        balance = float(input("How much money do you have ? "))
        break
    except ValueError :
        print("type the amount of your money !")
        continue 
while True :
    try :
        y = float(input("How much money do you want to withdraw ? "))
    except ValueError:
        print("please enter a number ! ")
        continue
    else :
        if y > balance :
           print("Insufficient balance ! ")
           continue
        elif y < 0 :
           print("Amount cannot be negative !")
           continue
        else :
            print("Successful transaction!")
            print("your new balance = ",balance - y)
            print("Thank you for using our ATM.")
            break
    
    
    
       
        


    
    


