# 1. Data Structures

# Exercise 1: Tuples

coordinates = (10, 20)
x, y = coordinates
print("x =", x)
print("y =", y)

thistuple = ("Banana", "Apple", "Cherry")
print(thistuple)

# Exercise 2: Sets

all_students = {"Alice", "Bob", "Charlie", "Diana"}
submitted = {"Alice", "Charlie"}
not_submitted = all_students.difference(submitted)

print("Students who did not submit:", not_submitted)

# Exercise 3: Dictionaries

my_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

my_dict = dict(brand="Ford", model="Mustang", year=1964)
print(my_dict)

# Exercise 4: Using Data Structures

# Task 1 - Tuples
a = 5
b = 10
# swap the values of a and b
a, b = (b, a)
print("a =", a)
print("b =", b)

# Task 2 - Sets

set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}

# return only names that are in both sets
common_names = set1.intersection(set2)
print(common_names)

# Task 3 - Dictionaries

def histogram(my_list):
    hist = {}
    for item in my_list:
        if item in hist:
            hist[item] += 1
        else:
            hist[item] = 1
    return hist

my_list = [1, 2, 3, 1, 2, 3, 4]
assert histogram(my_list) == {1: 2, 2: 2, 3: 2, 4: 1}
print(histogram(my_list))
 
# 2. Abstract Classes 

 # Abstract Classes
from abc import ABC, abstractmethod

class Dice(ABC):
    def __init__(self) -> None:
        self.face = None
    @abstractmethod
    def roll(self) -> int:
        pass

from random import randint

class SixSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 6)
        return self.face
    
# histogram for dice rolls x 1000 times
dice = SixSidedDice()
results = []
for _ in range(1000):
    results.append(dice.roll())
hist = histogram(results)
print(hist)

# 10 sided dice
class TenSidedDice(Dice):
    def roll(self) -> int:
        self.face = randint(1, 10)
        return self.face

# histogram for dice rolls x 1000 times
dice = TenSidedDice()
results = []
for _ in range(1000):
    results.append(dice.roll())
hist = histogram(results)
print(hist)

# 3. Portfolio Exercises

# Portfolio Exercise 5

from abc import ABC, abstractmethod
from typing import ClassVar, Dict
class AbstractTask(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

class PriorityTask(AbstractTask):
    PRIORITY_MAP: ClassVar[Dict[int, str]] = {1: "low", 2: "medium", 3: "high"}
    def __init__(self, title: str, description: str, priority: int):
        if priority not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1, 2, or 3")
        self._title: str = title
        self._description: str = description
        self._priority: int = priority
    @property
    def priority(self) -> int:
        return self._priority
    @priority.setter
    def priority(self, value: int) -> None:
        if value not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1, 2, or 3")
        self._priority = value
    def __str__(self) -> str:
        return f"[PriorityTask] {self._title}: {self._description} (Priority: {self.PRIORITY_MAP[self._priority]})"

# Testing PriorityTask functionality 
try:
    task = PriorityTask("Submit Report", "Complete and upload coursework.", 2)
    print(task)

    # Change priority
    task.priority = 3
    print("Updated:", task)

    # Trigger error with invalid priority
    task.priority = 5
except ValueError as e:
    print("Error:", e)
    
# Portfolio Exercise 6

from abc import ABC, abstractmethod
from typing import List, Dict, ClassVar
import csv
import os

# Abstract Task
class AbstractTask(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass

# Task Classes
class Task(AbstractTask):
    def __init__(self, title: str, description: str):
        self._title: str = title
        self._description: str = description
    def __str__(self) -> str:
        return f"[Task] {self._title}: {self._description}"

class RecurringTask(AbstractTask):
    def __init__(self, title: str, description: str, frequency: str):
        self._title: str = title
        self._description: str = description
        self._frequency: str = frequency
    def __str__(self) -> str:
        return f"[RecurringTask] {self._title}: {self._description} (Frequency: {self._frequency})"

class PriorityTask(AbstractTask):
    PRIORITY_MAP: ClassVar[Dict[int, str]] = {1: "low", 2: "medium", 3: "high"}
    def __init__(self, title: str, description: str, priority: int):
        if priority not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1, 2, or 3")
        self._title: str = title
        self._description: str = description
        self._priority: int = priority
    @property
    def priority(self) -> int:
        return self._priority
    @priority.setter
    def priority(self, value: int) -> None:
        if value not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1, 2, or 3")
        self._priority = value
    def __str__(self) -> str:
        return f"[PriorityTask] {self._title}: {self._description} (Priority: {self.PRIORITY_MAP[self._priority]})"

# Task Factory
class TaskFactory:
    @staticmethod
    def create_task(task_type: str, title: str, description: str, extra: str | int) -> AbstractTask:
        if task_type.lower() == "task":
            return Task(title, description)
        elif task_type.lower() == "recurring":
            return RecurringTask(title, description, str(extra))
        elif task_type.lower() == "priority":
            return PriorityTask(title, description, int(extra))
        raise ValueError("Invalid task type")

# Abstract DAO
class TaskDAO(ABC):
    @abstractmethod
    def get_all_tasks(self) -> List[AbstractTask]:
        pass
    @abstractmethod
    def save_all_tasks(self, tasks: List[AbstractTask]) -> None:
        pass

# CSV DAO
class TaskCsvDAO(TaskDAO):
    def __init__(self, filename: str):
        self.filename: str = filename
    def get_all_tasks(self) -> List[AbstractTask]:
        tasks: List[AbstractTask] = []
        if not os.path.exists(self.filename):
            return tasks
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if not row:
                    continue
                task_type, title, description, extra = row
                tasks.append(TaskFactory.create_task(task_type, title, description, extra))
        return tasks
    def save_all_tasks(self, tasks: List[AbstractTask]) -> None:
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in tasks:
                if isinstance(task, Task):
                    writer.writerow(["task", task._title, task._description, ""])
                elif isinstance(task, RecurringTask):
                    writer.writerow(["recurring", task._title, task._description, task._frequency])
                elif isinstance(task, PriorityTask):
                    writer.writerow(["priority", task._title, task._description, task._priority])

# CommandLineUI
class CommandLineUI:
    def __init__(self, dao: TaskDAO):
        self.dao: TaskDAO = dao
    def add_task(self) -> None:
        task_type = input("Enter task type (task/recurring/priority): ").lower()
        title = input("Enter title: ")
        description = input("Enter description: ")
        extra = ""
        if task_type == "recurring":
            extra = input("Enter frequency: ")
        elif task_type == "priority":
            extra = input("Enter priority (1=low, 2=medium, 3=high): ")
        task = TaskFactory.create_task(task_type, title, description, extra)
        tasks = self.dao.get_all_tasks()
        tasks.append(task)
        self.dao.save_all_tasks(tasks)
        print(f"Added: {task}")
    def display_tasks(self) -> None:
        tasks = self.dao.get_all_tasks()
        for task in tasks:
            print(task)
    def run(self) -> None:
        while True:
            action = input("Enter action (add/display/quit): ").lower()
            if action == "add":
                self.add_task()
            elif action == "display":
                self.display_tasks()
            elif action == "quit":
                break

# Run the App
if __name__ == "__main__":
    dao = TaskCsvDAO("tasks.csv")
    ui = CommandLineUI(dao)
    ui.run()
