# dao/user_dao_excel.py

import openpyxl
from models.user import User
from dao.user_dao_base import UserDAOBase
import os

class UserDAOExcel(UserDAOBase):
    def __init__(self, filepath: str):
        self.filepath = filepath
        # If the file doesn't exist, create it with a header row
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(["id", "name", "email"])
            workbook.save(filepath)

    def add_user(self, user: User):
        
        workbook = openpyxl.load_workbook(self.filepath)
        sheet = workbook.active

        new_id = sheet.max_row
        
        
        user_id = len(self.get_all_users()) + 1

        # Append the new user data as a row
        sheet.append([user_id, user.name, user.email])
        
        # Save the changes
        workbook.save(self.filepath)

    def get_all_users(self) -> list[User]:
        users = []
        try:
            workbook = openpyxl.load_workbook(self.filepath)
            sheet = workbook.active
            
            # Iterate through rows, skipping the header (row 1)
            for i, row in enumerate(sheet.iter_rows(min_row=2, values_only=True)):
                # Each row is a tuple: (id, name, email)
                id_, name, email = row
                users.append(User(int(id_), name, email))
        except FileNotFoundError:
            # If the file is somehow deleted between init and call, return empty list
            pass
        return users