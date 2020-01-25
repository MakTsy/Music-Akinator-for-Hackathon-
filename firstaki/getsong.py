import requests
import re
import urllib
import json
from django.http import HttpResponse

def Find_by_lyrics(text_of_song):
    data = {
        'q': text_of_song,
        'method': 'findLyrics',
        'return': 'timecode,apple_music,deezer,spotify',
        'api_token': '72bb766f568770641c6cd45e5b174eab'#'8c433296bcc90433f2d07bbe01dde04f'#'0fd92e90b5ec3402149b6b129cb28231'#'47ce4a1fae5e94935731595a0d33c30b'#'62c7cb8dc20ea60b78a0257c974c8a24'
    }
    result = requests.post('https://api.audd.io/', data=data).json()
    parser = re.search(r'v=(\w+)',result['result'][0]['media']).group(0)
    parserL = re.search(r'url":"\S{45}',result['result'][0]['media']).group(0)

    res = [result['result'][0]["full_title"], parser[2:], parserL[6:]]
    return res