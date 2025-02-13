from analizador import Analizador

class AnalizadorContinuidadRegistro(Analizador):
    def __init__(self, ruta):
        super().__init__(ruta)

    def __analizar_continuidad(self, lista_stream):
        anomalias = []
        for i in range(0,len(lista_stream)):
            if not self.__existe_continuidad(lista_stream[i]):
                anomalia = {
                    "stream": lista_stream[i],
                    "starttime": lista_stream[i][0].stats.starttime,
                    "endtime": lista_stream[i][-1].stats.endtime,
                    "julian_day": lista_stream[i][0].stats.starttime.julday
                }
                anomalias.append(anomalia)
        return anomalias

    def __existe_continuidad(self, stream):
        if stream[0].stats.sampling_rate == 0:
            return False
        delta = 1.0 / stream[0].stats.sampling_rate
        
        for i in range(0,len(stream)-1):
            registro_actual = stream[i]
            registro_siguiente = stream[i+1]
            fin_actual = registro_actual.stats.endtime
            inicio_esperado = fin_actual + delta
            inicio_real = registro_siguiente.stats.starttime

            if inicio_real != inicio_esperado:
                return False
        return True
    
    def analizar_stream_sismico(self):
        self.anomalias = self.__analizar_continuidad(self.lista_stream)
        return self.anomalias  # Devolver las anomalías detectadas
