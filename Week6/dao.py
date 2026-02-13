# dao.py
import datetime
from tasks import Task, RecurringTask # Assuming 'tasks.py' contains your Task and RecurringTask classes

class TaskTestDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def get_all_tasks(self) -> list[Task]:
        task_list = [
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4), "Milk, eggs, bread"),
            Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2), "Wash and fold clothes"),
            Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1), "Vacuum and dust"),
            Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3), "Math assignment"),
            Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5), "30-minute walk"),
            Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6), "Clean after dinner")
        ]
        # sample recurring task
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(),
                               datetime.timedelta(days=7))
        # propagate the recurring task with some completed dates
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28) # Set a past creation date

        task_list.append(r_task)
        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        # For TaskTestDAO, we don't actually save to a file.
        # This just simulates the call.
        print(f"INFO: TaskTestDAO - Pretending to save {len(tasks)} tasks to {self.storage_path}")
        pass
