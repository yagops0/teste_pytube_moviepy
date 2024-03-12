from os import *

from pytube import YouTube
from moviepy.editor import *

from pytube import YouTube
from moviepy.editor import AudioFileClip

# URL do vídeo do YouTube
url = str(input("Cole a url do vídeo que deseja baixar o áudio: "))

# Cria um objeto YouTube
yt = YouTube(url)


# Baixa apenas o áudio
yt.streams.filter(only_audio=True)  # Salvando como .mp4
yt.streams.filter(file_extension="mp4")

audio = yt.streams.get_audio_only().download(filename=yt.title)

# Convertendo para MP3 usando moviepy
clip = AudioFileClip(audio)
clip.write_audiofile(f"C:/Users/yagos/OneDrive/Documentos/Programacao/Python/Testes/teste_pytube3/{yt.title}.mp3")

# Excluindo o arquivo .mp4 após a conversão
remove(audio)


