from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, JsonResponse, FileResponse
from django.template import Template, Context
import os


# Create your views here.
def msgproc(request):
    datalist = []
    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now()
        with open('msgdata.txt', 'a+') as f:
            f.write("{}--{}--{}--{}--\n".format(userB, userA,\
                            msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open("msgdata.txt", "r") as f:
                cnt = 0
                for line in f:
                    linedata = line.split('--')
                    if linedata[0] == userC:
                        cnt = cnt + 1
                        d = {"userA":linedata[1], "msg":linedata[2]\
                             , "time":linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return render(request, "MsgSingleWeb.html", {"data":datalist})


def homeproc1(request):
    response = JsonResponse({'key': 'value1'})
    return response

def homeproc2(request):
    cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    response = FileResponse(open(cwd + "/msgapp/templates/PyLogo.png", "rb"))
    response['Content-Type'] = 'application/octet-stream'
    response['COntent-Disposition'] = 'attachment;filename="pylogo.png"'
    return response

def pgproc(request):
    template = Template("<h1>这个程序的名字是{{ name }}</h1>")
    context = Context({"name" : "实验平台"})
    return HttpResponse(template.render(context))


def homeproc(request):
    response = HttpResponse()
    response.write("<h1>这是首页, 具体留言功能请访问<a href='./msggate'>这里</a></h1>")
    response.write("<h1>这是首页, 具体json功能请访问<a href='./1'>这里</a></h1>")
    response.write("<h1>这是首页, 具体功下载图片能请访问<a href='./2'>这里</a></h1>")
    response.write("<h1>这是首页, 具体功传值重定向能请访问<a href='./playground'>这里</a></h1>")
    response.write("<h1>这是首页, 管理员请访问<a href='./admin'>这里</a></h1>")
    response.write("<h1>这是第尾页</h1>")
    return response
    #return HttpResponse("<h1>这是首页，具体功能请访问<a href='./msggate'>这里</a></h1>")


from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello ---- World!'
    return render(request, 'hello.html', context)


 #-*- coding: utf-8 -*-
# from django.http import HttpResponse
from .models import Test
# 数据库操作
#添加数据
# def testdb(request):
#     test1 = Test(name='runoob')
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")

#获取数据
# def testdb(request):
#     # 初始化
#     response = ""
#     response1 = ""
#
#     # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
#     list = Test.objects.all()
#
#     # filter相当于SQL中的WHERE，可设置条件过滤结果
#     response2 = Test.objects.filter(id=1)
#
#     # 获取单个对象
#     response3 = Test.objects.get(id=1)
#
#     # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
#     Test.objects.order_by('name')[0:2]
#
#     # 数据排序
#     Test.objects.order_by("id")
#
#     # 上面的方法可以连锁使用
#     Test.objects.filter(name="yun").order_by("id")
#
#     # 输出所有数据
#     for var in list:
#         response1 += var.name + " "
#     response = response1
#     return HttpResponse("<p>" + response + "</p>")

#更新数据
# def testdb(request):
#     # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
#     test1 = Test.objects.get(id=1)
#     test1.name = 'Google'
#     test1.save()
#
#     # 另外一种方式
#     # Test.objects.filter(id=1).update(name='Google')
#
#     # 修改所有的列
#     # Test.objects.all().update(name='Google')
#
#     return HttpResponse("<p>修改成功</p>")

#删除数据


from django.http import HttpResponse

from .models import Test


# 数据库操作
def testdb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")


# -*- coding: utf-8 -*-




# 表单
def search_form(request):
    return render(request, "search_form.html", {"data":request})

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def searchpost(request):
    ctx = {}
    # if request.POST:
    if request.method == "POST":
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

