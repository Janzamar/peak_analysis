# Extracción de secuencias en formato Fasta. Inciso A

# Usaré la estructura sugerida en la entrega del proyecto

# Función para leer el archivo fasta de E. Coli
def cargar_genoma(fasta_path):
    """Carga el genoma desde un archivo FASTA y devuelve una única cadena de texto."""
    secuencias = []  # Lista donde se guardarán las secuencias del genoma
    with open(fasta_path, "r") as archivo_geno:  # Abrimos el archivo FASTA en modo lectura
        for linea in archivo_geno:
            if not linea.startswith(">"):  # Si la línea no comienza con ">", significa que es parte de una secuencia
                secuencias.append(linea.strip())  # Eliminamos espacios innecesarios al principio y al final de cada línea
    return "".join(secuencias)  # Devolvemos todas las secuencias como una cadena de texto concatenada

# Función para leer el archivo de picos
def leer_achivo_picos(peak_path):
    """Lee el archivo de picos y devuelve una lista de diccionarios con TF_name, start y end."""
    peaks = []  # Lista donde se guardarán los datos de los picos (TF_name, start y end)
    with open(peak_path, "r") as archivo_peak:  # Abrimos el archivo de picos
        next(archivo_peak)  # Ignoramos la cabecera del archivo (primera línea)
        for linea in archivo_peak:  # Recorremos cada línea del archivo de picos
            # Dividimos cada línea en columnas usando el delimitador tabulador (\t)
            columnas = linea.strip().split("\t")  # La información en el archivo de picos está separada por tabuladores
            TF_name = columnas[1]  # El nombre del factor de transcripción está en la segunda columna
            peak_start = int(float(columnas[2]))  # La coordenada de inicio del pico está en la tercera columna
            peak_end = int(float(columnas[3]))  # La coordenada de fin del pico está en la cuarta columna
            # Almacenamos los datos extraídos en un diccionario y lo agregamos a la lista 'peaks'
            peaks.append({"TF_name": TF_name, "Peak_start": peak_start, "Peak_end": peak_end})
    return peaks  # Devolvemos la lista de picos con los datos extraídos

# Función para obtener las secuencias del genoma según las coordenadas de los picos
def extraer_secuencias(peak_data, genoma):
    """Agrupa las secuencias extraídas por TF_name en un diccionario."""
    secuencias_por_tf_name = {}  # Diccionario donde las claves son los TF_names y los valores son listas de secuencias
    for peak in peak_data:  # Recorremos cada pico en los datos extraídos
        tf = peak["TF_name"]  # Nombre del factor de transcripción
        start = int(peak["Peak_start"])  # Coordenada de inicio del pico (convertido a entero)
        end = int(peak["Peak_end"])  # Coordenada de fin del pico (convertido a entero)

        # Extraemos la secuencia del genoma en el rango indicado por las coordenadas del pico
        secuencia = genoma[start:end]  # Secuencia extraída del genoma entre las coordenadas de inicio y fin

        # Si el TF_name no existe aún en el diccionario, lo inicializamos con una lista vacía
        if tf not in secuencias_por_tf_name:
            secuencias_por_tf_name[tf] = []

        # Añadimos la secuencia extraída a la lista correspondiente al TF_name
        secuencias_por_tf_name[tf].append(secuencia)
    return secuencias_por_tf_name  # Devolvemos el diccionario con las secuencias agrupadas por TF_name

# Función para guardar los archivos FASTA por TF_name
def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
    """Guardar archivos FASTA separados por cada TF_name."""
    for tf_name, secuencias in secuencias_por_tf.items():  # Recorremos el diccionario de secuencias por TF_name
        nombre_archivo = output_dir + "/" + tf_name + ".fa"  # Construimos el nombre del archivo FASTA para cada TF_name
        with open(nombre_archivo, "w") as archivo:  # Abrimos el archivo en modo escritura
            for i, secuencia in enumerate(secuencias):  # Recorremos cada secuencia asociada al TF_name
                header = f">{tf_name}_peak_{i+1}"  # Creamos el encabezado en formato FASTA, que incluye el nombre del TF y el número del pico
                archivo.write(f"{header}\n{secuencia}\n")  # Escribimos el encabezado y la secuencia en el archivo FASTA

# Función principal
def main():
    """Principal que orquesta la ejecución del script."""
    # Pedimos al usuario que introduzca las rutas de los archivos y la carpeta de salida
    fasta_path = input("Introduce el nombre del archivo FASTA que vayas a utilizar: ")
    peaks_path = input("Introduce el nombre del archivo de picos que vayas a utilizar: ")
    output_dir = "C:\\Users\\asus\\OneDrive\\Documents\\AAAEstudiar LCG\\peak_analysis\\bin\\Extra_seq_fasta\\archivos de salida"

    # Usamos las funciones previamente definidas para cargar el genoma y los picos
    genoma = cargar_genoma(fasta_path)
    peaks_data = leer_achivo_picos(peaks_path)
    secuencias_extraidas = extraer_secuencias(peaks_data, genoma)

    # Guardamos las secuencias extraídas en archivos FASTA separados por TF_name
    guardar_fasta_por_tf(secuencias_extraidas, output_dir)

# Así jecutamos la función principal 
if __name__ == "__main__":
    main()
