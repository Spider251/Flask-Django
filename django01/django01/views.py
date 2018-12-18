from django.http import HttpResponse


def show_views(request):
    return HttpResponse("皮皮虾,我们走,我们是对好朋友")


def sh_views(request):
    return HttpResponse("访问路径中包含sh的处理程序")


# 匹配访问路径为 /show/四位数字 的时候
# 参数 year : 表示的是四位数字
def show1_views(request, year):
    return HttpResponse("传递过来的年份为:" + year)


def show2_views(request, year, month, day):
    return HttpResponse("生日为%s年%s月%s日" % (year, month, day))


def show3_views(request, name, age):
    return HttpResponse("姓名:%s,年龄:%d" % (name, age))
