from tollBooth import TollBooth
from vehicle import Vehicle
from tollOperator import TollOperator
import json

class TollPayment:
    def __init__(self, vehicle:Vehicle, tollbooth:TollBooth, operator:TollOperator, amount, method, date):
        self.transactionid = self.get_transaction_id()
        self.vehicle = vehicle
        self.tollboth = tollbooth
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
    # methods to get tollPayment class attribute ID value
    def get_transaction_id(self):
        with open('data/json_files/transactionid_id.json', 'r') as f:
            transaction_id = json.load(f)
        transaction_id += 1
        with open('data/json_files/transaction_id.json', 'w') as f:
            json.dump(transaction_id, f)
        return transaction_id
    
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
