from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from smartapp.models import Event, Add, Music, Playlist


class Sub(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, 'calender.html')

    def post(self, request):
        print("post로 호출")
        return render(request, 'calender.html')


# @csrf_exempt
# def test(request):
#     jsonObject = json.loads(request.body)
#     print(jsonObject.get('title'))
#     singer=jsonObject.get('title')
#     location=jsonObject.get('content')
#     Add.objects.create(edate=2, singer=singer,
#                        location=location, link=2)
#
#     return JsonResponse(jsonObject)

@csrf_exempt
def test(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('id'))
    id = jsonObject.get('id')
    e_list = Event.objects.filter(id=id)
    print(e_list[0].edate)
    print(e_list[0].singer)
    print(e_list[0].location)
    print(e_list[0].link)

    Add.objects.create(edate=e_list[0].edate, singer=e_list[0].singer,
                       location=e_list[0].location, link=e_list[0].link)

    return JsonResponse(jsonObject)


@csrf_exempt
def plistadd(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('music_num'))
    music_num = jsonObject.get('music_num')

    kmusic = Music.objects.filter(music_num=music_num)

    senti1 = kmusic[0].senti1
    senti2 = kmusic[0].senti2
    senti3 = kmusic[0].senti3
    senti4 = kmusic[0].senti4
    senti5 = kmusic[0].senti5

    pmusic = Music.objects.filter(senti1=senti1)

    pop = pmusic[0].music_num
    Playlist.objects.create(id=1, music_num=pop,
                            playlist_name=1)

    return JsonResponse(jsonObject)
