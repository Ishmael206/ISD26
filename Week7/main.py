# main.py
from controllers.task_manager_controller import TaskManagerController
from ui.command_line_ui import CommandLineUI

def main():
    # Get owner details first
    owner_name = input("Enter your name as the Task List owner: ")
    owner_email = input("Enter your email as the Task List owner: ")
    storage_file = input("Enter the task data file path (e.g., 'tasks.csv'): ")

    # Initialize the controller, passing owner details and storage path
    controller = TaskManagerController(owner_name, owner_email, storage_file)

    # Initialize the UI, passing the controller
    ui = CommandLineUI(controller)

    # Run the UI
    ui.run()

if __name__ == "__main__":
    main()
