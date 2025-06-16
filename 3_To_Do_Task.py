def task():
    tasks = []
    print("_____WELCOME TO PYTHON TO_DO LIST APP_____")
    total_task= int(input("Enter how many task you want to enter:  "))
    for i in range(1, total_task+1):
        add_task = input(f"Enter your task {i}:  ")
        tasks.append(add_task)

    while True:
        operation = int(input("1-Add task\n2-update task\n3-Delete\n4-View\n5-Exit\n"))
        
        if operation == 1:
            add_task1 = input("Enter your task: ")
            tasks.append(add_task1)
            print(f"You task {add_task1} is successfully added: ")
            
        elif operation == 2:
            add_task2 = input(f"Enter your task that you want to update: \n {tasks}\n")
            if add_task2 in tasks:
                add_task3 = input("Enter your Task: ")
                index1 = tasks.index(add_task2)
                tasks[index1] = add_task3
                print(f"Your task is successfully added!")
                
            else:
                print("This is not in task.")
                
        elif operation == 3:
            add_task4 = input("Enter your task, you want to delete.  ")
            if add_task4 in tasks:
                index2 = tasks.index(add_task4)
                del tasks[index2]
                print(f"We deleted you task {add_task4}")
            else:
                print("This is not in task! ")
                
        elif operation == 4:
            print(f"THESE ARE ALL TASKS\n {tasks}")
            
        elif operation == 5:
            print("Thanks for using this app! ")
            break
        
        else: 
            print("This is invalid:  ")
            
            
task()
            
            
        
        