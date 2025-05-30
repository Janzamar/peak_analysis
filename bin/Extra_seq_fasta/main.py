import argparse
import sys
import os
from genome import cargar_genoma
from io_utils import extraer_secuencias, guardar_fasta_por_tf
from peaks import leer_achivo_peak
""" Función principal, aquí todos los otros códigos convergen, se les llama y se importan sus funciones"""

def main():
    """Principal que orquesta la ejecución del script."""
    parser = argparse.ArgumentParser(description="Extrae secuencias desde un genoma y archivo de peaks, y guarda por TF.")
    
    parser.add_argument('-f', '--fasta', required=True, help='Ruta al archivo FASTA del genoma')
    parser.add_argument('-p', '--peaks', required=True, help='Ruta al archivo TSV de peaks')
    parser.add_argument('-o', '--output', required=True, help='Ruta a la carpeta de salida')
    
    args = parser.parse_args()

    # Usamos argumentos en lugar de input() como anteriormente se hacía
    fasta_path = args.fasta
    peaks_path = args.peaks
    output_dir = args.output

      # Verificamos que el archivo FASTA exista
    if not os.path.isfile(fasta_path):
        print(f"Error: El archivo FASTA '{fasta_path}' no existe.")
        sys.exit(1)  # Salir con código 1 para indicar error

    # Verificamos que el archivo de peaks exista
    if not os.path.isfile(peaks_path):
        print(f"Error: El archivo de peaks '{peaks_path}' no existe.")
        sys.exit(1)

    # Verificarmos que la carpeta de salida exista, si no, crearla
    if not os.path.isdir(output_dir):
        print(f"La carpeta de salida '{output_dir}' no existe. En creación...")
        try:
            os.makedirs(output_dir) # esta linea crea la carpeta si es que la solicitamos no existe
        except Exception as e:
            print(f"No se pudo crear la carpeta de salida: {e}")
            sys.exit(1)


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