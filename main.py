from pytube import YouTube

link = str(input("Enter the link of youtube video you want to download: "))
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()

print("Downloading....")
ys.download()

print("Download completed!!")
close = input("enter to close")
