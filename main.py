import datetime
import json

class Task:
    def __init__(self, name, due_date=None, start_time=None):
        self.name = name
        self.due_date = due_date
        self.start_time = start_time
        self.end_time = None

    def begin(self):
        self.start_time = datetime.datetime.now()

    def done(self):
        self.end_time = datetime.datetime.now()

    def pause(self):
        self.end_time = datetime.datetime.now()

    def resume(self):
        self.start_time = datetime.datetime.now()

    def get_duration(self):
        duration = (self.end_time - self.start_time).total_seconds()  # returns time in seconds
        return str(datetime.timedelta(seconds=duration))

class AIIntegratedTODO:
    def __init__(self):
        self.tasks = {}
        self.average_times = {}

    def add_task(self, task_name, due_date=None):
        while due_date is not None:
            try:
                due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d')
                if due_date_obj < datetime.datetime.now():
                    print("Due date is past due.")
                    return
                break
            except ValueError:
                print("Invalid date format. Please enter a date in the format YYYY-MM-DD.")
                due_date = input(f"Enter due date ({'YYYY-MM-DD'}): ")
        task = Task(task_name, due_date)
        self.tasks[task_name] = task
        print(f"Added task '{task_name}' due on {due_date}.")

    def begin_task(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name].begin()
            print(f"Started task '{task_name}'.")

    def end_task(self, task_name):
        if task_name in self.tasks:
            task = self.tasks[task_name]
            task.done()
            duration = task.get_duration()
            if task_name in self.average_times:
                self.average_times[task_name].append(duration)
            else:
                self.average_times[task_name] = [duration]
            print(f"Finished task '{task_name}' in {duration}.")
            duration_seconds = (task.end_time - task.start_time).total_seconds()
            hours, remainder = divmod(duration_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            print(f"Task duration: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")

    def pause_task(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name].pause()
            print(f"Paused task '{task_name}'.")

    def resume_task(self, task_name):
        if task_name in self.tasks:
            self.tasks[task_name].resume()
            print(f"Resumed task '{task_name}'.")

    def get_average_time(self, task_name):
        if task_name in self.average_times:
            times = self.average_times[task_name]
            return sum(times, datetime.timedelta()) / len(times)

    def suggest_tasks(self):
        # This is where your AI logic will go to suggest tasks based on user's average completion time.
        pass

# Prompt the user to add tasks and perform other actions
todo = AIIntegratedTODO()
while True:
    action = input("What would you like to do? (add, begin, end, pause, resume, suggest, exit) ")
    if action == "add":
        task_name = input("Enter task name: ")
        due_date = input(f"Enter due date ({'YYYY-MM-DD'}): ")
        todo.add_task(task_name, due_date)
        begin_task = input(f"Would you like to begin the task '{task_name}' now? (y/n) ")
        if begin_task.lower() == "y":
            todo.begin_task(task_name)
        else:
            print(f"Task '{task_name}' has been added but not started.")
    elif action == "begin":
        task_name = input("Enter task name: ")
        todo.begin_task(task_name)
    elif action == "end":
        task_name = input("Enter task name: ")
        todo.end_task(task_name)
    elif action == "pause":
        task_name = input("Enter task name: ")
        todo.pause_task(task_name)
    elif action == "resume":
        task_name = input("Enter task name: ")
        todo.resume_task(task_name)
    elif action == "suggest":
        todo.suggest_tasks()
    elif action == "exit":
        break
    else:
        print("Invalid action. Please try again.")