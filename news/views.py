from django.shortcuts import render
from .models import Article
def index(reuqest):
    news=Article.objects.all().order_by('-id')
    context = {
        'news':news
    }
    return render(request=reuqest, template_name='index.html', context=context)


def article_detail(request,id):
    new = Article.objects.get(id=id)
    context = {
        'new': new

    }

    return render(request=request, template_name='article_detail.html', context=context)
def sport_news(request):
    s_news=Article.objects.filter(tag='sport')
    context = {
        's_news':s_news
    }
    return render(
        request=request,
        template_name='sport.html',
        context=context
    )
def local_news(request):
    l_news=Article.objects.filter(tag='local')
    context = {
        'l_news':l_news
    }
    return render(
        request=request,
        template_name='local.html',
        context=context
    )
def world_news(request):
    w_news=Article.objects.filter(tag='world')
    context = {
        'w_news':w_news
    }
    return render(
        request=request,
        template_name='world.html',
        context=context
    )