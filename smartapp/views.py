from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse
from rest_framework import request
import json
from rest_framework import status
from .models import Event, Add, Music  # .models = models.py / Feed = 모델명
import os

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime

class Calender(APIView):
    def get(self, request):
        # event_list = Event.objects.all().order_by('-id')  # Feed 모든 데이터를 가져옴 == select * from content_feed
        return render(request, 'calender.html')


class Eboard(APIView):
    def get(self, request):
        event_list = Event.objects.all
        print(event_list)
        return render(request, 'event_board.html', {'event_list' : event_list})


class Add(APIView):

    def post(self, request):

        e_data = request.data.get('e_data')
        e_singer = request.data.get('e_singer')
        e_location = request.data.get('e_location')
        e_link = request.data.get('e_link')

        print(e_data)

        Add.objects.create(edate=e_data, singer=e_singer,
                           location=e_location, link=e_link)

        return Response(status=200)

class Main(APIView):
    def get(self, request):
        # event_list = Event.objects.all().order_by('-id')  # Feed 모든 데이터를 가져옴 == select * from content_feed
        return render(request, 'main.html')

class Cal(APIView):
    def get(self, request):
        # event_list = Event.objects.all().order_by('-id')  # Feed 모든 데이터를 가져옴 == select * from content_feed
        return render(request, 'daygrid-views.html')

class Musiclist(APIView):
    def get(self, request):
        music_list = Music.objects.all().order_by('music_num')
        return render(request, 'music_list.html', {'music_list' : music_list})