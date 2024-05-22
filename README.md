# Video to Text Transcription Tool

## Descripción
Este proyecto proporciona una herramienta para extraer audio de archivos de video y transcribirlo a texto utilizando Python. Utiliza `moviepy` para manejar archivos de video, `pydub` para operaciones de audio y `speech_recognition` para convertir audio a texto.

## Características
- Extrae audio de archivos de video.
- Divide el audio en segmentos de 1 minuto para una mejor gestión.
- Transcribe audio a texto utilizando la API de Google Speech Recognition.
- Guarda la transcripción en un archivo de texto.

## Requisitos
- Python 3.6 o superior
- moviepy
- SpeechRecognition
- pydub
- ffmpeg

## Instalación

### Clonar el Repositorio
Primero, clona este repositorio a tu máquina local usando:
```bash
git remote add origin git@github.com-ncastellanos:nelsonCastellanos/Video-to-Text-Transcription.git
git clone  git@github.com-ncastellanos:nelsonCastellanos/Video-to-Text-Transcription.git

cd tu-repositorio
```

### Instalar Dependencias
Instala las dependencias necesarias ejecutando:
```bash
pip install -r requirements.txt
```

### Instalar FFmpeg
Asegúrate de que `ffmpeg` está instalado y configurado correctamente en tu sistema. Las instrucciones varían según el sistema operativo:

#### Windows
- Descarga FFmpeg desde [ffmpeg.org](https://ffmpeg.org/download.html).
- Descomprime y añade la carpeta `bin` al PATH de tu sistema.

#### macOS
Utiliza Homebrew:
```bash
brew install ffmpeg
```

#### Linux
Para Ubuntu/Debian:
```bash
sudo apt-get install ffmpeg
```

## Uso
Para transcribir audio de un archivo de video a texto, ejecuta el script principal:
```bash
python transcribe_video.py --video tu_video.mp4
```

## Contribuir
Las contribuciones son bienvenidas! Por favor, lee `CONTRIBUTING.md` para más detalles sobre cómo contribuir y enviar pull requests al proyecto.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ve el archivo `LICENSE.md` para más detalles.