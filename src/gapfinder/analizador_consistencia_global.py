from src.gapfinder.analizador import Analizador
from obspy import read

class AnalizadorConsistenciaGlobal(Analizador):
    def __init__(self, ruta):
        super().__init__(ruta)
        
    def __existe_consistencia(self, stream):
        npts_esperado = sum(traza.stats.npts for traza in stream)
        sample_rate = stream[0].stats.sampling_rate

        max_endtime = max(traza.stats.endtime for traza in stream)
        min_starttime = min(traza.stats.starttime for traza in stream)
        
        duracion = max_endtime - min_starttime
        npts_calculado = round(duracion * sample_rate) + 1
        return (npts_esperado - npts_calculado) == 0

    def __analizar_consistencia_global(self):
        anomalias = []
        for i, stream in enumerate(self.lista_stream):
            if not self.__existe_consistencia(stream):
                anomalia = {
                    "stream": stream,
                    "starttime": stream[0].stats.starttime,
                    "endtime": stream[-1].stats.endtime,
                    "julian_day": stream[0].stats.starttime.julday
                }
                anomalias.append(anomalia)
        return anomalias

    def analizar_stream_sismico(self):
        self.anomalias = self.__analizar_consistencia_global()
        return self.anomalias  # Devolver las anomalías detectadas
