from analisis.pipeline_analisis import PipelineAnalisis
from restauracion.busqueda_gaps import BusquedaGaps
from restauracion.estaciones.arnl import Arnl

import os

def main():
    #RUTA 
    RUTA = "ARNL/DATACENTER/HHN.D"  
    pipeline = PipelineAnalisis(RUTA)
    resultados = pipeline.analizar()
    
    for key, value in resultados.items():
        print(f"Anomalías detectadas por {key}: {value}")
    
    busqueda_gaps = BusquedaGaps()
    
    estacion_arnl = Arnl(RUTA)
    busqueda_gaps.eventos.suscribir("ARNL", estacion_arnl)
    
    estacion_chl2 = Chl2(RUTA)
    busqueda_gaps.eventos.suscribir("CHL2", estacion_chl2)
    
    estacion_pplp = Pplp(RUTA)
    busqueda_gaps.eventos.suscribir("PPLP", estacion_pplp)
    
    busqueda_gaps.procesar_archivos_comunes("ARNL", list(resultados.values())[0])
    busqueda_gaps.procesar_archivos_saltos("ARNL", list(resultados.values())[1])

if __name__ == "__main__":
    main()
