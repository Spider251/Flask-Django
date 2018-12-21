from urllib.parse import urlencode
from urllib.request import Request, urlopen

from fake_useragent import UserAgent


def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    # print(response.read().decode())
    return response.read()


def save_html(filename, html_bytes):
    with open('/home/xiaojiuwo/python学习/Flask/django03/filename/'+filename, "wb") as f:
        f.write(html_bytes)


def main():
    countent = input("请输入要下载的内容:")
    num = input("请输入要下载多少页:")
    base_url = 'https://tieba.baidu.com/f?ie=utf-8&{}'
    for num in range(int(num)):
        args = {
            "pn": num * 50,
            "kw": countent
        }
        filename = "第"+str(num+1)+"页.html"
        args = urlencode(args)
        print("正在下载"+filename)
        html_bytes = get_html(base_url.format(args))
        save_html(filename,html_bytes)


if __name__ == '__main__':
    main()
