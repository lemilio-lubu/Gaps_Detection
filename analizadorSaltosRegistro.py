from analizador import Analizador
from obspy import read

class AnalizadorSaltosRegistro(Analizador):
    def __init__(self, ruta):
        super().__init__(ruta)
        self.stream_julian_days = self.__obtener_julian_days(self.lista_stream)
    
    def __obtener_julian_days(self, lista_stream):
        julian_days = []
        for stream in lista_stream:
            trace = stream[0]
            julian_day = trace.stats.starttime.julday
            julian_days.append(julian_day)
        return julian_days

    def __existe_salto(self, i):
        return self.stream_julian_days[i+1] - self.stream_julian_days[i] > 1

    
    def __analizar_salto_dias(self):
        stream = []
        for i in range(len(self.stream_julian_days)-1):
            if self.__existe_salto(i):
                stream.append(self.lista_stream[i])
                stream.append(self.lista_stream[i+1])
        return stream
    
    # Metodo publico polimorfico
    def analizar_stream_sismico(self):
        self.anomalias = self.__analizar_salto_dias()
        for salto in self.anomalias:
            print(salto)
    