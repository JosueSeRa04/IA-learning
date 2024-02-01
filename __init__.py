from GrabaAudio import grabar_audio, reconocer_audio

# Parametos de grabacion
nombre_archivo = "PruebaGrabacion.wav"
duracion_segundos = 5

# Llama a la funcion para grabar audio
grabar_audio(nombre_archivo, duracion_segundos)

texto = reconocer_audio(nombre_archivo)
# Fin del programa
