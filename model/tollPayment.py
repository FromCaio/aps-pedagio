from model.tollBooth import TollBooth
from model.vehicle import Vehicle
from model.tollOperator import TollOperator

class TollPayment:
    def __init__(self, transactionid, vehicle: Vehicle, tollbooth: TollBooth, operator: TollOperator, amount, method, date):
        self.transactionid = transactionid
        self.vehicle = vehicle
        self.tollbooth = tollbooth
        self.operator = operator
        self.amount = amount
        self.method = method
        self.date = date

    def __str__(self):
        return (f"TransactionID: {self.transactionid}, Vehicle: {self.vehicle}, TollBooth: {self.tollbooth},"
                f"Operator: {self.operator}, Amount: {self.amount},"
                f"Method: {self.method}, Date: {self.date}")

    def to_dict(self):
        return {
            'transactionid': self.transactionid,
            'vehicle': self.vehicle.to_dict(),  # Aqui usamos to_dict
            'tollbooth': self.tollbooth.to_dict(),  # Aqui usamos to_dict
            'operator': self.operator.to_dict(),  # Aqui usamos to_dict
            'amount': self.amount,
            'method': self.method,
            'date': self.date
        }

    @classmethod
    def from_dict(cls, data):
        vehicle = Vehicle.from_dict(data['vehicle'])  # Converte o dicionário de volta para o objeto Vehicle
        tollbooth = TollBooth.from_dict(data['tollbooth'])  # Converte o dicionário de volta para o objeto TollBooth
        operator = TollOperator.from_dict(data['operator'])  # Converte o dicionário de volta para o objeto TollOperator
        
        return cls(
            data['transactionid'],
            vehicle,
            tollbooth,
            operator,
            data['amount'],
            data['method'],
            data['date']
        )
