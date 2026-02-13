# task_manager_controller.py - Markdown Conversion

```python
# controllers/task_manager_controller.py
from datetime import datetime, timedelta
from typing import List, Optional, Tuple

from task_list import TaskList
from tasks import Task, RecurringTask, TaskFactory
from users import Owner
from dao import TaskCsvDAO # We'll use CSV DAO by default for actual persistence

class TaskManagerController:
    """
    Manages the business logic of the ToDo application.
    It interacts with TaskList, TaskFactory, and DAOs,
    but does not handle direct user input/output.
    """
    def __init__(self, owner_name: str, owner_email: str, storage_path: str = "tasks.csv"):
        self.owner = Owner(name=owner_name, email=owner_email)
        self.task_list = TaskList(owner=self.owner)
        self.dao = TaskCsvDAO(storage_path) # Default to CSV DAO

    def get_owner_info(self) -> str:
        """Returns the string representation of the owner."""
        return str(self.owner)

    def load_tasks(self) -> str:
        """Loads tasks from the DAO and updates the task list."""
        loaded_tasks = self.dao.get_all_tasks()
        self.task_list.tasks = [] # Clear existing tasks
        for task in loaded_tasks:
            self.task_list.add_task(task)
        return f"Loaded {len(loaded_tasks)} tasks."

    def save_tasks(self) -> str:
        """Saves current tasks to the DAO."""
        self.dao.save_all_tasks(self.task_list.tasks)
        return f"Saved {len(self.task_list.tasks)} tasks."

    def add_new_task(self, title: str, date_due_str: str, description: str, task_type: str, interval_days_str: Optional[str] = None) -> str:
        """
        Adds a new task (normal or recurring) to the list.
        Handles date and interval parsing.
        """
        try:
            date_due = None
            if date_due_str:
                date_due = datetime.strptime(date_due_str, "%Y-%m-%d")

            if task_type == "recurring":
                if interval_days_str:
                    interval = timedelta(days=int(interval_days_str))
                    new_task = TaskFactory.create_task(title, date_due, description=description, interval=interval)
                    self.task_list.add_task(new_task)
                    return "Recurring task added."
                else:
                    return "Invalid interval for recurring task. Task not added."
            elif task_type == "normal":
                new_task = TaskFactory.create_task(title, date_due, description=description)
                self.task_list.add_task(new_task)
                return "Normal task added."
            else:
                return "Invalid task type. Please choose 'recurring' or 'normal'."
        except ValueError as e:
            return f"Error adding task: {e}. Please use YYYY-MM-DD for date and valid numbers for interval."
        except Exception as e:
            return f"An unexpected error occurred while adding task: {e}"


    def get_all_tasks_display(self) -> str:
        """Returns a string representation of all tasks."""
        return self.task_list.view_tasks()

    def mark_task_completed(self, task_number: int) -> str:
        """Marks a task as completed."""
        try:
            if self.task_list.check_task_index(task_number - 1):
                task = self.task_list.get_task(task_number - 1)
                task.mark_completed()
                return "Task marked as completed."
            else:
                return "Invalid task number."
        except Exception as e:
            return f"An error occurred: {e}"

    def remove_task_by_number(self, task_number: int) -> str:
        """Removes a task by its 1-based number."""
        return self.task_list.remove_task(task_number)

    def get_overdue_tasks_display(self) -> str:
        """Returns a string representation of overdue tasks."""
        return self.task_list.view_overdue_tasks()

    def update_task_details(self, task_number: int, new_title: Optional[str], new_date_str: Optional[str], new_description: Optional[str]) -> str:
        """Updates the title, due date, or description of a task."""
        try:
            if not self.task_list.check_task_index(task_number - 1):
                return "Invalid task number."

            task = self.task_list.get_task(task_number - 1)
            original_task_str = str(task) # Capture before changes

            if new_title is not None and new_title != "":
                task.change_title(new_title)

            if new_date_str is not None and new_date_str != "":
                try:
                    new_date_obj = datetime.strptime(new_date_str, "%Y-%m-%d")
                    task.change_date_due(new_date_obj)
                except ValueError:
                    return "Invalid date format for due date. Task not updated."

            if new_description is not None: # Empty string means clear description
                task.change_description(new_description)

            return f"Task updated. Original: '{original_task_str}', New: '{task}'"
        except Exception as e:
            return f"An error occurred during task update: {e}"

```