# README - Extracción de Secuencias de Unión a Factores de Transcripción

## Descripción del proyecto:
El objetivo de este proyecto es extraer secuencias genómicas en archivos de formatos FASTA, estas siendo de datos de experimentos realizados con ChIP-Seq, y volverlos archivos FASTA individuales para cada uno de los Factores de Transcripción (TFs) que hay en _Escherichia Coli_

## Requisitos 
- Python ver 3.6 
- Sistema operativo Unix/Linux
- Uso de comandos Unix

## Instalación 
Usar el siguiente comando en la terminal CMD git para clonar el repositorio y abrirlo.
`` git clone https://github.com/Janzamar/peak_analysis``

## Uso de script 

### Ejecución del main.py
`` python main.py -f formato.fasta -p peaks_file.tsv -o output_dir``

Glosario:

"- f": Ruta de acceso al archivo FASTA 

"-p": Ruta de acceso al archivo de peaks

"-o": Ruta del directorio donde se guardarán los archivos FASTA extraídos


Estos tres puntos son requeridos para ejecutar _main.py_.

## Estructura del proyecto

``
Peak_analysis                                                                       
├───bin
│   └───Extra_seq_fasta
│       │   genome.py
│       │   io_utils.py
│       │   main.py
│       │   main_prueba.py
│       │   peaks.py
│       │
│       ├───data
│       │   │   E_coli_K12_MG1655_U00096.3.txt
│       │   │   union_peaks_file.tsv
│       │   │
│       │   ├───archivos de prueba # literalmente son archivos únicamente de prueba
│       │   │       archivo_picos.tsv
│       │   │       geno_ecoli.fa
│       │   │
│       │   └───archivos de salida de prueba
│       │
│       ├───original_script
│       │       extract_fasta.py
│       │
│       ├───output_files
│       └───__pycache__
│               genome.cpython-313.pyc
│               io_utils.cpython-313.pyc
│               peaks.cpython-313.pyc
│
├───data
│       E_coli_K12_MG1655_U00096.3.txt
│       U00096.3.bfile
│       union_peaks_file.tsv
│
├───doc
│       detalles_proyecto.md
│       README_TF_Binding_Project.md
│       test_cases.md
│
├───results
│       .gitkeep
│
└───src
        .gitkeep
``
