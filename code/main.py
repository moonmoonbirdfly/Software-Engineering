from models.user import User
from models.priority import Priority
from models.reminder import Reminder
from models.tag import Tag
from utils.database import Database

def main():
    db = Database()
    user = User(1, "Alice", "password123")
    db.add_user(user)

    # Login
    user.login("Alice", "password123")

    # Create tasks
    priority_high = Priority("High")
    priority_medium = Priority("Medium")
    user.create_task("Buy groceries", "Buy milk, bread, and eggs", "2024-12-01", priority_high)
    user.create_task("Finish project", "Complete the TODO list project", "2024-12-05", priority_high)
    user.create_task("Doctor appointment", "Visit the doctor for a check-up", "2024-12-10", priority_medium)

    # Mark a task as complete
    user.mark_task_completed(1)

    # Set a reminder
    user.set_reminder(2, "2024-12-04 10:00")

    # Edit a task
    user.edit_task(2, title="Finish project report", due_date="2024-12-07")

    # Add a tag to a task
    user.add_tag(2, "Work")

    # View tasks
    user.view_tasks("all")
    user.view_tasks("incomplete")
    user.view_tasks("completed")

    # Delete a task
    user.delete_task(3)

    # Check reminders
    for task in user.tasks:
        for reminder in task.reminders:
            reminder.check_reminder()

    # Logout
    user.logout()

if __name__ == "__main__":
    main()