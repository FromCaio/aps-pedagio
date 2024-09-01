import json
from model.tollPayment import TollPayment
from DAO.DAO import DAO

class TollPaymentDAO(DAO):   
    #constructor method
    def __init__(self):
        super().__init__()

    #method to load the data from the json file
    def load(self):
        try:
            with open('DAO/json_files/tollPayments.json', 'r') as f:
                self.tollPayments = [TollPayment.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.tollPayments = []
    
    def insert(self, tollPayment):
        self.tollPayments.append(tollPayment)
        self.close()
    
    def delete(self, tollPayment):
        for payment in self.tollPayments:
            if payment.transactionid == tollPayment.transactionid:
                self.tollPayments.remove(payment)
        self.close()
    
    def find(self, transactionid):
        for tollPayment in self.tollPayments:
            if tollPayment.transactionid == (str)(transactionid):
                return tollPayment

    #method to close the connection and save the data to the json file
    def close(self):   
        with open('DAO/json_files/tollPayments.json', 'w') as f:
            json.dump([tollPayment.to_dict() for tollPayment in self.tollPayments], f)