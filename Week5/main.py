from datetime import datetime, timedelta
from task_list import TaskList
from tasks import Task, RecurringTask
from users import User, Owner  # <<< Import User and Owner classes

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Populates the task list with sample tasks."""
    # Ensure current date is considered for overdue tasks
    now_gmt = datetime.now() # Current time is Wednesday, July 16, 2025 at 4:36:50 AM EAT.

    task_list.add_task(Task("Buy groceries", now_gmt - timedelta(days=4), "Milk, eggs, bread"))
    task_list.add_task(Task("Do laundry", now_gmt + timedelta(days=2), "Wash and fold clothes"))
    task_list.add_task(Task("Clean room", now_gmt - timedelta(days=1), "Vacuum and dust"))
    task_list.add_task(Task("Do homework", now_gmt + timedelta(days=3), "Math assignment"))
    task_list.add_task(Task("Walk dog", now_gmt + timedelta(days=5), "30-minute walk"))
    task_list.add_task(Task("Do dishes", now_gmt + timedelta(days=6), "Clean after dinner"))

    # Sample recurring task
    # Adjusting initial due date to be current or slightly in the past for propagation logic
    r_task = RecurringTask("Go to the gym", now_gmt, timedelta(days=7))
    # Add some past completed dates
    r_task.completed_dates.append(now_gmt - timedelta(days=7))
    r_task.completed_dates.append(now_gmt - timedelta(days=14))
    r_task.completed_dates.append(now_gmt - timedelta(days=21)) # Adjusted for consistent intervals
    r_task.date_created = now_gmt - timedelta(days=28) # Task created long ago

    # Recalculate date_due based on past completions, so it reflects the *next* due date
    if r_task.completed_dates:
        r_task.date_due = max(r_task.completed_dates) + r_task.interval
        r_task.completed = False # Ensure it's not marked completed for the *next* cycle

    task_list.add_task(r_task)
    return task_list

def main():
    # --- Portfolio Exercise 4 Modifications Start Here ---

    # 1. Create an Owner instance
    # Replace "Your Name" with actual owner details
    owner_name = input("Enter your name as the Task List owner: ")
    owner_email = input("Enter your email as the Task List owner: ")
    task_list_owner = Owner(name=owner_name, email=owner_email)

    # Print the owner details using the __str__ method (optional, for verification)
    print(f"\nCreated {task_list_owner}")

    # 2. Create the default task list with the owner instance
    task_list = TaskList(owner=task_list_owner)
    propagate_task_list(task_list)  # Populate with sample tasks

    # --- Portfolio Exercise 4 Modifications End Here ---

    while True:
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Change task title, due date, or description")
        print("5. Mark task as completed")
        print("6. View overdue tasks")
        print("7. Quit")

        choice = input("Enter choice (1–7): ")

        if choice == "1":
            task_type = input("Do you want to add a recurring task or a normal task? (recurring/normal): ").strip().lower()
            title = input("Enter task title: ")
            input_date = input("Enter a due date (YYYY-MM-DD): ")
            description = input("Enter task description (optional): ")

            try:
                date_object = datetime.strptime(input_date, "%Y-%m-%d")

                if task_type == "recurring":
                    interval_input = input("Enter recurrence interval in days (e.g., 7): ")
                    try:
                        interval = timedelta(days=int(interval_input))
                        task = RecurringTask(title, date_object, interval)
                        task_list.add_task(task)
                        print("Recurring task added.")
                    except ValueError:
                        print("Invalid number for recurrence interval. Task not added.")
                elif task_type == "normal":
                    task = Task(title, date_object, description)
                    task_list.add_task(task)
                    print("Normal task added.")
                else:
                    print("Invalid task type. Please choose 'recurring' or 'normal'.")

            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            try:
                ix = int(input("Enter index to remove: "))
                task_list.remove_task(ix)
            except ValueError:
                print("Invalid input. Please enter a number.")
            except IndexError:
                print("Task number out of range.")


        elif choice == "4":
            try:
                task_list.view_tasks() # Show tasks to help user pick
                ix = int(input("Enter the index of the task to update: ")) - 1
                task = task_list.get_task(ix)
                print(f"Current task: {task}")

                new_title = input(f"Enter new title (current: '{task.title}', press Enter to keep): ").strip()
                if new_title:
                    task.change_title(new_title)

                change_date = input(f"Change due date? (current: {task.date_due.strftime('%Y-%m-%d')}) (yes/no): ").strip().lower()
                if change_date == "yes":
                    new_date_str = input("Enter new due date (YYYY-MM-DD): ")
                    try:
                        new_date_obj = datetime.strptime(new_date_str, "%Y-%m-%d")
                        task.change_date_due(new_date_obj)
                    except ValueError:
                        print("Invalid date format. Date not updated.")

                change_desc = input(f"Change description? (current: '{task.description}', yes/no): ").strip().lower()
                if change_desc == "yes":
                    new_desc = input("Enter new description (press Enter to clear): ")
                    task.change_description(new_desc)

                print("Task updated.")
            except (ValueError, IndexError):
                print("Invalid input or task index.")

        elif choice == "5":
            try:
                task_list.view_tasks() # Show tasks to help user pick
                ix = int(input("Enter index to mark completed: ")) - 1
                task = task_list.get_task(ix)
                task.mark_completed()
                print("Task marked as completed.")
            except (ValueError, IndexError):
                print("Invalid input or task index.")
            except Exception as e:
                print(f"An error occurred: {e}")


        elif choice == "6":
            task_list.view_overdue_tasks()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()