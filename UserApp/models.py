from django.db import models
from TkApp.models import title
from BookApp.models import book
 
#用户数据
class User(models.Model):
    name = models.CharField(max_length=128,unique=True)#账号
    password = models.CharField(max_length=256)
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')    
    #isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "用户"

class User_Information(models.Model): 
    GENDER_CHOICES = (
        (u'男', u'男'),
        (u'女', u'女'),
    )
    name = models.CharField(max_length=30, verbose_name=u'姓名') 
    gender = models.CharField(max_length=30, verbose_name=u'性别', choices=GENDER_CHOICES) 
    experience = models.IntegerField(verbose_name=u'经验') 
    userID = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name=u'所属用户')
    bookID = models.ForeignKey(book, on_delete=models.CASCADE, blank=True, verbose_name=u'所学内容' )
    ClassroomID = models.ForeignKey('Classroom', on_delete=models.CASCADE, verbose_name=u'所属班级')
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "个人信息"

class Finished(models.Model): 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    userID = models.ForeignKey('User', on_delete=models.CASCADE,verbose_name=u'用户')
    subjectID = models.ForeignKey(title, on_delete=models.CASCADE,verbose_name=u'已做题目ID')


    class Meta:
        verbose_name_plural = "用户已做题目ID"

class Error(models.Model): 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    userID = models.ForeignKey('User', on_delete=models.CASCADE,verbose_name=u'用户')
    subjectID = models.ForeignKey(title, on_delete=models.CASCADE,verbose_name=u'错题ID')

    class Meta:
        verbose_name_plural = "用户错题ID"

class Collection(models.Model): 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')  
    userID = models.ForeignKey('User', on_delete=models.CASCADE,verbose_name=u'用户')
    subjectID = models.OneToOneField(title, on_delete=models.CASCADE,verbose_name=u'收藏ID')
    
    class Meta:
        verbose_name_plural = "用户收藏ID"

class Classroom(models.Model): 
    name = models.CharField(max_length=60,unique=True)
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "班级"