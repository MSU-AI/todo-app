from todo import AIIntegratedTODO
from csvclass import CSVReadWrite

# Create a new instance of the AIIntegratedTODO class
todo = AIIntegratedTODO()
csvclass = CSVReadWrite()

# Prompt the user to add tasks and perform other actions
while True:
    # Prompt user to enter action
    action = input("What would you like to do? (add, begin, end, pause, resume, predict, csv, exit) ")
    
    # Perform action based on user input
    if action == "add":
        # Prompt user to enter task name and due date
        task_name = input("Enter task name: ")
        due_date = input(f"Enter due date ({'YYYY-MM-DD'}): ")
        
        # Add task to tasks dictionary
        todo.add_task(task_name, due_date)
        
        # Prompt user to begin task
        begin_task = input(f"Would you like to begin the task '{task_name}' now? (y/n) ")
        
        if begin_task.lower() == "y":
            # Begin task
            todo.begin_task(task_name)
        else:
            # Print message indicating task has been added but not started
            print(f"Task '{task_name}' has been added but not started.")
    
    elif action == "begin":
        # Prompt user to enter task name
        task_name = input("Enter task name: ")
        
        # Begin task
        todo.begin_task(task_name)
    
    elif action == "end":
        # Prompt user to enter task name
        task_name = input("Enter task name: ")
        
        # End task
        todo.end_task(task_name)
    
    elif action == "pause":
        # Prompt user to enter task name
        task_name = input("Enter task name: ")
        
        # Pause task
        todo.pause_task(task_name)
    
    elif action == "resume":
        # Prompt user to enter task name
        task_name = input("Enter task name: ")
        
        # Resume task
        todo.resume_task(task_name)
    
    elif action == "predict":
        # Prompt user to enter task name
        task_name = input("Enter task name: ")

        # Predict task
        todo.predict_task(task_name)

    # elif action == "suggest":
    #     # Suggest tasks
    #     todo.suggest_tasks()
    
    elif action == "exit":
        # TODO: Save existing tasks into CSV before exiting
        # Exit the program
        break
    
    elif action == "csv":
        file = ""
        while file[-4:] != ".csv":
            file = input("What file would you like to use? ")
        rw = input("Would you like to read or write the CSV file? (w for write, r for read.) ")
        if rw == "w":
            append_write = input("True for append, False for write ")
            csvclass.write_csv(todo.tasks, append_write)
        elif rw == "r":
            print(csvclass.read_csv())

    else:
        # Print message indicating invalid action
        print("Invalid action. Please try again.")