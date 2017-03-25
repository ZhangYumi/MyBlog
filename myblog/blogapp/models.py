#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse


# Create your models here.
class Article(models.Model):
    art_title = models.CharField(max_length = 100)                   #博客题目
    art_datetime = models.DateTimeField(auto_now_add = True)         #博客创建日期   
    art_category = models.CharField(max_length = 50, blank = True)   #博客标签
    art_clicknum = models.IntegerField(null = True)                  #博客点击量
    art_commentnum = models.IntegerField(null = True)                #评论条数
    art_enjoylevel = models.CharField(max_length = 1, null = True)   #博客推荐等级，便于网站后台推送，分A,B,C,D
    art_type = models.CharField(max_length = 10, null = True)        #博客类型，分技术博客还是生活随笔
    art_imgurl = models.CharField(max_length = 255, null = True)     #博客上传图片链接
    art_content = models.TextField()                                 #博客内容

    def get_absolute_url(self) :
        path = reverse('detail', kwargs = {'id':self.id})
        return "http://127.0.0.1:8000%s" % path 

    def __unicode__(self) :
        return self.art_title


class UserInfo(models.Model):
    user_nickname = models.CharField(max_length = 20)    #博主昵称
    user_job = models.CharField(max_length = 50)         #博主职业
    user_company = models.CharField(max_length = 50)     #博主所在公司
    user_email = models.CharField(max_length = 20)       #博主邮箱



