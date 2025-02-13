import os
from abc import ABC, abstractmethod
from obspy import read

class Analizador(ABC):
    def __init__(self, ruta):
        self.lista_stream = self.__obtener_lista(ruta)

    def __obtener_lista(self, ruta):
        streams = []
        for archivo in sorted(os.listdir(ruta)):     
            streams.append(read(os.path.join(ruta, archivo))) 
        return streams
    
    @abstractmethod
    def analizar_stream_sismico(self):
        pass
