from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
<<<<<<< HEAD
    #path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
=======
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
>>>>>>> e69867ee7e2cdc3e6e1c9d6373dc7494232c8de5
]