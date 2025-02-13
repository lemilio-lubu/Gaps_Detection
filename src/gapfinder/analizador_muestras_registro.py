from src.gapfinder.analizador import Analizador
from obspy import read

class AnalizadorMuestrasRegistros(Analizador):
    def __init__(self, ruta):
        super().__init__(ruta)

    def __analizar_muestra_registros(self, lista_stream):
        anomalias = []
        for i, stream in enumerate(lista_stream):
            if not self.__existe_muestra_consistente(stream):
                anomalia = {
                    "stream": stream,
                    "starttime": stream[0].stats.starttime,
                    "endtime": stream[-1].stats.endtime,
                    "julian_day": stream[0].stats.starttime.julday
                }
                anomalias.append(anomalia)
        return anomalias
    
    def __existe_muestra_consistente(self, stream):
        npts_base = stream.stats.npts
        # Verificar que todos los registros excepto el último tengan el mismo número de muestras que el primer registro.
        for traza in stream:
            if traza.stats.npts != npts_base:
                return False  # Inconsistencia detectada: gap o overlap en las muestras.
        return True  # Todos los registros son consistentes.

    def analizar_stream_sismico(self):
        self.anomalias = self.__analizar_muestra_registros(self.lista_stream)
        return self.anomalias  # Devolver las anomalías detectadas

    def se_registraron_anomalias(self):
        return len(self.anomalias) > 0