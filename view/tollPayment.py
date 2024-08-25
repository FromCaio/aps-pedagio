import tkinter as tk
from datetime import datetime
from control.maincontrol import MainControl
from model.tollPayment import TollPayment
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk

class TollPaymentView:
    def __init__(self, root, email):
        self.root = root
        self.emailOperator = email

    def add_transaction(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Transaction")
        popup.geometry('350x500')
        popup.configure(bg='light blue')

        transactionid_frame = tk.Frame(popup)
        transactionid_frame.pack(anchor='w', expand=True)
        tk.Label(transactionid_frame, text="Transaction ID", width=15, bg='light blue').pack(side='left')
        self.transactionid_entry = tk.Entry(transactionid_frame, width=25)
        self.transactionid_entry.pack(side='left')

        plate_frame = tk.Frame(popup)
        plate_frame.pack(anchor='w', expand=True)
        tk.Label(plate_frame, text="Vehicle Plate", width=15, bg='light blue').pack(side='left')
        self.plate_entry = tk.Entry(plate_frame, width=25)
        self.plate_entry.pack(side='left')

        operator_frame = tk.Frame(popup)
        operator_frame.pack(anchor='w', expand=True)
        tk.Label(operator_frame, text="Operator Email", width=15, bg='light blue').pack(side='left')
        self.operator_entry = tk.Entry(operator_frame, width=25)
        self.operator_entry.pack(side='left')
        self.operator_entry.insert(0, self.emailOperator)  # Pré-insere o e-mail do operador

        tollbooth_frame = tk.Frame(popup)
        tollbooth_frame.pack(anchor='w', expand=True)
        tk.Label(tollbooth_frame, text="Tollbooth ID", width=15, bg='light blue').pack(side='left')
        self.tollbooth_entry = tk.Entry(tollbooth_frame, width=25)
        self.tollbooth_entry.pack(side='left')

        # Campo de Data e Hora preenchido automaticamente com o horário atual
        datetime_frame = tk.Frame(popup)
        datetime_frame.pack(anchor='w', expand=True)
        tk.Label(datetime_frame, text="Date and Time", width=15, bg='light blue').pack(side='left')
        
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_entry = tk.Entry(datetime_frame, width=25)
        self.datetime_entry.insert(0, current_datetime)
        self.datetime_entry.pack(side='left')

        amount_frame = tk.Frame(popup)
        amount_frame.pack(anchor='w', expand=True)
        tk.Label(amount_frame, text="Amount Paid", width=15, bg='light blue').pack(side='left')
        self.amount_entry = tk.Entry(amount_frame, width=25)
        self.amount_entry.pack(side='left')

        payment_frame = tk.Frame(popup)
        payment_frame.pack(anchor='w', expand=True)
        tk.Label(payment_frame, text="Payment Method", width=15, bg='light blue').pack(side='left')
        self.payment_entry = tk.Entry(payment_frame, width=25)
        self.payment_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit", command=self.submit_transaction).pack(side='left')
        tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side='left')

        self.popup = popup

    def submit_transaction(self):
        transactionid = self.transactionid_entry.get()
        plate = self.plate_entry.get()
        operator_email = self.operator_entry.get()
        tollbooth_id = self.tollbooth_entry.get()
        datetime = self.datetime_entry.get()
        amount = self.amount_entry.get()
        payment_method = self.payment_entry.get()

        vehicle = MainControl.find_vehicle(plate)
        operator = MainControl.find_tollOperator(operator_email)
        tollbooth = MainControl.find_tollBooth(tollbooth_id)

        if vehicle and operator and tollbooth:
            new_transaction = TollPayment(transactionid, vehicle, tollbooth, operator, amount, payment_method, datetime)
            MainControl.add_transaction(new_transaction)
            self.popup.destroy()
        else:
            error_label = tk.Label(self.popup, text="Invalid data. Please check your inputs.", fg='red', bg='light blue')
            error_label.pack()

    def list_transactions(self):
        transactions = MainControl.get_all_transactions()
        self.root.grid_rowconfigure(0, minsize=100)
        self.root.grid_columnconfigure(0, minsize=100)
        table_label = Label(self.root)
        tree = ttk.Treeview(table_label)
        tree["columns"] = ("Vehicle Plate", "Operator Email", "Booth ID", "Date and Time", "Amount", "Method")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Vehicle Plate", anchor=tk.W, width=120)
        tree.column("Operator Email", anchor=tk.CENTER, width=200)
        tree.column("Booth ID", anchor=tk.CENTER, width=100)
        tree.column("Date and Time", anchor=tk.CENTER, width=150)
        tree.column("Amount", anchor=tk.CENTER, width=100)
        tree.column("Method", anchor=tk.CENTER, width=150)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Vehicle Plate", text="Vehicle Plate", anchor=tk.CENTER)
        tree.heading("Operator Email", text="Operator Email", anchor=tk.CENTER)
        tree.heading("Booth ID", text="Booth ID", anchor=tk.CENTER)
        tree.heading("Date and Time", text="Date and Time", anchor=tk.CENTER)
        tree.heading("Amount", text="Amount", anchor=tk.CENTER)
        tree.heading("Method", text="Method", anchor=tk.CENTER)
        for i, transaction in enumerate(transactions):
            tree.insert(parent="", index=tk.END, iid=i, text="", values=(
                transaction.vehicle.plate, 
                transaction.operator.email, 
                transaction.tollbooth.boothid, 
                transaction.date,
                transaction.amount,
                transaction.method))
        tree.pack()
        table_label.grid(row=1, column=1, rowspan=4, columnspan=4, padx=10, pady=10)

        self.tree = tree
   
    def find_transaction_by_id(self):
        # Get the ID from the entry box
        transaction_id = self.transactionid_entry.get()

        # Find the transaction by ID, it might return None if the transaction is not found
        transaction = MainControl.find_transaction_by_id(transaction_id)

        # Remove all the items from the tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert the found transaction, if any
        if transaction:
            self.tree.insert(
                parent="",
                index=tk.END,
                iid=0,
                text="",
                values=(transaction.vehicle.plate, transaction.operator.email, transaction.tollbooth.boothid)
            )
        else:
            # If no transaction is found, display a message
            error_label = tk.Label(self.root, text="Transaction not found.", fg='red')
            error_label.grid(row=3, column=7, padx=10)


    def remove_transaction(self):
        selected_item = self.tree.selection()[0]
        transaction = MainControl.find_transaction_by_details(self.tree.item(selected_item)['values'])
        #MainControl.remove_tollPayment(transaction)
        self.tree.delete(selected_item)

