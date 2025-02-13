
from pipeline_analisis import PipelineAnalisis
import os

def main():
    #RUTA 
    RUTA = "ARNL/DATACENTER/HHN.D"  
    RUTA_STATION = "ARNL/STATION/"

    pipeline = PipelineAnalisis(RUTA)
    resultados = pipeline.analizar()
    for key, value in resultados.items():
        print(f"Anomalías detectadas por {key}: {value}")
    

    #Reportes
    #if arnl_registros.se_registraron_anomalias():
        #GENERA UN REPORTE DE LOS REGISTROS CON INCONSISTENCIAS
        #reportero_arnl = GAPReporte(arnl_registros)
        
        # Generar y mostrar el reporte
        #print(reportero_arnl.generar_reporte())
        
        #SE INSTANCIA UNA CLASE QUE OBTIENE LA TRAZA DE LOS REGISTROS CON INCONSISTENCIAS
        #folder_path = os.path.join(RUTA_STATION, f"20240{reportero_arnl.julian_day}", f"20240{reportero_arnl.julian_day}", "30444", "1")
        #station_arnl = StationARNL(folder_path, reportero_arnl.canal)
        # se obtiene los datos faltantes en el gap, en la carpeta station
        #station_arnl.obtener_traza_perdidas(reportero_arnl)
        

if __name__ == "__main__":
    main()
