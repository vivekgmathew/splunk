from abc import ABC, abstractmethod


class BaseIngestor(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, df):
        pass
