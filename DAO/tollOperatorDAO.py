import json
from model.tollOperator import TollOperator
from DAO.DAO import DAO

class TollOperatorDAO(DAO):
    #constructor method
    def __init__(self):
        super().__init__()

    #method to load the data from the json file
    def load(self):
        try:
            with open('DAO/json_files/tollOperators.json', 'r') as f:
                self.tollOperators = [TollOperator.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.tollOperators = []

    def insert(self, tollOperator):
        self.tollOperators.append(tollOperator)
    
    def delete(self, tollOperator):
        for toll_op in self.tollOperators:
            if toll_op.email == tollOperator.email:
                self.tollOperators.remove(toll_op)
    
    def find(self, email):
        for toll_op in self.tollOperators:
            if toll_op.email == email:
                return toll_op
    
    #method to close the connection and save the data to the json file    
    def close(self):
        with open('DAO/json_files/tollOperators.json', 'w') as f:
            json.dump([tollOperator.to_dict() for tollOperator in self.tollOperators], f)