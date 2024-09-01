from abc import ABC, abstractmethod

class GetAllStrategy(ABC):
    @abstractmethod
    def get_all(self):
        pass