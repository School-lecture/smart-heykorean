from django.shortcuts import render

# Create your views here.
def index(requset) :
    return render(requset ,'user/index.html')

def cal(requset) :
    return render(requset ,'cal/daygrid-views.html')