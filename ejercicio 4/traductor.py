from PIL import Image
from pytesseract import *
from translate import Translator

#Busca la instalacion del tesseract OCR
pytesseract.tesseract_cmd = r'C:\Users\ecmorenom\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

img = Image.open("image.png")

resultado = pytesseract.image_to_string(img)

print(resultado)

trad = Translator(
    from_lang="english",
    to_lang="spanish")
txt = resultado
res= trad.translate(txt)
print (res)

# Nombre del archivo de entrada y salida
archivo_salida ="traduccion.txt"

# Escribir las estadísticas en el archivo de salida
with open(archivo_salida, 'w') as file:
    file.write(f"Texto traducido: {res}")

print("La traduccion de la imagen se han guardado en 'traduccion.txt'.")
