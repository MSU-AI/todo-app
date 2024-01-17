import datetime
import csv
from task import Task

class CSVReadWrite:
    def __init__(self, file = '/Users/harshm04/Downloads/test.csv'):
        # file is temporary default arg that only works on Harsh's system
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
            mode = 'a'              # This mode appends to end of contents of self.file (does not erase)

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