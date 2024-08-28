from DAO.adminDAO import AdminDAO
from DAO.vehicleDAO import VehicleDAO
from DAO.tollBoothDAO import TollBoothDAO
from DAO.tollOperatorDAO import TollOperatorDAO
from DAO.tollPaymentDAO import TollPaymentDAO

class MainControl:
    #data_manager = DataManager()
    adminDAO = AdminDAO()
    vehicleDAO = VehicleDAO()
    tollBoothDAO = TollBoothDAO()
    tollOperatorDAO = TollOperatorDAO()
    tollPaymentDAO = TollPaymentDAO()

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
    
    @classmethod
    def login(cls, email, password):
        user = cls.find_admin(email)
        if user is None:
            user = cls.find_tollOperator(email)
            
        if user is not None:
            if user.password == password:
                return user
        return False

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
    def close_data_manager(cls):
        cls.adminDAO.close()
        cls.vehicleDAO.close()
        cls.tollBoothDAO.close()
        cls.tollOperatorDAO.close()
        cls.tollPaymentDAO.close()
