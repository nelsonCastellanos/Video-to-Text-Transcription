from moviepy.editor import VideoFileClip
import speech_recognition as sr
from pydub import AudioSegment
import os
import concurrent.futures

# Función para extraer audio de un video
def extract_audio(video_path, audio_path='temp_audio.wav'):
    if not os.path.exists(audio_path):
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        video.close()
    return audio_path

# Función para transcribir un chunk
def transcribe_chunk(chunk, index, recognizer):
    chunk_path = f"chunk{index}.wav"
    chunk.export(chunk_path, format="wav")
    text = ""
    try:
        with sr.AudioFile(chunk_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='es-ES') + " "
    except sr.UnknownValueError:
        print(f"No se pudo entender el audio del chunk {index}")
    except sr.RequestError as e:
        print(f"Error de solicitud: {e}")
    return index, text  # Devuelve el índice con el texto

# Función principal para transcribir audio
def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_wav(audio_path)
    chunks = list(audio[::60000])  # Dividir el audio en chunks de 1 minuto

    transcriptions = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_index = {executor.submit(transcribe_chunk, chunk, i, recognizer): i for i, chunk in enumerate(chunks)}
        for future in concurrent.futures.as_completed(future_to_index):
            index, text = future.result()
            transcriptions[index] = text

    # Escribir todo en un archivo en orden
    with open('transcription.txt', 'w') as f:
        for i in sorted(transcriptions.keys()):
            f.write(transcriptions[i])

    return "Transcripción completada y guardada en archivo."

# Ruta al archivo de video
video_path = 'tu_video.mp4'

# Extraer audio del video
audio_path = extract_audio(video_path)

# Transcribir el audio a texto y guardarlo en un archivo
result = transcribe_audio(audio_path)
print(result)
