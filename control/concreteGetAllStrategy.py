from control.getAllStrategy import GetAllStrategy
from DAO.adminDAO import AdminDAO
from DAO.vehicleDAO import VehicleDAO
from DAO.tollBoothDAO import TollBoothDAO
from DAO.tollOperatorDAO import TollOperatorDAO
from DAO.tollPaymentDAO import TollPaymentDAO

class GetAllAdminStrategy(GetAllStrategy):
    def get_all(self):
        list = AdminDAO().admins
        return list

class GetAllVehicleStrategy(GetAllStrategy):
    def get_all(self):
        return VehicleDAO().vehicles

class GetAllTollBoothStrategy(GetAllStrategy):
    def get_all(self):
        return TollBoothDAO().tollBooths

class GetAllTollOperatorStrategy(GetAllStrategy):
    def get_all(self):
        return TollOperatorDAO().tollOperators

class GetAllTransactionsStrategy(GetAllStrategy):
    def get_all(self):
        return TollPaymentDAO().tollPayments
