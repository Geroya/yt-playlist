import os
from pytube import Playlist

def downloadYTPlaylist():
    path = input("Download Path: ")
    pl = Playlist(input("Playlist URL: "))
    print(f'Downloading: '+pl.title)
    
    for video in pl.videos:
        try:
            videoFileName = video.title
            print("Downloading " + videoFileName)
            out_file = video.streams.filter(only_audio=True).first().download(output_path=path, max_retries=3)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

        except:
            print("Something went wrong with video " + videoFileName)
            continue

    print("Download finished.")

if __name__ == "__main__":
    downloadYTPlaylist()

