def to_do_list():
    tasks=[ ]
    
    while True:
        print("\n=======Task Management System=======\n")
        print(" 1. Add task")
        print(" 2. Remove task")
        print(" 3. Show tasks")
        print(" 4. Quit")
        choice= input("Enter your choice : ")
       #For Adding task
         if choice == "1":
            task=input("Enter your task : ")
            tasks.append(task)
       #For Removing task
         elif choice == "2":
            task=input("Enter your task to remove : ")
            if task in tasks:
                tasks.remove(task)
                print("task removed successfully")
            else:
                print("task not found")
       #For Showing task
         elif choice=="3":
            print("Tasks : ")
            for task in tasks:
                print(" - " + task)
       #For Quiting 
         elif choice=="4":
            print("Exited!!")
            break
        else:
            print("Invalid!! Enter your choice")
to_do_list()