import re
import requests


def adress(new_adr, seen_adr):

    words = [
             q
             for i in range(len(new_adr))
             for text in requests.get(new_adr[i]).text.split(' ')
             for q in re.findall('href="/\w.+"', text)
            ]

    words = {
                'https://moodle.tsu.ru' + words[i][6:len(words[i]) - 1]
                for i in range(len(words))
            }

    new_adr = [
                x
                for x in words
                if x not in seen_adr
              ]

    for x in words:
        if x not in seen_adr:
            seen_adr.append(x)

    if len(new_adr) > 0:
        adress(new_adr, seen_adr)
    else:
        put = open("Подразделы_сайта.txt", "w")
        put.write('\n'.join(seen_adr))
        put.close()
        adr_mail(seen_adr)


def adr_mail(c):
    words = {
             q
             for gr_1 in range(len(c))
             for text in requests.get(c[gr_1]).text.split(' ')
             for q in re.findall('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,4}', text)
            }
    viv = open("Адреса_электронной_почты.txt", "w")
    viv.write('\n'.join(words))
    viv.close()


adress(new_adr=['https://moodle.tsu.ru'], seen_adr=['https://moodle.tsu.ru'])
