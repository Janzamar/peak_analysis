# Proyecto de Automatización para la Identificación de Sitios de Unión de Factores de Transcripción en E. coli en experimentos de ChIP-Seq

Fecha: 29 de mayo de 2025

Participantes: 

- Jana Noemí Azamar Ramírez  
  jazamar@lcg.unam.mx

## Descripción del Problema

El proyecto busca automatizar la extracción y el análisis de secuencias genómicas donde los factores de transcripción se unen en _Escherichia coli_. Se cuenta con un archivo que contiene información sobre los picos de unión, y con otro archivo que posee la secuencia completa del genoma. El objetivo es generar archivos FASTA específicos para cada factor de transcripción (TF), agrupando las secuencias de los picos de unión correspondientes. 

## Especificación de Requisitos


### Requisitos Funcionales:

#### A. Extracción de Secuencias FASTA:
    
1.  **Entrada de Datos:**
    
    Los archivos siguientes se encuentran en la carpeta principal del repositorio llamada "data".
    -   Genoma completo de E. Coli en formato FASTA.
        Archivo: E_coli_K12_MG1655_U00096.3.txt

    -   Coordenadas de los picos de transcripción en el genoma de E. Coli
        Archivo: union_peaks_file.tsv

    Validar entradas:
    -   Verificación de existencia de los archivos que necesitaremos

2.  **Extracción y Procesamiento de Secuencias:**
    
    -   Leer el archivo de picos para obtener las posiciones de inicio y fin de los picos asociados a cada `TF_name` disponible en el archivo "union_peaks_file.tsv"
    -   Extraer las secuencias desde el archivo FASTA del genoma utilizando las coordenadas `Peak_start` y `Peak_end` del archivo de peaks, asegurándose de considerar solamente la cadena forward. Esta función está en el archivo ejecutable "genome.py"
        En la carpeta Extra_seq_fasta, el ejecutable para esto es "io_utils.py"



3.  **Generación de Archivos FASTA:**
    
    -   Crear archivos FASTA individuales para cada `TF_name`. Los nombres de los archivos deben coincidir con el `TF_name` y usar la extensión `.fa`.
    En la carpeta Extra_seq_fasta, el ejecutable para esto es "io_utils.py"
    -   Almacenar estos archivos en el directorio de salida especificado.
    En la carpeta Extra_seq_fasta, el ejecutable es el archivo "main.py" el cual es modulado para mejorar su funcionamiento.
    Pero también está disponible el archivo orginal (antes de ser modulado) en la carpeta Extra_seq_fasta, en original_script, el ejecutable se llama "extract_fasta.py".
    
    

### **Requisitos No Funcionales:**

-   **Portabilidad y Usabilidad:**
    
    -   Compatible con sistemas Unix/Linux y Windows.
    -   El sistema es ejecutable desde la línea de comandos usando rutas relativas o absolutas y usando argparse.
    -   Todos los datos de entrada a los programas deben pasarse via argumentos.
    -   Si se implementa código debe usarse python o scripts shell.
    
-   **Calidad y Mantenimiento:**
    
    -   Utilización de Git para el seguimiento y revisión del código.
    -   Documentación clara y comentarios efectivos deben acompañar todo el proyecto.
    -   Deben realizarse las pruebas necesarias para la validación correcta del software con archivos fasta de secuencias de nuestro interés más un archivo tabulado de coordenadas como "union_peaks_file.txt".
    - Asegurarnos de tener una carpeta de salida.



### Descripción de Datos de Entrada y Salida 

#### Formato del Archivo de Picos

Este archivo contiene información crucial sobre las regiones de unión de los 144 factores de transcripción (TFs) en _Escherichia coli_. Los datos están organizados en columnas que permiten identificar detalles específicos sobre la unión de los TFs a lo largo del genoma. El formato del archivo y la descripción de cada columna se detallan a continuación:

-   **Dataset_Ids:**
    
    -   _Descripción:_ Identificadores únicos para cada conjunto de datos. Estas IDs indican diferentes experimentos o condiciones bajo las cuales se determinaron los sitios de unión para los TFs.
    -   _Ejemplo:_ "DS001","DS002", etc.

-   **TF_name:**
    
    -   _Descripción:_ El nombre del factor de transcripción que se une al genoma en la región especificada.
    -   _Ejemplo:_ "AraC", "LacI", etc.

-   **Peak_start:**
    
    -   _Descripción:_ La posición inicial en el genoma donde comienza el pico de unión. Se refiere a la ubicación del primer nucleótido del pico.
    -   _Ejemplo:_ 345676, 123456, etc.

-   **Peak_end:**
    
    -   _Descripción:_ La posición final en el genoma donde termina el pico de unión. Se refiere a la ubicación del último nucleótido del pico.
    -   _Ejemplo:_ 345786, 123556, etc.

-   **Peak_center:**
    
    -   _Descripción:_ Posición central del pico de unión, calculada como el promedio o posición entre el `Peak_start` y `Peak_end`.
    -   _Ejemplo:_ 345731, 123501, etc.

-   **Peak_number:**
    
    -   _Descripción:_ Número secuencial utilizado para identificar picos dentro de un conjunto de datos. Esto es útil para referencias internas.
    -   _Ejemplo:_ 1, 2, 3, etc.

-   **Max_Fold_Enrichment:**
    
    -   _Descripción:_ Valor que representa el máximo enriquecimiento observado en el sitio de unión del pico.
    -   _Ejemplo:_ 15.4, 22.3, etc.

-   **Max_Norm_Fold_Enrichment:**
    
    -   _Descripción:_ Valor de máximo enriquecimiento normalizado, ajustado por un factor de control para comparaciones equitativas entre experimentos.
    -   _Ejemplo:_ 12.0, 20.1, etc.

-   **Proximal_genes:**
    
    -   _Descripción:_ Lista de genes cercanos al pico de unión, proporcionando contexto para el análisis funcional.
    -   _Ejemplo:_ "geneA, geneB", "geneX, geneY", etc.
    
-   **Center_position_type:**
    
    -   _Descripción:_ Denota la ubicación genómica del pico central, como intergénica, intrónica, etc.
    -   _Ejemplo:_ "intergénica", "intrónica", etc.




## Análisis y Diseño

#### Módulo 1: Extractor y Creador de Secuencias FASTA

**Objetivo:** Extraer las secuencias genómicas correspondientes a los picos de unión de los factores de transcripción y generar archivos FASTA individuales para cada `TF_name` y guardarlas en una carpeta especifica.

**Flujo de Trabajo:**

1.  **Lectura de Entradas:**
    
    -   Cargar el archivo de picos y el archivo FASTA del genoma.
    -   Obtener el directorio de salida desde la línea de comandos.
2.  **Procesamiento de Datos:**
    
    -   Leer cada fila del archivo de picos.
    -   Extraer los campos `TF_name`, `Peak_start`, `Peak_end` para cada entrada.
    -   Para cada `TF_name`, usar las posiciones `Peak_start` y `Peak_end` para extraer la secuencia correspondiente del archivo FASTA del genoma.
3.  **Generación de FASTA:**
    
    -   Agrupar las secuencias extraídas por `TF_name`.
    -   Crear un archivo FASTA por cada `TF_name` en el directorio de salida con la misma estructura `<TF_name>.fa`.


**Algoritmo**

```
1. Inicio
2. Leer archivo de picos
3. Para cada registro:
   a. Obtener TF_name, Peak_start, Peak_end
   b. Extraer secuencia del genoma usando Peak_start y Peak_end
   c. Agrupar secuencias por TF_name
4. Por cada TF_name:
   a. Crear archivo FASTA
   b. Escribir secuencias en archivo
5. Fin
```
**Arquitectura del código modulado**

- **main.py**
    - Codigo principal y punto de entrada.
    - Se lleva a cabo aquí el flujo de trabajo
    - Se usa argparse para poder interactuar con el código desde la terminal
    - Se hace uso de os para verficar si existen los docs que pedimos y para crear el outdir si no existe el que intrujimos 
    - Se hace uso de sys para terminar el programa si hay un error, este nos dice si hay éxito o no.

- **genome.py**
    - Lectura del archivo del genoma de E. Coli
    - El lector discrimina entre las lineas que empiezan con ">".
    - Se crea con la info de este archivo una secuencia de una sola linea y la devuelve.

- **peaks.py**
    - Lectura del archivo union_peaks_file.tsv
    - Guarda los peaks_starts, peaks_end y el TF_name en una lista.

- **io_utils.py**
    - Primer función "extraer_secuencias"
        -  Guarda las secuencias extraídas para cada TF_name
    
    - Segunda función "guardas_fasta_por_tf"
        - Guardan con cada TF_name las secuencias delimitadas por los peaks_start y los peaks_ends

La arquitectura de los códigos es la siguiente:
C:.
├───bin
│   └───Extra_seq_fasta
│       ├───data
│       │   ├───archivos de prueba
│       │   └───archivos de salida de prueba
│       ├───original_script
│       ├───output_files
│       └───__pycache__
├───data            # aqui se encuentran también los archivos usados en el proyecto.
├───doc
├───results
└───src