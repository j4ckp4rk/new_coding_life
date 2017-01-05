# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
from .models import Article

def index(request):
    # random_number = randint(1,100)
    ##
    # return HttpResponse("Hello, world.U R @ index {}".format(random_number))
    name = "JACK"
    article_list = Article.objects.all()
    # Article.objects.create(
    #     title = "hello",
    #     contents = "aaa",
    #     view_count = 0,
    # )
    ctx = {
        "article_list" : article_list,
        "name" : name,
    }

    # return render(request, "index.html", { "name" : name })
    return render(request, "index.html", ctx)
