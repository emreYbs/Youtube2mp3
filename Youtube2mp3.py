
##!/usr/bin/python3
#EmreYbs


# You may encounter some errors, especially when you download a lot. I mean this error: "ERROR: unable to download video data: HTTP Error 403: Forbidden"
# Solution: Removing the youtube_lb library cache generally helps. Just write in the terminal: "youtube-dl --rm-cache-dir"

import youtube_dl	
import cowsay 		# not necessary for the code to work. I just like more friendly looking terminal:)

cowsay.cow("Welcome to Youtube to Mp3 downloader")

print("\n\t\tGimme the Youtube video link and I'll give you the audio version.\n\n")

def download_convert():
    youtubeVideo_url = input("\n\tLet's begin, enter Youtube video url:  ")
    print("\tBeginning....it'll take a while:( \n")
    print("\t'Video downloading and then converting to high quality mp3 takes a little time:)'\n\n")
    youtubeVideo_info = youtube_dl.YoutubeDL().extract_info(
        url = youtubeVideo_url,download=False
    )
    filename = f"{youtubeVideo_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([youtubeVideo_info['webpage_url']])

    print ("\n\n\tYoutube video was downloaded, converted to mp3 and named as: {}".format(filename))
    cowsay.tux("\n\tBye till next mission\n")

if __name__=='__main__':
    download_convert()

