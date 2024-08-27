import json

class Admin:
    # class variable id
    def __init__(self, name, password, email, permission = 1):
        self.id = self.get_admin_id()
        self.name = name
        self.password = password
        self.email = email
        self.permission = permission
        self.history = []

    def __str__(self):
        return f"Admin: {self.name}, Email: {self.email}, Permission: {self.permission}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'password': self.password,
            'email': self.email,
            'permission': self.permission,
            'history': self.history
        }

    #method to get admin class attribute ID value
    def get_admin_id(self):
        with open('DAO/json_files/admin_id.json', 'r') as f:
            admin_id = json.load(f)
        admin_id += 1
        with open('DAO/json_files/admin_id.json', 'w') as f:
            json.dump(admin_id, f)
        return admin_id
    
    @classmethod
    def from_dict(cls, data):
        admin = cls(data['name'], data['password'], data['email'], data['permission'])
        admin.id = data['id']
        admin.history = data['history']
        return admin