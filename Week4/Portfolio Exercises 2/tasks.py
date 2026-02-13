import datetime

class Task:
    def __init__(self, title:str, date_due: datetime.date = datetime.datetime.now())-> None :
        self.title = title
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.completed = False
    def mark_completed(self)-> None :
        self.completed = True
        print(f"Task '{self.title}' marked as completed.")
    def change_title(self, new_title:str)-> None :
        self.title = new_title
        print(f"Task title changed to '{self.title}'.")
    def change_due_date(self, new_date:datetime.date)-> None :
        self.date_due = new_date
        print(f"Task due date changed to '{self.date_due}'.")
    def __str__(self)-> str :
        if self.completed:
            return f"Task: {self.title} (Completed)"
        else:
            return f"Task: {self.title} Created {self.date_created} Due:{self.date_due}"