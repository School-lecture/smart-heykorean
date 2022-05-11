from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import request
from user.models import User, Event,UserMusic, UserPlaylist
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def joinform(request):
    return render(request, 'user/joinform.html')

def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')

def index(request):
    return render(request, 'user/index.html')

def main(request):
    return render(request, 'main/main.html')



def join(request):
    user = User()
    user.id = request.POST['id']
    user.password = request.POST['password']
    user.name = request.POST['name']
    user.gender = request.POST['gender']
    user.phone_num = request.POST['phone_num']
    user.save()

    return HttpResponseRedirect('./joinsuccess')

def loginform(request) :
    return render(request, 'user/loginform.html')

def login(request):
    results = User.objects.filter(id=request.POST['id']).filter(password=request.POST['password'])

    # 로그인 실패
    if len(results)==0:
        return HttpResponseRedirect('/user/loginform?result=fail')

    # 로그인 처리
    authUser = results[0]
    request.session['authUser'] = model_to_dict(authUser)

    return HttpResponseRedirect('./main')

def logout(request) :
    del request.session['authUser']
    return HttpResponseRedirect('./index')

def updateform(request) :
    user = User.objects.get(id=request.session['authUser']['id'])
    data = {
        'user':user
    }
    return render(request, 'user/updateform.html', data)

def update(request) :
    user = User.objects.get(id=request.session['authUser']['id'])
    user.name = request.POST['name']

    user.gender = request.POST['gender']
    if request.POST['password'] is not '':
        user.password = request.POST['password']
    user.save()

    request.session['authUser']['name']=user.name
    return HttpResponseRedirect('/user/updateform?result=success')

def checkID(request):
    try :
        user = User.objects.get(id=request.GET['id'])
    except Exception as e:
        user = None
    result = {
        'result' : 'success',
        # 'data' : model_todict(user) # console에서 확인
        'data' : "not exist" if user is None else "exist"
    }
    return JsonResponse(result)

def calendar(request):
    cal = Event.objects.all()

    context = {
        "events":cal,
    }

    return render(request, 'cal/daygrid-views.html', context)


def calp(request):
    return render(request, 'cal/daygrid-views.html')

def loginform(request) :
    return render(request, 'user/loginform.html')
#-----------------------------------------------------------------------

class Musiclist(APIView):
    def get(self, request):
        music_list = UserMusic.objects.all().order_by('music_num')
        return render(request, 'main/main.html', {'music_list': music_list})

@csrf_exempt
def plistadd(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('music_num'))
    music_num = jsonObject.get('music_num')

    kmusic = UserMusic.objects.filter(music_num=music_num)


    senti1 = kmusic[0].senti1
    senti2 = kmusic[0].senti2
    senti3 = kmusic[0].senti3
    senti4 = kmusic[0].senti4
    senti5 = kmusic[0].senti5

    pmusic = UserMusic.objects.filter(senti1=senti1)

    pop = pmusic[0].music_num
    UserPlaylist.objects.create(id=1, music_num=pop,
                            playlist_name=1)

    return JsonResponse(jsonObject)
#=======================================================================


class list_select(APIView):
    def post(self, request):
        title = request.data.get('title')
        print(title)
        music_list1 = UserMusic.objects.filter(music_title=title)

        music_list = UserMusic.objects.all()

        for i in range(0, len(music_list)):
            print(music_list[i])

        print(music_list1)
        print(music_list1.values())
        print(music_list1[0].music_title)
        mtv = music_list1.values()

        # queryset_json = serializers.serialize('json', music_list1)
        # return HttpResponse(queryset_json, content_type="application/json")
        return Response(mtv)


class list_same(APIView):
    def post(self, request):
        title = request.data.get('title')
        music_list1 = UserMusic.objects.filter(music_title=title)
        music_list = UserMusic.objects.all()

        ml0 = music_list
        ml1 = music_list1

        print(ml0)
        print(ml1)
        data = {
            'title1': [],
            'music_path': [],
            'image_path': [],
            'youtube_path': [],
            'senti1': [],
            'senti2': [],
            'senti3': [],
            'senti4': [],
            'senti5': [],
            'same': []

        }
        frame = pd.DataFrame(data)
        print(frame)

        for i in range(0, len(ml0)):

            sum = 0

            print(ml0[i])
            print(sum)
            if (ml1[0].music_nation != ml0[i].music_nation):
                if (ml1[0].music_genre) == ml0[i].music_genre:
                    sum = (abs(ml1[0].senti1-ml0[i].senti1)+abs(ml1[0].senti2-ml0[i].senti2)+
                           abs(ml1[0].senti3-ml0[i].senti3)+abs(ml1[0].senti4-ml0[i].senti4)+
                           abs(ml1[0].senti5-ml0[i].senti5))
                    print(sum)
                    frame.loc[len(frame)] = [(ml0[i].music_title),(ml0[i].music_path),
                                             (ml0[i].image_path),(ml0[i].youtube_path),
                                             (ml0[i].senti1),(ml0[i].senti2),
                                            (ml0[i].senti3),(ml0[i].senti4),
                                             (ml0[i].senti5),sum]

                else :
                    frame.loc[len(frame)] = [(ml0[i].music_title),(ml0[i].music_path),
                                             (ml0[i].image_path),(ml0[i].youtube_path),
                                             (ml0[i].senti1),(ml0[i].senti2),
                                           (ml0[i].senti3),(ml0[i].senti4),
                                             (ml0[i].senti5),1000]
            else :
                frame.loc[len(frame)] = [(ml0[i].music_title),(ml0[i].music_path),
                                             (ml0[i].image_path),(ml0[i].youtube_path),
                                             (ml0[i].senti1),(ml0[i].senti2),
                                           (ml0[i].senti3),(ml0[i].senti4),
                                             (ml0[i].senti5),1000]

        frame = frame.sort_values('same')

        print(frame)

        return Response(frame)
