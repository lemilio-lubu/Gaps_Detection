from restauracion.busqueda_archivos import BusquedaArchivo
from restauracion.estacion import Estacion

class Chl2(Estacion):
    def actualizar(self, gap):
        self.__obtener_datos()