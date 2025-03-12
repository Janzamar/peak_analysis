### Casos de Prueba para el Módulo 1: Extractor y Creador de Secuencias FASTA


1.  **Caso: Archivo del genoma no se encuentra.**
    
    -   **Entradas:**
        -   Ruta incorrecta o inexistente para el archivo FASTA del genoma.
        -   Archivo de picos válido.
        -   Directorio de salida.
    -   **Esperado:** `"Error: Genome file not found"`
    
    ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
    ```
    ```
    Error: "Ecoli.fna" genome file not found
    ```
2.  **Caso: Archivo de picos vacío.**
    
    -   **Entradas:**
        -   Archivo de picos vacío.
        -   Archivo FASTA del genoma.
        -   Directorio de salida.
    -   **Esperado:** `"Error: the peak file is empty."`

 ```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```
  
```
Error: the peak file is empty
```

3.  **Caso: Posiciones `Peak_start` y `Peak_end` fuera del rango del genoma.**
    
    -   **Entradas:**
        -   Archivo de picos con algunas posiciones `Peak_start` y `Peak_end` fuera del tamaño del genoma.
        -   Archivo FASTA del genoma válido.
        -   Directorio de salida.
    -   **Esperado:**
        -   El sistema debe imprimir un mensaje de advertencia: `"Warning: Some peaks are bigger than the genome". Check the log.out file`
        
        -   Generar un archivo de log indicando los picos fuera de rango. El archivo debe contener las líneas del archivo de picos que tienen problemas.

```python
    mk_fasta_from_peaks.py -i peak_file.txt -g Ecoli.fna -o fasta_peaks/ 
```

```bash
ls
```

```bash
log.out
fasta_peaks/
```

4. ** Caso: El archivo log.out del inciso anterior esté vacío **
	**Entradas:**
	- El archivo **log.out** que contiene los peaks que están fuera del genoma esté vacío, pero sí se haya generado el archivo y aparezca 

	**Esperado:**
	- Poder hacer una función que cheque si el archivo fue hecho correctamente y si no es así, que lo genere de nuevo

5. ** Caso: Archivo de genoma vacío **
	**Entradas:**
	- Archivo del genoma está vacío aunque sí se encuentre el archivo en una dirección existente

	**Esperado:**
	- El sistema debe imprimir un error que diga:  `"Warning: This file is empty. Try with another file"`

6. ** Caso: No haya peak start ni peak end**
	**Entradas:**
	- Archivo de genoma válido
	- Archivo de picos no tiene posiciones de `Peak_start` y `Peak_end` en ninguna parte del genoma

**Esperado:**
	- El sistema debe imprimir un error que diga:  `"Peak start and peak end does not exist in this file "`
