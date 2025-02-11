from analizador import Analizador
from obspy import read

class AnalizadorMuestrasRegistros(Analizador):
    def __init__(self, ruta):
        super().__init__(ruta)

    def __analizar_muestra_registros(self, lista_stream):
        anomalias = []
        for i in range(0, len(lista_stream)):
            if not self.__existe_muestra_consistente(lista_stream[i]):
                anomalias.append(lista_stream[i])

        return anomalias
    
    def __existe_muestra_consistente(self, stream):
        npts_base = stream[0].stats.npts
        # Verificar que todos los registros excepto el último tengan el mismo número de muestras que el primer registro.
        for traza in stream[:-1]:
            if traza.stats.npts != npts_base:
                return False  # Inconsistencia detectada: gap o overlap en las muestras.
        return True  # Todos los registros son consistentes.


    def analizar_stream_sismico(self):
        self.anomalias = self.__analizar_muestra_registros(self.lista_stream)
        for inconsistencia in self.anomalias:
            print(inconsistencia)
