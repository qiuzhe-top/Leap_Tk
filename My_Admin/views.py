from django.shortcuts import render
from TkApp.forms import Subject_form
from UserApp.models import Classroom,User,User_Information,Finished,Error
from TkApp.models import title, information, radio, more
from BookApp.models import Measure, unit, book

from django.http import JsonResponse
import json
import time
import datetime

# 主页
def index(request):
    context = {}
    s1 = 0
    s2 = 0
    s3 = 0

    obj_data = title.objects.all()
    now_day = datetime.datetime.now().day
    for i in obj_data:
        star_day = i.star_time.day
        if star_day == now_day:
            s1 += 1

    Finished_data = Finished.objects.all()
    for i in Finished_data:
        star_day = i.star_time.day
        if star_day == now_day:
            s2 += 1

    context['index_active'] = 'active'
    context['obj_num'] = obj_data.count() #题量
    context['now_day_obj'] = s1 #今日增量
    context['now_day_Finished'] = s2 #今日做题
    context['user_num'] = User.objects.all().count() #学生量
    return render(request,'My_Admin/index.html',context)
# 题目录入页面Tk_add    # 题目保存add_subject  #批量上传页面Tk_add_all
def Tk_add(request):
    context = {}
    context['Tkadd_active'] = 'active'
    context['subject_form'] = Subject_form()
    context['books'] = book.objects.all()
    return render(request,'My_Admin/Tk_add.html',context)
def add_subject(request):
    context = {}
    data = request.POST.get('data') 
    data = data.split(",")
    subject = request.POST.get('subject') 
    # 查找数据实例
    subject_data = title.objects.filter(subject=subject).count() 
    try:
        Measure_examples = Measure.objects.get(pk = data[1])
        if subject_data == 0:
            title.objects.create(subject=subject)
            subject_examples = title.objects.get(subject=subject)
            information.objects.create(answer=data[3], types=data[2], minutiaID=Measure_examples,difficulty= int(data[10]), subjectID = subject_examples)
            if data[2] == "单选":
                radio.objects.create(AnswerA= data[4],AnswerB= data[5],AnswerC= data[6],AnswerD= data[7],subjectID = subject_examples)
            elif data[2] =="多选":
                more.objects.create(AnswerA= data[4],AnswerB= data[5],AnswerC= data[6],AnswerD= data[7],AnswerE= data[8],AnswerF= data[9],subjectID = subject_examples)
            context['msg'] = '题目保存成功'
        else:
            context['msg'] = '题目存在'
    except:
        context['msg'] = '信息填写异常'

    return JsonResponse(context)
def Tk_add_all(request):
    context = {}
    context['Tk_add_all_active'] = 'active'

    # start = time.clock()
    # title.objects.filter(id__gt=50).delete()
    # elapsed = (time.clock() - start)
    # print("Time used:",elapsed)

    return render(request,'My_Admin/Tk_add_all.html',context)
def add_all_subject(request):
    context = {}
    msg = {}
    data = request.POST.get('data') 
    a = eval(data)
    b = list(a)
    for i in b:
        d = dict(i)
        try:
            subject_data = title.objects.filter(subject=d['subject']).count()
            Measure_examples = Measure.objects.get(pk = d['measureID']) #小节实例
            if subject_data == 0: #判断这个题目在数据库里面是否存在
                title.objects.create(subject=d['subject']) #保存题目
                subject_examples = title.objects.get(subject=d['subject'])#题目实例
                information.objects.create(answer=d['answer'], types=d['types'],difficulty= int(d['difficulty']), minutiaID=Measure_examples, subjectID = subject_examples)
                if d['types'] == "单选":
                    radio.objects.create(AnswerA= d['AnswerA'],AnswerB= d['AnswerB'],AnswerC= d['AnswerC'],AnswerD= d['AnswerD'],subjectID = subject_examples)
                elif d['types'] =="多选":
                    more.objects.create(AnswerA= d['AnswerA'],AnswerB= d['AnswerB'],AnswerC= d['AnswerC'],AnswerD= d['AnswerD'],AnswerE= d['AnswerE'],AnswerF= d['AnswerF'],subjectID = subject_examples)
            else:
                # print('2题目存在')
                msg[d['subject']] = '题目存在'
        except:
            # print('3信息填写异常')
            msg[d['subject']] = '信息填写异常'
            
    context['msg'] =  json.dumps(msg)
    # print(context['msg'])

    return JsonResponse(context) 
# 题目分类信息  ajax
def Book_Get_Unit(request):
    context = {}
    data = request.POST.get('data') 
    print(data)
    unit_data = unit.objects.filter(bookID = data).values('title','id')
    context['data'] = json.dumps(list(unit_data))
    return JsonResponse(context)
def unit_Get_Measure(request):
    context = {}
    data = request.POST.get('data') 
    Measure_data = Measure.objects.filter(unitID = data).values('title','id')
    context['data'] = json.dumps(list(Measure_data))
    return JsonResponse(context) 
def query(request):
    context = {}
    context['index_active'] = 'active'
    return render(request,'My_Admin/query.html',context)
def query_new(request):
    context = {}
    data = request.POST.get('data') 
    Measure_data = title.objects.filter(subject__contains = data).values('subject','id')
    context['data'] = json.dumps(list(Measure_data))
    print(context['data'])
    return JsonResponse(context) 
def add_user(request):
    context = {}
    context['book'] = book.objects.all()
    context['Classroom'] = Classroom.objects.all()
    return render(request,'My_Admin/add_user.html',context)
# 学生信息  写入  批量
def add_user_ajax(request):
    context = {}
    ty = request.POST.get('ty') 
    if ty =="1":
        data = request.POST.get('data') 
        data = data.split(",")
        user_num = User.objects.filter(name = data[4]).count()
        try:
            if user_num == 0:
                User.objects.create(name = data[4],password = "123456")
                user_examples = User.objects.get(name = data[4])
                book_examples = book.objects.get(id = data[3])
                Classroom_examples = Classroom.objects.get(id = data[2])
                User_Information.objects.create(name = data[0],gender = data[1], experience = 100,userID = user_examples ,bookID = book_examples,ClassroomID= Classroom_examples)
                print("ok")
                context['msg'] = "添加成功"
            else:
                print("no")
                context['msg'] = "账号存在"
        except:
                context['msg'] = "保存错误"
    elif ty == "2": #批量上传
        msg = {}
        data = request.POST.get('data') 
        a = eval(data)
        b = list(a)
        for i in b:
            d = dict(i)
            print(d)
            user_num = User.objects.filter(name = d['username']).count()
            try:
                if user_num == 0:
                    User.objects.create(name = d['username'],password = "123456")
                    user_examples = User.objects.get(name = d['username'])
                    book_examples = book.objects.get(id = d['book'])
                    Classroom_examples = Classroom.objects.get(id = d['class'])
                    User_Information.objects.create(name = d['name'],gender = d['gender'], experience = 100,userID = user_examples ,bookID = book_examples,ClassroomID= Classroom_examples)
                    context['msg'] = "添加成功"
                else:
                    context['msg'] = "账号存在"
                    msg[d['username']] = d['name'] +  "：账号存在"
            except:
                    context['msg'] = "保存错误"
                    msg[d['username']] = d['name'] + "：保存错误"
            context['msg'] =  json.dumps(msg)
            
    return JsonResponse(context) 
def Section_completion(request):
    context = {}
    minutia_ID = request.POST.get('data')
    context['books'] = book.objects.all()
    context['class'] = Classroom.objects.all()
    return render(request,'My_Admin/Section_completion.html',context)
def Section_completion_ajax(request):
    context = {}
    data = {}
    complete_number = 0 #完成数量
    error_number = 0 #错误数量
    list_data = []
    msg_data = []
    #获取 > 学生ID 班级 小节  
    user_ID = request.session.get('user_ID')
    class_ID = request.POST.get('class_data') 
    minutia_ID = request.POST.get('minutia_data')
    # Mobj_data = information.objects.filter(minutiaID = minutia_data)

    Uobj_data = User_Information.objects.filter(ClassroomID = class_ID) #教室的所有学生

    Measure_obj = information.objects.filter(minutiaID = minutia_ID) #小节所有题目
    Measure_count = Measure_obj.count()
    for i in Uobj_data:
        # print(i.name)
        msg_data.append(i.name)
        complete_number = 0
        error_number = 0
        for j in Measure_obj:
            try:
                Finished.objects.get(userID=i.pk,subjectID=j.pk)    
                complete_number += 1
            except:
                pass
            try:
                Error.objects.get(userID=i.pk,subjectID=j.pk)    
                error_number += 1 
            except:
                pass
        completion = complete_number / Measure_count * 100 #完成率
        completion = round(completion,2)
        
        if complete_number != 0:
            correct_rate = complete_number / (error_number + complete_number) * 100 #正确率
            correct_rate = round(correct_rate,2)
        else:
            correct_rate = 0
        msg_data.append(complete_number)
        msg_data.append(error_number)
        msg_data.append(completion)
        msg_data.append(correct_rate)
        # print(complete_number,error_number,completion,correct_rate)
        list_data.append(msg_data)
        msg_data = []
    context['msg'] =  json.dumps(list_data)
    # print(context['msg'])
    return JsonResponse(context) 
def Error_rate_ranking(request):
    context = {}
    return render(request,'My_Admin/Error_rate_ranking.html',context)
#组卷部分
def Ks_add(request):
    context = {}
    Measure_data = {}
    unit_data = {}
    books_data = book.objects.all()#获取书
    if books_data[0] !='':
        units = unit.objects.filter(bookID = books_data[0].pk)
        
        # print(unit_data)
    for i in units:
        unit_data[i.pk] = i.title
        Measures = Measure.objects.filter(unitID=i.pk)
        # print(Measure_data)
        Measure_data[i.pk] = Measures
    context['books'] = books_data
    context['units'] = unit_data
    context['Measure'] = Measure_data
    # print(Measure_data)

    return render(request,'My_Admin/Ks_add.html',context)