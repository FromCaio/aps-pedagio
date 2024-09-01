from abc import ABC, abstractmethod

class AddStrategy(ABC):
    @abstractmethod
    def add(self, entity):
        pass