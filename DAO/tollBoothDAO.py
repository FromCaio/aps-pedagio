import json
from model.tollBooth import TollBooth

class TollBoothDAO:
    #constructor method
    def __init__(self):
        self.load_tollBooths()

    #method to load the data from the json file
    def load_tollBooths(self):
        try:
            with open('DAO/json_files/tollBooths.json', 'r') as f:
                self.tollBooths = [TollBooth.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.tollBooths = []

    def insert_tollBooth(self, tollBooth):
        self.tollBooths.append(tollBooth)
    
    def delete_tollBooth(self, tollBooth):
        for toll_booth in self.tollBooths:
            if toll_booth.boothid == tollBooth.id:
                self.tollBooths.remove(toll_booth)
    
    def find_tollBooth(self, id):
        for toll_booth in self.tollBooths:
            if toll_booth.boothid == id:
                return toll_booth
            
    #method to close the connection and save the data to the json file
    def close(self):
        with open('DAO/json_files/tollBooths.json', 'w') as f:
            json.dump([tollBooth.to_dict() for tollBooth in self.tollBooths], f)