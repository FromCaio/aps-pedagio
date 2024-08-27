import json
from model.admin import Admin

class AdminDAO:
    #constructor method
    def __init__(self):
        self.load_admins()

    #method to load the data from the json file
    def load_admins(self):
        try:
            with open('DAO/json_files/admins.json', 'r') as f:
                self.admins = [Admin.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.admins = []

    def insert_admin(self, admin):
        self.admins.append(admin)
    
    def delete_admin(self, admin):
        for adm in self.admins:
            if adm.email == admin.email:
                self.admins.remove(adm)
    
    def find_admin(self, email):
        for admin in self.admins:
            if admin.email == email:
                return admin
    
    #method to close the connection and save the data to the json file    
    def close(self):
        with open('DAO/json_files/admins.json', 'w') as f:
            json.dump([admin.to_dict() for admin in self.admins], f)