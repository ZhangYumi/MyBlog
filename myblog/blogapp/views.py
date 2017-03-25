#-*- coding:utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from datetime import datetime
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from blogapp.models import Article
from blogapp.models import UserInfo

# Create your views here.
#首页，获取所有博客信息
def index(request):
    limit = 3
    post_art = Article.objects.all()
    post_user = UserInfo.objects.first()
    
    post_art_sort = post_art.order_by('-art_datetime')    
    hot_clicks = post_art.order_by('-art_clicknum')[:5]
    recom_arts = post_art.order_by('-art_enjoylevel')[:5]

    paginator = Paginator(post_art_sort, limit)
    page = request.GET.get('page')
    try:
        post_art = paginator.page(page)
    except PageNotAnInteger:
        post_art = paginator.page(1)
    except EmptyPage:
        post_art = paginator.page(paganator.num_pages )
    
    
    return render(request,'index.html',{'post_art': post_art, 'post_user': post_user, 'hot_clicks': hot_clicks, 'recom_arts': recom_arts })

#点击题目，展开博文
def detail(request,id) :
    try:
        post=Article.objects.get(id = str(id))#get()获取的是一个对象，即一条记录，所以查询字段必须唯一
#    except Article.DoseNotExist():
#        raise Http404
    except:
        pass
    return render(request, 'post.html', {'post':post})

#获取IT技术类博客
def tech(request):
    tech_list = Article.objects.filter(art_type = "IT").order_by('-art_datetime')#filter()获取的是一个结果集，返回的是列表，满足查询条件的多条记录，字段可重复
    paginator = Paginator(tech_list, 3)
    page = request.GET.get('page')
    try:
        tech_list = paginator.page(page)
    except PageNotAnInteger:
        tech_list = paginator.page(1)
    except EmptyPage:
        tech_list = paginator.page(pagiantor.num_pages)
    return render(request, 'tech_IT.html', {'tech_list':tech_list})

#获取生活随笔类博客
def life(request):
    life_list = Article.objects.filter(art_type = "NIT").order_by('-art_datetime')
    paginator = Paginator(life_list, 3)
    page = request.GET.get('page')
    try :
        life_list = paginator.page(page)
    except PageNotAnInteger:
        life_list = paginator.page(1)
    except EmptyPage:
        life_list = paginator.page(paginator.num_pages)
    return render(request, 'life.html', {'life_list':life_list})
