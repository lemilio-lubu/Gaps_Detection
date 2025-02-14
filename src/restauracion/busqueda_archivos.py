from restauracion.registro_evento import RegistroEventos

class BusquedaArchivo:
    def __init__(self):
        self.eventos = RegistroEventos()

    def procesar_archivos(self, estacion, archivos):
        self.eventos.notificar(estacion, archivos)

