# coding=utf-8

import os

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://www.raiplayradio.it/playlist/2018/09/educazione-criminale-ec91f2ed-ac23-4a6d-a709-15f10e20cb29.html"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'html.parser')  # type: BeautifulSoup
    ols = soup.find_all("ol", class_="elencoPlaylist")

    for ul in ols:
        lis = ul.findAll('li')
        for li in lis:
            episode_number = unicode.strip(li['data-title'].split(':')[0])
            doc = requests.get(li['data-mediapolis'])
            complete_path = os.path.join('downloads', '{0}.mp3'.format(episode_number))
            with open(complete_path, 'wb') as f:
                f.write(doc.content)
