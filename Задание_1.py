import requests, re 
r = requests.get('https://moodle.tsu.ru/')
result = re.findall('[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,4}', r.text) 
seen = []
for i in result:
    if i not in seen:
        seen.append(i)
print (seen)