#Extracción de secuencias en formato Fasta. Inciso A

# Usaré la estructura sugerida en la entrega del proyecto

# Función para leer el archivo fasta de E. Coli
def cargar_genoma(fasta_path):
    """Carga el genoma desde un archivo FASTA y devuelve una única cadena de texto."""
    secuencias = []  # Lista donde se guardarán las secuencias del genoma
    with open(fasta_path, "r") as archivo_geno:  # Así abrimos el archivo FASTA en modo lectura
        for linea in archivo_geno:
            if not linea.startswith(">"):  # Si la línea no comienza con ">", significa que es parte de una secuencia
                secuencias.append(linea.strip())  # Eliminamos espacios innecesarios al principio y al final de cada línea
    return "".join(secuencias)  # Devolvemos todas las secuencias como una sola cadena, sin \n

# Función para leer el archivo de picos
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

# Función para obtener las secuencias del genoma según las coordenadas de los picos
def extraer_secuencias(peak_data, genoma):
    """Agrupa las secuencias extraídas por TF_name en un diccionario."""
    secuencias_por_tf_name = {}  # Diccionario donde guardaremos los TF_names y sus secuencias
    for peak in peak_data:  # Recorremos cada pico en los datos extraídos
        tf = peak["TF_name"]  # variable para cada nombre del tf
        start = peak["Peak_start"]  # Coordenada de inicio del pico 
        end = peak["Peak_end"]  # Coordenada de fin del pico 


        # Extraemos la secuencia del genoma dada por las coordenadas del archivo de peaks
        secuencia = genoma[start:end]  # Secuencia extraída del genoma entre las coordenadas de inicio y fin

        # Decimos que: si el TF_name no existe aún en el diccionario, lo inicializamos con una lista vacía y se agrega
        if tf not in secuencias_por_tf_name:
            secuencias_por_tf_name[tf] = []

        # Añadimos la secuencia extraída a la lista correspondiente al TF_name
        secuencias_por_tf_name[tf].append(secuencia)
    return secuencias_por_tf_name  # Devolvemos el diccionario con las secuencias agrupadas por TF_name

# Función para guardar los archivos FASTA por TF_name
def guardar_fasta_por_tf(secuencias_por_tf, peak_data, output_dir):
    """Guardar archivos FASTA separados por cada TF_name."""
    for tf_name, secuencias in secuencias_por_tf.items():  # Recorremos el diccionario de secuencias por TF_name
        nombre_archivo = output_dir + "/" + tf_name + ".fa"  # Construimos el nombre del archivo FASTA para cada TF_name
        with open(nombre_archivo, "w") as archivo:  # Abrimos el archivo en modo escritura
            for i, secuencia in enumerate(secuencias):  # Recorremos cada secuencia asociada al TF_name
                header = f">{tf_name}\npeak_{i+1}_start_{peak_data[i]['Peak_start']}\npeak_end_{peak_data[i]['Peak_end']}"  # Creamos el encabezado en formato FASTA, que incluye el nombre del TF y el número del pico
                archivo.write(f"{header}\n{secuencia}\n")  # Escribimos el encabezado y la secuencia en el archivo FASTA
    return secuencias_por_tf


# Función principal

def main():
    """Principal que orquesta la ejecución del script."""
    fasta_path = ("geno_ecoli.fa") #mod1
    peaks_path = ("archivo_picos.tsv") #mod2
    output_dir = input("Ingresa la Ruta absoluta de la carpeta donde quieres tus outputs: ")


    try: # uso el try para evitar que se ejecute todo el código si no existen los archivos con los cuales trabajar, si existe, se ejecuta lo siguiente
        # Usamos las funciones definidas para cargar el genoma y los peaks
        genoma = cargar_genoma(fasta_path)
        peaks_data = leer_achivo_peak(peaks_path)
        secuencias_extraidas = extraer_secuencias(peaks_data, genoma)

        # Guardamos las secuencias extraídas en archivos FASTA separados por TF_name
        guardar_fasta_por_tf(secuencias_extraidas, peaks_data, output_dir)
        print("Secuencias extraídas y guardadas correctamente.")
    except Exception as e:  # si los archivos no existen, se imprime a pantalla esto
        print(f"Ocurrió un error durante la ejecución: {e}") # la e significa excepción



if __name__ == "__main__":
    main()