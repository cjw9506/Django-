from django.shortcuts import render

from .models import Article

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year,month):
    a_list = Article.objects.filter(pub_date__month=month)
    context = {'year': year,'month':month, 'article_list': a_list}
    return render(request, 'news/month_archive.html', context)

<<<<<<< HEAD
=======
def article_detail(request, year,month,pk):
    a_list = Article.objects.filter(id=pk)
    context = {'year': year,'month':month, 'article_list': a_list}
    return render(request, 'news/detail_archive.html', context)
>>>>>>> e69867ee7e2cdc3e6e1c9d6373dc7494232c8de5
