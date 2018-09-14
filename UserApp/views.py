from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from . import models
from BookApp.models import book, unit, Measure, motto
import random
import time

def motto_text():
    # 返回一句格言
    try:
        motto_num = motto.objects.all().count()
        n = random.randint(1,motto_num)
        motto_data = motto.objects.get(id = n)
        motto_text = motto_data.title
    except:
        return "做好每一件事2018-7-22"
    return motto_text
# 主页
def home(request): 
    context = {}  
    corrects = {}
    context['message'] = "请登陆您的账号"
    if not request.session.get('is_login', None):
        context['motto_data'] = motto_text()
        return render(request,'Landing/Landing.html',context) 
    #获取用户信息 收藏 错题
    user_ID = request.session.get('user_ID')
    user_Finished = models.Finished.objects.filter(userID = user_ID)
    user_Error = models.Error.objects.filter(userID = user_ID)
    user_Collection = models.Collection.objects.filter(userID = user_ID)
    context['Finished'] = user_Finished.count()
    context['Error'] = user_Error.count()
    context['all'] = user_Finished.count() + user_Error.count()
    context['correct'] = 0
    if user_Finished.count() + user_Error.count() != 0:
        correct = user_Finished.count() / ( user_Finished.count() + user_Error.count())
        context['correct'] = round(correct,2)
    context['books'] = book.objects.all()
    context['unit'] = unit.objects.filter(bookID = request.session['user_book']) #单元
    context['Measure']= Measure.objects.all() #小节
    context['Exam']= Exam.objects.all() #测试
    context['user_Collection']= user_Collection
    context['user_Error']= user_Error
    context['user_book']= request.session.get('user_book')
    context['user_experience']= models.User_Information.objects.get(userID = user_ID).experience

    return render(request,'home/home.html',context)
# 登陆
def Landing(request):
    context = {}  
    context['motto_data'] = motto_text()
    name = request.POST.get('name')
    password = request.POST.get('password')
    context['message'] = "请登陆您的账号"
    try:
        User_mi = models.User.objects.get(name=name)
        user_data = models.User_Information.objects.get(userID = User_mi.pk)
    except:
        context['message'] = "用户信息不存在！"
        return render(request,'Landing/Landing.html',context)
    if User_mi.password == password:
        request.session['user_name'] = User_mi.name
        request.session['user_ID'] = User_mi.pk
        request.session['user_miname'] = user_data.name
        request.session['user_gender'] = user_data.gender
        request.session['user_experience'] = user_data.experience
        request.session['user_book'] = user_data.bookID.id
        request.session['user_Classroom'] = user_data.ClassroomID.name
        request.session['is_login'] = True
        return HttpResponseRedirect('/')
    else:
        context['message'] = "密码错误！"
        context['user_name'] = name
    return render(request,'Landing/Landing.html',context)
# 登出
def Logout(request):
    context = {}  
    context['motto_data'] = motto_text()
    context['message'] = "请登陆您的账号"
    if not request.session.get('is_login', None):
        return render(request,'Landing/Landing.html',context)  
    request.session.flush()
    context['message'] = "请登陆您的账号"
    return HttpResponseRedirect('/')
#更新用户所学内容
def updata_user_book(request):
    context = {}      
    id = request.POST.get('data')
    bookid = models.book.objects.get(pk=id)
    data = models.User_Information.objects.get(userID=request.session['user_ID'])
    print(data.bookID)
    data.bookID = bookid
    data.save()
    request.session['user_book'] = id
    return JsonResponse(context)
#更新用户排名
def rank_updata(request):
    corrects = {}
    context = {}
    user_all = models.User.objects.all()
    for i in user_all:
        user_ID = i.pk
        user_Finished = models.Finished.objects.filter(userID = user_ID)
        user_Error = models.Error.objects.filter(userID = user_ID)
        if user_Finished.count() + user_Error.count() != 0:
            correct = user_Finished.count() / ( user_Finished.count() + user_Error.count())
            corrects[i.name] = correct
    print(corrects)
    sorted_key_list = sorted(corrects)
    sorted_key_list = sorted(corrects, key=lambda x:corrects[x], reverse=True)   #倒序排列
    rank = sorted_key_list.index(request.session.get('user_name'))
    print(rank)
    context['msg'] =rank
    return JsonResponse(context)
    
def user_Collection_ajax(request):
    context = {}
    return JsonResponse(context)
    
def user_Error_ajax(request):
    userID = request.session.get('user_ID')
    context = {}
    return JsonResponse(context)

def user_password_ajax(request):
    context = {}
    user_ID = request.session.get('user_ID')
    password = request.POST.get('password')
    user_data = models.User.objects.get(id=user_ID) 
    context['msg'] = "修改失败"
    print(user_data.password)
    if user_data.password == password:
        new_password = request.POST.get('new_password')
        user_data.password = new_password
        user_data.save()
        print("修改成功")
        context['msg'] = "修改成功"
    print(user_data.password)
    return JsonResponse(context)
    
