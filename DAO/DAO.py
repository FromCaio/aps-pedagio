#abstract class
from abc import ABC, abstractmethod

class DAO(ABC):
    #constructor method
    def __init__(self):
        self.load()

    #method to load the data from the json file
    @abstractmethod
    def load(self):
        pass
    
    @abstractmethod
    def insert(self, atribute):
        pass
    
    @abstractmethod
    def delete(self, atribute):
        pass
    
    @abstractmethod
    def find(self, atribute):
        pass
    
    #method to close the connection and save the data to the json file    
    @abstractmethod
    def close(self):
        pass