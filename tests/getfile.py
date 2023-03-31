import mysql.connector
import requests

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='peter',
    password='Macskalaci22',
    database='music'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM song WHERE id=2')

res = mycursor.fetchall()
print(res)
url = res[0][4]
title = res[0][1]

def get_file(url_link, title):
    url=url_link
    r=requests.get(url)

    open(f'mp3files/{title}.mp3','wb').write(r.content)

get_file(url, title)
