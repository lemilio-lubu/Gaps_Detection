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
    pipeline_arnl = PipelineAnalisis(RUTA_ARNL_DATACENTER)
    resultados_arnl = pipeline_arnl.analizar()
    
    pipeline_chl2 = PipelineAnalisis(RUTA_CHL2_DATACENTER)
    resultados_chl2 = pipeline_chl2.analizar()

    pipeline_pplp = PipelineAnalisis(RUTA_PPLP_DATACENTER)
    resultados_pplp = pipeline_pplp.analizar()

    
    
    #OBTENCION DE DATOS
    busqueda_gaps = BusquedaArchivo()
    
    estacion_arnl = Arnl()
    busqueda_gaps.eventos.suscribir("ARNL", estacion_arnl)
    
    estacion_chl2 = Chl2()
    busqueda_gaps.eventos.suscribir("CHL2", estacion_chl2)
    
    estacion_pplp = Pplp()
    busqueda_gaps.eventos.suscribir("PPLP", estacion_pplp)
    
    busqueda_gaps.procesar_archivos("ARNL", resultados_arnl)
    busqueda_gaps.procesar_archivos("CHL2", resultados_chl2)
    busqueda_gaps.procesar_archivos("PPLP", resultados_pplp)

if __name__ == "__main__":
    main()
