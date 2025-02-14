from restauracion.registro_evento import RegistroEventos

class BusquedaArchivo:
    def __init__(self):
        self.eventos = RegistroEventos()

    def procesar_archivos(self, estacion, archivos):
        for key, value in archivos.items():
            print(f"Anomalías detectadas por {key}: {value}")
        self.eventos.notificar(estacion, archivos)

