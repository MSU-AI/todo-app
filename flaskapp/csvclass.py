import datetime
import csv
# from main import Task

class Task:
    # Task class to store information about a task
    def __init__(self, name = None, due_date : str = None, start_time = None, end_time = None):
        self.name = name                    # name of task
        self.due_date = due_date            # due date of task
        self.start_time = start_time        # start time of task
        self.end_time = end_time            # end time of task
    def __eq__(self, __value: object) -> bool:
        if type(self) != type(__value):
            return False        # where __value is not Task
        return (self.name == __value.name and self.due_date == __value.due_date and 
            self.start_time == __value.start_time and self.end_time == __value.end_time)

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

# import statement above commented, because there is no __name__ == '__main__'
# Temporarily, I'll just paste the Task class definition, and use that
# Use the import statement once we have a stable file with the class Task.

class CSVReadWrite:
    def __init__(self, file = '/Users/harshm04/Downloads/test.csv'):
        # file is temporary default arg that only works on Saatvik's system
        # Change to whatever works for you
        self.file = file
    
    def change_file(self, file):
        self.file = file

    def _tasktolist(self, task : Task) -> list:
        '''
        Returns list representation of input task that can be appended to csv data file.
        '''
        attributes = []
        attributes.append(task.name)
        attributes.append(task.due_date)
        
        start_str = task.start_time                 # start_str is datetime.datetime, or None
        if start_str is not None:                   # If datetime.datetime
            start_str = str(task.start_time)[2:]    # Convert to csv-friendly string, e.g. 2024 -> 24
        attributes.append(start_str)
        
        end_str = task.end_time                     # start_str is datetime.datetime, or None
        if end_str is not None:                     # If datetime.datetime
            end_str = str(task.end_time)[2:]        # Convert to csv-friendly string, e.g. 2024 -> 24
        attributes.append(end_str)
        
        return attributes                           # [name, due_date, start_time, end_time]

    def write_csv(self, tasks : list[Task], append=True):
        '''
        From list of tasks, writes each to CSV specified by self.file.
        :tasks: List of Task objects to be converted, and written.
        :append: a boolean determining if we are appending or overriding file.
        '''
        
        mode = 'w'                  # This mode erases contents of self.file, and starts writing
        if append:
            mode = 'a'              # This mode appends ot end of contents of self.file (does not erase)

        with open(self.file, mode=mode) as file:
            # Set up writer
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            if not append:          # If re-writing, write csv file header
                writer.writerow(['Name', 'Due Date', 'Start Time', 'End Time'])

            for task in tasks:      # Write tasks to CSV row by row (task by task)
                data = self._tasktolist(task)
                writer.writerow(data)
     
    def _listtotask(self, data : list) -> Task:
        '''
        Constructs Task from singular csv list
        '''
        if data[2] != 'None':
            # If the start_time is not None, then convert back to datetime.datetime
            data[2] = datetime.datetime.strptime(data[2], '%y-%m-%d %H:%M:%S.%f')
        else:
            # Else, it is None
            data[2] = None

        if data[3] != 'None':
            # If the end_time is not None, then convert back to datetime.datetime
            data[3] = datetime.datetime.strptime(data[3], '%y-%m-%d %H:%M:%S.%f')
        else:
            # Else, it is None
            data[3] = None
        return Task(*data)

    def read_csv(self) -> list[Task]:
        '''
        Reads csv file of data, and creates a task for each row.
        Returns list of tasks in CSV file self.file.
        '''        
        tasks = []

        with open(self.file) as csv_file:
            # Initialize reader
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader) # Skip header
            
            for row in csv_reader:
                tasks.append(self._listtotask(row))
        
        return tasks    