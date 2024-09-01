# this is the admin view class
# it handles the admin view
# we will be using tkinter for the view
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from view.vehicle import VehicleView
from view.tollOperator import TollOperatorView
from view.tollBooth import TollBoothView
from view.paymentAnalytics import PaymentAnalytics
from model.admin import Admin
from control.maincontrol import MainControl
from control.concreteAddStrategy import AddAdminStrategy
from control.concreteRemoveStrategy import RemoveAdminStrategy
from control.concreteGetAllStrategy import GetAllAdminStrategy


class AdminView:
    def __init__(self, root, user):
        self.user = user
        self.root = root
        self.root.title('Admin')
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        # this is the vehicle view object, we will use it to add and list vehicles, toll operators and booths
        self.vehicle = None
        self.tollOperator = None
        self.tollBooth = None
        self.root.geometry('1280x720')

    def create_widgets(self):
        # we will have a menu bar with the following options
        # 1. Admin (add, delete, find)
        # 2. Tolloperator (add, delete, find)
        # 3. Tollbooth (add, delete, find)
        # 4. Vehicle (add, delete, find)
        # 5. TollPayment (add, delete, find)
        menubar = Menu(self.root)
        adminmenu = Menu(menubar, tearoff=0)
        adminmenu.add_command(label="Add", command=self.add_admin)
        adminmenu.add_command(label="List", command=self.list_admin)
        menubar.add_cascade(label="Admin", menu=adminmenu)

        toperatormenu = Menu(menubar, tearoff=0)
        toperatormenu.add_command(label="Add", command=self.add_tollOperator)
        toperatormenu.add_command(label="List", command=self.list_tollOperator)
        menubar.add_cascade(label="Toll Operator", menu=toperatormenu)

        tollboothmenu = Menu(menubar, tearoff=0)
        tollboothmenu.add_command(label="Add", command=self.add_tollBooth)
        tollboothmenu.add_command(label="List", command=self.list_tollBooth)
        menubar.add_cascade(label="Toll Booth", menu=tollboothmenu)

        vehiclemenu = Menu(menubar, tearoff=0)
        vehiclemenu.add_command(label="Add", command=self.add_vehicle)
        vehiclemenu.add_command(label="List", command=self.list_vehicle)
        menubar.add_cascade(label="Vehicle", menu=vehiclemenu)

        tollPaymentmenu = Menu(menubar, tearoff=0)
        tollPaymentmenu.add_command(label="Analyse", command=self.paymentAnalytics)
        menubar.add_cascade(label="Toll Payment", menu=tollPaymentmenu)
        menubar.add_command(label="Exit", command=self.close) 
        
        self.root.config(menu=menubar)
    def add_admin(self):
        self.clear()
        # we need to check te admin permission, if it is 0
        # we will not allow the admin to add another admin
        if self.user.permission == 0:
            return
        # otherwise we will allow the admin to add another admin 
        popup = tk.Toplevel(self.root)
        popup.title("Add Admin")
        popup.geometry('300x400')
        popup.configure(bg='light blue')

        id_frame = tk.Frame(popup)
        id_frame.pack(anchor='w', expand=True)
        tk.Label(id_frame, text="Admin ID", width=12, bg='light blue').pack(side='left')
        self.id_entry = tk.Entry(id_frame, width=25)
        self.id_entry.pack(side='left')
        
        name_frame = tk.Frame(popup)
        name_frame.pack(anchor='w', expand=True)
        tk.Label(name_frame, text="Name", width=12, bg='light blue').pack(side='left')
        self.name_entry = tk.Entry(name_frame, width=25)
        self.name_entry.pack(side='left')

        password_frame = tk.Frame(popup)
        password_frame.pack(anchor='w', expand=True)
        tk.Label(password_frame, text="Password", width=12, bg='light blue').pack(side='left')
        self.password_entry = tk.Entry(password_frame, show="*", width=25)
        self.password_entry.pack(side='left')

        email_frame = tk.Frame(popup)
        email_frame.pack(anchor='w', expand=True)
        tk.Label(email_frame, text="Email", width=12, bg='light blue').pack(side='left')
        self.email_entry = tk.Entry(email_frame, width=25)
        self.email_entry.pack(side='left')

        permission_frame = tk.Frame(popup)
        permission_frame.pack(anchor='w', expand=True)
        tk.Label(permission_frame, text="Permission", width=12, bg='light blue').pack(side='left')
        self.permission_entry = tk.Entry(permission_frame, width=25)
        self.permission_entry.insert(0, "0")
        self.permission_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)

        # so that we don't have to change popup to self.popup in the code above I'm tieing it to self
        self.popup = popup

        tk.Button(button_frame, text="Submit", command=self.submit_admin).pack(side='left')
        tk.Button(button_frame, text="Cancel", command=self.popup.destroy).pack(side='left')


    def submit_admin(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        permission = int(self.permission_entry.get())
        new_admin = Admin(id, name, password, email, permission)
        # MainControl.add_admin(new_admin)
        add_admin_strategy = AddAdminStrategy()
        MainControl.add_entity(add_admin_strategy, new_admin)
        self.popup.destroy()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()

    def list_admin(self):
        # check if the user has permission to list admins
        if self.user.permission == 0:
            return
        self.clear()
        # get all the admins
        # admins = MainControl.get_all_admins()
        get_all_admins_strategy = GetAllAdminStrategy()
        admins = MainControl.get_all(get_all_admins_strategy)
        print(admins)
        # making every grid have a minimum size
        self.root.grid_rowconfigure(0, minsize=100)
        self.root.grid_columnconfigure(0, minsize=100)
        # table label
        table_label = Label(self.root)
        # creating tree
        tree = ttk.Treeview(table_label)
        # defining columns
        tree["columns"] = ("Name", "Email", "Permission")
        # format columns
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Name", anchor=tk.W, width=200)
        tree.column("Email", anchor=tk.CENTER, width=200)
        tree.column("Permission", anchor=tk.CENTER, width=80)
        # creaing headings
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Name", text="Name", anchor=tk.CENTER)
        tree.heading("Email", text="Email", anchor=tk.CENTER)
        tree.heading("Permission", text="Permission", anchor=tk.CENTER)
        # adding the fake data
        for i, admin in enumerate(admins):
            tree.insert(parent="", index=tk.END, iid=i, text="", values=(admin.name, admin.email, admin.permission))
        # placing tree
        tree.pack()
        # placing the table label
        table_label.grid(row=1, column=1, rowspan=4, columnspan=4, padx=10, pady=10)
        # label for search bar
        search_label = Label(self.root)
        # placing search label
        search_label.grid(row=1, column=7, padx=10, sticky='s', columnspan=2)
        name_label = Label(search_label, text="Name").grid(row=0, column=0)
        # entry boxes for search bar
        self.name_entry = Entry(search_label, width=30)
        self.name_entry.grid(row=1, column=0)
        # creating an empty label to create space
        empty_label = Label(self.root, width=40, bg='light blue')
        empty_label.grid(row=1, column=6)

        # creating buttons
        button_search = Button(self.root, text="Search", command=self.find_admin)
        button_search.grid(row=2, column=7, padx=10)
        button_refresh = Button(self.root, text="Refresh", command=self.refresh_table)
        button_refresh.grid(row=2, column=8, padx=10)
        # label for remove buttons
        remove_label = Label(self.root, bg='light blue')
        button_remove_one = Button(remove_label, text="Remove One", command=self.remove_one)
        button_remove_one.pack(side='left', padx=10)
        button_remove_many = Button(remove_label, text="Remove Many", command=self.remove_many)
        button_remove_many.pack(side='left', padx=10)
        remove_label.grid(row=6, column=2, padx=10)

        self.tree = tree
    def remove_one(self):
        # get the selected item
        selected_item = self.tree.selection()[0]
        # get the admin from the selected item
        print(selected_item)
        admin = MainControl.find_admin(self.tree.item(selected_item)['values'][1])
        # remove the admin
        # MainControl.remove_admin(admin)
        remove_admin_strategy = RemoveAdminStrategy()
        print(admin)
        MainControl.remove_entity(remove_admin_strategy, admin)
        # remove the selected item from the tree
        self.tree.delete(selected_item)
    def remove_many(self):
        # get the selected items
        selected_items = self.tree.selection()
        # remove the admins
        for item in selected_items:
            admin = MainControl.find_admin(self.tree.item(item)['values'][1])
            # MainControl.remove_admin(admin)
            remove_admin_strategy = RemoveAdminStrategy()
            MainControl.remove_entity(remove_admin_strategy, admin)
            self.tree.delete(item)
    def find_admin(self):
        # find admin by name and add it to the tree
        # first get the name from the entry box
        name = self.name_entry.get()
        # find the admin, it might return None if the admin is not found
        # or a list of admins if there are multiple admins with the same name
        # or a list with one admin if there is only one admin with that name
        admin = MainControl.find_admin_by_name(name)
        # remove all the items from the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        # insert the new admins
        for i, adm in enumerate(admin):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(adm.name, adm.email, adm.permission))

    def add_tollOperator(self):
        self.clear()
        if self.tollOperator is None:
            self.tollOperator = TollOperatorView(self.root, user = None, email = None)
        self.tollOperator.add_tollOperator()
    
    def list_tollOperator(self):
        # create a toll operator view object if it does not exist
        self.clear()
        if self.tollOperator is None:
            self.tollOperator = TollOperatorView(self.root, user=None, email = None)
        self.tollOperator.list_tollOperator()

    def add_vehicle(self): 
        self.clear()
        if self.vehicle is None:
            self.vehicle = VehicleView(self.root)
        self.vehicle.add_vehicle()

    def list_vehicle(self):
        # create a vehicle view object if it does not exist
        self.clear()
        if self.vehicle is None:
            self.vehicle = VehicleView(self.root)
        self.vehicle.list_vehicle()

    def add_tollBooth(self): 
        self.clear()
        if self.tollBooth is None:
            self.tollBooth = TollBoothView(self.root)
        self.tollBooth.add_tollBooth()

    def list_tollBooth(self):
        # create a toll booth view object if it does not exist
        self.clear()
        if self.tollBooth is None:
            self.tollBooth = TollBoothView(self.root)
        self.tollBooth.list_tollBooth()
    
    def refresh_table(self):
        # admins = MainControl.get_all_admins()
        get_all_admins_strategy = GetAllAdminStrategy()
        admins = MainControl.get_all(get_all_admins_strategy)
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, admin in enumerate(admins):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(admin.name, admin.email, admin.permission))

    def paymentAnalytics(self):
        self.clear()
        payment_analytics = PaymentAnalytics(self.root)
        payment_analytics.analytics()

    def donothing(self):
        pass
    def close(self):
        self.root.quit()