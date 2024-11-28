# -*- coding: utf-8 -*-
'''
This is the User class that represents a user of the task manager application.
'''
from datetime import datetime
from task import Task
from priority import Priority
from reminder import Reminder
from tag import Tag
class User:
    '''
    This class represents a user of the task manager application.
    '''
    def __init__(self, user_id: int, username: str, password: str):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.tasks = []

    def login(self, input_username: str, input_password: str):
        if self.username == input_username and self.password == input_password:
            print(f"Welcome, {self.username}!")
            return True
        print("Invalid username or password.")
        return False

    def logout(self):
        print(f"Goodbye, {self.username}!")

    def create_task(self, title, description, due_date, priority):
        # Validate priority
        if not isinstance(priority, Priority):
            print("Error: Priority must be a valid Priority object.")
            return
        # Validate priority level (1 to 3)
        priority_value = priority.to_numeric()
        if not 1 <= priority_value <= 3:
            print("Error: Priority must be between 1 (Low) and 3 (High).")
            return

        # Validate due_date
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj < datetime.now():
                print("Error: Due date must be a future date.")
                return
        except ValueError:
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return

        # If all validations passed, create the task
        task = Task(len(self.tasks) + 1, title, description, due_date, priority)
        self.tasks.append(task)
        print(f"Task '{title}' created with priority {priority}.")
    def add_tag(self, task_id : int ,tag : Tag ):
        self.tasks[task_id-1].add_tag(tag)
    def edit_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                task.update_task(**kwargs)
                print(f"Task {task_id} updated.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print(f"Task {task_id} deleted.")

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                print(f"Task {task_id} marked as completed.")
                return
        print("Task not found.")

    def view_tasks(self, filter_by="all"):
        if filter_by == "completed":
            tasks_to_view = [task for task in self.tasks if task.completed]
        elif filter_by == "incomplete":
            tasks_to_view = [task for task in self.tasks if not task.completed]
        else:
            tasks_to_view = self.tasks

        if not tasks_to_view:
            print("No tasks to display.")
            return

        print("\nYour tasks:")
        for task in sorted(tasks_to_view, key=lambda t: (t.priority.to_numeric(), t.due_date)):
            print(f"ID: {task.task_id}, Title: {task.title}, Due: {task.due_date}, "
                  f"Priority: {task.priority}, Completed: {task.completed}")

    def set_reminder(self, task_id, reminder_date):
        """Sets a reminder for a given task."""
        for task in self.tasks:
            if task.task_id == task_id:
                # Validate reminder date format
                try:
                    reminder_date_obj = datetime.strptime(reminder_date, "%Y-%m-%d %H:%M")
                    # Ensure reminder date is in the future and before due date
                    if reminder_date_obj < datetime.now():
                        print("Error: Reminder date must be in the future.")
                        return
                    elif reminder_date_obj > task.due_date:
                        print(f"Error: Reminder date must be before the task's \
                              due date ({task.due_date.strftime('%Y-%m-%d')}).")
                        return
                    # Create and add the reminder
                    reminder = Reminder(len(task.reminders) + 1, task.task_id, reminder_date)
                    task.reminders.append(reminder)
                    print(f"Reminder set for task {task.task_id} on {reminder_date}.")
                except ValueError:
                    print("Error: Invalid reminder date format. Use YYYY-MM-DD HH:MM.")
                return
        print(f"Task with ID {task_id} not found.")
