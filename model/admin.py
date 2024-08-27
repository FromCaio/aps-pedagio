import json

class Admin:
    def __init__(self, id, name, password, email, permission=1):
        self.id = id
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

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            password=data['password'],
            email=data['email'],
            permission=data['permission']
        )
