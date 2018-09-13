from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

import datetime
 
from UserApp.models import Finished, Error, Collection, User, User_Information
from BookApp.models import Measure
from . import models

# 根据接受前台单元渲染相关题目但不包含题目详细数据
def Exercise(request):
    context = {}
    # # 根据接受前台单元渲染相关题目 存在字典地址引用问题
    minutia_id = request.GET['pag']
    tm_list = {}
    Tm_information = models.information.objects.filter(minutiaID = minutia_id) #根据单元获取题目
    for i in Tm_information:
        tm_id = i.subjectID.pk
        tm_Error = Error.objects.filter(subjectID = tm_id, userID = request.session.get('user_ID')).count()
        if tm_Error != 0:
            typ = "min"
            if Finished.objects.filter(subjectID = tm_id, userID = request.session.get('user_ID')).count() != 0:
                typ = "miy"
        elif Finished.objects.filter(subjectID = tm_id, userID = request.session.get('user_ID')).count() != 0:
            typ = "miy"
        else:
            typ = ''
        key = '%s' %(tm_id)
        tm_list[key] = typ
    context['tm_list'] = tm_list
    context['minutia_text'] = Measure.objects.get(pk = minutia_id).title
    return render(request,'Practice/Practice.html',context)
# 获取前台题目id > 读取数据库 > 返回数据
def boj_ajax(request):
    context = {}
    obj_msg = []
    id = request.POST.get('id')
    obj_title = models.title.objects.get(pk = id)
    obj_msg.append(obj_title.subject)
    obj_information= models.information.objects.get(subjectID = id)
    obj_msg.append(obj_information.types)
    if obj_information.types == "单选":
        obj_radio= models.radio.objects.get(subjectID = id)
        obj_msg.append(obj_radio.AnswerA)
        obj_msg.append(obj_radio.AnswerD)
        obj_msg.append(obj_radio.AnswerC)
        obj_msg.append(obj_radio.AnswerB)
    elif obj_information.types == "多选":
        obj_radio= models.more.objects.get(subjectID = id)
        obj_msg.append(obj_radio.AnswerA)
        obj_msg.append(obj_radio.AnswerD)
        obj_msg.append(obj_radio.AnswerC)
        obj_msg.append(obj_radio.AnswerB)
        obj_msg.append(obj_radio.AnswerE)
        obj_msg.append(obj_radio.AnswerF)
    try:
        Collection.objects.get(subjectID = id, userID = request.session.get('user_ID'))
        context['tm_Collection'] = "glyphicon-star"
    except:
        context['tm_Collection'] = "glyphicon-star-empty"
    context['list'] = obj_msg 
    return JsonResponse(context)
def Collection_ajax(request):
    context = {}
    id = request.POST.get('id')
    ty = request.POST.get('ty') #2 取消收藏
    if ty == '2':
        Collection.objects.get(subjectID = id, userID = request.session.get('user_ID')).delete()
    elif ty == '1':
        user_instance = User.objects.get(pk = request.session.get('user_ID'))
        subject_instance = models.title.objects.get(pk = id)
        Collection.objects.create(subjectID = subject_instance, userID = user_instance)
    return JsonResponse(context)
# 题目判断
def IF_subject_ajax(request):
    context = {}   
    id = request.POST.get('id')
    answer = request.POST.get('answer') 
    userID = request.session.get('user_ID')
    try:
        models.information.objects.get(subjectID = id ,answer = answer)
        context['msg'] = 'yes' #题目回答正确，返回前端
        F_day = Finished.objects.filter(subjectID = id,userID = userID)
        F_num = F_day.count()
        if F_num != 0:
            star_day = F_day.order_by('-pk')[0].star_time.day
            now_day = datetime.datetime.now().day
            if star_day != now_day: #判断是不是同一天答题，防止刷正确率，第二天答对可再次写入
                #写入一条答对数据    
                user_instance = User.objects.get(pk = userID)
                subject_instance = models.title.objects.get(pk = id)
                Finished.objects.create(subjectID = subject_instance, userID = user_instance)
                User_experience = User_Information.objects.get(userID = userID)
                # print(User_experience.experience)
                User_experience.experience =  User_experience.experience + 3
                User_experience.save()
                # print(User_experience.experience)
                # print("第二天答题，加分")        
                
            # print("未保存")        
        else:
            #添加一条对题数据
            user_instance = User.objects.get(pk = userID)
            subject_instance = models.title.objects.get(pk = id)
            Finished.objects.create(subjectID = subject_instance, userID = user_instance)
            # print("第一次答题，加分")        
            User_experience = User_Information.objects.get(userID = userID)
            # print(User_experience.experience)
            User_experience.experience =  User_experience.experience + 3
            User_experience.save()
            # print(User_experience.experience)
    except:
        context['msg'] = 'no' #题目回答错误，返回前端
        #经验减一
        User_experience = User_Information.objects.get(userID = userID)
        User_experience.experience =  User_experience.experience - 1
        User_experience.save()
        try:
            Error.objects.get(subjectID = id,userID = userID)
        except:
            user_instance = User.objects.get(pk = userID)
            subject_instance = models.title.objects.get(pk = id)
            Error.objects.create(subjectID = subject_instance, userID = user_instance)
            
    return JsonResponse(context)
# 用户收藏夹错题列表 题目浏览
def See_the_title(request):
    context = {}
    context['objid'] = request.GET['pag']
    return render(request,'Practice/Practice.html',context)

def Delete_the_title(request):
    context = {}   
    id = request.POST.get('data')
    userID = request.session.get('user_ID')
    Collection.objects.get(userID = userID,subjectID = id).delete()
    return JsonResponse(context)
    
    