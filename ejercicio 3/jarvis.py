import pyttsx3
import os

# Función para convertir texto a voz y guardar el audio
def convertir_texto_a_voz(texto, archivo_audio):
    engine = pyttsx3.init()
    engine.save_to_file(texto, archivo_audio)
    engine.runAndWait()

if __name__ == "__main__":
    # Nombre del archivo de texto de entrada y archivo de audio de salida
    archivo_texto = "texto.txt"
    archivo_audio = "audio.wav"

    # Leer el texto del archivo de entrada
    try:
        with open(archivo_texto, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
    except FileNotFoundError:
        print(f"El archivo {archivo_texto} no se encontró.")
    else:
        # Convertir el texto a voz y guardar el audio
        convertir_texto_a_voz(texto, archivo_audio)
        print(f"Texto convertido a voz y guardado en {archivo_audio}")