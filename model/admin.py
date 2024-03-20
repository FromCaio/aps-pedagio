class Admin:
    id = 100000
    def __init__(self, name, password, email, permission = 1):
        self.name = name
        self.password = password
        self.email = email

        self.id = id+1
        self.permission = permission
        self.history = []
    def __str__(self):
        return f"Admin: {self.name}, Email: {self.email}, Permission: {self.permission}"