from analizadorConsistenciaGlobal import AnalizadorConsistenciaGlobal  # Asegúrate de que la importación sea correcta
from analizadorMuestrasRegistro import AnalizadorMuestrasRegistros
from analizadorContinuidadRegistro import AnalizadorContinuidadRegistro
from analizadorSaltosRegistro import AnalizadorSaltosRegistro

def main():
    #RUTA 
    RUTA = "ARNL/DATACENTER/HHE.D"  
    
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
    

if __name__ == "__main__":
    main()
