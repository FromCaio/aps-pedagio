import tkinter as tk
from datetime import datetime
from control.maincontrol import MainControl
from model.tollPayment import TollPayment
from tkinter import Menu
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

        # Geração da data e hora no formato correto
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("Data gerada:", current_datetime)  # Para verificar a saída no console

        self.datetime_entry = tk.Entry(datetime_frame, width=25)
        self.datetime_entry.insert(0, current_datetime)
        self.datetime_entry.pack(side='left')

        amount_frame = tk.Frame(popup)
        amount_frame.pack(anchor='w', expand=True)
        tk.Label(amount_frame, text="Amount Paid", width=15, bg='light blue').pack(side='left')
        self.amount_entry = tk.Entry(amount_frame, width=25)
        self.amount_entry.pack(side='left')
        self.amount_entry.insert(0, 6.45)  # Pré-insere o valor do pedagio

        payment_frame = tk.Frame(popup)
        payment_frame.pack(anchor='w', expand=True)
        tk.Label(payment_frame, text="Payment Method", width=15, bg='light blue').pack(side='left')
        # Criação do dropdown para os métodos de pagamento
        self.payment_entry = ttk.Combobox(payment_frame, width=25)
        self.payment_entry['values'] = ('Money', 'Debit Card', 'Credit Card', 'Pix')  # Adiciona as opções
        self.payment_entry.set('Select Payment Method')  # Define um texto padrão
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
            error_label = tk.Label(self.popup, text="Invalid vehicle, operator or toll booth. Please check your inputs.", fg='red', bg='light blue')
            error_label.pack()
    
    def list_transactions(self):
        transactions = MainControl.get_all_transactions()  # Obtendo as transações
        self.root.grid_rowconfigure(0, minsize=100)
        self.root.grid_columnconfigure(0, minsize=100)
        table_label = Label(self.root)
        tree = ttk.Treeview(table_label)
        tree["columns"] = ("ID", "Vehicle Plate", "Operator Email", "Amount", "Date", "Method")  # Adicionando os novos atributos
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("ID", anchor=tk.CENTER, width=80)
        tree.column("Vehicle Plate", anchor=tk.CENTER, width=150)
        tree.column("Operator Email", anchor=tk.CENTER, width=200)
        tree.column("Amount", anchor=tk.CENTER, width=100)
        tree.column("Date", anchor=tk.CENTER, width=150)  # Coluna para Data
        tree.column("Method", anchor=tk.CENTER, width=100)  # Coluna para Método
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("ID", text="ID", anchor=tk.CENTER) 
        tree.heading("Vehicle Plate", text="Vehicle Plate", anchor=tk.CENTER)  # Alterado para "Vehicle Plate"
        tree.heading("Operator Email", text="Operator Email", anchor=tk.CENTER)  # Alterado para "Operator Email"
        tree.heading("Amount", text="Amount", anchor=tk.CENTER)  # Alterado para "Amount"
        tree.heading("Date", text="Date", anchor=tk.CENTER)  # Alterado para "Date"
        tree.heading("Method", text="Method", anchor=tk.CENTER)  # Alterado para "Method"

        for i, transaction in enumerate(transactions):
            tree.insert(parent="", index=tk.END, iid=i, text="", values=(
                transaction.transactionid,  # ID da transação
                transaction.vehicle.plate, 
                transaction.operator.email, 
                transaction.amount,
                transaction.date,  # Data da transação
                transaction.method))  # Método de pagamento

        tree.pack()
        table_label.grid(row=1, column=1, rowspan=4, columnspan=4, padx=3, pady=10)

        self.search_label = Label(self.root)
        self.search_label.grid(row=1, column=7, padx=7, sticky='s', columnspan=2)  
        email_label = Label(self.search_label, text="Payment ID").grid(row=0, column=0)
        self.transactionid_entry = Entry(self.search_label, width=25)  # Ajustando a largura
        self.transactionid_entry.grid(row=1, column=0)

        button_search = Button(self.root, text="Search", command=self.find_transaction_by_id)
        button_search.grid(row=2, column=7, padx=5)  
        button_refresh = Button(self.root, text="Refresh", command=self.refresh_table)
        button_refresh.grid(row=2, column=8, padx=5)  

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
        # get the transaction from the selected item
        transaction = MainControl.find_transaction_by_id(self.tree.item(selected_item)['values'][0])
        # remove the transaction
        MainControl.remove_tollPayment(transaction)
        # remove the selected item from the tree
        self.tree.delete(selected_item)

    def remove_many(self):
        # get the selected items
        selected_items = self.tree.selection()
        # remove the transactions
        for item in selected_items:
            transaction = MainControl.find_transaction_by_id(self.tree.item(item)['values'][0])
            MainControl.remove_tollPayment(transaction)
            self.tree.delete(item) 

    def refresh_table(self):
        transactions = MainControl.get_all_transactions()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, transaction in enumerate(transactions):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(transaction.transactionid, transaction.vehicle.plate, transaction.operator.email, transaction.amount, transaction.date, transaction.method))
    
    def find_transaction_by_id(self):
        # Get the ID from the entry box
        transaction_id = self.transactionid_entry.get()

        # Find the transaction by ID, it might return None if the transaction is not found
        transaction = MainControl.find_transaction_by_id(transaction_id)

        # remove all the items from the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        # insert the new tollOperators
        self.tree.insert(parent="", index=tk.END, text="", values=(transaction.transactionid, transaction.vehicle.plate, transaction.operator.email, transaction.amount, transaction.date, transaction.method))


