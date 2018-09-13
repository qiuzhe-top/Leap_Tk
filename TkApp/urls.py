from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Exercise/', views.Exercise, name='Exercise'),
    path('See_the_title/', views.See_the_title, name='See_the_title'),#查看题目
    path('Delete_the_title', views.Delete_the_title, name='Delete_the_title'),#取消收藏题目
    path('boj_ajax', views.boj_ajax, name='boj_ajax'),# 获取前台题目id 读取数据库  返回数据
    path('Collection_ajax', views.Collection_ajax, name='Collection_ajax'), #答题界面收藏与取消收藏
    path('IF_subject_ajax', views.IF_subject_ajax, name='IF_subject_ajax'), #题目判断
]
