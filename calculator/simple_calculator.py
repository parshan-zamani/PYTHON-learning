def add(a,b):
    return a+b 

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b == 0 :
        return None 
    return a/b 

while True :

    print("<<<<<<< Python Calculator >>>>>>>")

    print("1.add")
    print("2.substract")
    print("3.multiply")
    print("4.divide")
    print("5.Exit")
    choose = int(input("please enter the number of the operator(1 to 5) : "))
    
    if choose == 5 :
        print("Goodbye!")
        break
    if choose not in [1,2,3,4] :
        print("please enter a number in range(1-5)")
        continue
    num1 = float(input("please enter the first number : "))
    num2 = float(input("please enter the second number : "))

    if choose == 1 :
        print("Result :",add(num1,num2))
    elif choose == 2 :
        print("Result :",substract(num1,num2))
    elif choose == 3 :
         print("Result :",multiply(num1,num2))
    elif choose == 4 :
         print("Result :",divide(num1,num2))
    
    




    
