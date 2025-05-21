"""Función para obtener las secuencias del genoma según las coordenadas de los picos dadas en el archivo seleccionado"""
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


"""" Función para guardar los archivos FASTA por su TF_name dado el archivo de nuestra elección"""
def guardar_fasta_por_tf(secuencias_por_tf, peak_data, output_dir):
    """Guardar archivos FASTA separados por cada TF_name."""
    for tf_name, secuencias in secuencias_por_tf.items():  # Recorremos el diccionario de secuencias por TF_name
        nombre_archivo = output_dir + "/" + tf_name + ".fa"  # Construimos el nombre del archivo FASTA para cada TF_name
        with open(nombre_archivo, "w") as archivo:  # Abrimos el archivo en modo escritura
            for i, secuencia in enumerate(secuencias):  # Recorremos cada secuencia asociada al TF_name
                header = f">{tf_name}\npeak_{i+1}_start_{peak_data[i]['Peak_start']}\npeak_end_{peak_data[i]['Peak_end']}"  # Creamos el encabezado en formato FASTA, que incluye el nombre del TF y el número del pico
                archivo.write(f"{header}\n{secuencia}\n")  # Escribimos el encabezado y la secuencia en el archivo FASTA
    return secuencias_por_tf