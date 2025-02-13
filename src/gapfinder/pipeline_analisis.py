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

        return resultados 