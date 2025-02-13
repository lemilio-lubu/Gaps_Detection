from analizador_consistencia_global import AnalizadorConsistenciaGlobal  
from analizador_muestras_registro import AnalizadorMuestrasRegistros
from analizador_continuidad_registro import AnalizadorContinuidadRegistro
from analizador_saltos_registro import AnalizadorSaltosRegistro

class PipelineAnalisis:
    def __init__(self, ruta):
        self.analizadores = [
            AnalizadorConsistenciaGlobal(ruta),
            AnalizadorContinuidadRegistro(ruta),
            AnalizadorSaltosRegistro(ruta),
            AnalizadorMuestrasRegistros(ruta)
        ]
    
    def analizar(self):
        resultados = {}

        for analizador in self.analizadores:
            resultado = analizador.analizar_stream_sismico()  
            resultados[analizador.__class__.__name__] = resultado 

        return self.sintetizar_resultados(resultados)
    
    def sintetizar_resultados(self, resultados):
        """
        Sintetiza los resultados de los analizadores, manteniendo el formato original.
        """
        gaps_comunes = []
        saltos_atipicos = []

        # Extraer los datos de los analizadores
        for nombre, anomalías in resultados.items():
            if nombre == "AnalizadorSaltosRegistro":
                saltos_atipicos = anomalías  # Guardamos los saltos inusuales
            else:
                # Agregar anomalías manteniendo el formato original
                for anomalia in anomalías:
                    if anomalia not in gaps_comunes:
                        gaps_comunes.append(anomalia)

        # Generar resumen final con el formato requerido
        resumen = {
            "gaps_comunes": gaps_comunes,
            "saltos_atipicos": saltos_atipicos
        }

        return resumen
