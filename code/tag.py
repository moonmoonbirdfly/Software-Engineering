# -*- coding: utf-8 -*-
'''
This is the Tag class that represents a tag in the task manager application.
'''
class Tag:
    '''
    This class represents a tag that can be associated with tasks.
    '''
    def __init__(self, tag_id: int, name: str):
        self.tag_id = tag_id
        self.name = name
        self.tasks = []  # Stores tasks associated with this tag

    def add_task(self, task):
        # Check if the task is already associated with the tag
        if any(t.task_id == task.task_id for t in self.tasks):
            print(f"Task {task.task_id} is already tagged with '{self.name}'.")
            return
        self.tasks.append(task)
        print(f"Task {task.task_id} tagged with '{self.name}'.")

    def remove_task(self, task_id):
        # Ensure the task exists in the tag before attempting removal
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} removed from tag '{self.name}'.")
                return
        print(f"Task {task_id} not found in tag '{self.name}'.")

    def count_tasks(self):
        # Count the number of tasks associated with this tag
        return len(self.tasks)

    def find_task(self, task_id):
        # Find and return a specific task by ID
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        print(f"Task {task_id} not found in tag '{self.name}'.")
        return None

    def display_tasks(self):
        # Display all tasks associated with the tag
        if not self.tasks:
            print(f"No tasks are associated with the tag '{self.name}'.")
            return
        print(f"\nTasks under tag '{self.name}':")
        for task in self.tasks:
            print(f"- Task ID: {task.task_id}, Title: {task.title}, Status: {task.status}")
