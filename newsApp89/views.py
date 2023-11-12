from django.shortcuts import get_object_or_404
from django.shortcuts import render
from pyquery import PyQuery as pq
from .models import MyNew
from django.core.paginator import Paginator


def news(request, newName):
    # 解析请求的新闻类型
    submenu = newName
    if newName == 'company':
        newName = '企业要闻'
    elif newName == 'industry':
        newName = '行业新闻'
    else:
        newName = '通知公告'
    # 从数据库获取、过滤和排序数据
    newList = MyNew.objects.all().filter(
        newType=newName).order_by('-publishDate')

    for mynew in newList:
        html = pq(mynew.description)  # 使用pq方法解析html内容
        # mytxt其实是个临时变量，真实的数据库模型MyNew并没有添加mytxt字段
        mynew.mytxt = pq(html)('p').text()  # 截取html段落文字
    # 分页
    p = Paginator(newList, 5)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        newList = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }
    return render(
        request, 'newList.html', {
            'active_menu': 'news',
            'sub_menu': submenu,
            'newName': newName,
            'newList': newList,
            'pageData': pageData,
        })


# 新闻详情页后台处理函数


def newDetail(request, id):
    mynew = get_object_or_404(MyNew, id=id)
    mynew.views += 1  # 每次浏览数加1
    mynew.save()
    return render(request, 'newDetail.html', {
        'active_menu': 'news',
        'mynew': mynew,
    })

# 新闻搜索对应的响应处理函数


def search(request):
    keyword = request.GET.get('keyword')  # 提取出用户输入的关键字信息
    newList = MyNew.objects.filter(
        title__icontains=keyword)  # 数据库模糊查询的方式找到新闻标题中包括的关键字
    newName = "关于 " + "\"" + keyword + "\"" + " 的搜索结果"
    return render(request, 'searchList.html', {
        'active_menu': 'news',
        'newName': newName,
        'newList': newList,
    })
