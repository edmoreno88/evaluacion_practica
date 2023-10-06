# Función para contar las líneas totales del archivo
def contar_lineas(archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
        return len(lineas)

# Función para contar las palabras totales del archivo
def contar_palabras(archivo):
    with open(archivo, 'r') as file:
        contenido = file.read()
        palabras = contenido.split()
        return len(palabras)

# Función para contar los caracteres totales del archivo
def contar_caracteres(archivo):
    with open(archivo, 'r') as file:
        contenido = file.read()
        return len(contenido)

# Función para contar el número de veces que aparece una palabra en el archivo
def contar_apariciones(archivo, palabra):
    with open(archivo, 'r') as file:
        contenido = file.read()
        return contenido.lower().count(palabra.lower())

# Nombre del archivo de entrada y salida
archivo_entrada = "entrada.txt"
archivo_salida = "salida.txt"

# Palabra que deseas contar en el archivo
palabra_a_contar = "camilo"

# Calcular las estadísticas
num_lineas = contar_lineas(archivo_entrada)
num_palabras = contar_palabras(archivo_entrada)
num_caracteres = contar_caracteres(archivo_entrada)
num_apariciones = contar_apariciones(archivo_entrada, palabra_a_contar)

# Escribir las estadísticas en el archivo de salida
with open(archivo_salida, 'w') as file:
    file.write(f"Líneas totales: {num_lineas}\n")
    file.write(f"Palabras totales: {num_palabras}\n")
    file.write(f"Caracteres totales: {num_caracteres}\n")
    file.write(f"Apariciones de '{palabra_a_contar}': {num_apariciones}\n")

print("Las estadísticas se han guardado en 'salida.txt'.")