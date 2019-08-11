from pytube import YouTube

def Youtube_Downloader(url):
    yt = YouTube(url)
    yt1=yt
    stream = yt.streams.filter(mime_type="video/3gpp",res='144p').first()
    stream.download('C:/Users/blithe/Downloads', filename=yt1.title)
    return print('{0} - 这个视频已经下载成功啦，主人'.format(yt1.title))
url = input('Please type in your url:   ')
Youtube_Downloader(url)
