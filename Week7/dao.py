import datetime
import csv
from tasks import Task, RecurringTask, PriorityTask  # ✅ Added PriorityTask

class TaskTestDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path
        self.sample_tasks = [
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)),
            Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)),
            Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)),
            Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)),
            Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)),
            Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))
        ]
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)
        self.sample_tasks.append(r_task)

    def get_all_tasks(self) -> list[Task]:
        return self.sample_tasks

    def save_all_tasks(self, tasks: list[Task]) -> None:
        print(f"INFO: TaskTestDAO - Pretending to save {len(tasks)} tasks to {self.storage_path}")
        pass


class TaskCsvDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path
        self.fieldnames = [
            "title", "type", "date_due", "completed", "interval",
            "completed_dates", "date_created", "description", "priority"  # ✅ Added priority
        ]

    def get_all_tasks(self) -> list[Task]:
        task_list = []
        try:
            with open(self.storage_path, "r", newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    task_type = row["type"]
                    task_title = row["title"]
                    task_date_due_str = row["date_due"]
                    task_completed_str = row["completed"]
                    task_interval_str = row["interval"]
                    task_date_created_str = row["date_created"]
                    task_completed_dates_str = row["completed_dates"]
                    task_description = row.get("description", "")
                    task_priority_str = row.get("priority", "")

                    # Parse date_due
                    task_date_due = None
                    if task_date_due_str and task_date_due_str.lower() != 'none':
                        for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
                            try:
                                task_date_due = datetime.datetime.strptime(task_date_due_str, fmt)
                                break
                            except ValueError:
                                continue

                    task_completed = task_completed_str.lower() == 'true'

                    # Parse date_created
                    task_date_created = None
                    if task_date_created_str and task_date_created_str.lower() != 'none':
                        for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
                            try:
                                task_date_created = datetime.datetime.strptime(task_date_created_str, fmt)
                                break
                            except ValueError:
                                continue

                    # Parse completed_dates
                    parsed_completed_dates = []
                    if task_completed_dates_str:
                        for date_str in task_completed_dates_str.split(';'):
                            date_str = date_str.strip()
                            for fmt in ("%Y-%m-%d %H:%M:%S.%f", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
                                try:
                                    parsed_completed_dates.append(datetime.datetime.strptime(date_str, fmt))
                                    break
                                except ValueError:
                                    continue

                    # Construct the correct task type
                    task = None
                    if task_type == "RecurringTask":
                        task_interval = None
                        if task_interval_str and task_interval_str.lower() != 'none':
                            try:
                                days_part = task_interval_str.split(' ')[0]
                                task_interval = datetime.timedelta(days=int(days_part))
                            except (ValueError, IndexError):
                                pass
                        task = RecurringTask(task_title, task_date_due, task_interval)
                        task.completed_dates = parsed_completed_dates
                        task.completed = task_completed

                    elif task_type == "PriorityTask":
                        try:
                            priority_value = int(task_priority_str) if task_priority_str else 1
                            task = PriorityTask(task_title, task_description, priority_value)
                            task.date_due = task_date_due
                            task.completed = task_completed
                        e
