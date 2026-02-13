from task_list import TaskList
from tasks import Task
from datetime import datetime, timedelta

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Propagates a task list with some sample tasks.
    Args: task_list (TaskList): Task list to propagate.
    Returns: TaskList: The propagated task list.
    """
    task_list.add_task(Task("Buy groceries", datetime.now() - timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.now() - timedelta(days=-2)))
    task_list.add_task(Task("Clean room", datetime.now() + timedelta(days=-1)))
    task_list.add_task(Task("Do homework", datetime.now() + timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.now() + timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.now() + timedelta(days=6)))
    return task_list
def main()->None:
    task_list = TaskList("YOUR NAME")
        # propagate the task list with some sample tasks
    task_list = propagate_task_list(task_list)
    while True:
        print("To-Do List Manager version 4")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Change task title")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.")
            continue
        if choice == "1":
            title = input("Enter a task: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            task = Task(title, date_object)
            task_list.add_task(task)
        elif choice == "2":
            task_list.view_tasks()
        elif choice == "3":
            ix = int(input("Enter the index of the task to remove: "))
            task_list.remove_task(ix)
        elif choice == "4":
            ix = int(input("Enter the index of the task to mark as completed: "))
            task_list.tasks[ix-1].mark_completed()
        elif choice == "5":
            ix = int(input("Enter the index of the task to change title: "))
            new_title = input("Enter the new title: ")
            task_list.tasks[ix-1].change_title(new_title)
            change_date = input("Do you want to change the due date? (yes/no): ")
            if change_date.lower() == "yes":
                new_date = input("Enter the new due date (YYYY-MM-DD): ")
                date_object = datetime.strptime(new_date, "%Y-%m-%d")
                task_list.tasks[ix-1].change_due_date(date_object)
        elif choice == "6":
            break

if __name__ == "__main__":
    main()

