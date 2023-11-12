from django.shortcuts import render
from productApp89.models import Product
from productApp89.models import ProductImg
from django.shortcuts import HttpResponse


# def home(request):
#     return render(request, 'home.html', {'active_menu': 'home', })

from newsApp89.models import MyNew
from django.db.models import Q  # 用于对象的复杂查询，可以对关键字参数进行封装，从而更好地应用于多条件查询


def home(request):
    # 新闻展报
    newList = MyNew.objects.all().filter(~Q(
        newType='通知公告')).order_by('-publishDate')
    postList = set()
    postNum = 0
    for s in newList:
        if s.photo:
            postList.add(s)
            postNum += 1
        if postNum == 3:
            break

    # 通知公告
    noteList = MyNew.objects.all().filter(
        Q(newType='通知公告')).order_by('-publishDate')
    if (len(noteList) > 4):
        noteList = noteList[0:4]

    productList = Product.objects.all().order_by('-views')
    if (len(productList) > 4):
        productList = productList[0:4]

    # 新闻列表
    if (len(newList) > 7):
        newList = newList[0:7]

    return render(request, 'home.html', {
        "active_menu": "home",
        "postList": postList,
        "newList": newList,
        "productList": productList,
    })
