import tkinter as tk
from control.maincontrol import MainControl
from model.tollBooth import TollBooth
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from control.concreteAddStrategy import AddTollBoothStrategy
from control.concreteRemoveStrategy import RemoveTollBoothStrategy
from control.concreteGetAllStrategy import GetAllTollBoothStrategy

class TollBoothView:
    def __init__(self, root):
        self.root = root
    def add_tollBooth(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Toll Booth")
        popup.geometry('300x400')
        popup.configure(bg='light blue')

        boothid_frame = tk.Frame(popup)
        boothid_frame.pack(anchor='w', expand=True)
        tk.Label(boothid_frame, text="Booth ID", width=12, bg='light blue').pack(side='left')
        self.boothid_entry = tk.Entry(boothid_frame, width=25)
        self.boothid_entry.pack(side='left')

        highway_frame = tk.Frame(popup)
        highway_frame.pack(anchor='w', expand=True)
        tk.Label(highway_frame, text="Highway", width=12, bg='light blue').pack(side='left')
        self.highway_entry = tk.Entry(highway_frame, width=25)
        self.highway_entry.pack(side='left')

        status_frame = tk.Frame(popup)
        status_frame.pack(anchor='w', expand=True)
        tk.Label(status_frame, text="Status", width=12, bg='light blue').pack(side='left')
        self.status_entry = tk.Entry(status_frame, width=25)
        self.status_entry.insert(0, "open")
        self.status_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit", command=self.submit_tollBooth).pack(side='left')
        tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side='left')

        self.popup = popup
    
    def submit_tollBooth(self):
        boothid = self.boothid_entry.get()
        highway = self.highway_entry.get()
        status = self.status_entry.get()
        new_tollbooth = TollBooth(boothid, highway, status)
        # MainControl.add_tollBooth(new_tollbooth)
        add_strategy = AddTollBoothStrategy()
        MainControl.add_entity(add_strategy, new_tollbooth)
        self.popup.destroy()

    def list_tollBooth(self):
        # tollBooths = MainControl.get_all_tollBooths()
        get_all_strategy = GetAllTollBoothStrategy()
        tollBooths = MainControl.get_all(get_all_strategy)
        self.root.grid_rowconfigure(0, minsize=100)
        self.root.grid_columnconfigure(0, minsize=100)
        table_label = Label(self.root)
        tree = ttk.Treeview(table_label)
        tree["columns"] = ("BoothID", "Highway", "Status")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("BoothID", anchor=tk.W, width=200)
        tree.column("Highway", anchor=tk.CENTER, width=200)
        tree.column("Status", anchor=tk.CENTER, width=80)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("BoothID", text="Booth ID", anchor=tk.CENTER)
        tree.heading("Highway", text="Highway", anchor=tk.CENTER)
        tree.heading("Status", text="Status", anchor=tk.CENTER)
        for i, tollBooth in enumerate(tollBooths):
            tree.insert(parent="", index=tk.END, iid=i, text="", values=(tollBooth.boothid, tollBooth.highway, tollBooth.status))
        tree.pack()
        table_label.grid(row=1, column=1, rowspan=4, columnspan=4, padx=10, pady=10)
        self.search_label = Label(self.root)
        self.search_label.grid(row=1, column=7, padx=10, sticky='s', columnspan=2)
        boothid_label = Label(self.search_label, text="highway").grid(row=0, column=0)
        self.highway_entry = Entry(self.search_label, width=30)
        self.highway_entry.grid(row=1, column=0)
        empty_label = Label(self.root, width=30, bg='light blue')
        empty_label.grid(row=1, column=6)
        button_search = Button(self.root, text="Search", command=self.find_booth_by_highway)
        button_search.grid(row=2, column=7, padx=10)
        button_refresh = Button(self.root, text="Refresh", command=self.refresh_table)
        button_refresh.grid(row=2, column=8, padx=10)
        remove_label = Label(self.root, bg='light blue')
        button_remove_one = Button(remove_label, text="Remove One", command=self.remove_one)
        button_remove_one.pack(side='left', padx=10)
        button_remove_many = Button(remove_label, text="Remove Many", command=self.remove_many)
        button_remove_many.pack(side='left', padx=10)
        remove_label.grid(row=6, column=2, padx=10, columnspan=2)

        self.tree = tree
    def remove_one(self):
        # get the selected item
        selected_item = self.tree.selection()[0]
        # get the toll both from the selected item
        tollBooth = MainControl.find_tollBooth(self.tree.item(selected_item)['values'][0])
        print(tollBooth)
        # remove the toll both
        # MainControl.remove_tollBooth(tollBooth)
        remove_strategy = RemoveTollBoothStrategy()
        MainControl.remove_entity(remove_strategy, tollBooth)
        # remove the selected item from the tree
        self.tree.delete(selected_item)

    def remove_many(self):
        # get the selected items
        selected_items = self.tree.selection()
        # remove the toll boths
        for item in selected_items:
            tollBooth = MainControl.find_tollBooth(self.tree.item(item)['values'][0])
            # MainControl.remove_tollBooth(tollBooth)
            remove_strategy = RemoveTollBoothStrategy()
            MainControl.remove_entity(remove_strategy, tollBooth)
            self.tree.delete(item)
    
    def find_booth_by_highway(self):
        # find toll both by highway and add it to the tree
        # first get the highway from the entry box
        highway = self.highway_entry.get()
        # find the toll both, it might return None if the tollBooth is not found
        # or a list of toll boths if there are multiple tollBooths with the same highway
        # or a list with one toll both if there is only one tollBooth with that highway
        tollBooths = MainControl.find_booth_by_highway(highway)
        # remove all the items from the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        # insert the new toll boths
        for i, booth in enumerate(tollBooths):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(booth.boothid, booth.highway, booth.status))
    def refresh_table(self):
        # tollBooths = MainControl.get_all_tollBooths()
        get_all_strategy = GetAllTollBoothStrategy()
        tollBooths = MainControl.get_all(get_all_strategy)
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, booth in enumerate(tollBooths):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(booth.boothid, booth.highway, booth.status))