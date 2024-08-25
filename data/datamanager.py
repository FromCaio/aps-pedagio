import json
from model.admin import Admin
from model.vehicle import Vehicle
from model.tollOperator import TollOperator
from model.tollBooth import TollBooth
from model.tollPayment import TollPayment

# this class is responsible for managing the data
# storing it in a json file, and reading it from the same file
# we will be storing a list of admins and a list of vehicles


class DataManager:
    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            with open('data/json_files/admins.json', 'r') as f:
                self.admins = [Admin.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.admins = []
        try:
            with open('data/json_files/vehicles.json', 'r') as f:
                self.vehicles = [Vehicle.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.vehicles = [] 
        try:
            with open('data/json_files/tollOperators.json', 'r') as f:
                self.tollOperators = [TollOperator.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.tollOperators = []
        try:
            with open('data/json_files/tollBooths.json', 'r') as f:
                self.tollBooths = [TollBooth.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.tollBooths = []
        try:
            with open('data/json_files/tollPayments.json', 'r') as f:
                self.tollPayments = [TollPayment.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.tollPayments = []
    
    # methods for admin
    def insert_admin(self, admin):
        self.admins.append(admin)

    def delete_admin(self, admin):
        for adm in self.admins:
            if adm.email == admin.email:
                self.admins.remove(adm)
    def find_admin(self, email):
        for admin in self.admins:
            if admin.email == email:
                return admin

    # methods for vehicle
    def insert_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def delete_vehicle(self, vehicle):
        for veh in self.vehicles:
            if veh.plate == (str)(vehicle.plate):
                self.vehicles.remove(veh)
    def find_vehicle(self, plate):
        for vehicle in self.vehicles:
            if vehicle.plate == (str)(plate):
                return vehicle


    # methods toll operators
    def insert_tollOperator(self, tollOperator):
        self.tollOperators.append(tollOperator)
    def delete_tollOperator(self, tollOperator):
        for toll_op in self.tollOperators:
            if toll_op.email == tollOperator.email:
                self.tollOperators.remove(toll_op)
    def find_tollOperator(self, email):
        for toll_op in self.tollOperators:
            if toll_op.email == email:
                return toll_op
            
    # methods toll boths
    def insert_tollBooth(self, tollBooth):
        self.tollBooths.append(tollBooth)
    def delete_tollBooth(self, tollBooth):
        for booth in self.tollBooths:
            if booth.boothid == tollBooth.boothid:
                self.tollBooths.remove(booth)
    def find_tollBooth(self, boothid):
        for tollBooth in self.tollBooths:
            if tollBooth.boothid == (str)(boothid):
                return tollBooth
    
    #methods toll payment
    def insert_tollPayment(self, tollPayment):
        self.tollPayments.append(tollPayment)
    def delete_tollPayment(self, tollPayment):
        for payment in self.tollPayments:
            if payment.transactionid == tollPayment.transactionid:
                self.tollPayments.remove(payment)
    def find_tollPayment(self, transactionid):
        for tollPayment in self.tollPayments:
            if tollPayment.transactionid == (str)(transactionid):
                return tollPayment

    # method to close the data manager and save the data
    def close(self):
        with open('data/json_files/admins.json', 'w') as f:
            json.dump([admin.to_dict() for admin in self.admins], f)
        with open('data/json_files/vehicles.json', 'w') as f:
            json.dump([vehicle.to_dict() for vehicle in self.vehicles], f)
        with open('data/json_files/tollOperators.json', 'w') as f:
            json.dump([tollOperator.to_dict() for tollOperator in self.tollOperators], f)
        with open('data/json_files/tollBooths.json', 'w') as f:
            json.dump([tollBooth.to_dict() for tollBooth in self.tollBooths], f)
        with open('data/json_files/tollPayments.json', 'w') as f:
            json.dump([tollPayment.to_dict() for tollPayment in self.tollPayments], f)