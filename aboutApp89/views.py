from django.shortcuts import render
from django.shortcuts import HttpResponse

from .models import Award


def survey(requset):  # 企业概况
    return render(requset, 'survey.html', {
        'active_menu': 'about1',
        'active_menu1': 'about',
        'sub_menu': 'survey',
    })


def honor(requset):
    # awards = Award.objects.all()  # 通过模型的objects.all()的得到一个查询集并存放于变量awards中
    award = Award.objects.all()
    return render(requset, 'honor.html', {
        'active_menu': 'about2',
        'active_menu1': 'about',
        'sub_menu': 'honor',
        'awards': award,
    })
