from abc import ABC, abstractmethod

class RemoveStrategy(ABC):
    @abstractmethod
    def remove(self, entity):
        pass