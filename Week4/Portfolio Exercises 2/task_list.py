# Python Classes
# Exercise 1: Creating Classes and Initializing Objects

from tasks import Task
import datetime

# Class to manage a list of tasks
class TaskList:
    def __init__(self, owner: str):
        self.owner = owner
        self.tasks: list[Task] = []

    # Method to add a task to the list
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    # Method to remove a task by index
    def remove_task(self, ix: int) -> None:
        del self.tasks[ix]

    # Method to display all tasks
    def view_tasks(self) -> None:
        print(f"Task list for {self.owner}:")
        for ix, task in enumerate(self.tasks):
            print(f"{ix}: {task}")

    # Method to view overdue tasks - checking what I’ve missed!
    def view_overdue_tasks(self) -> None:
        current_date = datetime.datetime.now()
        overdue_tasks = [task for task in self.tasks if task.date_due < current_date and not task.completed]
        if overdue_tasks:
            print(f"Overdue tasks for {self.owner}:")
            for ix, task in enumerate(overdue_tasks):
                print(f"{ix}: {task}")
        else:
            print(f"No overdue tasks for {self.owner}.")