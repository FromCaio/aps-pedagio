import tkinter as tk
from view.admin import AdminView
from model.admin import Admin
from model.tollOperator import TollOperator
from view.tollOperator import TollOperatorView
from control.maincontrol import MainControl

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1280x720')
        self.root.config(bg = 'light blue')
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def create_widgets(self):
        # we will have a login pagin with username and password
        # and a login and cancel button

        # username label and entry
        self.username_label = tk.Label(self.root, text = 'Username', bg = 'light blue')
        self.username_label.place(x = 500, y = 250)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(x = 600, y = 250)
        self.username_entry.insert(0, "admin@example.com")

        # password label and entry
        self.password_label = tk.Label(self.root, text = 'Password', bg = 'light blue')
        self.password_label.place(x = 500, y = 300)
        self.password_entry = tk.Entry(self.root, show = '*')
        self.password_entry.place(x = 600, y = 300)
        self.password_entry.insert(0, "password")

        # login button
        self.login_button = tk.Button(self.root, text = 'Login', bg = 'light grey', command = self.login)
        self.login_button.place(x = 650, y = 350)

        # cancel button
        self.cancel_button = tk.Button(self.root, text = 'Cancel', bg = 'light grey', command = self.root.quit)
        self.cancel_button.place(x = 550, y = 350)
    # the clear method will clear the root window, so that we can use it for the admin view
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    def login(self):
        # call control to check if the user exists, the password is correct and its an admin
        # if it is, we will call the admin view
        user = MainControl.login(self.username_entry.get(), self.password_entry.get())
        # check if user is of type admin
        if isinstance(user, Admin):
            admin = AdminView(self.root, user)
            self.clear()
            admin.create_widgets()
        # check if user is of type tollOperator
        elif isinstance(user, TollOperator):
            toll_operator_view = TollOperatorView(self.root, user, self.username_entry.get())
            self.clear()
            toll_operator_view.create_widgets()
        else:
            print('Invalid username or password')
    def close(self):
        self.root.quit()