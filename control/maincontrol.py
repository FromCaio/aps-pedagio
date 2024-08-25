from data.datamanager import DataManager

class MainControl:
    data_manager = DataManager()

    @classmethod
    def add_admin(cls, admin):
        cls.data_manager.insert_admin(admin)

    @classmethod
    def remove_admin(cls, admin):
        cls.data_manager.delete_admin(admin)

    @classmethod
    def find_admin(cls, email):
        return cls.data_manager.find_admin(email)
    
    @classmethod
    def find_admin_by_name(cls, name):
        matching_admins = []
        for admin in cls.data_manager.admins:
            if admin.name == name:
                matching_admins.append(admin)
        return matching_admins
    
    @classmethod
    def get_all_admins(cls):
        return cls.data_manager.admins

    @classmethod
    def add_vehicle(cls, vehicle):
        cls.data_manager.insert_vehicle(vehicle)

    @classmethod
    def remove_vehicle(cls, vehicle):
        cls.data_manager.delete_vehicle(vehicle)

    @classmethod
    def find_vehicle(cls, plate):
        return cls.data_manager.find_vehicle(plate)
    
    @classmethod
    def get_all_vehicles(cls):
        return cls.data_manager.vehicles

    @classmethod
    def find_vehicle_by_model(cls, model):
        matching_vehicles = []
        for vehicle in cls.data_manager.vehicles:
            if vehicle.model == model:
                matching_vehicles.append(vehicle)
        return matching_vehicles
    
    @classmethod
    def add_tollBooth(cls, tollBooth):
        cls.data_manager.insert_tollBooth(tollBooth)

    @classmethod
    def remove_tollBooth(cls, tollBooth):
        cls.data_manager.delete_tollBooth(tollBooth)

    @classmethod
    def find_tollBooth(cls, boothid):
        return cls.data_manager.find_tollBooth(boothid)
    
    @classmethod
    def get_all_tollBooths(cls):
        return cls.data_manager.tollBooths

    @classmethod
    def find_booth_by_highway(cls, highway):
        matching_tollBooths = []
        for tollBooth in cls.data_manager.tollBooths:
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
        cls.data_manager.insert_tollOperator(tollOperator)

    @classmethod
    def remove_tollOperator(cls, tollOperator):
        cls.data_manager.delete_tollOperator(tollOperator)

    @classmethod
    def find_tollOperator(cls, email):
        return cls.data_manager.find_tollOperator(email)
    
    @classmethod
    def get_all_tollOperators(cls):
        return cls.data_manager.tollOperators
    
    @classmethod
    def add_transaction(cls, tollPayment):
        cls.data_manager.insert_tollPayment(tollPayment)
    
    @classmethod
    def get_all_transactions(cls):
        return cls.data_manager.tollPayments
    
    @classmethod
    def find_transaction_by_id(cls, transaction_id):
        return cls.data_manager.find_tollPayment(transaction_id)
    
    @classmethod
    def remove_tollPayment(cls, transaction):
        cls.data_manager.delete_tollPayment(transaction)
    
    @classmethod
    def close_data_manager(cls):
        cls.data_manager.close()