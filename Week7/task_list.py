# task_list.py
from datetime import datetime
from typing import List
from tasks import Task
from users import Owner

class TaskList:
    """Manages a list of tasks."""

    def __init__(self, owner: Owner):
        self.owner: Owner = owner
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a new task to the list."""
        self.tasks.append(task)

    def view_tasks(self) -> str: # Changed return type to str for UI
        """Returns a formatted string of tasks for display."""
        output = f"\n--- Task List for {self.owner.name} (Email: {self.owner.email}) ---\n"
        if not self.tasks:
            output += "No tasks in the list.\n"
        else:
            for i, task in enumerate(self.tasks):
                output += f"{i + 1}: {task}\n"
            output += f"Total tasks: {len(self.tasks)}\n"
        return output

    def remove_task(self, task_number: int) -> str: # Changed return type to str for UI
        """Removes a task by its number (1-based) and returns a status message."""
        if self.check_task_index(task_number - 1): # Use the new check_task_index
            removed_task = self.tasks.pop(task_number - 1)
            return f"Removed task: '{removed_task.title}'"
        else:
            return "Invalid task number."

    def view_overdue_tasks(self) -> str: # Changed return type to str for UI
        """Returns a formatted string of all overdue tasks."""
        now = datetime.now()
        overdue_tasks = [task for task in self.tasks if not task.completed and task.date_due and task.date_due < now]

        output = ""
        if not overdue_tasks:
            output += "No overdue tasks.\n"
        else:
            output += "Overdue tasks:\n"
            for i, task in enumerate(overdue_tasks):
                output += f"{i + 1}: {task}\n"
        return output

    def get_task(self, index: int) -> Task:
        """Returns a task at a specific index (0-based)."""
        if self.check_task_index(index): # Use the new check_task_index
            return self.tasks[index]
        raise IndexError("Invalid task index.")

    def check_task_index(self, ix: int) -> bool: # <<< NEW METHOD
        """
        Checks if a task with the given 0-based index exists.
        Returns a Boolean value.
        """
        return 0 <= ix < len(self.tasks)
