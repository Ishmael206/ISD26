import tasks
class TaskList:
    def __init__(self, owner:str)-> None :
        self.owner = owner.upper()
        self.tasks: list[tasks.Task] = []
    def add_task(self, task:tasks.Task)-> None :
        self.tasks.append(task)
    def view_tasks(self)-> None :
            self.count = 0
            if not self.tasks:
                print("No tasks available.")
            return
            for task in self.tasks:
                self.count += 1
                print(f"{self.count}. {task}")
                print("Total tasks:", len(self.tasks), "\n")
    def remove_task(self, task_number:int)-> None :
        if 0 < task_number <= len(self.tasks):
            # del self.tasks[task_number - 1] # Using del to remove the task
            # or alternatively, you can use pop to remove and return the task
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")