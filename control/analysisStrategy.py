from abc import ABC, abstractmethod

class AnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, toll_payments):
        pass