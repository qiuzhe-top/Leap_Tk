from django.db import models
from BookApp.models import Measure
 
from ckeditor_uploader.fields import RichTextUploadingField

class title(models.Model):
    subject = RichTextUploadingField(verbose_name=u'题目')  
    isDelete = models.BooleanField(default=True,verbose_name=u'是否可用') 
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')    
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "题目"  

class information(models.Model):

    ob_types = (
         ('单选','单选'),
         ('多选','多选'),
         ('判断','判断'),
    )

    answer = models.CharField(max_length=60, verbose_name=u'答案')     
    types = models.CharField(max_length=60, choices = ob_types,  verbose_name=u'题型')
    minutiaID = models.ForeignKey(Measure, on_delete=models.CASCADE,verbose_name=u'小节ID') #小节
    subjectID = models.OneToOneField(title, on_delete=models.CASCADE,verbose_name=u'题目ID')
    note = models.CharField(max_length=300, blank=True, verbose_name=u'备注')

    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')    
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期') 

    
    class Meta:
        verbose_name_plural = "答案" 

class radio(models.Model):
    AnswerA = models.CharField(max_length=60, verbose_name=u'选项A')      
    AnswerB = models.CharField(max_length=60, verbose_name=u'选项B')      
    AnswerC = models.CharField(max_length=60, verbose_name=u'选项C')      
    AnswerD = models.CharField(max_length=60, verbose_name=u'选项D') 
    subjectID = models.OneToOneField(title, on_delete=models.CASCADE,verbose_name=u'题目ID')
    
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')    
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期') 

    class Meta:
        verbose_name_plural = "单选内容"

class more(models.Model):
    AnswerA = models.CharField(max_length=60, verbose_name=u'选项A')      
    AnswerB = models.CharField(max_length=60, verbose_name=u'选项B')      
    AnswerC = models.CharField(max_length=60, verbose_name=u'选项C')      
    AnswerD = models.CharField(max_length=60, verbose_name=u'选项D') 
    AnswerE = models.CharField(max_length=60, verbose_name=u'选项E')      
    AnswerF = models.CharField(max_length=60, verbose_name=u'选项F')  
    subjectID = models.OneToOneField(title, on_delete=models.CASCADE,verbose_name=u'题目ID')
    
    star_time = models.DateTimeField(auto_now_add=True,verbose_name=u'创建日期')    
    last_time = models.DateTimeField(auto_now=True,verbose_name=u'最后一次修改日期')  
        
    class Meta:
        verbose_name_plural = "多选内容"
        