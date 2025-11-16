def to_do_list():
    tasks=[ ]
    
    while True:
        print("\n=======Task Management System=======\n")
        print(" 1. Add task")
        print(" 2. Remove task")
        print(" 3. Show tasks")
        print(" 4. Quit")
        choice= input("Enter your choice : ")
       
        if choice == "1":#For Adding task
            task=input("Enter your task : ")
            tasks.append(task)
     
        elif choice == "2":  #For Removing task
            task=input("Enter your task to remove : ")
            if task in tasks:
                tasks.remove(task)
                print("task removed successfully")
            else:
                print("task not found")
      
        elif choice=="3": #For Showing task
            print("Tasks : ")
            for task in tasks:
                print(" - " + task)
      
        elif choice=="4": #For Quiting 
            print("Exited!!")
            break
        else:
            print("Invalid!! Enter your choice")
to_do_list()