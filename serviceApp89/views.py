from django.shortcuts import get_object_or_404
import os
from django.http import StreamingHttpResponse
from django.shortcuts import render

# def platform(request):
#     return render(request, 'platform.html', {'active_menu': 'platform'})


# def download(request):
#     return render(request, 'docList.html', {'active_menu': 'docList'})

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Doc
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404
from django.http import StreamingHttpResponse
import os


def read_file(file_name, size):
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break


def getDoc(request, id):
    doc = get_object_or_404(Doc, id=id)
    update_to, filename = str(doc.file).split('/')
    filepath = '%s/media/%s/%s' % (os.getcwd(), update_to, filename)
    response = StreamingHttpResponse(read_file(filepath, 512))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(
        filename)
    return response


def download(request):
    # 从数据库获取、过滤和排序数据
    docList = Doc.objects.all().order_by('-publishDate')
    # 分页
    p = Paginator(docList, 5)
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
        request, 'docList.html', {
            'newName': '资料下载',
            'active_menu': 'service',
            'sub_menu': 'download',
            'docList': docList,
            'pageData': pageData,
        })


def platform(request):
    return render(
        request, 'platform.html', {
            'newName': '人工智能开放平台',
            'active_menu': 'service',
            'sub_menu': 'platform',
        })
