from obspy import read, UTCDateTime
from obspy import UTCDateTime

ruta = "PPLP\STATION\data\EC-PPLP_4-20230308040459"
stream = read(ruta)

# Define el tiempo a verificar (ajusta la fecha y hora según necesites)
tiempo_a_verificar = UTCDateTime("2023-03-08T03:05:00")

for traza in stream:
    if traza.stats.channel == "HHN":
        # Verifica si el tiempo a verificar se encuentra entre starttime y endtime
        if traza.stats.starttime <= tiempo_a_verificar <= traza.stats.endtime:
            print(f"El tiempo {tiempo_a_verificar} está dentro de la traza: {traza.stats}")
        else:
            print(f"El tiempo {tiempo_a_verificar} NO está dentro de la traza: {traza.stats}")

