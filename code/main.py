# -*- coding: utf-8 -*-
'''
This is the main file that runs the Task Manager System.
'''
from user import User
from priority import Priority
from tag import Tag
from database import Database
def main():
    db = Database()
    print("Welcome to the Task Manager System!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(1, username, password)
    db.add_user(user)
    user.login(username, password)

    while True:
        print("\nOptions:")
        print("1. Create a task")
        print("2. Set a reminder")
        print("3. Mark a task as complete")
        print("4. Edit a task")
        print("5. Add a tag to a task")
        print("6. View tasks")
        print("7. Delete a task")
        print("8. Check reminders")
        print("9. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low/Medium/High): ")
            priority_obj = Priority(priority)
            user.create_task(title, description, due_date, priority_obj)
        elif choice == "2":
            task_id = int(input("Enter task ID: "))
            reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
            user.set_reminder(task_id, reminder_time)
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            user.mark_task_completed(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            new_title = input("Enter new title: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            user.edit_task(task_id, title=new_title, due_date=new_due_date)
        elif choice == "5":
            task_id = int(input("Enter task ID: "))
            tag_name = input("Enter tag name: ")
            new_tag = Tag(len(user.tasks[task_id-1].tags) + 1, tag_name)
            user.add_tag(task_id, new_tag)
        elif choice == "6":
            filter_by = input("View all/incomplete/completed tasks: ")
            user.view_tasks(filter_by)
        elif choice == "7":
            task_id = int(input("Enter task ID to delete: "))
            user.delete_task(task_id)
        elif choice == "8":
            for task in user.tasks:
                for reminder in task.reminders:
                    reminder.check_reminder()
        elif choice == "9":
            user.logout()
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
