# tasks.py
from datetime import datetime, timedelta
from typing import Any # Needed for TaskFactory kwargs

class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime = None, description: str = "") -> None:
        self.title: str = title
        self.date_due: datetime = date_due
        self.date_created: datetime = datetime.now()
        self.description: str = description
        self.completed: bool = False

    def mark_completed(self) -> None:
        """Marks the task as completed."""
        self.completed = True

    def change_title(self, new_title: str) -> None:
        """Changes the title of the task."""
        self.title = new_title

    def change_date_due(self, new_date: datetime) -> None:
        """Changes the due date of the task."""
        self.date_due = new_date

    def change_description(self, new_description: str) -> None:
        """Changes the description of the task."""
        self.description = new_description

    def __str__(self) -> str:
        """Returns a string representation of the task."""
        status: str = "✓" if self.completed else "✗"
        due_date_str = self.date_due.strftime("%Y-%m-%d") if self.date_due else "N/A"
        desc = f" - {self.description}" if self.description else ""
        return f"[{status}] {self.title} (Due: {due_date_str}){desc}"


class RecurringTask(Task):
    """Represents a recurring task in a to-do list."""

    def __init__(self, title: str, date_due: datetime = None, interval: timedelta = None):
        """Creates a new recurring task.

        Args:
            title (str): Title of the task.
            date_due (datetime): Due date of the task.
            interval (timedelta): Interval between each repetition.
        """
        super().__init__(title, date_due)
        self.interval: timedelta = interval
        self.completed_dates: list[datetime] = []

    def _compute_next_due_date(self) -> datetime:
        """Computes the next due date of the task."""
        if self.date_due and self.interval:
            return self.date_due + self.interval
        return self.date_due # Or handle error/no interval case

    def mark_completed(self) -> None:
        """Marks the recurring task as completed and updates the due date."""
        self.completed_dates.append(datetime.now())
        if self.interval: # Only update due date if an interval exists
            self.date_due = self._compute_next_due_date()
            self.completed = False # Recurring tasks are not "completed" permanently for next cycle
        else:
            self.completed = True # If no interval, treat like a one-off completion
        print(f"Recurring task marked as completed. Next due date: {self.date_due.strftime('%Y-%m-%d') if self.date_due else 'N/A'}")

    def __str__(self) -> str:
        """Returns a string representation of the recurring task."""
        completed_str = ';'.join(date.strftime('%Y-%m-%d %H:%M:%S.%f') for date in self.completed_dates)
        due_date_str = self.date_due.strftime("%Y-%m-%d") if self.date_due else "N/A"
        interval_str = f"{self.interval.days} days" if self.interval else "N/A"
        status: str = "✓" if self.completed else "✗"
        return (
            f"[{status}] {self.title} (Type: Recurring, Due: {due_date_str}, "
            f"Interval: {interval_str}, Completed on: [{completed_str}])"
        )

class TaskFactory:
    """A factory for creating Task and RecurringTask objects."""

    @staticmethod
    def create_task(title: str, date_due: datetime = None, description: str = "", **kwargs: Any) -> Task:
        
        if "interval" in kwargs and isinstance(kwargs["interval"], timedelta):
            # For RecurringTask, description is not directly in init, but can be set later if needed
            recurring_task = RecurringTask(title, date_due, kwargs["interval"])
            recurring_task.change_description(description) # Set description for RecurringTask too
            return recurring_task
        else:
            return Task(title, date_due, description)
