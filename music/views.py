from django.http import JsonResponse
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
        title1 = request.data.get('title')
        print(title1)
        music_list1 = Music.objects.filter(music_title=title1)
        print(music_list1)

        return render(request, 'music/music.html', context=dict(music_list1=music_list1))

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