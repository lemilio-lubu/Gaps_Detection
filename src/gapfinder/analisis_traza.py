from analizador_consistencia_global import AnalizadorConsistenciaGlobal  # Asegúrate de que la importación sea correcta
from analizador_muestras_registro import AnalizadorMuestrasRegistros
from analizador_continuidad_registro import AnalizadorContinuidadRegistro
from analizador_saltos_registro import AnalizadorSaltosRegistro
import os

def main():
    #RUTA 
    RUTA = "ARNL/DATACENTER/HHE.D"  
    RUTA_STATION = "ARNL/STATION/"
    
    #Analizadores
    #arnl_consistencia = AnalizadorConsistenciaGlobal(RUTA)  
    arnl_registros = AnalizadorMuestrasRegistros(RUTA)
    #arnl_continuidad = AnalizadorContinuidadRegistro(RUTA)
    #arnl_saltos = AnalizadorSaltosRegistro(RUTA)

    #Analisis
    #arnl_saltos.analizar_stream_sismico()
    #arnl_consistencia.analizar_stream_sismico()
    #arnl_continuidad.analizar_stream_sismico()
    arnl_registros.analizar_stream_sismico()
    if arnl_registros.se_registraron_anomalias():
        #GENERA UN REPORTE DE LOS REGISTROS CON INCONSISTENCIAS
        reportero_arnl = GAPReporte(arnl_registros)
        
        # Generar y mostrar el reporte
        print(reportero_arnl.generar_reporte())
        
        #SE INSTANCIA UNA CLASE QUE OBTIENE LA TRAZA DE LOS REGISTROS CON INCONSISTENCIAS
        #folder_path = os.path.join(RUTA_STATION, f"20240{reportero_arnl.julian_day}", f"20240{reportero_arnl.julian_day}", "30444", "1")
        #station_arnl = StationARNL(folder_path, reportero_arnl.canal)
        # se obtiene los datos faltantes en el gap, en la carpeta station
        #station_arnl.obtener_traza_perdidas(reportero_arnl)
        

if __name__ == "__main__":
    main()
