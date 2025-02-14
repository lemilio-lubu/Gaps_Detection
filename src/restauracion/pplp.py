from restauracion.estacion import Estacion
from restauracion.busqueda_archivos import BusquedaArchivo

class Pplp(Estacion):
    def actualizar(self, gap):
        self.__obtener_datos()