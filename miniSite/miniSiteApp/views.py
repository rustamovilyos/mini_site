from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

def index(request):
    maqola = Article.objects.all()
    return render(request, 'miniSiteApp/index.html', {'maqolalar': maqola})


class ArticleView(DetailView):
    model = Article
    template_name = 'miniSiteApp/articleView.html'