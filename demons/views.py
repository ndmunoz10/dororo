from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from demons.models import Demon


def get_demons(request):
    demon_list = Demon.objects.order_by("body_part")
    template = loader.get_template("demons/demons.html")
    context = {
        "demon_list": demon_list
    }
    return HttpResponse(template.render(context, request))


def search_demons(request):
    if request.method == 'POST':
        form_data = request.POST
        user_input = form_data['user_input']
        demon_list = Demon.objects.filter(body_part__contains=user_input)
        template = loader.get_template("demons/demons.html")
        context = {
            "demon_list": demon_list
        }
        return HttpResponse(template.render(context, request))
    else:
        redirect('/demons')
