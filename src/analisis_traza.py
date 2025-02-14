from analisis.pipeline_analisis import PipelineAnalisis
from restauracion.busqueda_archivos import BusquedaArchivo
from restauracion.arnl import Arnl
from restauracion.chl2 import Chl2
from restauracion.pplp import Pplp
import os

def main():
    #DATACENTER 
    RUTA_ARNL_DATACENTER = "ARNL/DATACENTER/HHN.D"
    RUTA_CHL2_DATACENTER = "CHL2/DATACENTER/HHN.D"
    RUTA_PPLP_DATACENTER = "PPLP/DATACENTER/HHN.D"
    
    

    #IDENTIFICACCIÓN DE GAPS
    pipeline = PipelineAnalisis(RUTA_ARNL_DATACENTER)
    resultados = pipeline.analizar()
    
    for key, value in resultados.items():
        print(f"Anomalías detectadas por {key}: {value}")
    
    #OBTENCION DE DATOS
    busqueda_gaps = BusquedaArchivo()
    
    estacion_arnl = Arnl()
    busqueda_gaps.eventos.suscribir("ARNL", estacion_arnl)
    
    #estacion_chl2 = Chl2(RUTA_CHL2_ESTACION)
    #busqueda_gaps.eventos.suscribir("CHL2", estacion_chl2)
    
    #estacion_pplp = Pplp(RUTA_PPLP_ESTACION)
    #busqueda_gaps.eventos.suscribir("PPLP", estacion_pplp)
    
    busqueda_gaps.procesar_archivos("ARNL", resultados)

if __name__ == "__main__":
    main()
