from django.contrib import admin

from .models import book, unit, Measure,motto

@admin.register(book)
class bookeleAdmin(admin.ModelAdmin):
    list_display = ('id','name','star_time','last_time')

@admin.register(unit)
class uniteleAdmin(admin.ModelAdmin):
    list_display = ('id','title','bookID','star_time','last_time') 
    
@admin.register(Measure)
class MeasureeleAdmin(admin.ModelAdmin):
    list_display = ('id','title','unitID','star_time','last_time')
    
# @admin.register(Exam)
# class ExameleAdmin(admin.ModelAdmin):
#     list_display = ('id','title','unitID','star_time','last_time')

@admin.register(motto)
class mottoeleAdmin(admin.ModelAdmin):
    list_display = ('id','title','star_time','last_time')