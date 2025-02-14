from restauracion.estacion import Estacion
from restauracion.busqueda_archivos import BusquedaArchivo
import os
from obspy import read
from obspy import UTCDateTime

class Pplp(Estacion):
    def __init__(self):
        self.lista = []
    
    def __agregar_datos(self, ruta):
        streams = []
        for archivo in sorted(os.listdir(ruta)):
            streams.append(read(os.path.join(ruta, archivo)))
        return streams
    
    def __encontrar_traza(self, lista, gap):
        canal = gap['stream'][0].stats.channel
        tiempo =  gap['starttime'].datetime.date()
        for stream in lista:
            for traza in stream:
                if traza.stats.channel == canal:
                    if traza.stats.starttime <= tiempo <= traza.stats.endtime:
                        return traza
        return None
    def actualizar(self, gap):
        datos = list(gap.values())[0]
        for gap in datos:
            try:
                self.ruta = f"PPLP/STATION/data"
                if not os.path.isdir(self.ruta):
                    raise FileNotFoundError(f"El sistema no puede encontrar la ruta especificada: '{self.ruta}'")
            except FileNotFoundError as error:
                print(error)
                continue
            self.lista = self.__agregar_datos(self.ruta)
            resultado = self.__encontrar_traza(self.lista, gap)
            print(resultado)