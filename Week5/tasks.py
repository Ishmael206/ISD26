from datetime import datetime, timedelta

class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime, description: str = "") -> None:
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
        desc = f" - {self.description}" if self.description else ""
        return f"[{status}] {self.title} (Due: {self.date_due.date()}){desc}"


class RecurringTask(Task):
    """Represents a recurring task in a to-do list."""

    def __init__(self, title: str, date_due: datetime, interval: timedelta):
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
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        """Marks the recurring task as completed and updates the due date."""
        self.completed_dates.append(datetime.now())
        self.date_due = self._compute_next_due_date()
        print(f"Recurring task marked as completed. Next due date: {self.date_due.date()}")

    def __str__(self) -> str:
        """Returns a string representation of the recurring task."""
        completed_str = ', '.join(date.strftime('%Y-%m-%d') for date in self.completed_dates)
        return (
            f"{self.title} - Recurring (created: {self.date_created.date()}, "
            f"due: {self.date_due.date()}, completed on: [{completed_str}], "
            f"interval: {self.interval.days} days)"
        )
