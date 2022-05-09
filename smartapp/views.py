from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status
from .models import Event, Add  # .models = models.py / Feed = 모델명
import os



class Calender(APIView):
    def get(self, request):
        # event_list = Event.objects.all().order_by('-id')  # Feed 모든 데이터를 가져옴 == select * from content_feed
        return render(request, 'calender.html')


class Eboard(APIView):
    def get(self, request):
        event_list = Event.objects.all()
        print(event_list)
        return render(request, 'event_board.html', context=dict(event_list=event_list))


class Add(APIView):

    def post(self, request):

        edata = request.data.get('event_data')
        singer = request.data.get('singer')
        location = request.data.get('loca')
        link = request.data.get('li')

        Add.objects.create(edate=edata, singer=singer,
                           location=location, link=link)

        return Response(status=200)

