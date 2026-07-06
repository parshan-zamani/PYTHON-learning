def add(a,b) :
    return a + b

def subtract(a,b) :
    return a - b 

def multiplication(a,b) :
    return a * b 

def division(a,b) :
    if b == 0 :
        return None
    return a / b 

def get_numbers() :
    a = float(input(" please enter the first number : "))
    b = float(input(" please enter the second number : "))
    return a , b 

def show_operation_list() :
    print("<<<<<<< Python Calculator >>>>>>>")
    print("1.add")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.Exit")
    choice = int(input(" Please enter the number corresponding to the required operator(1 to 5) : "))
    return choice 
while True :
    choice = show_operation_list()
    if choice not in range(1,6) :
        print(" enter a number between 1 to 5  .")
        continue
    if choice == 5 :
        print("Goodbye!") 
        break
    a,b = get_numbers()
    if choice == 1 :
        print("result :" ,add(a,b))
    elif choice == 2 :
        print("result :" ,subtract(a,b))
    elif choice == 3 :
        print("result :" ,multiplication(a,b))
    elif choice == 4 : 
        print("result :" ,division(a,b))



    






