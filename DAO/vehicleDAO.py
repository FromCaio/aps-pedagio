from model.vehicle import Vehicle
import json

class VehicleDAO:
    #constructor method
    def __init__(self):
        self.load_vehicles()
    
    #method to load the data from the json file
    def load_vehicles(self):
        try:
            with open('DAO/json_files/vehicles.json', 'r') as f:
                self.vehicles = [Vehicle.from_dict(data) for data in json.load(f)]
        except (json.JSONDecodeError, FileNotFoundError):
            self.vehicles = []
    
    def insert_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def delete_vehicle(self, vehicle):
        for veh in self.vehicles:
            if veh.plate == (str)(vehicle.plate):
                self.vehicles.remove(veh)
    
    def find_vehicle(self, plate):
        for vehicle in self.vehicles:
            if vehicle.plate == (str)(plate):
                return vehicle
    
    #method to close the connection and save the data to the json file    
    def close(self):   
        with open('DAO/json_files/vehicles.json', 'w') as f:
            json.dump([vehicle.to_dict() for vehicle in self.vehicles], f)