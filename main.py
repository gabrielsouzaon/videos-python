import os
import yt_dlp

arquivovideos = "VideosBaixados"
if not os.path.exists(arquivovideos):
    os.makedirs(arquivovideos)

# função para fazer as conveções pra fazer dowload | com o parametro URL - LINK 
def download_video(url):
    YTP = {
        'outtmpl': os.path.join(arquivovideos, '%(title)s.%(ext)s'), 
}
    try:
        with yt_dlp.YoutubeDL(YTP) as ydl:
            ydl.download([url])
        print("Download concluído! O vídeo está salvo na pasta:", arquivovideos)
    except Exception as e:
        print("Ocorreu um erro durante o download:", e)

video_url = input("Cole aqui a sua URL: ")
download_video(video_url)
