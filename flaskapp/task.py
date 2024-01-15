import datetime

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

    def get_duration(self, seconds=False):
        duration = (self.end_time - self.start_time).total_seconds()    # get time in seconds
        if not seconds:
          return str(datetime.timedelta(seconds=duration))              # returns time in HH:MM:SS format
        else:                                                           # HH: hours, MM: minutes, SS: seconds
          return duration                                               # returns time in seconds 