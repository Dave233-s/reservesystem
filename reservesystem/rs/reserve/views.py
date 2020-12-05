from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.forms import model_to_dict
#from reserve.models import Admin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from reserve.models import Reservation
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def logining(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username and password:
            try:
                user = auth.authenticate(username=username, password=password)
            except:
                return redirect('/login/')
            if user:
                auth.login(request, user)
                request.session['user'] = username
                return HttpResponseRedirect('/ad/')
            else:
                return redirect('/login/')
        else:
            return redirect('/login/')


def reserve(request):
    return render(request, 'reserve.html')


def search(request):
    return render(request, 'search.html')


@login_required
def ad(request):
    username = request.session.get('user', '')
    return render(request, 'ad.html')


#获取维修内容接口
def get_r(request):
    res = Reservation.objects.all()
    lis = []
    for i in res:
        if (i.dele == False):
            dic = model_to_dict(i)
            lis.append(dic)
        else:
            i.delete()
            i.save()
    print({'data': lis})
    return JsonResponse({'data': lis})


#管理员提上日程接口
@csrf_exempt
def post_status(request):
    if request.method == 'POST':
        re = request.POST
        tem = re.get('id')
        li = Reservation.objects.get(id=tem)
        li.to_agenda= True
        li.save()
        print(li)
    return JsonResponse({'good': 1})


#管理员删除预约接口
@csrf_exempt
def delete_r(request):
    if request.method == 'POST':
        re = request.POST
        tem = re.get('id')
        li = Reservation.objects.filter(id=tem)
        li.delete()

    return JsonResponse({'ok': 1})


@csrf_exempt
def put_r(request):
    if request.method == 'POST':
        re = request.POST
        phone = re.get('phone')
        service_type = re.get('service_type')
        print(phone)
        print(service_type)
        r1 = Reservation.objects.create(phone=phone, service_type=service_type)
    return JsonResponse({'ok': 1})


@csrf_exempt
def post_search(request):
    if request.method == 'POST':
        re = request.POST
        phone = re.get('phone')
        li_ = []
        print(phone)
        p = Reservation.objects.filter(phone=phone)
        print(p)
        for i in p:
            dic = model_to_dict(i)
            li_.append(dic)
    return JsonResponse({'data': li_})




