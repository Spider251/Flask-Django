import urllib.request as ul
import urllib.parse as uz
import http.cookiejar as cookielib
from json import loads

c = cookielib.LWPCookieJar()  # 先把cookie对象存储为cookiejar的对象
cookie = ul.HTTPCookieProcessor(c)  # 把cookiejar对象转换为一个handle
opener = ul.build_opener(cookie)  # 建立一个模拟浏览器，需要handle作为参数
ul.install_opener(opener)  # 安装一个全局模拟浏览器，代表无论怎么访问都是一个浏览器操作而不是分开获取验证码等msg
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
url = 'https://kyfw.12306.cn/otn/login/init'

code = ['45, 45', '120, 45', '180, 45', '255, 45', '45, 120', '120, 120', '180, 120', '255, 120']


# 获取验证码
def get_code():
    req = ul.Request(
        'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.6758635422370105')
    req.headers = headers
    code_file = opener.open(req).read()
    with open(r'./12306images/code.png', 'wb') as f:
        f.write(code_file)


def main_():
    get_code()
    code = input('输入验证码：')
    req = ul.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
    req.headers = headers

    data = {
        'answer':code,
        'login_site':'E',
        'rand':'sjrand'
    }
    data = uz.urlencode(data).encode()#把字典转换为URL query string,此时是str，要把它变为byts。

    html = opener.open(req,data= data).read().decode()#读取出来是byts格式，转换为‘utf-8（默认）
    print(html)
    result = loads(html)
    if result['result_code']=='4':
        print('验证码通过')
        rep = ul.Request('https://kyfw.12306.cn/passport/web/login')
        rep.headers = headers
        data = {'username':'13613519952',
                'password':'tt2008gax',
                'appid':'otn'
        }
        data = uz.urlencode(data).encode() #看到了吗，这就是你给服务器回复的东西

        html1 = opener.open(rep,data = data ).read().decode()
        result1 = loads(html1)
        if result1['result_code'] == 0:
            print('账户密码验证通过')
        else:
            print(result1['result_message'])

    else:
        print('验证码校验失败，重来')


if __name__ == '__main__':
    main_()
