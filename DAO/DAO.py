#abstract class
from abc import ABC, abstractmethod

class DAO(ABC):
    #variavel para armazenar as instancias
    _instance = None

    #metodo Padrao Singleton
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DAO, cls).__new__(cls)
        return cls._instance
    
    #constructor method
    def __init__(self):
        self.load()

    #method to load the data from the json file
    @abstractmethod
    def load(self):
        pass
    
    @abstractmethod
    def insert(self, attribute):
        pass
    
    @abstractmethod
    def delete(self, attribute):
        pass
    
    @abstractmethod
    def find(self, attribute):
        pass
    
    #method to close the connection and save the data to the json file    
    @abstractmethod
    def close(self):
        pass