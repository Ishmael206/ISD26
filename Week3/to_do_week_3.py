# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.\n")

# Function to view current tasks in the list
def view_tasks():
    if not tasks:
        print("Your task list is empty.\n")
    else:
        print("Your current tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

# Function to remove a task from the list
def remove_task():
    if not tasks:
        print("There are no tasks to remove.\n")
        return

    view_tasks()
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' removed successfully.\n")
        else:
            print("Invalid task number. Please try again.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main program loop
while True:
    print("=== To-Do List Manager ===")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye! Thank you for using the To-Do List Manager.")
        break
    else:
        print("Invalid choice. Please try again.\n")
