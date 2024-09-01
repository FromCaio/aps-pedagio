import tkinter as tk
from control.maincontrol import MainControl
from model.vehicle import Vehicle
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from control.concreteAddStrategy import AddVehicleStrategy
from control.concreteRemoveStrategy import RemoveVehicleStrategy
from control.concreteGetAllStrategy import GetAllVehicleStrategy

class VehicleView:
    def __init__(self, root):
        self.root = root
    def add_vehicle(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Vehicle")
        popup.geometry('300x400')
        popup.configure(bg='light blue')

        plate_frame = tk.Frame(popup)
        plate_frame.pack(anchor='w', expand=True)
        tk.Label(plate_frame, text="Plate", width=12, bg='light blue').pack(side='left')
        self.plate_entry = tk.Entry(plate_frame, width=25)
        self.plate_entry.pack(side='left')

        model_frame = tk.Frame(popup)
        model_frame.pack(anchor='w', expand=True)
        tk.Label(model_frame, text="Model", width=12, bg='light blue').pack(side='left')
        self.model_entry = tk.Entry(model_frame, width=25)
        self.model_entry.pack(side='left')

        color_frame = tk.Frame(popup)
        color_frame.pack(anchor='w', expand=True)
        tk.Label(color_frame, text="Color", width=12, bg='light blue').pack(side='left')
        self.color_entry = tk.Entry(color_frame, width=25)
        self.color_entry.pack(side='left')

        status_frame = tk.Frame(popup)
        status_frame.pack(anchor='w', expand=True)
        tk.Label(status_frame, text="Status", width=12, bg='light blue').pack(side='left')
        self.status_entry = tk.Entry(status_frame, width=25)
        self.status_entry.insert(0, "licensed")
        self.status_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit", command=self.submit_vehicle).pack(side='left')
        tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side='left')

        self.popup = popup
    def submit_vehicle(self):
        plate = self.plate_entry.get()
        model = self.model_entry.get()
        color = self.color_entry.get()
        status = self.status_entry.get()
        new_vehicle = Vehicle(plate, model, color, status)
        # MainControl.add_vehicle(new_vehicle)
        add_strategy = AddVehicleStrategy()
        MainControl.add_entity(add_strategy, new_vehicle)
        self.popup.destroy()
    def list_vehicle(self):
        # vehicles = MainControl.get_all_vehicles()
        get_all_strategy = GetAllVehicleStrategy()
        vehicles = MainControl.get_all(get_all_strategy)
        self.root.grid_rowconfigure(0, minsize=100)
        self.root.grid_columnconfigure(0, minsize=100)
        table_label = Label(self.root)
        tree = ttk.Treeview(table_label)
        tree["columns"] = ("Plate", "Model", "Color", "Status")
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Plate", anchor=tk.W, width=200)
        tree.column("Model", anchor=tk.CENTER, width=200)
        tree.column("Color", anchor=tk.CENTER, width=80)
        tree.column("Status", anchor=tk.CENTER, width=80)
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Plate", text="Plate", anchor=tk.CENTER)
        tree.heading("Model", text="Model", anchor=tk.CENTER)
        tree.heading("Color", text="Color", anchor=tk.CENTER)
        tree.heading("Status", text="Status", anchor=tk.CENTER)
        for i, vehicle in enumerate(vehicles):
            tree.insert(parent="", index=tk.END, iid=i, text="", values=(vehicle.plate, vehicle.model, vehicle.color, vehicle.status))
        tree.pack()
        table_label.grid(row=1, column=1, rowspan=4, columnspan=4, padx=10, pady=10)
        self.search_label = Label(self.root)
        self.search_label.grid(row=1, column=7, padx=10, sticky='s', columnspan=2)
        plate_label = Label(self.search_label, text="Model").grid(row=0, column=0)
        self.model_entry = Entry(self.search_label, width=30)
        self.model_entry.grid(row=1, column=0)
        empty_label = Label(self.root, width=30, bg='light blue')
        empty_label.grid(row=1, column=6)
        button_search = Button(self.root, text="Search", command=self.find_vehicle_by_model)
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
        # get the vehicle from the selected item
        vehicle = MainControl.find_vehicle(self.tree.item(selected_item)['values'][0])
        # remove the vehicle
        # MainControl.remove_vehicle(vehicle)
        remove_strategy = RemoveVehicleStrategy()
        MainControl.remove_entity(remove_strategy, vehicle)
        # remove the selected item from the tree
        self.tree.delete(selected_item)

    def remove_many(self):
        # get the selected items
        selected_items = self.tree.selection()
        # remove the vehicles
        for item in selected_items:
            vehicle = MainControl.find_vehicle(self.tree.item(item)['values'][0])
            # MainControl.remove_vehicle(vehicle)
            remove_strategy = RemoveVehicleStrategy()
            MainControl.remove_entity(remove_strategy, vehicle)
            self.tree.delete(item)
    
    def find_vehicle_by_model(self):
        # find vehicle by model and add it to the tree
        # first get the model from the entry box
        model = self.model_entry.get()
        # find the vehicle, it might return None if the vehicle is not found
        # or a list of vehicles if there are multiple vehicles with the same model
        # or a list with one vehicle if there is only one vehicle with that model
        vehicles = MainControl.find_vehicle_by_model(model)
        # remove all the items from the tree
        for item in self.tree.get_children():
            self.tree.delete(item)
        # insert the new vehicles
        for i, veh in enumerate(vehicles):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(veh.plate, veh.model, veh.color, veh.status))
    def refresh_table(self):
        # vehicles = MainControl.get_all_vehicles()
        get_all_strategy = GetAllVehicleStrategy()
        vehicles = MainControl.get_all(get_all_strategy)
        for item in self.tree.get_children():
            self.tree.delete(item)
        for i, vehicle in enumerate(vehicles):
            self.tree.insert(parent="", index=tk.END, iid=i, text="", values=(vehicle.plate, vehicle.model, vehicle.color, vehicle.status))