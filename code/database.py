# -*- coding: utf-8 -*-
'''
This is Database class that stores the users.
'''
class Database:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"User {user.username} added to database.")
