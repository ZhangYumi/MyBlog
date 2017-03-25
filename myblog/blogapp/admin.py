from django.contrib import admin
from blogapp.models import Article
from blogapp.models import UserInfo

# Register your models here.
admin.site.register(Article)
admin.site.register(UserInfo)
