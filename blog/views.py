from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    return render(request, 'blog/index.html')


def posts(request):
    return render(request, 'blog/list_detail.html')



def get_by_name(request, name_post):
    context = {
        'name_post': name_post,
    }
    return render(request, 'blog/detail_by_name.html', context=context)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'blog/guinnessworldrecords.html', context=context)


def get_by_num(request, num):
    context = {
        'num': num,
    }
    return render(request, 'blog/detail_by_number.html', context=context)
