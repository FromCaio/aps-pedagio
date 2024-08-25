from model.tollBooth import TollBooth
from model.vehicle import Vehicle
from model.tollOperator import TollOperator

class TollPayment:
    def __init__(self, transactionid, vehicle:Vehicle, tollbooth:TollBooth, operator:TollOperator, amount, method, date):
        self.transactionid = transactionid
        self.vehicle = vehicle
        self.tollbooth = tollbooth
        self.operator = operator
        self.amount = amount
        self.method = method
        self.date = date

    def __str__(self):
        return (f"Vehicle: {self.vehicle}, TollBooth: {self.tollbooth},"
                f"Operator: {self.operator}, Amount: {self.amount},"
                f"Method: {self.method}, Date: {self.date}")
   
    def to_dict(self):
        return {
            'transactionid': self.transactionid,
            'vehicle': str(self.vehicle),  
            'tollbooth': str(self.tollbooth),  
            'operator': str(self.operator),  
            'amount': self.amount,
            'method': self.method,
            'date': self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['transactionid'],
            data['vehicle'],  
            data['tollbooth'],  
            data['operator'], 
            data['amount'],
            data['method'],
            data['date']
        )
