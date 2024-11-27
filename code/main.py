from models.user import User
from models.priority import Priority
from models.reminder import Reminder
from models.tag import Tag
from utils.database import Database
def main():
    db = Database()  # 初始化数据库
    print("Welcome to the Task Manager System!")

    # 用户登录
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    user = User(1, username, password)
    db.add_user(user)
    user.login(username, password)

    # 任务操作循环
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
            # 创建任务
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low/Medium/High): ")
            priority_obj = Priority(priority)
            user.create_task(title, description, due_date, priority_obj)
        elif choice == "2":
            # 设置提醒
            task_id = int(input("Enter task ID: "))
            reminder_time = input("Enter reminder time (YYYY-MM-DD HH:MM): ")
            user.set_reminder(task_id, reminder_time)
        elif choice == "3":
            # 标记任务为完成
            task_id = int(input("Enter task ID: "))
            user.mark_task_completed(task_id)
        elif choice == "4":
            # 编辑任务
            task_id = int(input("Enter task ID: "))
            new_title = input("Enter new title: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            user.edit_task(task_id, title=new_title, due_date=new_due_date)
        elif choice == "5":
            # 添加标签
            task_id = int(input("Enter task ID: "))
            tag_name = input("Enter tag name: ")
            new_tag = Tag(len(user.tasks[task_id-1].tags) + 1, tag_name)
            user.add_tag(task_id, new_tag)
        elif choice == "6":
            # 查看任务
            filter_by = input("View all/incomplete/completed tasks: ")
            user.view_tasks(filter_by)
        elif choice == "7":
            # 删除任务
            task_id = int(input("Enter task ID to delete: "))
            user.delete_task(task_id)
        elif choice == "8":
            # 检查提醒
            for task in user.tasks:
                for reminder in task.reminders:
                    reminder.check_reminder()
        elif choice == "9":
            # 注销
            user.logout()
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()