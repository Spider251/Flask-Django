# 模拟浏览器访问
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import simplejson

ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'

# 电影数据链接
url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

jurl = 'https://movie.douban.com/j/search_subjects'

s = '热门'
a = str(s.encode('utf-8')).replace('\\x', '%')[1:]

d = {
    'type': 'movie',
    'tag': s,
    'page_limit': 100,
    'page_start': 100
}

req = Request('{}?{}'.format(jurl, urlencode(d)), headers={
    'User-Agent': ua
})

with urlopen(req) as res:
    subjects = simplejson.loads(res.read())
    print(len(subjects['subjects']))
    print(subjects)


