from DAO.adminDAO import AdminDAO
from DAO.vehicleDAO import VehicleDAO
from DAO.tollBoothDAO import TollBoothDAO
from DAO.tollOperatorDAO import TollOperatorDAO
from DAO.tollPaymentDAO import TollPaymentDAO
from control.analysisStrategy import AnalysisStrategy
from control.addStrategy import AddStrategy
from control.removeStrategy import RemoveStrategy
from control.getAllStrategy import GetAllStrategy
from control.concreteGetAllStrategy import GetAllTransactionsStrategy

class MainControl:
    #data_manager = DataManager()
    adminDAO = AdminDAO()
    vehicleDAO = VehicleDAO()
    tollBoothDAO = TollBoothDAO()
    tollOperatorDAO = TollOperatorDAO()
    tollPaymentDAO = TollPaymentDAO()

    #strategy: AnalysisStrategy
    #is a type hint that indicates that the argument should be
    #an instance of the AnalysisStrategy class or one of its subclasses
    @classmethod
    def analyze_transactions(cls, strategy: AnalysisStrategy):
        # toll_payments = cls.get_all_transactions()
        get_all_strategy = GetAllTransactionsStrategy()
        toll_payments = cls.get_all(get_all_strategy)
        return strategy.analyze(toll_payments)
    
    @classmethod
    def add_entity(cls, strategy: AddStrategy, entity):
        strategy.add(entity)
    
    @classmethod
    def remove_entity(cls, strategy: RemoveStrategy, entity):
        strategy.remove(entity)

    @classmethod
    def get_all(cls, strategy: GetAllStrategy):
        return strategy.get_all()
    

    # metodos find
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
    def find_vehicle(cls, plate):
        return cls.vehicleDAO.find(plate)
    @classmethod
    def find_vehicle_by_model(cls, model):
        matching_vehicles = []
        for vehicle in cls.vehicleDAO.vehicles:
            if vehicle.model == model:
                matching_vehicles.append(vehicle)
        return matching_vehicles
    @classmethod
    def find_tollBooth(cls, boothid):
        return cls.tollBoothDAO.find(boothid)
    @classmethod
    def find_booth_by_highway(cls, highway):
        matching_tollBooths = []
        for tollBooth in cls.tollBoothDAO.tollBooths:
            if tollBooth.highway == highway:
                matching_tollBooths.append(tollBooth)
        return matching_tollBooths
    @classmethod
    def find_tollOperator(cls, email):
        return cls.tollOperatorDAO.find(email)
    @classmethod
    def find_transaction_by_id(cls, transaction_id):
        return cls.tollPaymentDAO.find(transaction_id)

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