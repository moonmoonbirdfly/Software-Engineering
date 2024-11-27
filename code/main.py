from models.user import User
from models.priority import Priority
from models.reminder import Reminder
from models.tag import Tag
from utils.database import Database

def main():
    db = Database()
    print("Welcome to the Task Manager!")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    # Login
    user = db.login(username, password)
    if user:
        print("Login successful!")
    else:
        print("Login failed. Please check your username and password.")
        return

    while True:
        print("\nOptions:")
        print("1. Create a task")
        print("2. Mark a task as complete")
        print("3. Set a reminder")
        print("4. Edit a task")
        print("5. Add a tag to a task")
        print("6. View tasks")
        print("7. Delete a task")
        print("8. Check reminders")
        print("9. Logout")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (High/Medium/Low): ")
            priority_obj = Priority(priority)
            user.create_task(title, description, due_date, priority_obj)

        elif choice == "2":
            task_id = int(input("Enter task ID to mark as complete: "))
            user.mark_task_completed(task_id)

        elif choice == "3":
            task_id = int(input("Enter task ID to set a reminder: "))
            reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
            user.set_reminder(task_id, reminder_time)

        elif choice == "4":
            task_id = int(input("Enter task ID to edit: "))
            new_title = input("Enter new task title: ")
            new_due_date = input("Enter new task due date (YYYY-MM-DD): ")
            user.edit_task(task_id, title=new_title, due_date=new_due_date)

        elif choice == "5":
            task_id = int(input("Enter task ID to add a tag: "))
            tag_name = input("Enter tag name: ")
            user.add_tag(task_id, tag_name)

        elif choice == "6":
            status = input("View all tasks, incomplete tasks, or completed tasks? (all/incomplete/completed): ")
            user.view_tasks(status)

        elif choice == "7":
            task_id = int(input("Enter task ID to delete: "))
            user.delete_task(task_id)

        elif choice == "8":
            for task in user.tasks:
                for reminder in task.reminders:
                    reminder.check_reminder()

        elif choice == "9":
            user.logout()
            print("Logged out successfully!")
            break

        elif choice == "10":
            print("Exiting the Task Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()