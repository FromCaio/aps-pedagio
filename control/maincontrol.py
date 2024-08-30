from DAO.adminDAO import AdminDAO
from DAO.vehicleDAO import VehicleDAO
from DAO.tollBoothDAO import TollBoothDAO
from DAO.tollOperatorDAO import TollOperatorDAO
from DAO.tollPaymentDAO import TollPaymentDAO
from collections import Counter
from datetime import datetime

class MainControl:
    #data_manager = DataManager()
    adminDAO = AdminDAO()
    vehicleDAO = VehicleDAO()
    tollBoothDAO = TollBoothDAO()
    tollOperatorDAO = TollOperatorDAO()
    tollPaymentDAO = TollPaymentDAO()

    #metodos Admin
    @classmethod
    def add_admin(cls, admin):
        cls.adminDAO.insert(admin)
    @classmethod
    def remove_admin(cls, admin):
        cls.adminDAO.delete(admin)
    @classmethod
    def find_admin(cls, email):
        return cls.adminDAO.find(email)
    @classmethod
    def find_admin_by_name(cls, name):
        matching_admins = []
        for admin in cls.adminDAO.admins:
            if admin.name == name:
                matching_admins.append(admin)
        return matching_admins
    @classmethod
    def get_all_admins(cls):
        return cls.adminDAO.admins

    #metodos vehicle
    @classmethod
    def add_vehicle(cls, vehicle):
        cls.vehicleDAO.insert(vehicle)

    @classmethod
    def remove_vehicle(cls, vehicle):
        cls.vehicleDAO.delete(vehicle)
    @classmethod
    def find_vehicle(cls, plate):
        return cls.vehicleDAO.find(plate)
    @classmethod
    def get_all_vehicles(cls):
        return cls.vehicleDAO.vehicles
    @classmethod
    def find_vehicle_by_model(cls, model):
        matching_vehicles = []
        for vehicle in cls.vehicleDAO.vehicles:
            if vehicle.model == model:
                matching_vehicles.append(vehicle)
        return matching_vehicles
    
    #metodos tollBooth
    @classmethod
    def add_tollBooth(cls, tollBooth):
        cls.tollBoothDAO.insert(tollBooth)
    @classmethod
    def remove_tollBooth(cls, tollBooth):
        cls.tollBoothDAO.delete(tollBooth)
    @classmethod
    def find_tollBooth(cls, boothid):
        return cls.tollBoothDAO.find(boothid)
    @classmethod
    def get_all_tollBooths(cls):
        return cls.tollBoothDAO.tollBooths
    @classmethod
    def find_booth_by_highway(cls, highway):
        matching_tollBooths = []
        for tollBooth in cls.tollBoothDAO.tollBooths:
            if tollBooth.highway == highway:
                matching_tollBooths.append(tollBooth)
        return matching_tollBooths

    #metodo login
    @classmethod
    def login(cls, email, password):
        user = cls.find_admin(email)
        if user is None:
            user = cls.find_tollOperator(email)
            
        if user is not None:
            if user.password == password:
                return user
        return False

    #metodos tollOperator
    @classmethod
    def add_tollOperator(cls, tollOperator):
        cls.tollOperatorDAO.insert(tollOperator)
    @classmethod
    def remove_tollOperator(cls, tollOperator):
        cls.tollOperatorDAO.delete(tollOperator)
    @classmethod
    def find_tollOperator(cls, email):
        return cls.tollOperatorDAO.find(email)
    @classmethod
    def get_all_tollOperators(cls):
        return cls.tollOperatorDAO.tollOperators
    
    #metodos tollPayment
    @classmethod
    def add_transaction(cls, tollPayment):
        cls.tollPaymentDAO.insert(tollPayment)
    @classmethod
    def get_all_transactions(cls):
        return cls.tollPaymentDAO.tollPayments
    @classmethod
    def find_transaction_by_id(cls, transaction_id):
        return cls.tollPaymentDAO.find(transaction_id)
    @classmethod
    def remove_tollPayment(cls, transaction):
        cls.tollPaymentDAO.delete(transaction)
    @classmethod
    def get_total_amount(cls):
        tollPayments = cls.get_all_transactions()
        total = 0
        for tollPayment in tollPayments:
            total += float(tollPayment.amount)
        return total
    @classmethod
    def get_transactions_by_operators(cls):
        toll_payments = cls.get_all_transactions()
        # Analisar as transações por operador
        operator_counts = Counter()
        # Contando as ocorrências de cada operador
        for payment in toll_payments:
            if payment.operator and payment.operator.name:  # Verifica se o operador existe e tem nome
                operator_counts[payment.operator.name] += 1
        operators = list(operator_counts.keys())
        counts = list(operator_counts.values())
        return operators, counts
    @classmethod 
    def get_peak_times(cls):
        toll_payments = cls.get_all_transactions()    
         # Extraindo as horas das transações
        hours = [datetime.strptime(payment.date, "%Y-%m-%d %H:%M:%S").hour for payment in toll_payments]
        # Contabilizando a frequência de cada hora
        hour_counts = Counter(hours)
        return hour_counts
    @classmethod
    def get_payments_by_method(cls):
        toll_payments = cls.get_all_transactions()    
        # Contar as ocorrências de cada método de pagamento
        method_counts = Counter()
        for payment in toll_payments:
            if payment.method:  # Verifica se o método de pagamento existe
                method_counts[payment.method] += 1
        methods = list(method_counts.keys())
        print(methods)
        counts = list(method_counts.values())
        print(counts)
        return methods, counts

    #metodo close all data managers 
    @classmethod
    def close_data_manager(cls):
        cls.adminDAO.close()
        cls.vehicleDAO.close()
        cls.tollBoothDAO.close()
        cls.tollOperatorDAO.close()
        cls.tollPaymentDAO.close()
