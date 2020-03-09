from django.shortcuts import render


def get_companion_items(request):
    return render(request, "companion/companion.html")
