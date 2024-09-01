import json
from model.admin import Admin
from DAO.DAO import DAO

class AdminDAO(DAO):
    def __init__(self):
        super().__init__()

    #method to load the data from the json file
    def load(self):
        try:
            with open('DAO/json_files/admins.json', 'r') as f:
                self.admins = [Admin.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.admins = []

    def insert(self, admin):
        print(self.admins)
        print(admin)
        self.admins.append(admin)
        self.close()
    
    def delete(self, admin):
        print(admin)
        for adm in self.admins:
            if adm.email == admin.email:
                self.admins.remove(adm)
        self.close()
    
    def find(self, email):
        for admin in self.admins:
            if admin.email == email:
                return admin
    
    #method to close the connection and save the data to the json file    
    def close(self):
        with open('DAO/json_files/admins.json', 'w') as f:
            json.dump([admin.to_dict() for admin in self.admins], f)