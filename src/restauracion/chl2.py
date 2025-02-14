from restauracion.busqueda_archivos import BusquedaArchivo
from restauracion.estacion import Estacion
import os 
from obspy import read

class Chl2(Estacion):
    def __init__(self):
        self.lista = []

    def __obtener_fecha(self, gap):
        año = gap['starttime'].year
        mes = str(gap['starttime'].month).zfill(2)
        dia = f"{gap['starttime'].day:02d}"
        return año, mes, dia

    def __agregar_datos(self, ruta):
        streams = []
        for archivo in sorted(os.listdir(ruta)):
            streams.append(read(os.path.join(ruta, archivo)))
        return streams

    def __encontrar_traza(self, lista, gap):
        # Obtener el canal definido en el gap
        canal_gap = gap['stream'][0].stats.channel

        # Usar los timestamps completos en UTC para comparar los tiempos
        gap_start_time = gap['starttime'].datetime
        gap_end_time = gap['endtime'].datetime

        # Buscar traza individual (retornamos la trace completa)
        for stream in lista:
            for traza in stream:
                if traza.stats.channel != canal_gap:
                    continue
                trace_start_time = traza.stats.starttime.datetime
                trace_end_time = traza.stats.endtime.datetime
                if trace_start_time <= gap_start_time and trace_end_time >= gap_end_time:
                    return ("trace", traza)

        # Si no se encontró una traza individual, verificar si el stream completo cumple
        for stream in lista:
            if not stream or stream[0].stats.channel != canal_gap:
                continue
            stream_start_time = stream[0].stats.starttime.datetime
            stream_end_time = stream[-1].stats.endtime.datetime
            if stream_start_time <= gap_start_time and stream_end_time >= gap_end_time:
                return ("stream", stream)

        return (None, None)

    def actualizar(self, gap):
        datos = list(gap.values())[0]
        for gap_item in datos:
            año, mes, dia = self.__obtener_fecha(gap_item)
            try:
                self.ruta = f"CHL2/STATION/{año}/{mes}/{dia}"
                if not os.path.isdir(self.ruta):
                    raise FileNotFoundError(f"El sistema no puede encontrar la ruta especificada: '{self.ruta}'")
            except FileNotFoundError as error:
                print(error)
                continue
            self.lista = self.__agregar_datos(self.ruta)
            resultado = self.__encontrar_traza(self.lista, gap_item)
            print(resultado)