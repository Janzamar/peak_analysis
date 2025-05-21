""" Función para leer el archivo de picos que usaremos"""
def leer_achivo_peak(peak_path):
    """Lee el archivo de picos y devuelve una lista de diccionarios con TF_name, start y end."""
    peaks = []  # Lista donde se guardarán los datos de los picos (TF_name, start y end)
    with open(peak_path, "r") as archivo_peak:  # Abrimos el archivo de picos para lectura
        next(archivo_peak)  # Ignoramos la cabecera del archivo (primera línea)
        for linea in archivo_peak:  # Recorremos cada línea del archivo de picos
            # Dividimos cada línea en columnas usando el delimitador tabulador (\t)
            columnas = linea.strip().split("\t")  # La información en el archivo de picos está separada por tabuladores
            TF_name = columnas[2].strip()  # El nombre del factor de transcripción está en la segunda columna
            peak_start = int(float(columnas[3].strip()))  # La coordenada de inicio del pico está en la tercera columna
            peak_end = int(float(columnas[4].strip()))  # La coordenada de fin del pico está en la cuarta columna
            # Almacenamos los datos extraídos en un diccionario y lo agregamos a la lista 'peaks'
            peaks.append({"TF_name": TF_name, 
                          "Peak_start": peak_start, "Peak_end": peak_end})
    return peaks  # Devolvemos la lista de picos con los datos extraídos