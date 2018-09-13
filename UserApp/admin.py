from django.contrib import admin

from .models import User, Classroom, User_Information, Finished, Error, Collection

@admin.register(User)
class UserleAdmin(admin.ModelAdmin):
    list_display = ('id','name','password','star_time','last_time')

@admin.register(User_Information)
class User_InformationleAdmin(admin.ModelAdmin):
    list_display = ('id','name','gender','userID','bookID','ClassroomID','star_time','last_time')

@admin.register(Finished)
class FinishedleAdmin(admin.ModelAdmin):
    list_display = ('id','userID','subjectID','star_time')
    
@admin.register(Error)
class ErrorleAdmin(admin.ModelAdmin):
    list_display = ('id','userID','subjectID','star_time')
    
@admin.register(Collection)
class CollectionleAdmin(admin.ModelAdmin):
    list_display = ('id','userID','subjectID','star_time')
    
@admin.register(Classroom)
class ClassroomleAdmin(admin.ModelAdmin):
    list_display = ('id','name','star_time','last_time')
    
