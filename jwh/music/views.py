import json
from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User
from playlist.models import PlaylistPlaylist, MusicMusic
from datetime import datetime

# Create your views here.
import pandas as pd



class List(APIView):
    def get(self, request):
        music_list = MusicMusic.objects.filter(music_nation=1)

        user = User.objects.get(id=request.session['authUser']['id'])

        session=user.id

        play_list = PlaylistPlaylist.objects.filter(id=session)




        list=[]

        for i in range(len(play_list)):
            test_id = play_list[i]
            id2 = test_id.music_num
            list.append(id2)

        mlist=[]
        for j in range(len(list)):
            test_num = list[j]
            mnum = MusicMusic.objects.filter(music_num=test_num)
            mlist.append(mnum)

        return render(request, 'main/main1.html', context=dict(music_list=music_list, play_list=play_list, list=mlist))




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


        mtv = music_list1.values()

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
            'num': [],
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
                    frame.loc[len(frame)] = [(ml0[i].music_num), (ml0[i].music_title), (ml0[i].music_singer), (ml0[i].music_path),
                                             (ml0[i].image_path), (ml0[i].youtube_path),
                                             (ml0[i].senti1), (ml0[i].senti2),
                                             (ml0[i].senti3), (ml0[i].senti4),
                                             (ml0[i].senti5), sum]

        frame = frame.sort_values('same')
        print(frame)
        return Response(frame)

class list_dam(APIView):

    def post(self, request):
        music_num = request.data.get('music_num2')

        user = User.objects.get(id=request.session['authUser']['id'])
        # data = {
        #     'user': user
        # }
        session = user.id

        print(session)

        PlaylistPlaylist.objects.create(id=session, music_num=music_num, playlist_date=datetime.now())

        return Response(session)


    # for i in ml0:
    #
    #     if (ml1[0].music_nation != ml0[0].music_nation):
    #         if (ml)

# def show_eng(request):
#     input_val = request.GET.get('input_val')
#     print(input_val)
#
#     if input_val=='??????':
#         eng='apple'
#     else:
#         eng="?????????"
#
#     context={'eng':eng}
#     return JsonResponse(context)
