from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
from app01.models import UserInfo


def index(request):
    return render(request, 'main.html')


def product_list(request):
    return render(request, "product_list.html")


def news(req):
    # 1.定义一些新闻（字典或者列表） 或 去数据库  网络请求去联通新闻
    # 向地址：http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news 发送请求
    # 第三方模块：requests  (pip install requests)
    import requests
    res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news")
    data_list = res.json()
    print(data_list)

    return render(req, 'news.html', {"news_list": data_list})


def login(req):
    # CSRF token verification
    if req.method == "GET":
        return render(req, "login.html")
    username = req.POST.get("user")
    password = req.POST.get("pwd")
    if username == 'root' and password == "123":
        # return HttpResponse("登录成功")
        return redirect("http://www.destiny2.com/")

    # return HttpResponse("登录失败")
    return render(req, 'login.html', {"error_msg": "用户名或密码错误"})


def orm(request):
    #UserInfo.objects.create(name="a",password="123",plan="monthly",age=19)
    #UserInfo.objects.create(name="b", password="123", plan="monthly", age=12)
    #UserInfo.objects.create(name="c", password="123", plan="monthly", age=20)

    return HttpResponse("成功")


def info_add(req):
    if req.method == "GET":
        return render(req, 'info_add.html')

    user = req.POST.get("user")
    pwd = req.POST.get("pwd")
    age = req.POST.get("age")

    UserInfo.objects.create(name=user, password=pwd, age=age)

    return redirect("/info/list")


def info_list(request):
    # 1.获取数据库中所有的用户信息
    # [对象,对象,对象]
    data_list = UserInfo.objects.all()

    # 2.渲染，返回给用户
    return render(request, "info_list.html", {"data_list": data_list})