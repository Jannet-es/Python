import requests
from bs4 import BeautifulSoup
import re
from queue import Queue
import threading
import time

def f_1(url, queue):
    posts = []
    while True:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")

        soup_find = soup.find_all('div', ['newItem', 'actNew'])
        main_new = soup.find('div', ['def-main-new'])
        title = main_new.find('div', 'mainTitle').text[:-5]
        t = main_new.find('div', 'mainTime').text
        content = main_new.find('div', 'mainAnons').text

        if title not in posts:
            posts.append(title)
            queue.put({
                        'title': title,
                        'time': t,
                        'content': content
                    })
        for i in soup_find:
            title = i.find(['div'], ['mainTitle', 'newItem-s', 'actNew-a']).text
            t = i.find(['div', 'span'], ['newItem-f', 'actNew-d']).text

            if title not in posts:
                posts.append(title)
                queue.put({
                            'title':title,
                            'time':t,
                            'content':'N/A'
                        })
        time.sleep(360)

queue = Queue()
url = 'https://www.riatomsk.ru/'
thread = threading.Thread(target=f_1, args=(url, queue))
thread.start()
while True:
    news = queue.get()
    print(news['time'])
    print(news['title'])
    if news['content'] != 'N/A':
        print(news['content'])
    print('\n')

