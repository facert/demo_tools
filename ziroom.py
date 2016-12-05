import requests
import time

with open('ziroom.txt', 'a+') as f:
    for i in xrange(10, 9001, 10):
        payload = {'step': i}
        res = requests.post('http://m.ziroom.com/list/ajax-get-data', data=payload)
        for i in res.json()['data']:
            print i['id']
            f.write(str(i)+'\n')
        time.sleep(3)
