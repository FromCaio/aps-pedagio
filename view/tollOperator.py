# this is the toll operatort view class
# it handles the admin view
# we will be using tkinter for the view
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from model.tollOperator import TollOperator
from control.maincontrol import MainControl
from view.vehicle import VehicleView
from view.tollPayment import TollPaymentView


class TollOperatorView:
    def __init__(self, root, user):
        self.user = user
        self.root = root
        self.root.title('toll Operator')
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        # this is the tollOperator view object, we will use it to add and list tollOperators
        self.tollOperator = None
        self.root.geometry('1280x720')
        self.vehicle = None
        self.tollPayment = None

    def create_widgets(self):
        # we will have a menu bar with the following options
        # 1. tollOperator (add, delete, find)
        # 2. Transaction (add, delete, find)
        menubar = Menu(self.root)

        vehiclemenu = Menu(menubar, tearoff=0)
        vehiclemenu.add_command(label="Add", command=self.add_vehicle)
        vehiclemenu.add_command(label="List", command=self.list_vehicle)
        menubar.add_cascade(label="Vehicle", menu=vehiclemenu)

        transactionmenu = Menu(menubar, tearoff=0)
        transactionmenu.add_command(label="Add", command=self.add_tollPayment)
        transactionmenu.add_command(label="List", command=self.list_tollPayment)
        menubar.add_cascade(label="Transaction", menu=transactionmenu)
        menubar.add_command(label="Exit", command=self.close) 
        self.root.config(menu=menubar)
    
    def add_tollOperator(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Toll Operator")
        popup.geometry('300x400')
        popup.configure(bg='light blue')

        operatorid_frame = tk.Frame(popup)
        operatorid_frame.pack(anchor='w', expand=True)
        tk.Label(operatorid_frame, text="Operator ID", width=12, bg='light blue').pack(side='left')
        self.operatorid_entry = tk.Entry(operatorid_frame, width=25)
        self.operatorid_entry.pack(side='left')

        name_frame = tk.Frame(popup)
        name_frame.pack(anchor='w', expand=True)
        tk.Label(name_frame, text="Name", width=12, bg='light blue').pack(side='left')
        self.name_entry = tk.Entry(name_frame, width=25)
        self.name_entry.pack(side='left')

        email_frame = tk.Frame(popup)
        email_frame.pack(anchor='w', expand=True)
        tk.Label(email_frame, text="Email", width=12, bg='light blue').pack(side='left')
        self.email_entry = tk.Entry(email_frame, width=25)
        self.email_entry.pack(side='left')

        password_frame = tk.Frame(popup)
        password_frame.pack(anchor='w', expand=True)
        tk.Label(password_frame, text="Password", width=12, bg='light blue').pack(side='left')
        self.password_entry = tk.Entry(password_frame, show="*", width=25)
        self.password_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit", command=self.submit_tollOperator).pack(side='left')
        self.popup = popup
        tk.Button(button_frame, text="Cancel", command=self.popup.destroy).pack(side='left')

    
    def submit_tollOperator(self):
        operatorid = self.operatorid_entry.get()
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        new_operator = TollOperator(operatorid, name, email, password)
        MainControl.add_tollOperator(new_operator)
        self.popup.destroy()
        
    def list_tollOperator(self):
        tollOperators = MainControl.get_all_tollOperators()
        self.root.grid_rowconfigure(0, minsize=100)
        self.root.grid_columnconfigure(0, minsize=100)
        table_label = Label(self.root)
        tree = ttk.Treeview(table_label)
        tree["columns"] = ("OperatorID", "Name", "Email", "Password")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("OperatorID", anchor=tk.W, width=120)
        tree.column("Name", anchor=tk.CENTER, width=150)
        tree.column("Email", anchor=tk.CENTER, width=200)
        tree.column("Password", anchor=tk.CENTER, width=100)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("OperatorID", text="Operator ID", anchor=tk.CENTER)
        tree.heading("Name", text="Name", anchor=tk.CENTER)
        tree.heading("Email", text="Email", anchor=tk.CENTER)
        tree.heading("Password", text="Password", anchor=tk.CENTER)
        for i, toll_op in enumerate(tollOperators):
            tree.insert(parent="", index=tk.END, iid=i, text="", values=(toll_op.operatorid, toll_op.name, toll_op.email, toll_op.password))
        tree.pack()
        table_label.grid(row=1, column=1, rowspan=4, columnspan=4, padx=10, pady=10)
        self.search_label = Label(self.root)
        self.search_label.grid(row=1, column=7, padx=10, sticky='s', columnspan=2)
        email_label = Label(self.search_label, text="Email").grid(row=0, column=0)
        self.email_entry = Entry(self.search_label, width=30)
        self.email_entry.grid(row=1, column=0)
        empty_label = Label(self.root, width=30, bg='light blue')
        empty_label.grid(row=1, column=6)
        button_search = Button(self.root, text="Search", command=self.find_tollOperator)
        button_search.grid(row=2, column=7, padx=10)
        button_refresh = Button(self.root, text="Refresh", command=self.refresh_table)
        button_refresh.grid(row=2, column=8, padx=10)
        remove_label = Label(self.root, bg='light blue')
        button_remove_one = Button(remove_label, text="Remove One", command=self.remove_one)
        button_remove_one.pack(side='left', padx=10)
        button_remove_many = Button(remove_label, text="Remove Many", command=self.remove_many)
        button_remove_many.pack(side='left', padx=10)
        remove_label.grid(row=6, column=2, padx=10)
        self.tree = tree
    
    def refresh_table(self):
        tollOperators = MainControl.get_all_tollOperators()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, toll_op in enumerate(tollOperators):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(toll_op.operatorid, toll_op.name, toll_op.email, toll_op.password)) 
            
    def find_tollOperator(self):
        # find tollOperator by model and add it to the tree
        # first get the model from the entry box
        email = self.email_entry.get()
        # find the tollOperator, it might return None if the tollOperator is not found
        # or a list of tollOperators if there are multiple tollOperators with the same model
        # or a list with one tollOperator if there is only one tollOperator with that model
        operator = MainControl.find_tollOperator(email)
        # remove all the items from the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        # insert the new tollOperators
        self.tree.insert(parent="", index=tk.END, text="", values=(operator.operatorid, operator.name, operator.email, operator.password))
    
    def remove_one(self):
        # get the selected item
        selected_item = self.tree.selection()[0]
        # get the toll operator from the selected item
        tollOperator = MainControl.find_tollOperator(self.tree.item(selected_item)['values'][2])

        # remove the toll operator
        MainControl.remove_tollOperator(tollOperator)
        # remove the selected item from the tree
        self.tree.delete(selected_item)

    def remove_many(self):
        # get the selected items
        selected_items = self.tree.selection()
        # remove the toll operators
        for item in selected_items:
            tollOperator = MainControl.find_tollOperator(self.tree.item(item)['values'][2])
            MainControl.remove_tollOperator(tollOperator)
            self.tree.delete(item)
    
    # the clear method will clear the root window
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()

    def donothing(self):
        pass
    def close(self):
        MainControl.close_data_manager()
        self.root.quit()

    def list_vehicle(self):
        # create a vehicle view object if it does not exist
        self.clear()
        if self.vehicle is None:
            self.vehicle = VehicleView(self.root)
        self.vehicle.list_vehicle()

    def add_vehicle(self): 
        self.clear()
        if self.vehicle is None:
            self.vehicle = VehicleView(self.root)
        self.vehicle.add_vehicle()

    def list_tollPayment(self):
        # create a vehicle view object if it does not exist
        self.clear()
        if self.tollPayment is None:
            self.tollPayment = TollPaymentView(self.root)
        self.tollPayment.list_transactions()

    def add_tollPayment(self): 
        self.clear()
        if self.tollPayment is None:
            self.tollPayment = TollPaymentView(self.root)
        self.tollPayment.add_transaction()