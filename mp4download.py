# -*- coding: utf-8 -*-
import requests
from contextlib import closing
import random
headers={
    'user-agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50',
    'Range':'bytes=0-'
}
proxies=[{'http':'1.199.31.183:9999'}]
def download_file(url, path):
    with closing(requests.get(url,headers=headers,proxies=random.choice(proxies),stream=True)) as r:
        chunk_size = 1024
        content_size = int(r.headers['content-length'])
        print('下载开始')
        print(r)
        with open(path, "wb") as f:
            n = 1
            for chunk in r.iter_content(chunk_size=chunk_size):
                loaded = n*1024.0/content_size
                f.write(chunk)
                print('已下载{0:%}'.format(loaded))
                n += 1
if __name__ == '__main__':
    url = 'https://f.us.sinaimg.cn/004bgO59lx07vzX5w54s01041200o1Lx0E010.mp4?label=mp4_hd&template=480x480.23.0&trans_finger=53d43933e6520536fed61835e8c1d811&Expires=1563700113&ssig=0KmhQCol0S&KID=unistore,video'
    path =r'E:\学习\1.mp4'
    download_file(url, path)