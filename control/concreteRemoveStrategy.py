from control.removeStrategy import RemoveStrategy
from DAO.adminDAO import AdminDAO
from DAO.vehicleDAO import VehicleDAO
from DAO.tollBoothDAO import TollBoothDAO
from DAO.tollOperatorDAO import TollOperatorDAO
from DAO.tollPaymentDAO import TollPaymentDAO

class RemoveAdminStrategy(RemoveStrategy):
    def remove(self, entity):
        AdminDAO().delete(entity)

class RemoveVehicleStrategy(RemoveStrategy):
    def remove(self, entity):
        VehicleDAO().delete(entity)

class RemoveTollBoothStrategy(RemoveStrategy):
    def remove(self, entity):
        TollBoothDAO().delete(entity)

class RemoveTollOperatorStrategy(RemoveStrategy):
    def remove(self, entity):
        TollOperatorDAO().delete(entity)

class RemoveTollPaymentStrategy(RemoveStrategy):
    def remove(self, entity):
        TollPaymentDAO().delete(entity)