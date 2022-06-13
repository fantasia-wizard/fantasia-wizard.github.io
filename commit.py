#!/usr/bin/python3
from json import dumps
import os
import string
from httplib2 import Http
dir = os.getcwd()
os.chdir('..')
parent_dir = os.getcwd()
os.chdir(dir)
name = dir.removeprefix(parent_dir + '/')

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
os.system('git add \.\/\* >> ../add.txt && git commit -m \'' + commit_message + '\' >> ../commit.txt && git push -u origin main')
git_messages = 'Add:\n'
with open('../add.txt', 'r') as file:
    for x in file.readlines():
        git_messages += x
    file.close()
with open('../commit.txt', 'r') as file:
    git_messages += '\nCommit:\n'
    for x in file.readlines():
        git_messages += x
    file.close()
message('New commit pushed to main branch ' + name + ' : ' + commit_message + '\\n' + git_messages)
os.remove('../add.txt')
os.remove('../commit.txt')