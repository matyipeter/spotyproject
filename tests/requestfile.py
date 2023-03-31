import requests

def get_file():
    url='http://192.168.0.28:8080/000001.mp3'
    r=requests.get(url)

    open('mp3files/testmusic.mp3','wb').write(r.content)

get_file()
