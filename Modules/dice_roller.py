import random 
number = random.randint(1,6)
print("🎲 you rolled : ",number)
while True :
    
    again = str(input("do you want to roll again ? (y/n) : "))
    
    if again in  ["y", "Y", "yes", "Yes", "YES"] :
        number = random.randint(1,6)
        print("🎲 you rolled : ",number)
    elif again in ["n", "N", "no", "No", "NO"] :
        print("goodbye")
        break
    else :
        print("please enter just y or n ! ")
        continue
