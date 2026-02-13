import datetime

# Class to represent a single task
class Task:
    # Constructor to initialise task details - adding description as an option!
    def __init__(self, title: str, date_due: datetime.datetime, description: str = ""):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due
        self.description = description

    # Method to change the task title
    def change_title(self, new_title: str) -> None:
          self.title = new_title

    # Method to change the due date
    def change_date_due(self, date_due: datetime.datetime) -> None:
        self.date_due = date_due

    # Method to mark the task as completed
    def mark_completed(self) -> None:
        self.completed = True

    # Method to change the task description - handy for more details!
    def change_description(self, new_description: str) -> None:
        self.description = new_description

    # Method to return a string version of the task - including my new description!
    def __str__(self) -> str:
        return f"{self.title} (created: {self.date_created}, due: {self.date_due}, completed: {self.completed}, description: {self.description})"