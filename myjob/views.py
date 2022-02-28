from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.


# 3.新增功能函数及业务逻辑
def get_index_page(request):
    return HttpResponse('hello world!')
