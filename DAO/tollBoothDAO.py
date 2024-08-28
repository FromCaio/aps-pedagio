import json
from model.tollBooth import TollBooth
from DAO.DAO import DAO

class TollBoothDAO(DAO):
    #constructor method
    def __init__(self):
        super().__init__()

    #method to load the data from the json file
    def load(self):
        try:
            with open('DAO/json_files/tollBooths.json', 'r') as f:
                self.tollBooths = [TollBooth.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.tollBooths = []

    def insert(self, tollBooth):
        self.tollBooths.append(tollBooth)
    
    def delete(self, tollBooth):
        for toll_booth in self.tollBooths:
            if toll_booth.boothid == tollBooth.boothid:
                self.tollBooths.remove(toll_booth)
    
    def find(self, id):
        for toll_booth in self.tollBooths:
            if toll_booth.boothid == (str)(id):
                return toll_booth
            
    #method to close the connection and save the data to the json file
    def close(self):
        with open('DAO/json_files/tollBooths.json', 'w') as f:
            json.dump([tollBooth.to_dict() for tollBooth in self.tollBooths], f)