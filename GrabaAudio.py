import pyaudio
import wave
from ReconocimientoVoz import reconocer_audio

def grabar_audio(nombre_archivo, duracion_segundos, frecuencia_muestreo=44100, formato=pyaudio.paInt16, canales=1):
    chunk = 1024 # Tamaño del bloque de audio
    p = pyaudio.PyAudio() # Configura el sistema de PortAudio

    # Abre el stream para la grabacion
    stream = p.open(format=formato,
                    channels=canales,
                    rate=frecuencia_muestreo,
                    input=True,
                    frames_per_buffer=chunk)
    
    print("Grabando...")

    frames = [] # Lista para almacenar los frames

    # Grabación de audio
    for i in range(0, int(frecuencia_muestreo / chunk * duracion_segundos)):
        data = stream.read(chunk)
        frames.append(data)

    print("Grabación finalizada.")

    # Detiene y cierra el stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Guarda la grabación en un archivo WAV

    wf = wave.open(nombre_archivo, 'wb')
    wf.setnchannels(canales)
    wf.setsampwidth(p.get_sample_size(formato))
    wf.setframerate(frecuencia_muestreo)
    wf.writeframes(b''.join(frames))
    wf.close()
