from restauracion.estacion import Estacion
from obspy import read
import os
from restauracion.busqueda_archivos import BusquedaArchivo
from obspy import UTCDateTime
# Eliminar importación redundante de UTCDateTime ya que los gap ya son UTCDateTime

class Arnl(Estacion):
    def __init__(self):
        self._lista = []

    def __obtener_fecha(self, gap):
        year = gap['starttime'].year
        jday = str(gap['julian_day'])
        if len(jday) == 2:
            jday = "0" + jday
        return str(year) + jday

    def __agregar_datos(self, ruta):
        streams = []
        for archivo in sorted(os.listdir(ruta)):
            if archivo.lower().endswith('.xml'):
                continue
            streams.append(read(os.path.join(ruta, archivo)))
        return streams

    def __encontrar_traza(self, lista, gap):
        # Filtrar por el canal del gap
        canal_gap = gap['stream'][0].stats.channel

        # Usamos solo la parte de la fecha (día y mes) del gap
        gap_start_date = gap['starttime'].datetime.date()
        gap_end_date = gap['endtime'].datetime.date()

        # Buscar traza individual que cumpla con los criterios basados en día y mes
        for stream in lista:
            for traza in stream:
                trace_start_date = traza.stats.starttime.datetime.date()
                trace_end_date = traza.stats.endtime.datetime.date()
                if (traza.stats.channel == canal_gap and 
                    trace_start_date <= gap_start_date and 
                    trace_end_date >= gap_end_date):
                    return ("trace", traza.stats)

        # Si no se encontró una traza individual, verificar si el stream completo cumple
        for stream in lista:
            if stream[0].stats.channel != canal_gap:
                continue
            stream_start_date = stream[0].stats.starttime.datetime.date()
            stream_end_date = stream[-1].stats.endtime.datetime.date()
            if (stream_start_date <= gap_start_date and 
                stream_end_date >= gap_end_date):
                return ("stream", stream)

        return (None, None)

    def actualizar(self, datos_gap):
        datos = list(datos_gap.values())[0]
        for gap in datos:
            fecha = self.__obtener_fecha(gap)
            try:
                self.ruta = f"ARNL/STATION/{fecha}/30444/1"
                if not os.path.isdir(self.ruta):
                    raise FileNotFoundError(f"El sistema no puede encontrar la ruta especificada: '{self.ruta}'")
            except FileNotFoundError as error:
                print(error)
                continue
            self.lista = self.__agregar_datos(self.ruta)
            resultado = self.__encontrar_traza(self.lista, gap)
            print(resultado)

