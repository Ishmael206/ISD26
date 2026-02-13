# command_line_ui.py - Markdown Conversion

```python
# ui/command_line_ui.py
from controllers.task_manager_controller import TaskManagerController

class CommandLineUI:
    """
    Handles all user input and output for the ToDo application.
    It calls methods on TaskManagerController to perform actions.
    """
    def __init__(self, controller: TaskManagerController):
        self.controller = controller

    def _print_menu(self) -> None:
        """Prints the main menu options."""
        print("\n--- TO-DO LIST MANAGER ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Change task details (title, due date, description)")
        print("5. Mark task as completed")
        print("6. View overdue tasks")
        print("7. Load tasks")
        print("8. Save tasks")
        print("9. Quit")

    def run(self) -> None:
        """Main loop for the command-line interface."""
        print(f"Welcome to your ToDo App, {self.controller.get_owner_info()}")

        while True:
            self._print_menu()
            choice = input("Enter choice (1–9): ").strip()

            if choice == "1":
                self._add_task_menu()
            elif choice == "2":
                print(self.controller.get_all_tasks_display())
            elif choice == "3":
                self._remove_task_menu()
            elif choice == "4":
                self._update_task_details_menu()
            elif choice == "5":
                self._mark_completed_menu()
            elif choice == "6":
                print(self.controller.get_overdue_tasks_display())
            elif choice == "7":
                self._load_tasks_menu()
            elif choice == "8":
                self._save_tasks_menu()
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def _add_task_menu(self) -> None:
        """Handles user input for adding a new task."""
        task_type = input("Do you want to add a normal, recurring, or priority task? (normal/recurring/priority): ").strip().lower()
        title = input("Enter task title: ").strip()
        date_due_str = input("Enter a due date (YYYY-MM-DD, leave blank for no due date): ").strip()
        description = input("Enter task description (optional): ").strip()

        interval_days_str = None
        priority_level_str = None

        if task_type == "recurring":
            interval_days_str = input("Enter recurrence interval in days (e.g., 7): ").strip()
        elif task_type == "priority":
            priority_level_str = input("Enter priority (1 for low, 2 for medium, 3 for high): ").strip()

        # Delegate to controller
        message = self.controller.add_new_task(
            title, date_due_str, description, task_type, interval_days_str, priority_level_str
        )
        print(message)

    def _remove_task_menu(self) -> None:
        """Handles user input for removing a task."""
        print(self.controller.get_all_tasks_display())
        try:
            task_num = int(input("Enter the number of the task to remove: ").strip())
            message = self.controller.remove_task_by_number(task_num)
            print(message)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def _mark_completed_menu(self) -> None:
        """Handles user input for marking a task as completed."""
        print(self.controller.get_all_tasks_display())
        try:
            task_num = int(input("Enter index to mark completed: ").strip())
            message = self.controller.mark_task_completed(task_num)
            print(message)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def _update_task_details_menu(self) -> None:
        """Handles user input for updating task details."""
        print(self.controller.get_all_tasks_display())
        try:
            task_num = int(input("Enter the number of the task to update: ").strip())

            # These will be None if user presses Enter
            new_title = input("Enter new title (press Enter to keep current): ").strip()
            new_date_str = input("Enter new due date (YYYY-MM-DD, press Enter to keep current): ").strip()
            new_description = input("Enter new description (press Enter to clear, or 'current' to keep): ")

            # Simple logic to distinguish between keeping current and clearing description
            if new_description.lower() == 'current':
                new_description = None  # Means don't change
            elif not new_description:
                new_description = ""  # Means clear

            message = self.controller.update_task_details(
                task_num,
                new_title if new_title else None,
                new_date_str if new_date_str else None,
                new_description
            )
            print(message)

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _load_tasks_menu(self) -> None:
        """Handles user input for loading tasks."""
        message = self.controller.load_tasks()  # DAO path is set in controller init
        print(message)

    def _save_tasks_menu(self) -> None:
        """Handles user input for saving tasks."""
        message = self.controller.save_tasks()  # DAO path is set in controller init
        print(message)

```