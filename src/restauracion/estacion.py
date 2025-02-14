from abc import ABC, abstractmethod

class Estacion(ABC):
    @abstractmethod
    def actualizar(self, gap):
        pass
