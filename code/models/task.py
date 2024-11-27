from datetime import datetime
from models.priority import Priority
from models.reminder import Reminder
from models.tag import Tag

class TaskStatus:
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class Task:

    def __init__(self, task_id: int, title: str, description: str = '', due_date: str = "2024-12-01", priority: Priority = Priority("Low")):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = self.validate_due_date(due_date)
        self.priority = self.validate_priority(priority)
        self.status = TaskStatus.PENDING
        self.reminders = []
        self.tags = []
        self.completed = False

    @staticmethod
    def validate_due_date(due_date):
        try:
            due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj < datetime.now():
                raise ValueError("Due date must be a future date.")
            return due_date_obj
        except ValueError as e:
            raise ValueError(f"Invalid due date: {e}")

    @staticmethod
    def validate_priority(priority):
        if not isinstance(priority, Priority):
            raise ValueError("Priority must be a valid Priority object.")
        return priority

    def mark_as_complete(self):
        if self.status == TaskStatus.COMPLETED:
            print(f"Task {self.task_id} is already completed.")
        else:
            self.status = TaskStatus.COMPLETED
            print(f"Task {self.task_id} marked as complete.")

    def set_reminder(self, reminder_date):
        try:
            reminder_date_obj = datetime.strptime(reminder_date, "%Y-%m-%d %H:%M")
            if reminder_date_obj > self.due_date:
                raise ValueError("Reminder date must be before the task due date.")
            elif reminder_date_obj < datetime.now():
                raise ValueError("Reminder date must be in the future.")
            reminder = Reminder(len(self.reminders) + 1, self.task_id, reminder_date)
            self.reminders.append(reminder)
            print(f"Reminder set for task {self.task_id} on {reminder_date}.")
        except ValueError as e:
            print(f"Error setting reminder: {e}")

    def add_tag(self, tag_name):
        if any(tag.name == tag_name for tag in self.tags):
            print(f"Tag '{tag_name}' already exists for task {self.task_id}.")
        else:
            tag = Tag(len(self.tags) + 1, tag_name)
            self.tags.append(tag)
            print(f"Tag '{tag_name}' added to task {self.task_id}.")

    def update_task(self, **kwargs):
        for key, value in kwargs.items():
            if key == "title":
                self.title = value
            elif key == "description":
                self.description = value
            elif key == "due_date":
                self.due_date = self.validate_due_date(value)
            elif key == "priority":
                self.priority = self.validate_priority(value)
            else:
                print(f"Unknown field: {key}")
        print(f"Task {self.task_id} updated.")

    def print_details(self):
        print(f"Task ID: {self.task_id}")
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Due Date: {self.due_date.strftime('%Y-%m-%d')}")
        print(f"Priority: {self.priority}")  # Priority is now a Priority object
        print(f"Status: {self.status}")
        print("Tags:", ", ".join(tag.name for tag in self.tags))
        print("Reminders:", ", ".join(reminder.reminder_date for reminder in self.reminders))
