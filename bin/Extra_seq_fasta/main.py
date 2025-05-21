from genome import cargar_genoma
from io_utils import extraer_secuencias, guardar_fasta_por_tf
from peaks import leer_achivo_peak
""" Función principal, aquí todos los otros códigos convergen, se les llama y se importan sus funciones"""

def main():
    """Principal que orquesta la ejecución del script."""
    fasta_path = ("E_coli_K12_MG1655_U00096.3.txt") #mod1
    peaks_path = ("union_peaks_file.tsv") #mod2
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