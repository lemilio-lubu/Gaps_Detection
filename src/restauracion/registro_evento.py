from typing import Dict, List, Callable

# Clase encargada de manejar eventos
class RegistroEventos:
    def __init__(self):
        self.suscriptores: Dict[str, List[Callable]] = {}

    def suscribir(self, event_type: str, listener: Callable):
        if event_type not in self.suscriptores:
            self.suscriptores[event_type] = []
        self.suscriptores[event_type].append(listener)

    def notificar(self, event_type: str, data):
        if event_type in self.suscriptores:
            for listener in self.suscriptores[event_type]:
                listener.actualizar(data)