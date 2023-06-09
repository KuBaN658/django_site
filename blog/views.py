from django.template.loader import render_to_string
from django.http import HttpResponse

def blog(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return HttpResponse("<h2>Все посты блога</h2>")


def num_post(request, number_post):
    return HttpResponse(f"Здесь содержится информация о посте под номером {number_post}")


def info_post(request, name_post):
    return HttpResponse(f"Информация о посте {name_post}")
