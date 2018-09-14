from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('tkadd', views.Tk_add, name='Tk_add'),
    path('query', views.query, name='query'),
    path('tkaddall', views.Tk_add_all, name='Tk_add_all'),
    path('add_all_subject', views.add_all_subject, name='add_all_subject'), #批量添加
    path('add', views.add_subject, name='add_subject'), #添加题目
    path('add_user', views.add_user, name='add_user'), #添加题目
    path('query_new', views.query_new, name='query_new'), #查询题目
    path('getunit', views.Book_Get_Unit, name='Book_Get_Unit'), #根据book获取Unit ajax
    path('getminutia', views.unit_Get_Measure, name='unit_Get_Measure'), #根据Unit获取Measure ajax
    path('add_user_ajax', views.add_user_ajax, name='add_user_ajax'), #添加User ajax
    path('Section_completion', views.Section_completion, name='Section_completion'), #小节完成情况
    path('Section_completion_ajax', views.Section_completion_ajax, name='Section_completion_ajax'), #
    path('Error_rate_ranking', views.Error_rate_ranking, name='Error_rate_ranking'), #错误率排行
    path('Ks_add', views.Ks_add, name='Ks_add'), #组卷

]
 