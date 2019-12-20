'''
gevent图片下载器
'''
import gevent
from gevent import monkey
import urllib.request

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", 'https://imgoss.douyucdn.cn/bj/yuba/default/2019/10/08/201910080638294841940242230.jpg'),
        gevent.spawn(downloader, "2.jpg", 'https://imgoss.douyucdn.cn/bj/yuba/weibo/2019/09/30/201909300411555146667141008.png')
    ])


if __name__ == "__main__":
    main()


