from django.db import models
# from TkApp.models import title
# import TkApp.models 

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=60, verbose_name=u'书名')     
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "书本"

class unit(models.Model):
    title = models.CharField(max_length=60, verbose_name=u'单元')     
    bookID = models.ForeignKey('book', on_delete=models.CASCADE,verbose_name=u'书ID')

    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')    

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = "单元"
    
class Measure(models.Model):
    title = models.CharField(max_length=60, verbose_name=u'小节')     
    unitID = models.ForeignKey('unit', on_delete=models.CASCADE,verbose_name=u'单元ID')
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')    
 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "小节"



class motto(models.Model):
    title = models.CharField(max_length=60, verbose_name=u'格言')     
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')   
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
      
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "格言"