# task_list.py - Markdown Conversion

```python
from datetime import datetime
from typing import List
from tasks import Task  # Assuming 'tasks.py' contains your Task and RecurringTask classes
from users import Owner # <<< This line imports the Owner class from your 'users' module

class TaskList:
    """Manages a list of tasks."""

    # <<< The 'owner' parameter now expects an 'Owner' object
    def __init__(self, owner: Owner):
        # The 'owner' attribute now stores the Owner object directly
        self.owner: Owner = owner
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """Adds a new task to the list."""
        self.tasks.append(task)

    def view_tasks(self) -> None:
        """Displays the list of tasks."""
        # <<< Access the name and email attributes of the owner object
        print(f"\n--- Task List for {self.owner.name} (Email: {self.owner.email}) ---")
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
            # Printing the title of the removed task is often more informative
            print(f"Removed task: '{removed_task.title}'")
        else:
            print("Invalid task number.")

    def view_overdue_tasks(self) -> None:
        """Displays all overdue tasks."""
        now = datetime.now() # Current time is July 16, 2025, 4:32:54 AM EAT
        overdue_tasks = [task for task in self.tasks if not task.completed and task.date_due < now]

        if not overdue_tasks:
            print("No overdue tasks.")
        else:
            print("Overdue tasks:")
            for i, task in enumerate(overdue_tasks):
                print(f"{i + 1}: {task}")

    def get_task(self, index: int) -> Task:
        """Returns a task at a specific index (0-based)."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        raise IndexError("Invalid task index.")
```