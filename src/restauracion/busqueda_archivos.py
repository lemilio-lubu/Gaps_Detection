from registro_evento import RegistroEventos

class BusquedaArchivo:
    def __init__(self):
        self.eventos = RegistroEventos()

    def procesar_archivos_comunes(self, estacion, archivos):
        self.eventos.notificar(estacion, archivos)

    def procesar_archivos_saltos(self, estacion, archivos):
        self.eventos.notificar(estacion, archivos)