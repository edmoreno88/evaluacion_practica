import random

#creamos las variables cadena de texto
minus = "abcdefghijklmnopqrstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos ="@()[]{}*,;/-_¿?.¡!$<#>$+%="

base = minus+mayus+numeros+simbolos
longitud = 8

#creamos la variable muestra y password
muestra =random.sample(base, longitud)
password = "".join(muestra)
print(password)


# Mostrar la contraseña en la consola
print("Contraseña generada:", password)

# Guardar la contraseña en un archivo de texto plano
with open("contraseña.txt", "w") as archivo:
    archivo.write(password)

print("Contraseña guardada en 'contraseña.txt'")