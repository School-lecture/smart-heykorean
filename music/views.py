import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from playlist.models import PlaylistPlaylist, MusicMusic
from datetime import datetime

# Create your views here.
import pandas as pd



class List(APIView):
    def get(self, request):
        music_list = MusicMusic.objects.all()
        print(music_list)
        # play_list = Playlist.objects.all()

        play_list = PlaylistPlaylist.objects.filter(music_num=3)

        print(play_list)

        list=[]

        for i in range(len(play_list)):
            test_id = play_list[i]
            id2 = test_id.music_num
            list.append(id2)

        print(list)

        mlist=[]
        for j in range(len(list)):
            mlist.append(MusicMusic.objects.filter(music_num=list[j]))

        print(mlist)


        return render(request, 'main/main.html', context=dict(music_list=music_list, play_list=play_list, list=mlist))




#
# class List_select(APIView):
#     def get(self, request):
#         list_select = Music.objects.filter(music_title='music_title')
#         return render(request, context=dict(list_select=list_select))


class list_select(APIView):
    def post(self, request):
        music_num = request.data.get('music_num')
        print(music_num)
        music_list1 = MusicMusic.objects.filter(music_num=music_num)

        music_list = MusicMusic.objects.all()

        for i in range(0, len(music_list)):
            print(music_list[i])

        # print(music_list1)
        # print(music_list1.values())
        # print(music_list1[0].music_title)
        mtv = music_list1.values()

        # queryset_json = serializers.serialize('json', music_list1)
        # return HttpResponse(queryset_json, content_type="application/json")
        return Response(mtv)


class list_same(APIView):
    def post(self, request):
        music_num = request.data.get('music_num')
        music_list1 = MusicMusic.objects.filter(music_num=music_num)
        music_list = MusicMusic.objects.all()

        ml0 = music_list
        ml1 = music_list1

        print(ml0)
        print(ml1)
        data = {
            'title1': [],
            'music_singer': [],
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
            if ml1[0].music_nation != ml0[i].music_nation:
                if ml1[0].music_genre == ml0[i].music_genre:
                    sum = (abs(ml1[0].senti1 - ml0[i].senti1) + abs(ml1[0].senti2 - ml0[i].senti2) +
                           abs(ml1[0].senti3 - ml0[i].senti3) + abs(ml1[0].senti4 - ml0[i].senti4) +
                           abs(ml1[0].senti5 - ml0[i].senti5))
                    print(sum)
                    frame.loc[len(frame)] = [(ml0[i].music_title), (ml0[i].music_singer), (ml0[i].music_path),
                                             (ml0[i].image_path), (ml0[i].youtube_path),
                                             (ml0[i].senti1), (ml0[i].senti2),
                                             (ml0[i].senti3), (ml0[i].senti4),
                                             (ml0[i].senti5), sum]

        frame = frame.sort_values('same')

        return Response(frame)

class list_dam(APIView):

    def post(self, request):
        music_num = request.data.get('music_num')
        music_list1 = MusicMusic.objects.filter(music_num=music_num)
        music_list = MusicMusic.objects.all()

        ml0 = music_list
        ml1 = music_list1

        print(ml0)
        print(ml1)
        data = {
            'title1': [],
            'music_singer': [],
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
            if ml1[0].music_nation != ml0[i].music_nation:
                if ml1[0].music_genre == ml0[i].music_genre:
                    sum = (abs(ml1[0].senti1 - ml0[i].senti1) + abs(ml1[0].senti2 - ml0[i].senti2) +
                           abs(ml1[0].senti3 - ml0[i].senti3) + abs(ml1[0].senti4 - ml0[i].senti4) +
                           abs(ml1[0].senti5 - ml0[i].senti5))
                    print(sum)
                    frame.loc[len(frame)] = [(ml0[i].music_title), (ml0[i].music_singer), (ml0[i].music_path),
                                             (ml0[i].image_path), (ml0[i].youtube_path),
                                             (ml0[i].senti1), (ml0[i].senti2),
                                             (ml0[i].senti3), (ml0[i].senti4),
                                             (ml0[i].senti5), sum]

        frame = frame.sort_values('same')
        print(frame['title1'][0])
        dam = frame['title1'][0]
        damgi = MusicMusic.objects.filter(music_title=dam)
        damggi = damgi[0].music_num

        PlaylistPlaylist.objects.create(id=1, music_num=damggi, playlist_date=datetime.now())

        return Response(frame)



    # for i in ml0:
    #
    #     if (ml1[0].music_nation != ml0[0].music_nation):
    #         if (ml)

# def show_eng(request):
#     input_val = request.GET.get('input_val')
#     print(input_val)
#
#     if input_val=='사과':
#         eng='apple'
#     else:
#         eng="ㅋㅋㅋ"
#
#     context={'eng':eng}
#     return JsonResponse(context)
