# -*- coding: utf-8 -*-
'''
This is the Reminder class that represents a reminder for a task.
'''
from datetime import datetime

class Reminder:
    '''
    This class represents a reminder for a task.
    '''
    def __init__(self, reminder_id: int, task_id: int,
                 reminder_date, message="Task is due soon.", repeat_interval=None):
        """
        :param reminder_id: Unique ID of the reminder
        :param task_id: ID of the associated task
        :param reminder_date: The date and time for the reminder (datetime object or valid string)
        :param message: Custom notification message for the reminder
        :param repeat_interval: Time interval for repeated reminders (timedelta object or None)
        """
        if isinstance(reminder_date, str):
            self.reminder_date = datetime.strptime(reminder_date, "%Y-%m-%d %H:%M:%S")
        elif isinstance(reminder_date, datetime):
            self.reminder_date = reminder_date
        else:
            raise ValueError("Invalid date format. \
                             Use datetime object or 'YYYY-MM-DD HH:MM:SS' string.")
        if self.reminder_date < datetime.now():
            raise ValueError("Reminder date must be in the future.")

        self.reminder_id = reminder_id
        self.task_id = task_id
        self.message = message
        self.repeat_interval = repeat_interval  # None or timedelta object
        self.is_triggered = False

    def notify_user(self):
        """Notify the user and update the reminder status."""
        if self.is_triggered:
            print(f"Reminder {self.reminder_id} already triggered.")
            return

        print(f"Reminder: {self.message} (Task {self.task_id}, Scheduled for {self.reminder_date})")
        self.is_triggered = True

        if self.repeat_interval:
            self.schedule_next_reminder()

    def schedule_next_reminder(self):
        """Schedule the next occurrence of the reminder if it is repetitive."""
        if not self.repeat_interval:
            print("This reminder does not repeat.")
            return

        self.reminder_date += self.repeat_interval
        self.is_triggered = False
        print(f"Next reminder scheduled for {self.reminder_date}.")

    def edit_reminder(self, new_date=None, new_message=None, new_repeat_interval=None):
        """Edit the reminder's attributes."""
        if new_date:
            if isinstance(new_date, str):
                new_date = datetime.strptime(new_date, "%Y-%m-%d %H:%M:%S")
            if new_date < datetime.now():
                raise ValueError("New reminder date must be in the future.")
            self.reminder_date = new_date
        if new_message:
            self.message = new_message

        if new_repeat_interval:
            self.repeat_interval = new_repeat_interval

        print(f"Reminder {self.reminder_id} updated: Date={self.reminder_date}, \
              Message='{self.message}', Repeat={self.repeat_interval}.")

    def check_reminder(self):
        """Check if the reminder is due and notify the user if it is."""
        current_time = datetime.now()
        if current_time >= self.reminder_date and not self.is_triggered:
            self.notify_user()
        elif current_time < self.reminder_date:
            print(f"Reminder {self.reminder_id} is scheduled for {self.reminder_date}.")
