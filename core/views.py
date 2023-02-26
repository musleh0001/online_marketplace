from django.shortcuts import render

from item import models


def index(request):
    items = models.Item.objects.filter(is_sold=False)[0:6]
    categories = models.Category.objects.all()

    return render(
        request, "core/index.html", {"categories": categories, "items": items}
    )


def contact(request):
    return render(request, "core/contact.html")
