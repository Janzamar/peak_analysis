"""Función para leer el archivo fasta de E. Coli en este caso nuestro"""
def cargar_genoma(fasta_path):
    """Carga el genoma desde un archivo FASTA y devuelve una única cadena de texto."""
    secuencias = []  # Lista donde se guardarán las secuencias del genoma
    with open(fasta_path, "r") as archivo_geno:  # Así abrimos el archivo FASTA en modo lectura
        for linea in archivo_geno:
            if not linea.startswith(">"):  # Si la línea no comienza con ">", significa que es parte de una secuencia
                secuencias.append(linea.strip())  # Eliminamos espacios innecesarios al principio y al final de cada línea
    return "".join(secuencias)  # Devolvemos todas las secuencias como una sola cadena, sin \n