import datetime
# pip install datetime
import numpy as np
# pip install numpy
import pandas as pd
# pip install pandas
import sklearn

"""
READ THESE and install the packages if you don't have them installed already:
I recommend reading the [Machine Learning intro.py] first. It has a lot of useful information. 
I usually use pip to install packages. You can use pip to install packages as well.
datetime: https://docs.python.org/3/library/datetime.html
What is machine learning: https://www.geeksforgeeks.org/machine-learning/
numpy: https://numpy.org/doc/stable/user/absolute_beginners.html
pandas: https://pandas.pydata.org/docs/getting_started/index.html
sklearn: https://scikit-learn.org/stable/user_guide.html
Matplotlib: https://matplotlib.org/stable/tutorials/pyplot.html
"""


class Task:
    # Task class to store information about a task
    def __init__(self, name, due_date=None, start_time=None):
        self.name = name                    # name of task
        self.due_date = due_date            # due date of task
        self.start_time = start_time        # start time of task
        self.end_time = None                # end time of task

    # Begin task
    def begin(self):
        self.start_time = datetime.datetime.now()                       # set start time to current time

    def done(self):
        self.end_time = datetime.datetime.now()                         # set end time to current time

    def pause(self):
        self.end_time = datetime.datetime.now()                         # set end time to current time

    def resume(self):
        self.start_time = datetime.datetime.now()                       # set start time to current time

    def get_duration(self):
        duration = (self.end_time - self.start_time).total_seconds()    # returns time in seconds
        return str(datetime.timedelta(seconds=duration))                # returns time in HH:MM:SS format
                                                                        # HH: hours, MM: minutes, SS: seconds


# TODO class to store tasks and perform actions on tasks
class AIIntegratedTODO:
    def __init__(self):
        # initialize tasks and average_times as empty dictionaries
        self.tasks = {}             # tasks dictionary to store tasks
        self.average_times = {}     # average_times dictionary to store average times for each task

    # Add task to tasks dictionary
    def add_task(self, task_name, due_date=None):
        while due_date is not None:
            # check if date is valid
            try:
                due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d') # convert string to datetime object
                
                if due_date_obj < datetime.datetime.now():                      # check if date is in the past
                    print("Due date is past due.")
                    return
                break
            
            # if date is invalid, prompt user to enter date again
            except ValueError:
                print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
                due_date = input(f"Enter due date ({'YYYY-MM-DD'}): ")
        
        task = Task(task_name, due_date)                                        # create task object
        
        self.tasks[task_name] = task                                            # add task to tasks dictionary
        
        print(f"Added task '{task_name}' due on {due_date}.")

    # Begin task
    def begin_task(self, task_name):
        # check if task exists
        if task_name in self.tasks:
            self.tasks[task_name].begin()
            print(f"Started task '{task_name}'.")
        else:
            print(f"Task '{task_name}' does not exist.")

    # End task
    def end_task(self, task_name):
        # check if task exists
        if task_name in self.tasks:
            task = self.tasks[task_name]                # get task object
            task.done()                                 # set end time to current time
            duration = task.get_duration()              # get duration of task
            
            # add duration to average_times dictionary
            if task_name in self.average_times:
                self.average_times[task_name].append(duration)              # append duration to list of durations
            else:
                self.average_times[task_name] = [duration]                  # create new list of durations
            print(f"Finished task '{task_name}' in {duration}.")
            duration_seconds = (task.end_time - task.start_time).total_seconds()    # Calculate the duration of the task in seconds

            # Divide the total seconds by 3600 (seconds in an hour) to get the number of hours and the remainder
            hours, remainder = divmod(duration_seconds, 3600)

            # Divide the remainder by 60 (seconds in a minute) to get the number of minutes and the remaining seconds
            minutes, seconds = divmod(remainder, 60)

            print(f"Task duration: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}") # Print the duration in HH:MM:SS format

    # Pause task
    def pause_task(self, task_name):
        # check if task exists
        if task_name in self.tasks:
            self.tasks[task_name].pause()               # set end time to current time
            print(f"Paused task '{task_name}'.")
        else:
            print(f"Task '{task_name}' does not exist.")

    # Resume task
    def resume_task(self, task_name):
        # check if task exists
        if task_name in self.tasks:
            self.tasks[task_name].resume()              # set start time to current time
            print(f"Resumed task '{task_name}'.")
        else:
            print(f"Task '{task_name}' does not exist.")

    # Get average time for a task
    def get_average_time(self, task_name):
        # check if task exists
        if task_name in self.average_times:
            times = self.average_times[task_name]                   # get list of durations
            return sum(times, datetime.timedelta()) / len(times)    # return average time

    def suggest_tasks(self):
        """
        The purpose of this function is to suggest tasks to the user based on their schedule and predicted time to complete that task and the due date of the task.
        This is where your AI logic will go to suggest tasks based on user's average completion time.
        I have left this blank for us to discuss and work on together.
        **Supervised vs unsupervised learning: https://www.geeksforgeeks.org/supervised-unsupervised-learning/**
        Linear regression: https://www.geeksforgeeks.org/ml-linear-regression/
        Decision tree: https://www.geeksforgeeks.org/decision-tree-implementation-python/
        Random forest: https://www.geeksforgeeks.org/random-forest-regression-in-python/
        Neural network: https://www.geeksforgeeks.org/introduction-to-neural-networks/
        Hierarchical clustering: https://www.geeksforgeeks.org/ml-hierarchical-clustering-agglomerative-and-divisive-clustering/
        K-means clustering: https://www.geeksforgeeks.org/ml-k-means-algorithm/
        And there are many more ways to do this. We can discuss and decide on the best way to do this.
        """
        pass

# Create a new instance of the AIIntegratedTODO class
todo = AIIntegratedTODO()

# Prompt the user to add tasks and perform other actions
while True:
    # Prompt user to enter action
    action = input("What would you like to do? (add, begin, end, pause, resume, suggest, exit) ")
    
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
    
    elif action == "suggest":
        # Suggest tasks
        todo.suggest_tasks()
    
    elif action == "exit":
        # Exit the program
        break
    
    else:
        # Print message indicating invalid action
        print("Invalid action. Please try again.")