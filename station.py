from obspy import read, UTCDateTime

ruta = "ARNL/STATION/2024094/30444/1/070000000000_000D693A400.MSD"
stream = read(ruta)
canal_gap = "HHN"
# Changed gap_start and gap_end per specification
gap_start = UTCDateTime("2024-04-03T00:00:00")
gap_end = UTCDateTime("2024-04-03T23:59:59.990000")

def encontrar_traza_o_stream(stream, canal_gap, gap_start, gap_end):
    # Buscar traza individual que cumpla los criterios
    for trace in stream:
        if (trace.stats.channel == canal_gap and 
            trace.stats.starttime <= gap_start and 
            trace.stats.endtime >= gap_end):
            return ("trace", trace)
    # Si ninguna traza individual, verificar si el stream completo cumple
    if (stream[0].stats.channel == canal_gap and 
        stream[0].stats.starttime <= gap_start and 
        stream[-1].stats.endtime >= gap_end):
        return ("stream", stream)
    return (None, None)

tipo, encontrado = encontrar_traza_o_stream(stream, canal_gap, gap_start, gap_end)
if tipo == "trace":
    print("Trace encontrada:")
    print(encontrado)
elif tipo == "stream":
    print("Stream completo encontrado:")
    print(encontrado)
else:
    print("No se encontró traza ni stream que cumpla con los criterios.")