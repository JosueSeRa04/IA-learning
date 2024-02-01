import speech_recognition as sr
from BuscadorNavegador import realizar_busqueda_en_navegador

palabraClave = ["Buscar", "Busca", "Buscador", "Buscando", "Buscá", "Buscáme", "Buscame","Búscame"]

def reconocer_audio(nombre_archivo):
    recognizer = sr.Recognizer()

    with sr.AudioFile(nombre_archivo) as source:
        audio_data = recognizer.record(source, duration=5)
    try:
        texto = recognizer.recognize_google(audio_data, language="es-ES")
        print("Texto reconocido:", texto)
        for palabraPrueba in palabraClave:
            if palabraPrueba.lower() in texto.lower():
                nuevo_texto = texto.replace(palabraPrueba, " ")
                realizar_busqueda_en_navegador(nuevo_texto)
                continue
            else:
                nuevo_texto = texto


    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))
