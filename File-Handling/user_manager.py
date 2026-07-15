print("========== USER MANAGER ==========\n1. Add User\n2. Show Users\n3. Search User\n4. Exit")
while True :
    while True :
        try :
            choose = int(input("Choose an option : "))
            if choose not in [1,2,3,4] :
               print("enter an integer number between 1 to 4 !")
               continue
            break
        except ValueError :
            print("please enter an integer number between 1 to 4 !")
            continue
    
    if choose == 1 :
       name = input("Name : ")
       while True :
           try :
               age = int(input("Age : "))
               break
           except ValueError :
               print("you should enter an integer number as age : ")
               continue
       country = input("Country : ")
       file = open("file handling/users.txt","a")
       file.write(f"\n Name : {name} | Age : {age} | Country : {country}")
       print("✅ User added successfully!")
       file.close()
    elif choose == 2 :
         file = open("file handling/users.txt","r")
         text = file.read()
         print("========== USERS ==========")
         print(text)
         file.close()
    elif choose == 3 : 
        search = input("Enter the name you are looking for : ")
        file = open("file handling/users.txt","r")
        lines = file.readlines()
        found = False 
        for line in lines :
            if search in line :
                print("User found ! ", line)
                found = True
                break
        if not found :
            print("User not found !")
    elif choose == 4 :
        print("Goodbye")
        break
                
                
        





    
    
