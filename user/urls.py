from django.urls import path
from . import views
from rest_framework.views import APIView

from .views import list_select, list_same, Musiclist

app_name = 'user'

urlpatterns = [
    # 회원가입 
    path('joinform', views.joinform, name='joinform'),
    path('join', views.join, name='join'),
    path('joinsuccess', views.joinsuccess, name='joinsuccess'),
    # 로그인
    path('loginform', views.loginform, name='loginform'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    # 회원 수정
    path('updateform', views.updateform, name='updateform'),
    path('update', views.update, name='update'),
    # 중복체크
    path('api/checkID', views.checkID, name='checkID'),
    path('index', views.index, name ='index'),
    path('main', views.main, name ='main'),
    # 이벤트 달력
    path('calp', views.calp, name='calp'),
    path('calendar', views.calendar, name='calendar'),

    # 음악
    path('list_select', list_select.as_view(), name='list_select'),
    path('list_same', list_same.as_view(), name='list_same'),


    path('plistadd/', views.plistadd, name='plistadd'),
    path('Musiclist', Musiclist.as_view(), name='Musiclist'),

]