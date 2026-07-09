import random 
import time
attempts = 1  
print("Hello, and welcome to the number guessing game. Please note that you must guess only whole numbers between 1 and 100!")
print("📯PAY ATTENTION !!!!📯")
print("You must guess—and only guess—the integer between 1 and 100 that the system has randomly and secretly selected!!")
print("LET'S START !")
print("------------------------------------------------------------------------------------------------------------------------------------------")
print("🤖The system is selecting a number!")
print("please wait ... ")
time.sleep(4)
secret_number = random.randint(1,100)
print("The number has been selected! Start guessing!")
while True :
    try :
        guess = int(input("please enter the desired number : "))
    except ValueError :
        print("please enter a valid number ! ")
        continue
    if guess < 1 or guess > 100  :
        print("Please select an integer between 1 and 100!")
        continue
    elif  guess == secret_number :
        print(f"🎉 Congratulations!You guessed the number in {attempts} Effort(s)")
        break
    elif guess > (secret_number+5) :
        print("Too high !")
    elif secret_number < guess <= (secret_number+5) :
        print("You've gotten too close; come down a bit.")
    elif guess < (secret_number-5) : 
        print("Too low !")
    elif (secret_number-5) <= guess < secret_number :
        print("You've gotten too close; come up a bit.")
    attempts += 1 
    
    

