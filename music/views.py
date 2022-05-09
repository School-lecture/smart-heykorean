import json
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from music.models import Music
# Create your views here.


class List(APIView):
    def get(self, request):
        music_list = Music.objects.all()
        print(music_list)
        return render(request, 'music/music.html', context=dict(music_list=music_list))
#
# class List_select(APIView):
#     def get(self, request):
#         list_select = Music.objects.filter(music_title='music_title')
#         return render(request, context=dict(list_select=list_select))

class list_select(APIView):
    def post(self, request):
        title = request.data.get('title')
        print(title)
        music_list1 = Music.objects.filter(music_title=title)

        music_list = Music.objects.all()

        for i in music_list:
            print(music_list[i])

        print(music_list1)
        print(music_list1.values())
        print(music_list1[0].music_title)

        mtv = music_list1.values()


        # queryset_json = serializers.serialize('json', music_list1)
        # return HttpResponse(queryset_json, content_type="application/json")
        return Response(mtv)



# class list_same(APIView):
#     def post(self, request):
#         title = request.data.get('title')
#         print(title)
#
#         music_list1 = Music.objects.filter(music_title=title)
#
#         music_list = Music.objects.all()
#
#         ml0 = music_list
#         ml1 = music_list1

    # for i in ml0:
    #
    #     if (ml1[0].music_nation != ml0[0].music_nation):
    #         if (ml)







        return Response(ml1)



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