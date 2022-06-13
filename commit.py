#!/usr/bin/python3
from json import dumps
import os
import string
from httplib2 import Http
dir = os.getcwd()
os.chdir('..')
parent_dir = os.getcwd()
os.chdir(dir)
name = dir.removeprefix(parent_dir)

def message(text: string):
    """Hangouts Chat incoming webhook quickstart."""
    url = 'https://chat.googleapis.com/v1/spaces/AAAA9EakoSo/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=ETmHwLjxmOSeSLRgfC-6EVhOXNTg6C2HyIWKETZDOhI%3D'
    bot_message = {
            'text' : text}

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)
commit_message = input('Commit message: ')
os.system('git add \.\/\* && git commit -m \'' + commit_message + '\' && git push -u origin main')
message('New commit pushed to main branch' + name + ': ' + commit_message)