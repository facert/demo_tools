# -*- coding: utf-8 -*-

import requests
import time


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36', 'Cookie': '****'}
payloads = {'ck': 'n1iQ', 'rv_comment': 'up', 'start': '0', 'submit_btn': u'加上去'}

def main():
    while True:
        res = requests.post('https://www.douban.com/group/topic/93461964/add_comment', data=payloads, headers=headers)
        print res
        time.sleep(60*60)

if __name__ == '__main__':
    main()
