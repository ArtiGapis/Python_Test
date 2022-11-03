import pytube
from urllib.parse import urlparse


def youtube(link):
    yt = pytube.YouTube(link)
    x = input('A - audio,\nH - Hight video resolution \nL - Low video resolution \nD - exit\nWhich is your choice? : ')

    if x.upper() == 'A':
        yt.streams.get_audio_only().download()
        print('Downloaded audio material from the link \n', link)
    elif x.upper() == 'H':
        yt.streams.get_highest_resolution().download()
        print('Downloaded high quality video material from the link \n', link)
    elif x.upper() == 'L':
        yt.streams.get_lowest_resolution().download()
        print('Downloaded the low video material from the link \n', link)
    elif x.upper() == 'D':
        print('EXIT')
    elif x.upper() != 'A' or x.upper() != 'H' or x.upper() != 'L' or x.upper() != 'D':
        print('Follow the instructions')
        return youtube(link)


def web():
    link = input('Enter the URL : \n')
    result = urlparse(link)
    http = result.scheme
    yt = result.netloc
    if http != 'https':
        print('This is not URL')
        web()
    elif yt != 'www.youtube.com':
        print('This is not Youtube URL')
        web()
    else:
        youtube(link)


web()
