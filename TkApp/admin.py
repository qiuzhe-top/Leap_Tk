from django.contrib import admin

from .models import title, information, radio, more
# Register your models here.
@admin.register(title)
class titleleAdmin(admin.ModelAdmin):
    list_display = ('id','subject','star_time','last_time')
    
@admin.register(information)
class informationleAdmin(admin.ModelAdmin):
    list_display = ('id','answer','types','minutiaID','subjectID','note','star_time','last_time')
    
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)
  
    #list_editable 设置默认可编辑字段
    list_editable = ['answer', 'types','minutiaID']
  
    #fk_fields 设置显示外键字段
    # fk_fields = ('types','minutiaID')

    #筛选器
    list_filter =('answer', 'types', 'minutiaID', 'note') #过滤器
    search_fields =('id', 'subjectID', 'answer') #搜索字段
    date_hierarchy = 'star_time'    # 详细时间分层筛选 

@admin.register(radio)
class radioleAdmin(admin.ModelAdmin):
    list_display = ('id','AnswerA','AnswerB','AnswerC','AnswerD','star_time','last_time')
        
@admin.register(more)
class moreleAdmin(admin.ModelAdmin):
    list_display = ('id','AnswerE','AnswerF','star_time','last_time')


