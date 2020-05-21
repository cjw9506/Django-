from django.contrib import admin

from . import models
from .models import Article, Reporter
admin.site.register(models.Article)
admin.site.register(Reporter)