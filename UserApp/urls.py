from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Landing', views.Landing, name='Landing'),
    path('Logout', views.Logout, name='Logout'),
    path('updata_user_book', views.updata_user_book, name='updata_user_book'),#更新用户所学内容
    path('rank_updata', views.rank_updata, name='rank_updata'),#更新用户排名
    path('user_Collection_ajax', views.user_Collection_ajax, name='user_Collection_ajax'),#更新用户收藏
    path('user_Error_ajax', views.user_Error_ajax, name='user_Error_ajax'),#更新用户错题
    path('user_password_ajax', views.user_password_ajax, name='user_password_ajax'),#更新用户密码
]
