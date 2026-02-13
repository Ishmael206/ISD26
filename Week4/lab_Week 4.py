# ============================
# 1. Python Classes
#===========================
#  -- Exercise 1: Creating Classes and Initializing Objects --

class TaskList1:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner.upper()
        self.tasks = []
my_task_list = TaskList1("Thomas")
print(my_task_list.owner)

someone_else_task_list = TaskList1("Jane")
print(someone_else_task_list.owner)


#  -- Exercise 2: Adding methods to the Tasklist class --

class TaskList2:
    """Manages a list of tasks for a specific user."""
    def __init__(self, owner: str) -> None:
        self.owner: str = owner.upper()
        self.tasks = []

    # Method to add a task to the task list
    def add_task(self, task: str) -> None:
        """
        Adds a new task to the task list.

        Args:
            task (str): The task to add to the list.
        """
        self.tasks.append(task)

    # Method to display task from the task list
    def view_tasks(self) -> None:
        """
        Displays all tasks in the task list.
        Prints each task with its index. 
        """
        for index, task in enumerate(self.tasks):
            print(f"{index}: {task}")

    # Method to remove a task to the task list
    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            # del self.tasks[task_number - 1] # Using del to remove the task
            # or alternatively, you can use pop to remove and return the task
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")



    def list_options(self) -> None:
        """
        Displays the task manager menu and handles user interaction.

        Provides options to add, view, or remove tasks, or to quit the program.
        """
        while True:
            print("To-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Quit")
            choice = input("Enter your choice: ")
            if choice == "1":
                task = input("Enter a task: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                ix = int(input("Enter the index of the task to remove: "))
                self.remove_task(ix)
            elif choice == "4":
                break


#--- Exercise 3: Testing the Functionality ---

# Testing the TaskList functionality
if __name__ == "__main__":
    # Create a TaskList object with Our Group Members
    my_task_list = TaskList2("Our Group Members")

    # Pre-fill some sample tasks to test functionality
    my_task_list.tasks = ["Do Homework", "Do Laundry", "Go Shopping"]

    # Launch the task list manager menu
    my_task_list.list_options()


#---Exercise 4: Composition---
# Represents a single task
class Task:
    def __init__(self, title: str) -> None:
        self.title: str = title                # Task name
        self.completed: bool = False           # Completion status, default is False

    def mark_completed(self) -> None:
        """
        Marks the task as completed.

        Sets the 'completed' attribute to True.
        """
        # Marks the task as completed
        self.completed = True

    def change_title(self, new_title: str) -> None:
        """
        Changes the title of the task.
        Args:
            new_title (str): The new title to assign to the task.
        """
        # Changes the title of the task
        self.title = new_title

    def __str__(self) -> str:
        # Custom string representation of the task
        status: str = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"



from typing import List

class TaskList3:
    def __init__(self, owner: str):
        self.owner: str = owner.upper()
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Adds a new task to the task list.

        Args:
            task (Task): The task to add to the list.
        """
        self.tasks.append(task)

    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}: {task}")
            print("Total tasks:", len(self.tasks), "\n")

    def remove_task(self, task_number: int) -> None:
        """
        Removes a task by its index (1-based).

        Args:
            task_number (int): The 1-based index of the task to remove.
        """
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")

    def list_options(self) -> None:
        while True:
            print("\n--- TO-DO LIST MENU ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark task as completed")
            print("5. Change task title")
            print("6. Quit")
            choice = input("Enter choice (1–6): ")

            if choice == "1":
                title = input("Enter task title: ")
                task = Task(title)
                self.add_task(task)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                try:
                    ix = int(input("Enter index to remove: "))
                    self.remove_task(ix)
                except ValueError:
                    print("Invalid input.")

            elif choice == "4":
                try:
                    ix = int(input("Enter index to mark completed: "))
                    self.tasks[ix].mark_completed()
                except (ValueError, IndexError):
                    print("Invalid index.")

            elif choice == "5":
                try:
                    ix = int(input("Enter index to change title: "))
                    new_title = input("Enter new title: ")
                    self.tasks[ix].change_title(new_title)
                except (ValueError, IndexError):
                    print("Invalid input.")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    my_task_list = TaskList3("Your Name")
    my_task_list.tasks = [
        Task("Do Homework"),
        Task("Do Laundry"),
        Task("Go Shopping")
    ]
    my_task_list.list_options()




 #==============================================
 # --- 2. Python Libraries ---
 #==============================================
 
 # --- Exercise 1: Adding Dates ---


import datetime
# tasks.py

import datetime
from typing import List


class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        self.title: str = title
        self.date_due: datetime.datetime = date_due
        self.completed: bool = False

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def change_title(self, new_title: str) -> None:
        """Changes the title of the task."""
        self.title = new_title

    def change_date_due(self, new_date: datetime.datetime) -> None:
        """Changes the due date of the task."""
        self.date_due = new_date

    def __str__(self) -> str:
        """Returns a string representation of the task."""
        status: str = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Due: {self.date_due.date()})"


class TaskList4:
    """Manages a list of tasks."""

    def __init__(self, owner: str):
        self.owner: str = owner.upper()
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a new task to the list."""
        self.tasks.append(task)

    def view_tasks(self) -> None:
        """Displays the list of tasks."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}: {task}")
            print(f"Total tasks: {len(self.tasks)}\n")

    def remove_task(self, task_number: int) -> None:
        """Removes a task by its number (1-based)."""
        if 1 <= task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")

    def list_options(self) -> None:
        """Displays the menu and handles user interaction."""
        while True:
            print("\n--- TO-DO LIST MANAGER ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark task as completed")
            print("5. Change task title or due date")
            print("6. Quit")

            choice = input("Enter choice (1–6): ")

            if choice == "1":
                title = input("Enter task title: ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                try:
                    date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                    task = Task(title, date_object)
                    self.add_task(task)
                    print("Task added.")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                try:
                    ix = int(input("Enter index to remove: "))
                    self.remove_task(ix)
                except ValueError:
                    print("Invalid input. Please enter a number.")

            elif choice == "4":
                try:
                    ix = int(input("Enter index to mark completed: ")) - 1
                    self.tasks[ix].mark_completed()
                    print("Task marked as completed.")
                except (ValueError, IndexError):
                    print("Invalid index.")

            elif choice == "5":
                try:
                    ix = int(input("Enter the index of the task to change title:  ")) - 1
                    if 0 <= ix < len(self.tasks):
                        new_title = input("Enter new title (or press Enter to keep current): ")
                        if new_title.strip():
                            self.tasks[ix].change_title(new_title)
                        change_date = input("Change due date? (yes/no): ").strip().lower()
                        if change_date == "yes":
                            new_date = input("Enter new due date (YYYY-MM-DD): ")
                            try:
                                new_date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                                self.tasks[ix].change_date_due(new_date_obj)
                            except ValueError:
                                print("Invalid date format.")
                        print("Task updated.")
                    else:
                        print("Invalid index.")
                except ValueError:
                    print("Invalid input.")

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Try again.")


if __name__ == "__main__":
    # Example tasks
    my_task_list = TaskList4("Group")
    my_task_list.tasks = [
        Task("DIY", datetime.datetime(2025, 7, 20)),
        Task("Laundry", datetime.datetime(2025, 7, 16)),
        Task("Shopping", datetime.datetime(2025, 7, 17))
    ]
    my_task_list.list_options()


