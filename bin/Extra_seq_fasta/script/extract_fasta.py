# Extracción de secuencias en formato Fasta. Inciso A

# Usaré la estructura sugerida en la entrega del proyecto

# Función para leer el archivo fasta de E. Coli
def cargar_genoma(fasta_path):
    """Carga el genoma desde un archivo FASTA y devuelve una única cadena de texto."""
    secuencia = [] # lista donde se guardará la secuencia sin saltos de líneas, solo siendo un renglón
    with open(fasta_path, "r") as archivo_geno: # función para leer el archivo de interés
        for linea in archivo_geno:
            if not linea.startswith(">"): # aquí queremos decir que si la línea empieza con >, la ignoramos
                secuencia.append(linea.strip()) # se guardan las secuencias y se eliminan los espacios al inicio o al final de la secuencia
    return "".join(secuencia) # se devuelve la secuencia de una sola cadena ya completa

# Función para leer el archivo de picos
def leer_achivo_picos(peak_path):
     """Lee el archivo de picos y devuelve una lista de diccionarios con TF_name, start y end."""
     peaks = [] # lista donde se guardará TF_name, el peak start y end
     with open (peak_path, "r") as archivo_peak: # leemos el archivo de picos
         next(archivo_peak) # así ignoramos la primer columna donde están los nombres
         for linea in archivo_peak: # leemos por linea en el archivo de interés
             # dividimos en columnas la info que viene en el archivo
             columnas = linea.strip().split("\t") #usamos .split con el \t porque así es como se dividen las columnas en el archivo
             TF_name = columnas[1] # extraemos los TF_names que se encuentran en la primer columna (por eso es [1])
             peak_start = float(columnas[2]) # extraemos la coordenada que se encuentra en la columna dos. Uso float porque no todos son enteros
             peak_end = float(columnas[3]) # extraemos coordenadas que se encuentran en la columna 3
             # se crea diccionario con .append, para que se ordene todo en la lista con la info que ya extrajimos
             peaks.append({"TF_name: ": TF_name, "Peak_start: ": peak_start, "Peak_end: ": peak_end})
        return peaks; # se regresaría la lista  

# Función para obtener los tf_names y ponerlos en un diccionario
def extraer_secuencias(peak_data, genoma):
    """Agrupa las secuencias extraídas por TF_name en un diccionario."""
    secuencias_por_tf_name = {} # creación de diccionario donde estarán los peak start y end y el nombre
    for peak in peak_data:
        tf = peak["TF_name"]
        start = peak["Peak_start"]
        end = peak["Peak_end"]
        
        # Variable para guardar la secuencia del genoma
        secuencia = genoma[start:end] # así solo obtenemos la secuencia donde está el peak del inicio y del final según las coordenadas que ya tenemos 

        return secuencias_por_tf_name

#función para hacer un archivo fasta para cada tf_name
#def guardar_fasta_por_tf(secuencias_por_tf, output_dir):
 #   ""Guardar archivos FASTA separados por cada TF_name."" 




#""Principal que orquesta la ejecución del script.""
