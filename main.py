from pytubefix import YouTube
from pytubefix.cli import on_progress
import os


def list_downloaded_audios():
    """
    Lit la liste des titres des audios déjà téléchargés depuis un fichier.
    Crée le fichier s'il n'existe pas.
    """
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    file_path = 'downloads/audio_list.txt'

    if not os.path.exists(file_path):
        open(file_path, 'w', encoding='utf-8').close()

    with open(file_path, 'r',  encoding='utf-8') as file:
        downloaded_list = file.read().splitlines()

    return downloaded_list


def get_list_to_download_urls():
    """
    Lit la liste des URLs depuis le fichier `video_urls.txt`.
    """
    file_path = 'video_urls.txt'

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            "Le fichier 'video_urls.txt' est introuvable. Ajoutez vos URLs dans ce fichier.")

    with open(file_path, 'r',  encoding='utf-8') as file:
        url_list = file.read().splitlines()

    return url_list


def save_downloaded_audios(downloaded_list):
    """
    Sauvegarde la liste des titres des audios téléchargés dans un fichier.
    """
    file_path = 'downloads/audio_list.txt'

    with open(file_path, 'w',  encoding='utf-8') as file:
        file.write('\n'.join(downloaded_list))

to_download_urls = get_list_to_download_urls()
downloaded_list = list_downloaded_audios()

for url in to_download_urls:
    try:
        print(f"Processing URL: {url}")
        yt = YouTube(url, on_progress_callback=on_progress)

        video_title = yt.title.strip()
        print(f"Video Title: {video_title}")

        if video_title in downloaded_list:
            print(f"Skipping: {video_title} (already downloaded)")
            continue

        ys = yt.streams.get_audio_only()
        ys.download(output_path='downloads/audio',
                    filename=f"{video_title}.mp3")
        print(f"Downloaded: {video_title}")

        downloaded_list.append(video_title)

    except Exception as e:
        print(f"An error occurred with URL {url}: {e}")

save_downloaded_audios(downloaded_list)
print("Download process completed.")
