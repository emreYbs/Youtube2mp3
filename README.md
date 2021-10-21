# Youtube2mp3
**a simple CLI tool to download Youtube videos and convert to Mp3**

# USAGE: 
**python3 Youtube2mp3.py**

*Note:* I use this tool to listen to some podcasts and archive them. I do not suggest to download music since they are copyrighted and even listening to Spotify Free is much better than breaking the rules of Youtube or the countries you live. But, everyone should be free to decide for themselves. Mine was just as friendly reminder:)

I added a screenshot from my terminal and it can give you an idea. This is a very simple and handy CLI tool. 


![image](https://user-images.githubusercontent.com/59505246/138336099-824873c0-9a5a-4256-a106-9e555814d09e.png)

- In this screenshot, you can notice that some Turkish letters are missing but when downloaded and converted to mp3, the name is just as it is in Youtube.

**Note:**

- You may encounter some errors, especially when you download a lot. 
I mean this error: *"ERROR: unable to download video data: HTTP Error 403: Forbidden"*

 *Solution:*
Removing the youtube_lb library cache generally helps. Just write in the terminal: **youtube-dl --rm-cache-dir**

- **The downloading process is slow.** 7-8Mb can take 2-3 minutes. Not a problem for me, but some of you need a faster tool.
-  The video is first downloaded and then converted to best audio format, I set the mp3 as default but with the best quality version. You can change it and download as flac, ogg, etc. *youtube-dl module* automatically removes the video and you just get the audio output in the folder where you have the python script.


![image](https://user-images.githubusercontent.com/59505246/138339080-94709da2-b4d2-4654-afef-5a91e4c63cab.png)
