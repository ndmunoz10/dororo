from django.http import HttpResponse
from django.template import loader

from fights.models import Fight


def get_fights(request):
    fight_list = Fight.objects.order_by("winner_name")
    template = loader.get_template("fights/fights.html")
    context = {
        "fight_list": fight_list
    }
    return HttpResponse(template.render(context, request))
