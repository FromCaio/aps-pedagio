from control.addStrategy import AddStrategy
from DAO.adminDAO import AdminDAO
from DAO.vehicleDAO import VehicleDAO
from DAO.tollBoothDAO import TollBoothDAO
from DAO.tollOperatorDAO import TollOperatorDAO
from DAO.tollPaymentDAO import TollPaymentDAO

class AddAdminStrategy(AddStrategy):
    def add(self, entity):
        AdminDAO().insert(entity)

class AddVehicleStrategy(AddStrategy):
    def add(self, entity):
        VehicleDAO().insert(entity)

class AddTollBoothStrategy(AddStrategy):
    def add(self, entity):
        TollBoothDAO().insert(entity)

class AddTollOperatorStrategy(AddStrategy):
    def add(self, entity):
        TollOperatorDAO().insert(entity)

class AddTransactionStrategy(AddStrategy):
    def add(self, entity):
        TollPaymentDAO().insert(entity)